# -*- coding: utf-8 -*-
"""
ios screen record
"""
from flybirds.core import global_resource as gr

__open__ = ["ScreenRecordInfo"]


class ScreenRecordInfo:
    name = "ios_screen_record"
    instantiation_timing = "plugin"

    def __init__(self):
        self.support = False
        self.start_time = None
        self.end_time = None
        self.process = None
        # 0 Just created 1 Reset state 2 Start recording
        self.status = 0

        self.use_airtest_record = gr.get_frame_config_value(
            "use_airtest_record", False
        )

    def reset(self):
        """
        Reset object
        """
        self.start_time = None
        self.end_time = None
        self.status = 1

    def destroy(self):
        """
        Destroy all recorded video processes after the task runs
        """
        pass

    def record_support(self):
        pass

    def start_record(self, timeout, bit_rate_level=1, bit_rate=None):
        """
        Start recording
        """
        pass

    def stop_record(self):
        """
        Stop the current screen recording
        """
        return None

    def link_record(self, scenario, step_index):
        """
        Associate screenshots to report
        """
        pass

    def copy_record(self, save_path):
        """
        Copy the screen recording from the mobile phone to the current client
        """
        pass

    def clear_record(self):
        """
        Delete the existing screen recording file
        """
        pass
