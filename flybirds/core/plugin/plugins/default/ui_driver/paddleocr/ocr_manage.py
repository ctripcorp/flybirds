# -*- coding: utf-8 -*-
"""
Poco manage api
"""
from flybirds.core.global_context import GlobalContext as g_Context


def ocr_init():
    """
    Initialize the paddleocr object
     :return:
    """
    from paddleocr import PaddleOCR
    # Paddleocr support languages
    # example`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True,
                    lang="ch")  # need to run only once to download and load model into memory

    return ocr

