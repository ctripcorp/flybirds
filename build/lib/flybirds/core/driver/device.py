# -*- coding: utf-8 -*-
"""
This module contains the device Core APIs.
"""
import flybirds.utils.flybirds_log as log

from flybirds.core.global_context import GlobalContext as g_Context


def device_connect(device_id):
    """
    Initialize device with uri, and set as current device.
    :param device_id: device id
    :return: device instance
    """
    dev = g_Context.device.device_connect(device_id)
    log.info("device connect info:{}".format(dev))
    return dev


def use_shell(cmd):
    """
    Start remote shell in the target device and execute the command
      :platforms: Android
    :param cmd:  command to be run on device, e.g. "ls /data/local/tmp"
    :return:
    """
    return g_Context.device.use_shell(cmd)
