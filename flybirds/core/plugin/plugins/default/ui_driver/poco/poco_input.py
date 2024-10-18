# -*- coding: utf-8 -*-
"""
Poco element input
"""
from airtest.core.api import text, time
from airtest.core.helper import G
import subprocess

import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.ui_driver.poco import poco_manage


def air_bdd_input(
        poco, select_dsl_str, optional, input_str, after_input_wait=None
):
    """
    input text
    :param poco:
    :param select_dsl_str:
    :param input_str:
    :param optional:
    :param after_input_wait:
    :return:
    """
    poco_ele.wait_exists(poco, select_dsl_str, optional)
    poco_object = poco_manage.create_poco_object_by_dsl(
        poco, select_dsl_str, optional
    )
    try:
        poco_object.set_text(input_str)
    except Exception as input_error:
        try:
            log.info(f"air_bdd_input has error:{str(input_error)} change ime to yosemite")
            package_name = "com.netease.nie.yosemite"
            if not check_app_status(package_name):
                G.DEVICE.yosemite_ime.start()
                time.sleep(30)
                # G.DEVICE.start_app(package_name, '/.ime.ImeService')
                log.info("start yosemite ime successfully")
            poco_object.click()
            text(input_str)
        except Exception as input_error:
            log.error(f"air_bdd_input has error:{str(input_error)}")
            raise input_error

    if not (after_input_wait is None):
        time.sleep(after_input_wait)


def is_app_installed(package_name):
    try:
        result = subprocess.run(['adb', 'shell', 'pm', 'list', 'packages'], capture_output=True, text=True)
        return package_name in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error checking if app is installed: {e}")
        return False


def is_app_running(package_name):
    try:
        result = subprocess.run(['adb', 'shell', 'ps'], capture_output=True, text=True)
        return package_name in result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error checking if app is running: {e}")
        return False


def check_app_status(package_name):
    package_name = "com.netease.nie.yosemite"
    if is_app_installed(package_name) and is_app_running(package_name):
        log.info(f"{package_name} is installed and running")
        return True
    else:
        return False

