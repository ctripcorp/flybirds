#! usr/bin/python
# -*- coding:utf-8 -*-
import cv2
import numpy as np
from baseImage.constant import Place

from image_registration.matching.template import CudaMatchTemplate
from image_registration.matching.keypoint.base import BaseKeypoint
from image_registration.exceptions import NoEnoughPointsError, CudaOrbDetectorError
from typing import Union


class ORB(BaseKeypoint):
    METHOD_NAME = 'ORB'
    Dtype = np.uint8
    Place = (Place.UMat, Place.Ndarray)

    def __init__(self, threshold: Union[int, float] = 0.8, rgb: bool = True, **kwargs):
        super().__init__(threshold=threshold, rgb=rgb, **kwargs)
        self.descriptor = self.create_descriptor()

    def create_matcher(self, **kwargs):
        """
        创建特征点匹配器

        Returns:
            cv2.FlannBasedMatcher
        """
        matcher = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE_HAMMING)
        return matcher

    def create_detector(self, **kwargs):
        nfeatures = kwargs.get('nfeatures', 50000)
        scaleFactor = kwargs.get('scaleFactor', 1.2)
        nlevels = kwargs.get('nlevels', 8)
        edgeThreshold = kwargs.get('edgeThreshold', 31)
        firstLevel = kwargs.get('firstLevel', 0)
        WTA_K = kwargs.get('WTA_K', 2)
        scoreType = kwargs.get('scoreType', cv2.ORB_HARRIS_SCORE)
        patchSize = kwargs.get('patchSize', 31)
        fastThreshold = kwargs.get('fastThreshold', 20)

        params = dict(
            nfeatures=nfeatures, scaleFactor=scaleFactor, nlevels=nlevels,
            edgeThreshold=edgeThreshold, firstLevel=firstLevel, WTA_K=WTA_K,
            scoreType=scoreType, patchSize=patchSize, fastThreshold=fastThreshold,
        )
        detector = cv2.ORB_create(**params)
        return detector

    @staticmethod
    def create_descriptor():
        # https://docs.opencv.org/master/d7/d99/classcv_1_1xfeatures2d_1_1BEBLID.html
        # https://github.com/iago-suarez/beblid-opencv-demo
        descriptor = cv2.xfeatures2d.BEBLID_create(0.75)
        return descriptor

    def get_keypoint_and_descriptor(self, image):
        if image.channels == 3:
            image = image.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            image = image.data

        keypoints = self.detector.detect(image, None)
        keypoints, descriptors = self.descriptor.compute(image, keypoints)

        if len(keypoints) < 2:
            raise NoEnoughPointsError('{} detect not enough feature points in input images'.format(self.METHOD_NAME))
        return keypoints, descriptors


class CUDA_ORB(BaseKeypoint):
    METHOD_NAME = 'CUDA_ORB'
    Dtype = np.uint8
    Place = (Place.GpuMat,)

    def __init__(self, threshold: Union[int, float] = 0.8, rgb: bool = True, **kwargs):
        super().__init__(threshold=threshold, rgb=rgb, **kwargs)
        self.template = CudaMatchTemplate(threshold=threshold, rgb=rgb)

    def create_matcher(self, **kwargs):
        """
        创建特征点匹配器

        Returns:
            cv2.FlannBasedMatcher
        """
        matcher = cv2.cuda.DescriptorMatcher_createBFMatcher(cv2.NORM_HAMMING)
        return matcher

    def create_detector(self, **kwargs):
        nfeatures = kwargs.get('nfeatures', 50000)
        scaleFactor = kwargs.get('scaleFactor', 1.2)
        nlevels = kwargs.get('nlevels', 8)
        edgeThreshold = kwargs.get('edgeThreshold', 31)
        firstLevel = kwargs.get('firstLevel', 0)
        WTA_K = kwargs.get('WTA_K', 2)
        scoreType = kwargs.get('scoreType', cv2.ORB_HARRIS_SCORE)
        patchSize = kwargs.get('patchSize', 31)
        fastThreshold = kwargs.get('fastThreshold', 20)
        blurForDescriptor = kwargs.get('blurForDescriptor', False)

        params = dict(
            nfeatures=nfeatures, scaleFactor=scaleFactor, nlevels=nlevels,
            edgeThreshold=edgeThreshold, firstLevel=firstLevel, WTA_K=WTA_K,
            scoreType=scoreType, patchSize=patchSize, fastThreshold=fastThreshold,
            blurForDescriptor=blurForDescriptor
        )

        detector = cv2.cuda.ORB_create(**params)
        return detector

    def get_keypoint_and_descriptor(self, image):
        if image.channels == 3:
            image = image.cvtColor(cv2.COLOR_BGR2GRAY).data
        else:
            image = image.data

        try:
            keypoints, descriptors = self.detector.detectAndComputeAsync(image, None)
        except cv2.error:
            # https://github.com/opencv/opencv/issues/10573
            raise CudaOrbDetectorError('{} detect error, Try adjust detector params'.format(self.METHOD_NAME))
        else:
            keypoints = self.detector.convert(keypoints)

        if len(keypoints) < 2:
            raise NoEnoughPointsError('{} detect not enough feature points in input images'.format(self.METHOD_NAME))
        return keypoints, descriptors
