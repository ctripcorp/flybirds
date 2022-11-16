#! usr/bin/python
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from baseImage import Image, Rect

from .matchTemplate import MatchTemplate
from .utils import (generate_result, get_keypoint_from_matches, keypoint_distance, rectangle_transform)
from .exceptions import (NoEnoughPointsError, PerspectiveTransformError, HomographyError, MatchResultError,
                         InputImageError)
from typing import List


class BaseKeypoint(object):
    FILTER_RATIO = 1
    METHOD_NAME = None
    Dtype = None
    Place = None
    template = MatchTemplate()

    def __init__(self, threshold=0.6, rgb=True, **kwargs):
        """
        init

        Args:
            threshold: recognition threshold(0~1)
            rgb: Whether to use rgb channel for verification
        """
        self.threshold = threshold
        self.rgb = rgb
        self.detector = self.create_detector(**kwargs)
        self.matcher = self.create_matcher(**kwargs)

    def create_matcher(self, **kwargs):
        raise NotImplementedError

    def create_detector(self, **kwargs):
        raise NotImplementedError

    def find_best_result(self, im_source, im_search, threshold=None, rgb=None, **kwargs):
        """
        Through feature point matching, find the range that best matches im_search in im_source

        Args:
            im_source: image to be matched
            im_search: image template
            threshold: recognition threshold(0~1)
            rgb: Whether to use rgb channel for verification

        Returns:

        """
        max_count = 1
        ret = self.find_all_results(im_source=im_source, im_search=im_search, threshold=threshold, rgb=rgb,
                                    max_count=max_count, **kwargs)
        if ret:
            return ret[0]
        return None

    def find_all_results(self, im_source, im_search, threshold=None, rgb=None, max_count=10, max_iter_counts=20,
                         distance_threshold=150):
        """
        Through feature point matching, find all the ranges that match im_search in im_source

        Args:
             im_source: the image to be matched
             im_search: image template
             threshold: recognition threshold (0~1)
             rgb: whether to use the rgb channel for verification
             max_count: the maximum number of matches that can be returned
             max_iter_counts: The maximum number of searches, which needs to be greater than max_count
             distance_threshold: distance threshold, after the feature point (first_point) is greater than
                                 the threshold, no subsequent screening will be done

        Returns:

        """
        threshold = self.threshold if threshold is None else threshold
        rgb = self.rgb if rgb is None else rgb

        im_source, im_search = self.input_image_check(im_source, im_search)
        result = []
        if im_source.channels == 1:
            rgb = False

        kp_src, des_src = self.get_keypoint_and_descriptor(image=im_source)
        kp_sch, des_sch = self.get_keypoint_and_descriptor(image=im_search)

        kp_src, kp_sch = list(kp_src), list(kp_sch)
        # In the feature point set, match the closest feature point
        matches = np.array(self.match_keypoint(des_sch=des_sch, des_src=des_src))
        kp_sch_point = np.array([(kp.pt[0], kp.pt[1], kp.angle) for kp in kp_sch])
        kp_src_matches_point = np.array([[(*kp_src[dMatch.trainIdx].pt, kp_src[dMatch.trainIdx].angle)
                                          if dMatch else np.nan for dMatch in match] for match in matches])
        _max_iter_counts = 0
        src_pop_list = []
        while True:
            # not use of matches to judge nan, because the type is wrong
            if (np.count_nonzero(~np.isnan(kp_src_matches_point)) == 0) or (len(result) == max_count) or (
                    _max_iter_counts >= max_iter_counts):
                break
            _max_iter_counts += 1
            filtered_good_point, angle, first_point = self.filter_good_point(matches=matches, kp_src=kp_src,
                                                                             kp_sch=kp_sch,
                                                                             kp_sch_point=kp_sch_point,
                                                                             kp_src_matches_point=kp_src_matches_point)
            if first_point.distance > distance_threshold:
                break

            rect, confidence = None, 0
            try:
                rect, confidence = self.extract_good_points(im_source=im_source, im_search=im_search, kp_src=kp_src,
                                                            kp_sch=kp_sch, good=filtered_good_point, angle=angle,
                                                            rgb=rgb)
                # print(f'good:{len(filtered_good_point)}, rect={rect}, confidence={confidence}')
            except PerspectiveTransformError:
                pass
            finally:

                if rect and confidence >= threshold:
                    br, tl = rect.br, rect.tl
                    for index, match in enumerate(kp_src_matches_point):
                        x, y = match[:, 0], match[:, 1]
                        flag = np.argwhere((x < br.x) & (x > tl.x) & (y < br.y) & (y > tl.y))
                        for _index in flag:
                            src_pop_list.append(matches[index, _index][0].trainIdx)
                            kp_src_matches_point[index, _index, :] = np.nan
                            matches[index, _index] = np.nan
                    result.append(generate_result(rect, confidence))
                else:
                    for match in filtered_good_point:
                        flags = np.argwhere(matches[match.queryIdx, :] == match)
                        for _index in flags:
                            kp_src_matches_point[match.queryIdx, _index, :] = np.nan
                            matches[match.queryIdx, _index] = np.nan
        return result

    def get_keypoint_and_descriptor(self, image):
        """
        Get image keypoint (keypoint) and descriptor (descriptor)

        Args:
            image: Grayscale image to be detected

        Returns:

        """
        if image.channels == 3:
            image = image.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            image = image.data
        keypoint, descriptor = self.detector.detectAndCompute(image, None)

        # if len(keypoint) < 2:
        #    raise NoEnoughPointsError('{} detect not enough feature points in input images'.format(self.METHOD_NAME))
        return keypoint, descriptor

    @staticmethod
    def filter_good_point(matches, kp_src, kp_sch, kp_sch_point, kp_src_matches_point):
        """ Filter the sweet spot """
        # Assume that the first point and the point with the smallest distance are the reference points
        sort_list = [sorted(match, key=lambda x: x is np.nan and float('inf') or x.distance)[0]
                     for match in matches]
        sort_list = [v for v in sort_list if v is not np.nan]

        first_good_point: cv2.DMatch = sorted(sort_list, key=lambda x: x.distance)[0]
        first_good_point_train: cv2.KeyPoint = kp_src[first_good_point.trainIdx]
        first_good_point_query: cv2.KeyPoint = kp_sch[first_good_point.queryIdx]
        first_good_point_angle = first_good_point_train.angle - first_good_point_query.angle

        def get_points_origin_angle(point_x, point_y, offset):
            points_origin_angle = np.arctan2(
                (point_y - offset.pt[1]),
                (point_x - offset.pt[0])
            ) * 180 / np.pi

            points_origin_angle = np.where(
                points_origin_angle == 0,
                points_origin_angle, points_origin_angle - offset.angle
            )
            points_origin_angle = np.where(
                points_origin_angle >= 0,
                points_origin_angle, points_origin_angle + 360
            )
            return points_origin_angle

        # Calculate the rotation angle between this point and other feature points on the template image
        first_good_point_sch_origin_angle = get_points_origin_angle(kp_sch_point[:, 0], kp_sch_point[:, 1],
                                                                    first_good_point_query)

        # Calculate the angle between the point and other feature points in the target image
        kp_sch_rotate_angle = kp_sch_point[:, 2] + first_good_point_angle
        kp_sch_rotate_angle = np.where(kp_sch_rotate_angle >= 360, kp_sch_rotate_angle - 360, kp_sch_rotate_angle)
        kp_sch_rotate_angle = kp_sch_rotate_angle.reshape(kp_sch_rotate_angle.shape + (1,))

        kp_src_angle = kp_src_matches_point[:, :, 2]
        good_point = np.array([matches[index][array[0]] for index, array in
                               enumerate(np.argsort(np.abs(kp_src_angle - kp_sch_rotate_angle)))])

        # Calculate the rotation angle of each point with first_good_point as the origin
        good_point_nan = (np.nan, np.nan)
        good_point_pt = np.array([good_point_nan if dMatch is np.nan else (*kp_src[dMatch.trainIdx].pt,)
                                  for dMatch in good_point])
        good_point_origin_angle = get_points_origin_angle(good_point_pt[:, 0], good_point_pt[:, 1],
                                                          first_good_point_train)
        threshold = round(5 / 360, 2) * 100
        point_bool = (np.abs(good_point_origin_angle - first_good_point_sch_origin_angle) / 360) * 100 < threshold
        _, index = np.unique(good_point_pt[point_bool], return_index=True, axis=0)
        good = good_point[point_bool]
        good = good[index]
        return good, int(first_good_point_angle), first_good_point

    def match_keypoint(self, des_sch, des_src, k=10):
        """
        Feature point matching

        Args:
             des_src: descriptor set of the image to be matched
             des_sch: descriptor set for image templates
             k(int): how many matching points to get

        Returns:
            List[List[cv2.DMatch]]: contains the best matching descriptor
        """
        # k=2 means that each feature point takes out the 2 most matching corresponding points
        matches = self.matcher.knnMatch(des_sch, des_src, k)
        return matches

    def get_good_in_matches(self, matches):
        """
        Feature point filtering

        Args:
            matches: Feature point set

        Returns:
            List[cv2.DMatch]: Filtered descriptor set
        """
        if not matches:
            return None
        good = []
        for match_index in range(len(matches)):
            match = matches[match_index]
            for DMatch_index in range(len(match)):
                if match[DMatch_index].distance <= self.FILTER_RATIO * match[-1].distance:
                    good.append(match[DMatch_index])
        return good

    def extract_good_points(self, im_source, im_search, kp_src, kp_sch, good, angle, rgb):
        """
        According to the number of matching points (good), extract the recognition area

        Args:
             im_source: the image to be matched
             im_search: image template
             kp_src: keypoint set
             kp_sch: keypoint set
             good: descriptor set
             angle: rotation angle
             rgb: whether to use the rgb channel for verification

        Returns:
            range, and confidence
        """
        len_good = len(good)
        confidence, rect, target_img = None, None, None

        if len_good == 0:
            pass
        elif len_good == 1:
            target_img, rect = self._handle_one_good_points(im_source=im_source, im_search=im_search,
                                                            kp_sch=kp_sch, kp_src=kp_src, good=good, angle=angle)
        elif len_good == 2:
            target_img, rect = self._handle_two_good_points(im_source=im_source, im_search=im_search,
                                                            kp_sch=kp_sch, kp_src=kp_src, good=good, angle=angle)
        elif len_good == 3:
            target_img, rect = self._handle_three_good_points(im_source=im_source, im_search=im_search,
                                                              kp_sch=kp_sch, kp_src=kp_src, good=good, angle=angle)
        else:  # len > 4
            target_img, rect = self._handle_many_good_points(im_source=im_source, im_search=im_search,
                                                             kp_sch=kp_sch, kp_src=kp_src, good=good)

        if target_img:
            confidence = self._cal_confidence(im_source=im_search, im_search=target_img, rgb=rgb)

        return rect, confidence

    def _handle_one_good_points(self, im_source, im_search, kp_src, kp_sch, good, angle):
        """
        When the number of feature point matching is equal to 1, the rectangle is scaled according
        to the size of the feature point, and the recognized target image is obtained according to
        the rotation angle.

        Args:
             im_source: the image to be matched
             im_search: image template
             kp_sch: keypoint set
             kp_src: keypoint set
             good: descriptor set
             angle: rotation angle

        Returns:
            Image to be verified
        """
        sch_point = get_keypoint_from_matches(kp=kp_sch, matches=good, mode='query')[0]
        src_point = get_keypoint_from_matches(kp=kp_src, matches=good, mode='train')[0]

        scale = src_point.size / sch_point.size
        h, w = im_search.size
        _h, _w = h * scale, w * scale
        src = np.float32(rectangle_transform(point=sch_point.pt, size=(h, w), mapping_point=src_point.pt,
                                             mapping_size=(_h, _w), angle=angle))
        dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        output = self._perspective_transform(im_source=im_source, im_search=im_search, src=src, dst=dst)
        rect = self._get_perspective_area_rect(im_source=im_source, src=src)
        return output, rect

    def _handle_two_good_points(self, im_source, im_search, kp_src, kp_sch, good, angle):
        """
        When the number of feature points matching is equal to 2, the rectangle is scaled
        according to the distance difference between the two points, and the recognized target
        image is obtained according to the rotation angle.

        Args:
             im_source: the image to be matched
             im_search: image template
             kp_sch: keypoint set
             kp_src: keypoint set
             good: descriptor set
             angle: rotation angle

        Returns:
            Image to be verified
        """
        sch_point = get_keypoint_from_matches(kp=kp_sch, matches=good, mode='query')
        src_point = get_keypoint_from_matches(kp=kp_src, matches=good, mode='train')

        sch_distance = keypoint_distance(sch_point[0], sch_point[1])
        src_distance = keypoint_distance(src_point[0], src_point[1])

        try:
            scale = src_distance / sch_distance  # Calculate the zoom size
        except ZeroDivisionError:
            if src_distance == sch_distance:
                scale = 1
            else:
                return None, None

        h, w = im_search.size
        _h, _w = h * scale, w * scale
        src = np.float32(rectangle_transform(point=sch_point[0].pt, size=(h, w), mapping_point=src_point[0].pt,
                                             mapping_size=(_h, _w), angle=angle))
        dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        output = self._perspective_transform(im_source=im_source, im_search=im_search, src=src, dst=dst)
        rect = self._get_perspective_area_rect(im_source=im_source, src=src)
        return output, rect

    def _handle_three_good_points(self, im_source, im_search, kp_src, kp_sch, good, angle):
        """
        When the number of feature points matching is equal to 3, the rectangle is scaled
        according to the difference in the area of the triangle formed by the three points,
        and the recognized target image is obtained according to the rotation angle.

        Args:
             im_source: the image to be matched
             im_search: image template
             kp_sch: keypoint set
             kp_src: keypoint set
             good: descriptor set
             angle: rotation angle

        Returns:
            Image to be verified
        """
        sch_point = get_keypoint_from_matches(kp=kp_sch, matches=good, mode='query')
        src_point = get_keypoint_from_matches(kp=kp_src, matches=good, mode='train')

        def _area(point_list):
            p1_2 = keypoint_distance(point_list[0], point_list[1])
            p1_3 = keypoint_distance(point_list[0], point_list[2])
            p2_3 = keypoint_distance(point_list[1], point_list[2])

            s = (p1_2 + p1_3 + p2_3) / 2
            area = (s * (s - p1_2) * (s - p1_3) * (s - p2_3)) ** 0.5
            return area

        sch_area = _area(sch_point)
        src_area = _area(src_point)

        try:
            scale = src_area / sch_area  # Calculate the zoom size
        except ZeroDivisionError:
            if sch_area == src_area:
                scale = 1
            else:
                return None, None

        h, w = im_search.size
        _h, _w = h * scale, w * scale
        src = np.float32(rectangle_transform(point=sch_point[0].pt, size=(h, w), mapping_point=src_point[0].pt,
                                             mapping_size=(_h, _w), angle=angle))
        dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
        output = self._perspective_transform(im_source=im_source, im_search=im_search, src=src, dst=dst)
        rect = self._get_perspective_area_rect(im_source=im_source, src=src)
        return output, rect

    def _handle_many_good_points(self, im_source, im_search, kp_src, kp_sch, good):
        """
        When the number of feature point matching is >= 4,
        use single matrix mapping to obtain the recognized target image

        Args:
             im_source: the image to be matched
             im_search: image template
             kp_sch: keypoint set
             kp_src: keypoint set
             good: descriptor set

        Returns:
            Perspective transformed image
        """

        sch_pts, img_pts = np.float32([kp_sch[m.queryIdx].pt for m in good]).reshape(
            -1, 1, 2), np.float32([kp_src[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        # M is the transformation matrix
        M, mask = self._find_homography(sch_pts, img_pts)
        # Calculate the transformed coordinates of the four corner matrices,
        # that is, the vertex coordinates of the target area in the large image:
        h, w = im_search.size
        h_s, w_s = im_source.size
        pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
        try:
            dst: np.ndarray = cv2.perspectiveTransform(pts, M)
            # img = im_source.clone().data
            # img2 = cv2.polylines(img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
            # Image(img).imshow('dst')
            pypts = [tuple(npt[0]) for npt in dst.tolist()]
            src = np.array([pypts[0], pypts[3], pypts[1], pypts[2]], dtype=np.float32)
            dst = np.float32([[0, 0], [w, 0], [0, h], [w, h]])
            output = self._perspective_transform(im_source=im_source, im_search=im_search, src=src, dst=dst)
        except cv2.error as err:
            raise PerspectiveTransformError(err)

        # img = im_source.clone().data
        # cv2.polylines(img, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
        # Image(img).imshow()
        # cv2.waitKey(0)

        rect = self._get_perspective_area_rect(im_source=im_source, src=src)
        return output, rect

    @staticmethod
    def _target_image_crop(img, rect):
        """
        Capture target image

        Args:
            img: image
            rect: Image range

        Returns:
            cropped image
        """
        try:
            target_img = img.crop(rect)
        except OverflowError:
            raise MatchResultError(f"Target area({rect}) out of screen{img.size}")
        return target_img

    def _cal_confidence(self, im_source, im_search, rgb):
        """
        Scale the screenshot and the recognition result to the same size, and calculate the reliability

        Args:
             im_source: the image to be matched
             im_search: image template
             rgb: whether to use the rgb channel for verification

        Returns:

        """
        h, w = im_source.size
        im_search = im_search.resize(w, h)
        if rgb:
            confidence = self.template.cal_rgb_confidence(im_source=im_source, im_search=im_search)
        else:
            confidence = self.template.cal_ccoeff_confidence(im_source=im_source, im_search=im_search)

        confidence = (1 + confidence) / 2
        return confidence

    def input_image_check(self, im_source, im_search):
        im_source = self._image_check(im_source)
        im_search = self._image_check(im_search)

        if im_source.place != im_search.place:
            raise InputImageError(
                'image type must be same, source={}, search={}'.format(im_source.place, im_search.place))
        elif im_source.dtype != im_search.dtype:
            raise InputImageError(
                'image data type must be same, source={}, search={}'.format(im_source.dtype, im_search.dtype))
        elif im_source.channels != im_search.channels:
            raise InputImageError(
                'image channel must be same, source={}, search={}'.format(im_source.channels, im_search.channels))

        return im_source, im_search

    def _image_check(self, data):
        if not isinstance(data, Image):
            data = Image(data, dtype=self.Dtype)

        if data.place not in self.Place:
            raise TypeError(f'{self.METHOD_NAME}method,Image type must be(Place.UMat, Place.Ndarray)')
        return data

    @staticmethod
    def _find_homography(sch_pts, src_pts):
        """
        When there are multiple sets of feature point pairs, obtain the unidirectional matrix
        """
        try:
            # M, mask = cv2.findHomography(sch_pts, src_pts, cv2.RANSAC)
            M, mask = cv2.findHomography(sch_pts, src_pts, cv2.RANSAC, 4.0, None, 2000, 0.99)
        except cv2.error:
            import traceback
            traceback.print_exc()
            raise HomographyError("OpenCV error in _find_homography()...")
        else:
            if mask is None:
                raise HomographyError("In _find_homography(), find no mask...")
            else:
                return M, mask

    @staticmethod
    def _perspective_transform(im_source, im_search, src, dst):
        """
        Calculate the perspective transformation according to the
        four pairs of corresponding points, and crop the corresponding picture

        Args:
             im_source: the image to be matched
             im_search: template to be matched
             src: The coordinates of the corresponding quad vertices in the target
                  image (upper left, upper right, lower left, lower right)
             dst: coordinates of the quad vertices in the source image (upper left,
                  upper right, lower left, lower right)

        Returns:

        """
        h, w = im_search.size
        matrix = cv2.getPerspectiveTransform(src=src, dst=dst)
        # warpPerspective https://github.com/opencv/opencv/issues/11784
        output = im_source.warpPerspective(matrix, size=(w, h), flags=cv2.INTER_CUBIC)

        return output

    @staticmethod
    def _get_perspective_area_rect(im_source, src):
        """
        According to the coordinates of the four vertices
        of the rectangle, obtain the largest circumscribed rectangle in the original image

        Args:
            im_source: image to be matched
            src: the coordinates of the corresponding quadrilateral vertices in the target image

        Returns:
            Maximum circumscribed rectangle
        """
        h, w = im_source.size

        x = [int(i[0]) for i in src]
        y = [int(i[1]) for i in src]
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        # Selecting the target rectangular area may be out of bounds,
        # and directly set it as the boundary when the boundary is exceeded:
        # If it exceeds the left boundary, it takes 0, if it exceeds the right boundary,
        # it takes w_s-1, if it exceeds the lower boundary, it takes 0, and if it exceeds
        # the upper boundary, it takes h_s-1.
        # When x_min is less than 0, take 0. When x_max is less than 0, take 0.
        x_min, x_max = int(max(x_min, 0)), int(max(x_max, 0))
        # When x_min is greater than w_s, the value is w_s-1. When x_max is greater than w_s-1, take w_s-1。
        x_min, x_max = int(min(x_min, w - 1)), int(min(x_max, w - 1))
        # When y_min is less than 0, take 0. When y_max is less than 0, take 0.
        y_min, y_max = int(max(y_min, 0)), int(max(y_max, 0))
        # When y_min is greater than h_s, the value is h_s-1. When y_max is greater than h_s-1, take h_s-1.
        y_min, y_max = int(min(y_min, h - 1)), int(min(y_max, h - 1))
        rect = Rect(x=x_min, y=y_min, width=(x_max - x_min), height=(y_max - y_min))
        return rect
