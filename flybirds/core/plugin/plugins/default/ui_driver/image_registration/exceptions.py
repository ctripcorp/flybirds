#! usr/bin/python
# -*- coding:utf-8 -*-
class BaseError(Exception):
    def __init__(self, message="", *args, **kwargs):
        self.message = message

    def __repr__(self):
        return repr(self.message)


class NoModuleError(BaseError):
    """ Missing dependent module """


class CreateExtractorError(BaseError):
    """ An error occurred while create Extractor """


class NoEnoughPointsError(BaseError):
    """ detect not enough feature points in input images"""


class CudaSurfInputImageError(BaseError):
    """ The image size does not conform to CUDA standard """
    # https://stackoverflow.com/questions/42492060/surf-cuda-error-while-computing-descriptors-and-keypoints
    # https://github.com/opencv/opencv_contrib/blob/master/modules/xfeatures2d/src/surf.cuda.cpp#L151


class CudaOrbDetectorError(BaseError):
    """ An CvError when orb detector error occurred """


class HomographyError(BaseError):
    """ An error occurred while findHomography """


class MatchResultError(BaseError):
    """ An error occurred while result out of screen"""


class PerspectiveTransformError(BaseError):
    """ An error occurred while perspectiveTransform """


class InputImageError(BaseError):
    """ An error occurred while input image place/dtype/channels error"""
