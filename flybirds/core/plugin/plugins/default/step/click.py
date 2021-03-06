# -*- coding: utf-8 -*-
"""
Step implement of element click.
"""
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap \
    as find_snap
import flybirds.utils.dsl_helper as dsl_helper
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.core.plugin.plugins.default.step.verify import ocr_txt_exist


def click_ele(context, param):
    """
    Click  element
    """
    param_dict = dsl_helper.params_to_dic(param)
    poco_instance = gr.get_value("pocoInstance")

    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    verify_dsl_str = None
    verify_optional = {}
    verify_action = None
    if "verifyEle" in param_dict.keys():
        verify_dsl_str = param_dict["verifyEle"]
        verify_action = param_dict["verifyAction"]
    if "verifyIsPath" in param_dict.keys():
        verify_optional["path"] = param_dict["verifyIsPath"]
    elif "verifyIsMultiSelector" in param_dict.keys():
        verify_optional["multiSelector"] = param_dict["verifyIsMultiSelector"]
    if "verifyTimeout" in param_dict.keys():
        verify_optional["timeout"] = float(param_dict["verifyTimeout"])
    else:
        verify_optional["timeout"] = gr.get_frame_config_value(
            "click_verify_timeout", 10
        )

    g_Context.element.air_bdd_click(
        poco_instance,
        selector_str,
        optional,
        verify_dsl_str,
        verify_optional,
        verify_action,
    )


def click_text(context, param):
    param_dict = dsl_helper.params_to_dic(param)
    poco_instance = gr.get_value("pocoInstance")

    selector_str = param_dict["selector"]
    if "fuzzyMatch" in param_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    verify_dsl_str = None
    verify_optional = {}
    verify_action = None
    if "verifyEle" in param_dict.keys():
        verify_dsl_str = param_dict["verifyEle"]
        verify_action = param_dict["verifyAction"]
    if "verifyIsPath" in param_dict.keys():
        verify_optional["path"] = param_dict["verifyIsPath"]
    elif "verifyIsMultiSelector" in param_dict.keys():
        verify_optional["multiSelector"] = param_dict["verifyIsMultiSelector"]
    if "verifyTimeout" in param_dict.keys():
        verify_optional["timeout"] = float(param_dict["verifyTimeout"])
    else:
        verify_optional["timeout"] = gr.get_frame_config_value(
            "click_verify_timeout", 10
        )

    g_Context.element.air_bdd_click(
        poco_instance,
        selector_str,
        optional,
        verify_dsl_str,
        verify_optional,
        verify_action,
    )


def click_coordinates(context, x, y):
    poco_instance = gr.get_value("pocoInstance")
    screen_size = gr.get_device_size()
    x_coordinate = float(x) / screen_size[0]
    y_coordinate = float(y) / screen_size[1]
    poco_instance.click([x_coordinate, y_coordinate])
    if gr.get_frame_config_value("use_snap", False):
        find_snap.fix_refresh_status(True)


def click_ocr_text(context, param):
    ocr_txt_exist(context, param)
    for line in g_Context.ocr_result:
        if line[1][0] == param:
            box = line[0]
            x = (box[0][0] + box[1][0]) / 2
            y = (box[0][1] + box[2][1]) / 2
            poco_instance = gr.get_value("pocoInstance")
            x_coordinate = float(x) / g_Context.image_size[0]
            y_coordinate = float(y) / g_Context.image_size[1]
            poco_instance.click([x_coordinate, y_coordinate])

