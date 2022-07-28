#! usr/bin/python
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from baseImage import Image, Rect

from image_registration.matching import MatchTemplate
from image_registration.utils import (generate_result, get_keypoint_from_matches, keypoint_distance, rectangle_transform)
from image_registration.exceptions import (NoEnoughPointsError, PerspectiveTransformError, HomographyError, MatchResultError,
                                           InputImageError)
from typing import List


class BaseKeypoint(object):
    FILTER_RATIO = 1
    METHOD_NAME = None
    Dtype = None
    Place = None
    template = MatchTemplate()

    def __init__(self, threshold=0.8, rgb=True, **kwargs):
        """
        初始化

        Args:
            threshold: 识别阈值(0~1)
            rgb: 是否使用rgb通道进行校验
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
        通过特征点匹配,在im_source中找到最符合im_search的范围

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            threshold: 识别阈值(0~1)
            rgb: 是否使用rgb通道进行校验

        Returns:

        """
        max_count = 1
        ret = self.find_all_results(im_source=im_source, im_search=im_search, threshold=threshold, rgb=rgb,
                                    max_count=max_count, **kwargs)
        if ret:
            return ret[0]
        return None

    def find_all_results(self, im_source, im_search, threshold=None, rgb=None, max_count=10, max_iter_counts=20, distance_threshold=150):
        """
        通过特征点匹配,在im_source中找到全部符合im_search的范围

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            threshold: 识别阈值(0~1)
            rgb: 是否使用rgb通道进行校验
            max_count: 最多可以返回的匹配数量
            max_iter_counts: 最大的搜索次数,需要大于max_count
            distance_threshold: 距离阈值,特征点(first_point)大于该阈值后,不做后续筛选

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
        # 在特征点集中,匹配最接近的特征点
        matches = np.array(self.match_keypoint(des_sch=des_sch, des_src=des_src))
        kp_sch_point = np.array([(kp.pt[0], kp.pt[1], kp.angle) for kp in kp_sch])
        kp_src_matches_point = np.array([[(*kp_src[dMatch.trainIdx].pt, kp_src[dMatch.trainIdx].angle)
                                          if dMatch else np.nan for dMatch in match] for match in matches])
        _max_iter_counts = 0
        src_pop_list = []
        while True:
            # 这里没有用matches判断nan, 是因为类型不对
            if (np.count_nonzero(~np.isnan(kp_src_matches_point)) == 0) or (len(result) == max_count) or (_max_iter_counts >= max_iter_counts):
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
                                                            kp_sch=kp_sch, good=filtered_good_point, angle=angle, rgb=rgb)
                # print(f'good:{len(filtered_good_point)}, rect={rect}, confidence={confidence}')
            except PerspectiveTransformError:
                pass
            finally:

                if rect and confidence >= threshold:
                    br, tl = rect.br, rect.tl
                    # 移除改范围内的所有特征点 ??有可能因为透视变换的原因，删除了多余的特征点
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

        # 一下代码用于删除目标图片中的特征点,以后会用
        # src_pop_list = list(set(src_pop_list))
        # src_pop_list.sort(reverse=True)
        # mask = np.ones(len(des_src), dtype=bool)
        # for v in src_pop_list:
        #     kp_src.pop(v)
        #     mask[v] = False
        #
        # des_src = des_src[mask, ...]
        return result

    def get_keypoint_and_descriptor(self, image):
        """
        获取图像关键点(keypoint)与描述符(descriptor)

        Args:
            image: 待检测的灰度图像

        Returns:

        """
        if image.channels == 3:
            image = image.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            image = image.data
        keypoint, descriptor = self.detector.detectAndCompute(image, None)

        if len(keypoint) < 2:
            raise NoEnoughPointsError('{} detect not enough feature points in input images'.format(self.METHOD_NAME))
        return keypoint, descriptor

    @staticmethod
    def filter_good_point(matches, kp_src, kp_sch, kp_sch_point, kp_src_matches_point):
        """ 筛选最佳点 """
        # 假设第一个点,及distance最小的点,为基准点
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

        # 计算模板图像上,该点与其他特征点的旋转角
        first_good_point_sch_origin_angle = get_points_origin_angle(kp_sch_point[:, 0], kp_sch_point[:, 1],
                                                                    first_good_point_query)

        # 计算目标图像中,该点与其他特征点的夹角
        kp_sch_rotate_angle = kp_sch_point[:, 2] + first_good_point_angle
        kp_sch_rotate_angle = np.where(kp_sch_rotate_angle >= 360, kp_sch_rotate_angle - 360, kp_sch_rotate_angle)
        kp_sch_rotate_angle = kp_sch_rotate_angle.reshape(kp_sch_rotate_angle.shape + (1,))

        kp_src_angle = kp_src_matches_point[:, :, 2]
        good_point = np.array([matches[index][array[0]] for index, array in
                               enumerate(np.argsort(np.abs(kp_src_angle - kp_sch_rotate_angle)))])

        # 计算各点以first_good_point为原点的旋转角
        good_point_nan = (np.nan, np.nan)
        good_point_pt = np.array([good_point_nan if dMatch is np.nan else (*kp_src[dMatch.trainIdx].pt, )
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
        特征点匹配

        Args:
            des_src: 待匹配图像的描述符集
            des_sch: 图片模板的描述符集
            k(int): 获取多少匹配点

        Returns:
            List[List[cv2.DMatch]]: 包含最匹配的描述符
        """
        # k=2表示每个特征点取出2个最匹配的对应点
        matches = self.matcher.knnMatch(des_sch, des_src, k)
        return matches

    def get_good_in_matches(self, matches):
        """
        特征点过滤

        Args:
            matches: 特征点集

        Returns:
            List[cv2.DMatch]: 过滤后的描述符集
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
        根据匹配点(good)数量,提取识别区域

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            kp_src: 关键点集
            kp_sch: 关键点集
            good: 描述符集
            angle: 旋转角度
            rgb: 是否使用rgb通道进行校验

        Returns:
            范围,和置信度
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
        特征点匹配数量等于1时,根据特征点的大小,对矩形进行缩放,并根据旋转角度,获取识别的目标图片

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            kp_sch: 关键点集
            kp_src: 关键点集
            good: 描述符集
            angle: 旋转角度

        Returns:
            待验证的图片
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
        特征点匹配数量等于2时,根据两点距离差,对矩形进行缩放,并根据旋转角度,获取识别的目标图片

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            kp_sch: 关键点集
            kp_src: 关键点集
            good: 描述符集
            angle: 旋转角度

        Returns:
            待验证的图片
        """
        sch_point = get_keypoint_from_matches(kp=kp_sch, matches=good, mode='query')
        src_point = get_keypoint_from_matches(kp=kp_src, matches=good, mode='train')

        sch_distance = keypoint_distance(sch_point[0], sch_point[1])
        src_distance = keypoint_distance(src_point[0], src_point[1])

        try:
            scale = src_distance / sch_distance  # 计算缩放大小
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
        特征点匹配数量等于3时,根据三个点组成的三角面积差,对矩形进行缩放,并根据旋转角度,获取识别的目标图片

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            kp_sch: 关键点集
            kp_src: 关键点集
            good: 描述符集
            angle: 旋转角度

        Returns:
            待验证的图片
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
            scale = src_area / sch_area  # 计算缩放大小
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
        特征点匹配数量>=4时,使用单矩阵映射,获取识别的目标图片

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            kp_sch: 关键点集
            kp_src: 关键点集
            good: 描述符集

        Returns:
            透视变换后的图片
        """

        sch_pts, img_pts = np.float32([kp_sch[m.queryIdx].pt for m in good]).reshape(
            -1, 1, 2), np.float32([kp_src[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
        # M是转化矩阵
        M, mask = self._find_homography(sch_pts, img_pts)
        # 计算四个角矩阵变换后的坐标，也就是在大图中的目标区域的顶点坐标:
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
        截取目标图像

        Args:
            img: 图像
            rect: 图像范围

        Returns:
            裁剪后的图像
        """
        try:
            target_img = img.crop(rect)
        except OverflowError:
            raise MatchResultError(f"Target area({rect}) out of screen{img.size}")
        return target_img

    def _cal_confidence(self, im_source, im_search, rgb):
        """
        将截图和识别结果缩放到大小一致,并计算可信度

        Args:
            im_source: 待匹配图像
            im_search: 图片模板
            rgb:是否使用rgb通道进行校验

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
            raise InputImageError('输入图片类型必须相同, source={}, search={}'.format(im_source.place, im_search.place))
        elif im_source.dtype != im_search.dtype:
            raise InputImageError('输入图片数据类型必须相同, source={}, search={}'.format(im_source.dtype, im_search.dtype))
        elif im_source.channels != im_search.channels:
            raise InputImageError('输入图片通道必须相同, source={}, search={}'.format(im_source.channels, im_search.channels))

        return im_source, im_search

    def _image_check(self, data):
        if not isinstance(data, Image):
            data = Image(data, dtype=self.Dtype)

        if data.place not in self.Place:
            raise TypeError(f'{self.METHOD_NAME}方法,Image类型必须为(Place.UMat, Place.Ndarray)')
        return data

    @staticmethod
    def _find_homography(sch_pts, src_pts):
        """
        多组特征点对时，求取单向性矩阵
        """
        try:
            # M, mask = cv2.findHomography(sch_pts, src_pts, cv2.RANSAC)
            M, mask = cv2.findHomography(sch_pts, src_pts, cv2.USAC_MAGSAC, 4.0, None, 2000, 0.99)
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
        根据四对对应点计算透视变换, 并裁剪相应图片

        Args:
            im_source: 待匹配图像
            im_search: 待匹配模板
            src: 目标图像中相应四边形顶点的坐标 (左上,右上,左下,右下)
            dst: 源图像中四边形顶点的坐标 (左上,右上,左下,右下)

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
        根据矩形四个顶点坐标,获取在原图中的最大外接矩形

        Args:
            im_source: 待匹配图像
            src: 目标图像中相应四边形顶点的坐标

        Returns:
            最大外接矩形
        """
        h, w = im_source.size

        x = [int(i[0]) for i in src]
        y = [int(i[1]) for i in src]
        x_min, x_max = min(x), max(x)
        y_min, y_max = min(y), max(y)
        # 挑选出目标矩形区域可能会有越界情况，越界时直接将其置为边界：
        # 超出左边界取0，超出右边界取w_s-1，超出下边界取0，超出上边界取h_s-1
        # 当x_min小于0时，取0。  x_max小于0时，取0。
        x_min, x_max = int(max(x_min, 0)), int(max(x_max, 0))
        # 当x_min大于w_s时，取值w_s-1。  x_max大于w_s-1时，取w_s-1。
        x_min, x_max = int(min(x_min, w - 1)), int(min(x_max, w - 1))
        # 当y_min小于0时，取0。  y_max小于0时，取0。
        y_min, y_max = int(max(y_min, 0)), int(max(y_max, 0))
        # 当y_min大于h_s时，取值h_s-1。  y_max大于h_s-1时，取h_s-1。
        y_min, y_max = int(min(y_min, h - 1)), int(min(y_max, h - 1))
        rect = Rect(x=x_min, y=y_min, width=(x_max - x_min), height=(y_max - y_min))
        return rect
