# -*- coding: utf-8 -*-
"""
ui driver proxy
"""
from flybirds.core.global_context import GlobalContext


def poco_init():
    return GlobalContext.ui_driver.poco_init()


def air_bdd_screen_size(dr_instance):
    return GlobalContext.ui_driver.air_bdd_screen_size(dr_instance)
