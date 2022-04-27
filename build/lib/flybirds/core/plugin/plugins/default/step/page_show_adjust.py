# -*- coding: utf-8 -*-
"""
Step implement of page adjust.
"""
import re

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_swipe as ps
import flybirds.utils.dsl_helper as dsl_helper


def swipe_to_ele(context, param1, param2, param3):
    poco_instance = gr.get_value("pocoInstance")

    param1_dict = dsl_helper.params_to_dic(param1)
    container_dsl_str = param1_dict["selector"]
    container_optional = {}
    if "path" in param1_dict.keys():
        container_optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        container_optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        container_optional["timeout"] = int(param1_dict["timeout"])
    else:
        container_optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_timeout", 10
        )

    param3_dict = dsl_helper.params_to_dic(param3)

    search_dsl_str = param3_dict["selector"]
    search_optional = {}
    if "path" in param3_dict.keys():
        search_optional["path"] = param3_dict["path"]
    elif "multiSelector" in param3_dict.keys():
        search_optional["multiSelector"] = param3_dict["multiSelector"]

    swipe_count = None
    if "swipeCount" in param3_dict.keys():
        swipe_count = int(param3_dict["swipeCount"])
    else:
        swipe_count = gr.get_frame_config_value("swipe_search_count", 5)

    screen_size = gr.get_device_size()

    direction = param2.strip()

    start_x = None
    if "startX" in param3_dict.keys():
        start_x = float(param3_dict["startX"])
    start_y = None
    if "startY" in param3_dict.keys():
        start_y = float(param3_dict["startY"])

    distance = None
    if "distance" in param3_dict.keys():
        distance = float(param3_dict["distance"])
    else:
        distance = gr.get_frame_config_value("swipe_search_distance", 0.3)

    duration = None
    if gr.get_frame_config_value("use_search_swipe_duration", False):
        duration = gr.get_frame_config_value("search_swipe_duration", 1)
    if "duration" in param3_dict.keys():
        duration = float(param3_dict["duration"])

    ps.air_bdd_swipe_search(
        poco_instance,
        container_dsl_str,
        container_optional,
        search_dsl_str,
        search_optional,
        swipe_count,
        screen_size,
        direction,
        start_x,
        start_y,
        distance,
        duration,
    )


def handle_str(un_handle_str):
    res = re.match(r"([\S\s]+),\s*[0-9_]+\s*", un_handle_str)
    if res is not None:
        return res.group(1)
    else:
        return un_handle_str


def full_screen_swipe_to_ele_aaa(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")
    handled_param2_temp = handle_str(param2)
    param2_dict = dsl_helper.params_to_dic(handled_param2_temp)

    search_dsl_str = param2_dict["selector"]
    search_optional = {}
    if "path" in param2_dict.keys():
        search_optional["path"] = param2_dict["path"]
    elif "multiSelector" in param2_dict.keys():
        search_optional["multiSelector"] = param2_dict["multiSelector"]

    swipe_count = None
    if "swipeCount" in param2_dict.keys():
        swipe_count = int(param2_dict["swipeCount"])
    else:
        swipe_count = gr.get_frame_config_value("swipe_search_count", 5)

    direction = param1.strip()

    screen_size = gr.get_device_size()

    start_x = None
    if "startX" in param2_dict.keys():
        start_x = float(param2_dict["startX"])
    start_y = None
    if "startY" in param2_dict.keys():
        start_y = float(param2_dict["startY"])

    distance = None
    if "distance" in param2_dict.keys():
        distance = float(param2_dict["distance"])
    else:
        distance = gr.get_frame_config_value("swipe_search_distance", 0.3)

    duration = None
    if gr.get_frame_config_value("use_search_swipe_duration", False):
        duration = gr.get_frame_config_value("search_swipe_duration", 1)
    if "duration" in param2_dict.keys():
        duration = float(param2_dict["duration"])

    ps.full_screen_swipe_search(
        poco_instance,
        search_dsl_str,
        search_optional,
        swipe_count,
        direction,
        screen_size,
        start_x,
        start_y,
        distance,
        duration,
    )
