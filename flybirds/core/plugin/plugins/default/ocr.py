# -*- coding: utf-8 -*-
"""
Device ocr method.
"""

from PIL import Image
from paddleocr import PaddleOCR, draw_ocr

import flybirds.utils.flybirds_log as log


class BaseOcr:

    @staticmethod
    def image_ocr(img_path):
        # Paddleocr support languages
        # example`ch`, `en`, `fr`, `german`, `korean`, `japan`
        ocr = PaddleOCR(use_angle_cls=True,
                        lang="ch")  # need to run only once to download and load model into memory
        result = ocr.ocr(img_path, cls=True)
        for line in result:
            log.info(f"[image scan result] scan line info is:{line}")
        # show result
        image = Image.open(img_path).convert('RGB')
        boxes = [line[0] for line in result]
        txts = [line[1][0] for line in result]
        scores = [line[1][1] for line in result]
        im_show = draw_ocr(image, boxes, txts, scores, font_path='./fonts/simfang.ttf')
        im_show = Image.fromarray(im_show)
        im_show.save('result.jpg')
