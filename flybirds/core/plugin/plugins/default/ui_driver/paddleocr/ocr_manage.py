# -*- coding: utf-8 -*-
"""
Poco manage api
"""
import flybirds.core.global_resource as gr


def ocr_init():
    """
    Initialize the paddleocr object
     :return:
    """
    ocr_lang = gr.get_app_config_value("ocr_lang")
    from paddleocr import PaddleOCR
    # Paddleocr support languages
    # example`ch`, `en`, `fr`, `german`, `korean`, `japan`
    ocr = PaddleOCR(use_angle_cls=True,
                    lang=ocr_lang)  # need to run only once to download and load model into memory

    return ocr

