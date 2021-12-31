# -*- coding: utf-8 -*-
"""
android device core api implement.
"""
from airtest.core.api import (connect_device, shell)

__open__ = ["Device"]


class Device:
    """Android Device Class"""

    name = "android_device"

    def device_connect(self, device_id):
        """
        Initialize device with uri, and set as current device.
        """
        dev = connect_device("Android:///" + device_id)
        return dev

    def use_shell(self, cmd):
        """
        Start remote shell in the target device and execute the command
        :platforms: Android
        """
        return shell(cmd)
