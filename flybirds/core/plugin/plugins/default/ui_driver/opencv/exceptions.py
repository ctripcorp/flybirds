#! usr/bin/python
# -*- coding:utf-8 -*-
class BaseError(Exception):
    def __init__(self, message="", *args, **kwargs):
        self.message = message

    def __repr__(self):
        return repr(self.message)


class NoEnoughPointsError(BaseError):
    """ detect not enough feature points in input images"""


class HomographyError(BaseError):
    """ An error occurred while findHomography """


class MatchResultError(BaseError):
    """ An error occurred while result out of screen"""


class PerspectiveTransformError(BaseError):
    """ An error occurred while perspectiveTransform """


class InputImageError(BaseError):
    """ An error occurred while input image place/dtype/channels error"""
