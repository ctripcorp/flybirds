"""
android app core api implement
"""

from airtest.core.api import (time, start_app, stop_app, install, uninstall)

__open__ = ["App"]


class App:
    """Android App Class"""

    name = "android_app"

    def wake_app(self, package_name, wait_time=None):
        """
        Start the target application on device
        """
        start_app(package_name)
        if not (wait_time is None):
            time.sleep(wait_time)

    def shut_app(self, package_name):
        """
        关闭测试app
        """
        stop_app(package_name)

    def install_app(self, package_path, wait_time=None):
        """
        Install application on device

        :param package_path: the path to file to be installed on target device
        :param wait_time:
        :return: None
        :platforms: Android
        :Example:
            >>> install_app(r"D:\\demo\\test.apk")
        """
        i_result = install(package_path)
        if not (wait_time is None):
            time.sleep(wait_time)
        return i_result

    def uninstall_app(self, package_name, wait_time=None):
        """
        Uninstall application on device

        :param package_name: name of the package, see also `start_app`
        :param wait_time:
        :return: None
        :platforms: Android
        :Example:
            >>> uninstall("com.flyBirds.music")
        """
        uninstall(package_name)
        if not (wait_time is None):
            time.sleep(wait_time)
