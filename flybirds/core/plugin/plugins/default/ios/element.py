# -*- coding: utf-8 -*-
"""
ios element core api implement
"""

from flybirds.core.plugin.plugins.default.base_element import BaseElement

__open__ = ["Element"]


class Element(BaseElement):
    """IOS Element Class"""

    name = "ios_element"

    def ui_driver_init(self):
        """
        Initialize the poco object
         :return:
        """
        from poco.drivers.ios import iosPoco

        ios_poco = iosPoco()
        return ios_poco
