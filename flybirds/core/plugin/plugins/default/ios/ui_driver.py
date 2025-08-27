# -*- coding: utf-8 -*-
"""
ui driver
"""
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage import \
    poco_init
from flybirds.core.plugin.plugins.default.ui_driver.paddleocr.ocr_manage import \
    ocr_init
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_screen import \
    air_bdd_screen_size

__open__ = ["UIDriver"]


class UIDriver:
    """
    ui driver
    """
    name = "ios_ui_driver"

    @staticmethod
    def init_driver():
        return poco_init()

    @staticmethod
    def init_ocr(lang=None):
        return ocr_init(lang)

    @staticmethod
    def air_bdd_screen_size(dr_instance):
        return air_bdd_screen_size(dr_instance)

    @staticmethod
    def close_driver():
        screen_record = gr.get_value("screenRecord")
        try:
            log.info("close screen record")
            if screen_record is not None and hasattr(screen_record, "destroy"):
                screen_record.destroy()
        except Exception as e:
            log.info(f"clear driver error :{e}")
        if screen_record is not None and hasattr(screen_record, "destroy"):
            screen_record.destroy()
