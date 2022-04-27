# -*- coding: utf-8 -*-
"""
android Element core api implement
"""
from flybirds.core.plugin.plugins.default.base_element import BaseElement

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

        poco = AndroidUiautomationPoco(
            use_airtest_input=True, screenshot_each_action=False
        )
        return poco
