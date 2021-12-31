# -*- coding: utf-8 -*-
"""
android step implements class
"""

from flybirds.core.plugin.plugins.default.app_base_step import AppBaseStep
from flybirds.core.plugin.plugins.default.step.app \
    import (install_app, uninstall_app, to_app_home, app_login, app_logout,
            return_pre_page)
from flybirds.core.plugin.plugins.default.step.schema import jump_to_page

__open__ = ["Step"]


class Step(AppBaseStep):
    """Android Step Class"""

    name = "android_step"

    def install_app(self, context, param):
        install_app(context, param)

    def uninstall_app(self, context, param):
        uninstall_app(context, param)

    def to_app_home(self, context):
        to_app_home(context)

    def app_login(self, context, param1, param2):
        app_login(context, param1, param2)

    def app_logout(self, context):
        app_logout(context)

    def return_pre_page(self, context):
        return_pre_page(context)

    def jump_to_page(self, context, param):
        jump_to_page(context, param)
