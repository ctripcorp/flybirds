# -*- coding: utf-8 -*-
"""
ui driver
"""
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage import \
    poco_init
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_screen import \
    air_bdd_screen_size

__open__ = ["UIDriver"]


class UIDriver:
    name = "android_ui_driver"

    def poco_init(self):
        return poco_init()

    def air_bdd_screen_size(self, dr_instance):
        return air_bdd_screen_size(dr_instance)
