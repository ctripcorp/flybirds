# -*- coding: utf-8 -*-
"""
android screen record
"""
from flybirds.core.plugin.plugins.default.screen_record import ScreenRecord

__open__ = ["ScreenRecordInfo"]


class ScreenRecordInfo(ScreenRecord):
    name = "android_screen_record"
    instantiation_timing = "plugin"

    def __init__(self):
        ScreenRecord.__init__(self)
