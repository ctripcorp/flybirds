#! usr/bin/python
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from typing import Union, Tuple, List
from baseImage import Image

from image_registration.matching.keypoint.base import BaseKeypoint


image_type = Union[str, bytes, np.ndarray, cv2.cuda.GpuMat, cv2.Mat, cv2.UMat, Image]
keypoint_type = Tuple[cv2.KeyPoint, ...]
matches_type = Tuple[Tuple[cv2.DMatch, ...], ...]
good_match_type = List[cv2.DMatch]


class AKAZE(BaseKeypoint):
    def __init__(self, threshold: Union[int, float] = 0.8, rgb: bool = True,
                 descriptor_type: int = cv2.AKAZE_DESCRIPTOR_MLDB, descriptor_size: int = 0,
                 descriptor_channels: int = 3, _threshold: float = 0.001, diffusivity: int = cv2.KAZE_DIFF_PM_G2,
                 nOctaveLayers: int = 4, nOctaves: int = 4): ...
