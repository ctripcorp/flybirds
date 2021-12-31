# -*- coding: utf-8 -*-
"""
ios app core api implement
"""

from airtest.core.api import (time, start_app, stop_app)

__open__ = ["App"]


class App:
    """IOS App Class"""

    name = "ios_app"

    def wake_app(self, package_name, wait_time=None):
        """
        Start the target application on device
        """
        start_app(package_name)
        if not (wait_time is None):
            time.sleep(wait_time)

    def shut_app(self, package_name):
        """
        stop the target application on device
        """
        stop_app(package_name)

    def install_app(self, package_path, wait_time=None):
        raise NotImplementedError

    def uninstall_app(self, package_name, wait_time=None):
        raise NotImplementedError
