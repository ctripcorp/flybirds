# -*- coding: utf-8 -*-
"""
hold global config
"""
import logging

import flybirds.utils.flybirds_log as log

_global_dict = {}


def init_glb():
    """
    initialize global variables
    """
    global _global_dict
    _global_dict = {
        "configManage": None,
        "projectScript": None,
        "userData": {},
        "deviceInstance": None,
        "pocoInstance": None,
        "ocrInstance": None,
        "rerunFailInfo": None,
        "appEnvConfig": None,
        "packageName": None,
        "package_path": None,
        "deviceid": None,
        "platform": None,
        "run_info": None,
        "web_driver_agent": None,
        "playwright": None,
        "browser": None,
        "plugin_page": None,
        "interceptionRequest": {},
        "interceptionValues": {},
        "browser_context": None
    }


def set_value(key, value):
    """
    update or add global attributes
    """
    global _global_dict
    _global_dict[key] = value


def get_value(key, def_value=None):
    """
    get global attribute value
    """
    if key in _global_dict.keys():
        value = _global_dict[key]
        if value is not None:
            return value
    return def_value


def get_frame_config_value(key, def_value=None):
    """
    Get a value in the frame_info.json configuration file
    """
    if hasattr(_global_dict["configManage"].frame_info, key):
        value = getattr(_global_dict["configManage"].frame_info, key)
        if value is not None:
            return value
    return def_value


def get_app_config_value(key, def_value=None):
    """
    get a value in the app_info.json configuration file
    """
    if hasattr(_global_dict["configManage"].app_info, key):
        value = getattr(_global_dict["configManage"].app_info, key)
        if value is not None:
            return value
    return def_value


def get_flow_behave_value(key, def_value=None):
    """
    get a value in the flow_behave.json configuration file
    """
    if hasattr(_global_dict["configManage"].flow_behave, key):
        value = getattr(_global_dict["configManage"].flow_behave, key)
        if value is not None:
            return value
    return def_value


def get_device_id():
    """
    get the id of the device currently in use
    """
    if hasattr(_global_dict["configManage"].device_info, "device_id"):
        value = _global_dict["configManage"].device_info.device_id
        if value is not None:
            return value
    return _global_dict["deviceid"]


def get_web_driver_agent():
    """
    get the id of the device currently in use
    """
    if hasattr(_global_dict["configManage"].device_info,
               "web_driver_agent"):
        value = _global_dict["configManage"].device_info.web_driver_agent
        if value is not None:
            return value
    return _global_dict["web_driver_agent"]


def get_platform():
    """
    get the device platform currently in use
    """
    if hasattr(_global_dict["configManage"].device_info, "platform"):
        value = _global_dict["configManage"].device_info.platform
        if value is not None:
            return value
    return _global_dict["platform"]


def get_device_size(def_value=[1080, 1920]):
    """
    get the schema url of the specified page
    """
    if hasattr(_global_dict["configManage"].device_info, "screen_size"):
        value = _global_dict["configManage"].device_info.screen_size
        if value is not None:
            return value
    return def_value


def get_page_schema_url(page_name):
    """
    get the schema url of the page
    """
    all_schema_url = _global_dict["configManage"].schema_info.all_schema_url
    if all_schema_url is None:
        log.warn("[get_page_schema_url] cannot find schema_url.json file")
        return page_name
    page_url = all_schema_url.get(page_name)
    if page_url is None:
        log.warn(f"the schema_url.json has no schema configuration"
                 f" for [{page_name}]")
        return page_name
    if isinstance(page_url, str):
        return page_url
    platform = get_platform().lower()
    if page_url.get(platform) is None:
        raise Exception(
            f"The [{page_name}] has no schema configuration for the"
            f" [{platform}] platform in schema_url.json")
    return page_url.get(platform)


def get_app_package_name(def_value=None):
    """
    get the package name of the page
    """
    if hasattr(_global_dict["configManage"].app_info, "package_name"):
        value = _global_dict["configManage"].app_info.package_name
        if value is not None:
            return value
    return _global_dict["packageName"]


def get_app_package_path(def_value=None):
    """
    get the schema url of the specified page
    """
    if hasattr(_global_dict["configManage"].app_info, "package_path"):
        value = _global_dict["configManage"].app_info.package_path
        if value is not None:
            return value
    return _global_dict["package_path"]


def get_user_data(key, default_value=None):
    """
    get the data passed in by the user
    """
    return _global_dict["userData"].get(key, default_value)


def update_user_data(key, new_value):
    """
    update the data passed in by the user
    """
    _global_dict["userData"][key] = new_value


def get_screen_save_dir():
    """
    Or the directory where the screenshots are stored
    """
    if hasattr(_global_dict["configManage"].report_info, "screen_shot_dir"):
        return _global_dict["configManage"].report_info.screen_shot_dir
    else:
        return None


def get_log_level():
    """
    get the level of log output
    """
    if "_global_dict" in globals().keys():
        level = _global_dict["configManage"].log_config.level
    else:
        level = "info"
    switcher = {
        "fatal": logging.FATAL,
        "error": logging.ERROR,
        "warn": logging.WARNING,
        "info": logging.INFO,
        "debug": logging.DEBUG,
    }
    return switcher.get(level, logging.INFO)


def get_rerun_info(relevance_id):
    """
    get information about failure scenarios
    including failed screenshots, failed screen recordings,
     feature and scenario names
    """
    return _global_dict["rerunFailInfo"].get(relevance_id, None)


def get_env_config():
    """
    get current environment variables
    """
    return _global_dict["appEnvConfig"]


def get_run_info():
    """
    get run base info
    """
    return _global_dict["run_info"]


def get_web_info_value(key, def_value=None):
    """
    get a value in the web_info configuration
    """
    if hasattr(_global_dict["configManage"].web_info, key):
        value = getattr(_global_dict["configManage"].web_info, key)
        if value is not None:
            return value
    return def_value


def get_ele_locator(key):
    """
    Get the configuration value of the element locator for the current
    runtime platform
    """
    all_locators = _global_dict[
        "configManage"].ele_locator_info.all_ele_locator
    if all_locators is None:
        log.warn("[get_ele_locator] cannot find ele_locator.json file")
        return key
    ele_locator = all_locators.get(key)
    if ele_locator is None:
        log.debug(
            f"the ele_locator.json has no element locator configuration "
            f"for [{key}]")
        return key
    if isinstance(ele_locator, str):
        return ele_locator
    platform = get_platform().lower()
    if ele_locator.get(platform) is None:
        raise Exception(
            f"The [{key}] has no element locator configuration for the"
            f" [{platform}] platform in ele_locator.json")
    return ele_locator.get(platform)


def get_service_ignore_nodes(service):
    """
    Get the ignore nodes configuration value of the service interface
    """
    all_ignore_nodes = _global_dict[
        "configManage"].ignore_node_info.all_ignore_nodes
    if all_ignore_nodes is None:
        log.warn("[get_service_ignore_nodes] cannot find configuration value "
                 "from interfaceIgnoreConfig folder")
        return
    service_ignore_nodes = all_ignore_nodes.get(service)
    if service_ignore_nodes is None:
        log.info(f"interface service [{service}] has not set ignore nodes")
    return service_ignore_nodes


def get_paddle_fix_value():
    """
    get paddle_fix value in the paddleFixConfig.json configuration file
    """
    paddle_fix_nodes = _global_dict[
        "configManage"].paddle_fix_info.paddle_fix_node
    if len(paddle_fix_nodes) == 0:
        # log.info("paddle_fix_nodes not found")
        return None
    return paddle_fix_nodes
