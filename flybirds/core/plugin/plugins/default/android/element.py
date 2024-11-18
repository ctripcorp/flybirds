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

        attempts = 3
        while attempts > 0:
            try:
                poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
                log.info("AndroidUiautomationPoco init success")
                return poco
            except Exception as e:
                attempts -= 1
                time.sleep(1)
                if attempts == 0:
                    raise RuntimeError("Failed to initialize AndroidUiautomationPoco after 3 attempts") from e
