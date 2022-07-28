#! usr/bin/python
# -*- coding:utf-8 -*-
""" opencv matchTemplate"""
import warnings
import cv2
import numpy as np
from baseImage import Image, Rect
from baseImage.constant import Place


from typing import Union, Any, Tuple, Type


class MatchTemplate(object):
    METHOD_NAME: str = 'tpl'
    Dtype: Type[np.uint8] = np.uint8
    Place: tuple = (Place.Ndarray, )

    def __init__(self, threshold: Union[int, float] = 0.8, rgb: bool = True):
        self.threshold: Union[int, float] = threshold
        self.rgb: bool = rgb
        self.matcher: cv2.matchTemplate = cv2.matchTemplate

    def find_best_result(self, im_source: Image, im_search: Image, threshold: Union[int, float] = None, rgb: bool = None) -> dict: ...

    def find_all_results(self, im_source: Image, im_search: Image, threshold: Union[int, float] = None, rgb: bool = None, max_count: int = 10) -> list: ...

    def _get_template_result_matrix(self, im_source: Image, im_search: Image) -> Image: ...

    def input_image_check(self, im_source: Any, im_search: Any) -> Image: ...

    def _image_check(self, data: Union[str, bytes, np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat, Image]) -> Image: ...

    @staticmethod
    def minMaxLoc(result: np.ndarray) -> Tuple[float, float, Tuple[int, int], Tuple[int, int]]: ...

    def match(self, img1: np.ndarray, img2: np.ndarray) -> np.ndarray: ...

    def cal_confidence(self, im_source: Image, im_search: Image, crop_rect: Rect, max_val: float, rgb: bool) -> float: ...

    def cal_rgb_confidence(self, im_source: Image, im_search: Image) -> float: ...

    def cal_ccoeff_confidence(self, im_source: Image, im_search: Image) -> float: ...

    def _get_confidence_from_matrix(self, img_crop: Image, im_search: Image, max_val: float, rgb: bool) -> float: ...


class CudaMatchTemplate(MatchTemplate):
    METHOD_NAME: str = 'tpl'
    Dtype: Type[np.uint8] = np.uint8
    Place: tuple = Place.GpuMat

    @staticmethod
    def minMaxLoc(result: cv2.cuda.GpuMat) -> tuple:...

    def match(self, img1: cv2.cuda.GpuMat, img2: cv2.cuda.GpuMat) -> cv2.cuda.GpuMat: ...
