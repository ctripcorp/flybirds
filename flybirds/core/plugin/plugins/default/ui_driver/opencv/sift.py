#! usr/bin/python
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from baseImage.constant import Place

from .base import BaseKeypoint


class SIFT(BaseKeypoint):
    FLANN_INDEX_KDTREE = 0
    METHOD_NAME = 'SIFT'
    Dtype = np.uint8
    Place = (Place.UMat, Place.Ndarray)

    def create_matcher(self, **kwargs) -> cv2.DescriptorMatcher:
        """
        Create a feature point matcher

        Returns:
            cv2.FlannBasedMatcher
        """
        index_params = {'algorithm': self.FLANN_INDEX_KDTREE, 'tree': 5}
        # Specifies the number of recursive traversals.
        # The higher the value, the more accurate the result, but the more time it takes
        search_params = {'checks': 50}
        matcher = cv2.FlannBasedMatcher(index_params, search_params)
        return matcher

    def create_detector(self, **kwargs) -> cv2.SIFT:
        nfeatures = kwargs.get('nfeatures', 0)
        nOctaveLayers = kwargs.get('nOctaveLayers', 3)
        contrastThreshold = kwargs.get('contrastThreshold', 0.04)
        edgeThreshold = kwargs.get('edgeThreshold', 10)
        sigma = kwargs.get('sigma', 1.6)

        detector = cv2.SIFT_create(nfeatures=nfeatures, nOctaveLayers=nOctaveLayers, contrastThreshold=contrastThreshold,
                                   edgeThreshold=edgeThreshold, sigma=sigma)
        return detector
