# -*- coding: utf-8 -*-
"""
This module contains the App Core APIs.
"""

from flybirds.core.global_context import GlobalContext as g_context

"""
App Apis
"""


def wake_app(package_name, wait_time=None):
    """
    Start the target application on device
    :param package_name: package name
    :param wait_time:  wait time
    :return:
    """
    g_context.app.wake_app(package_name, wait_time)


def shut_app(package_name):
    """
    Stop the target application on device
    :param package_name: package name
    :return:
    """
    g_context.app.shut_app(package_name)


def install_app(package_path, wait_time=None):
    """
    Install application on device

    :param package_path: the path to file to be installed on target device
    :param wait_time:
    :return: None
    :platforms: Android
    :Example:
        >>> install_app(r"D:\\demo\\test.apk")
    """
    return g_context.app.install_app(package_path, wait_time)


def uninstall_app(package_name, wait_time=None):
    """
    Uninstall application on device

    :param package_name: name of the package, see also `start_app`
    :param wait_time:
    :return: None
    :platforms: Android
    :Example:
        >>> uninstall_app("com.flyBirds.music")
    """
    g_context.app.uninstall_app(package_name, wait_time)
