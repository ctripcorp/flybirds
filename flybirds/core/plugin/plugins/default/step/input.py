# -*- coding: utf-8 -*-
"""
Step implement of element input.
"""
import time
import flybirds.core.global_resource as gr
import flybirds.utils.dsl_helper as dsl_helper
from flybirds.core.global_resource import get_device_id
from airtest.core.android.adb import *

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.core.plugin.plugins.default.step.click import click_ocr_text


def ele_input(context, param1, param2):
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

    param2_dict = dsl_helper.params_to_dic(param2, "inputStr")
    input_str = param2_dict["inputStr"]
    use_poco_input = False
    if "pocoInput" in param2_dict.keys():
        use_poco_input = True if param2_dict["pocoInput"] else False
    else:
        use_poco_input = gr.get_frame_config_value("use_poco_input", False)
    after_input_wait = None
    if "afterInputWait" in param2_dict.keys():
        after_input_wait = float(param2_dict["afterInputWait"])
    else:
        after_input_wait = gr.get_frame_config_value("after_input_wait", 1)

    if use_poco_input:
        g_Context.element.air_bdd_input(
            poco_instance, selector_str, optional, input_str, after_input_wait
        )
    else:
        g_Context.element.air_bdd_click(
            poco_instance, selector_str, optional, None, None, None
        )
        g_Context.element.str_input(input_str, after_input_wait)


def ocr_text_input(context, param1, param2):
    click_ocr_text(context, param1)
    try:
        after_input_wait = gr.get_frame_config_value("after_input_wait", 1)
        time.sleep(after_input_wait)
        keyboard_clear(context)
        g_Context.element.str_input(param2, after_input_wait)
    except Exception:
        raise Exception("[ocr_text_input] ocr input text error!")


def keyboard_clear(context):
    time.sleep(1)
    dev = ADB()
    device_id = get_device_id()
    move_end = "-s {} shell input keyevent KEYCODE_MOVE_END".format(device_id)
    long_del = "-s {} shell input keyevent --longpress 67 67 67 67 67 67 67 67 67 67 " \
               "67 67 67 67 67 67 67 67 67 67 67".format(device_id)
    dev.start_cmd(move_end, False)
    dev.start_cmd(long_del, False)

