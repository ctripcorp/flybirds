# -*- coding: utf-8 -*-
"""
Element swipe
"""
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_swipe as ps
import flybirds.utils.dsl_helper as dsl_helper


def ele_swipe(context, param1, param2, param3):
    poco_instance = gr.get_value("pocoInstance")

    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    optional = {}
    if "path" in param1_dict.keys():
        optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    param3_dict = dsl_helper.params_to_dic(param3, "swipeNumber")

    start_point = [0.5, 0.5]
    if "startX" in param3_dict.keys():
        start_point[0] = float(param3_dict["startX"])
    if "startY" in param3_dict.keys():
        start_point[1] = float(param3_dict["startY"])

    screen_size = gr.get_device_size()

    direction = param2.strip()

    distance = float(param3_dict["swipeNumber"])

    duration = None
    if gr.get_frame_config_value("use_swipe_duration", False):
        duration = gr.get_frame_config_value("swipe_duration", 1)
    if "duration" in param3_dict.keys():
        duration = float(param3_dict["duration"])

    ready_time = gr.get_frame_config_value("swipe_ready_time", 3)
    if "readyTime" in param3_dict.keys():
        ready_time = float(param3_dict["readyTime"])

    ps.air_bdd_ele_swipe(
        poco_instance,
        selector_str,
        optional,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time,
    )


def full_screen_swipe(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")

    param2_dict = dsl_helper.params_to_dic(param2, "swipeNumber")

    start_point = [0.5, 0.5]
    if "startX" in param2_dict.keys():
        start_point[0] = float(param2_dict["startX"])
    if "startY" in param2_dict.keys():
        start_point[1] = float(param2_dict["startY"])

    screen_size = gr.get_device_size()

    direction = param1.strip()

    distance = float(param2_dict["swipeNumber"])

    duration = None
    if gr.get_frame_config_value("use_swipe_duration", False):
        duration = gr.get_frame_config_value("swipe_duration", 1)
    if "duration" in param2_dict.keys():
        duration = float(param2_dict["duration"])

    ready_time = gr.get_frame_config_value("swipe_ready_time", 3)
    if "readyTime" in param2_dict.keys():
        ready_time = float(param2_dict["readyTime"])

    ps.air_bdd_full_screen_swipe(
        poco_instance,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time,
    )
