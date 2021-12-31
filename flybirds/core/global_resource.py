# -*- coding: utf-8 -*-
"""
hold global config
"""
import logging

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
        "rerunFailInfo": None,
        "appEnvConfig": None,
        "packageName": None,
        "package_path": None,
        "deviceid": None,
        "platform": None,
        "run_info": None,
        "web_driver_agent": None
    }


def set_value(key, value):
    """
    pdate or add global attributes
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
    获取指定页面的schema url
    """
    if hasattr(_global_dict["configManage"].device_info, "device_id"):
        return _global_dict["configManage"].schema_info.all_schema_url[
            page_name
        ]
    return page_name


def get_app_package_name(def_value=None):
    """
    get the schema url of the specified page
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
