# -*- coding: utf-8 -*-
"""
android Element core api implement
"""
import time

from flybirds.core.plugin.plugins.default.base_element import BaseElement
import flybirds.utils.flybirds_log as log

__open__ = ["Element"]


class Element(BaseElement):
    """Android Element Class"""

    name = "android_element"

    def ui_driver_init(self):
        """
        Initialize the poco object
         :return:
        """
        from poco.drivers.android.uiautomation import AndroidUiautomationPoco

        try:
            poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
            log.info("AndroidUiautomationPoco init success")
            return poco
        except Exception as e:
            # raise Exception(f"Failed to initialize AndroidUiautomationPoco {e}")
            log.error(f"Failed to initialize AndroidUiautomationPoco {e}")
