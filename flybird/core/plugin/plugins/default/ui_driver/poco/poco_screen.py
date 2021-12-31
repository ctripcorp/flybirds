# -*- coding: utf-8 -*-
"""
Poco screen api
"""


def air_bdd_screen_size(poco_instance):
    """
    get the screen size of the device in use
    """
    return poco_instance.get_screen_size()
