#! usr/bin/python
# -*- coding:utf-8 -*-
""" opencv matchTemplate"""
import warnings
import cv2
import numpy as np
from baseImage import Image, Rect
from baseImage.constant import Place

from .exceptions import MatchResultError, InputImageError
from .utils import generate_result


class MatchTemplate(object):
    METHOD_NAME = 'tpl'
    Dtype = np.uint8
    Place = (Place.Ndarray, )

    def __init__(self, threshold=0.8, rgb=True):
        """
        init

        Args:
             threshold: recognition threshold (0~1)
             rgb: whether to use the rgb channel for verification
        """
        assert 0 <= threshold <= 1, 'threshold value between 0 and 1'

        self.threshold = threshold
        self.rgb = rgb
        self.matcher = cv2.matchTemplate

    def find_best_result(self, im_source, im_search, threshold=None, rgb=None):
        """
        Template matching, return the range with the highest
        matching degree and greater than the threshold

        Args:
             im_source: the image to be matched
             im_search: image template
             threshold: recognition threshold (0~1)
             rgb: whether to use the rgb channel for verification

        Returns:
            generate_result
        """
        threshold = threshold or self.threshold
        rgb = rgb or self.rgb

        im_source, im_search = self.input_image_check(im_source, im_search)
        if im_source.channels == 1:
            rgb = False

        result = self._get_template_result_matrix(im_source=im_source, im_search=im_search)
        # Find the best match

        min_val, max_val, min_loc, max_loc = self.minMaxLoc(result.data)

        h, w = im_search.size
        # Seek credibility
        crop_rect = Rect(max_loc[0], max_loc[1], w, h)

        confidence = self.cal_confidence(im_source, im_search, crop_rect, max_val, rgb)
        # Returns None if the confidence is less than the threshold
        if confidence < (threshold or self.threshold):
            return None
        x, y = max_loc
        rect = Rect(x=x, y=y, width=w, height=h)
        return generate_result(rect, confidence)

    def find_all_results(self, im_source, im_search, threshold=None, rgb=None, max_count=10):
        """
        Template matching, return the range with matching degree greater
        than the threshold, and the maximum number does not exceed max_count

        Args:
             im_source: the image to be matched
             im_search: image template
             threshold:: recognition threshold (0~1)
             rgb: whether to use the rgb channel for verification
             max_count: maximum number of matches

        Returns:

        """
        threshold = threshold or self.threshold
        rgb = rgb or self.rgb

        im_source, im_search = self.input_image_check(im_source, im_search)
        if im_source.channels == 1:
            rgb = False

        result = self._get_template_result_matrix(im_source=im_source, im_search=im_search)
        results = []
        # Find the best match
        h, w = im_search.size
        while True:
            min_val, max_val, min_loc, max_loc = self.minMaxLoc(result.data)
            img_crop = im_source.crop(Rect(max_loc[0], max_loc[1], w, h))
            confidence = self._get_confidence_from_matrix(img_crop, im_search, max_val=max_val, rgb=rgb)
            x, y = max_loc
            rect = Rect(x, y, w, h)

            if (confidence < (threshold or self.threshold)) or len(results) >= max_count:
                break
            results.append(generate_result(rect, confidence))
            result.rectangle(rect=Rect(int(max_loc[0] - w / 2), int(max_loc[1] - h / 2), w, h), color=(0, 0, 0), thickness=-1)

        return results if results else None

    def _get_template_result_matrix(self, im_source, im_search):
        """Get the result matrix of template matching."""
        if im_source.channels == 3:
            i_gray = im_source.cvtColor(cv2.COLOR_BGR2GRAY).data
            s_gray = im_search.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            i_gray = im_source.data
            s_gray = im_search.data

        result = self.match(i_gray, s_gray)
        result = Image(data=result, dtype=np.float32, clone=False, place=im_source.place)
        return result

    def input_image_check(self, im_source, im_search):
        im_source = self._image_check(im_source)
        im_search = self._image_check(im_search)

        if im_source.place != im_search.place:
            raise InputImageError('image type must be same, source={}, search={}'.format(im_source.place, im_search.place))
        elif im_source.dtype != im_search.dtype:
            raise InputImageError('image data type must be same, source={}, search={}'.format(im_source.dtype, im_search.dtype))
        elif im_source.channels != im_search.channels:
            raise InputImageError('image channel must be same, source={}, search={}'.format(im_source.channels, im_search.channels))

        if im_source.place == Place.UMat:
            warnings.warn('Umat has error,will clone new image with np.ndarray '
                          '(https://github.com/opencv/opencv/issues/21788)')
            im_source = Image(im_source, place=Place.Ndarray, dtype=im_source.dtype)
            im_search = Image(im_search, place=Place.Ndarray, dtype=im_search.dtype)

        return im_source, im_search

    def _image_check(self, data):
        if not isinstance(data, Image):
            data = Image(data, dtype=self.Dtype)

        if data.place not in self.Place:
            raise TypeError('Image type must be(Place.UMat, Place.Ndarray)')
        return data

    @staticmethod
    def minMaxLoc(result):
        return cv2.minMaxLoc(result)

    def match(self, img1, img2):
        return self.matcher(img1, img2, cv2.TM_CCOEFF_NORMED)

    def cal_confidence(self, im_source, im_search, crop_rect, max_val, rgb):
        """
        Scale the screenshot and the recognition result
        to the same size, and calculate the reliability

        Args:
             im_source: the image to be matched
             im_search: image template
             crop_rect: The area that needs to be intercepted in im_source
             max_val: the maximum value obtained by matchTemplate
             rgb: whether to use the rgb channel for verification

        Returns:
            float: credibility(0~1)
        """
        try:
            target_img = im_source.crop(crop_rect)
        except OverflowError:
            raise MatchResultError(f"Target area({crop_rect}) out of screen{im_source.size}")
        confidence = self._get_confidence_from_matrix(target_img, im_search, max_val, rgb)
        return confidence

    def cal_rgb_confidence(self, im_source, im_search):
        """
        Calculate the confidence of two picture rgb three-channel

        Args:
             im_source: the image to be matched
             im_search: image template

        Returns:
            float: minimum confidence
        """
        # im_search = im_search.copyMakeBorder(10, 10, 10, 10, cv2.BORDER_REPLICATE)
        #
        # img_src_hsv = im_source.cvtColor(cv2.COLOR_BGR2HSV)
        # img_sch_hsv = im_search.cvtColor(cv2.COLOR_BGR2HSV)

        src_split = im_source.split()
        sch_split = im_search.split()

        # Calculate the confidence of the BGR three channels and store it in bgr_confidence:
        bgr_confidence = [0, 0, 0]
        for i in range(3):
            res_temp = self.match(sch_split[i], src_split[i])
            min_val, max_val, min_loc, max_loc = self.minMaxLoc(res_temp)
            bgr_confidence[i] = max_val

        return min(bgr_confidence)

    def cal_ccoeff_confidence(self, im_source, im_search):
        if im_source.channels == 3:
            img_src_gray = im_source.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            img_src_gray = im_source.data

        if im_search.channels == 3:
            img_sch_gray = im_search.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            img_sch_gray = im_search.data

        res_temp = self.match(img_sch_gray, img_src_gray)
        min_val, max_val, min_loc, max_loc = self.minMaxLoc(res_temp)
        return max_val

    def _get_confidence_from_matrix(self, img_crop, im_search, max_val, rgb):
        """Find confidence from the result matrix."""
        # Seek credibility:
        if rgb:
            # If there is color verification, perform
            # BGR three-channel verification on the target area:
            confidence = self.cal_rgb_confidence(img_crop, im_search)
        else:
            confidence = max_val
        return confidence


