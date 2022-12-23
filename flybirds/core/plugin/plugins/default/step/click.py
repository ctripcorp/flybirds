# -*- coding: utf-8 -*-
"""
Step implement of element click.
"""
import re
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap \
    as find_snap
import flybirds.utils.dsl_helper as dsl_helper
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.core.plugin.plugins.default.step.verify import paddle_fix_txt, ocr_txt_exist, ocr_regional_txt_exist
from flybirds.core.plugin.plugins.default.step.common import img_verify
import flybirds.utils.flybirds_log as log


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
    flag = False
    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    for line in g_Context.ocr_result:
        try:
            if "fuzzyMatch" in param_dict.keys() and re.search(selector_str, line[1][0], flags=0) is not None:
                log.info(f"[click ocr txt] click txt fuzzyMatch found: {line[1][0]}")
                flag = True
            else:
                trim_param = selector_str.replace(" ", "")
                fixed_txt = paddle_fix_txt([line[1][0]], True)
                line_param = trim_param.replace("-", "")
                line_txt = fixed_txt[0].replace("-", "")
                if trim_param == fixed_txt[0] or line_param == line_txt:
                    log.info(f"[click ocr txt] click txt found: {line[1][0]}")
                    flag = True
            if flag is True:
                box = line[0]
                x = (box[0][0] + box[1][0]) / 2
                y = (box[0][1] + box[2][1]) / 2
                poco_instance = gr.get_value("pocoInstance")
                x_coordinate = float(x) / g_Context.image_size[1]
                y_coordinate = float(y) / g_Context.image_size[0]
                poco_instance.click([x_coordinate, y_coordinate])
                break
        except Exception:
            raise Exception("[click ocr text] click ocr text error !")
    if flag is False:
        raise Exception("[click ocr text] click ocr text is not found !")


def click_image(context, param):
    result = img_verify(context, param)
    try:
        if len(result) > 0:
            log.info(f"[click_image]image found: {result}")
            x = result[0].get('rect').x + result[0].get('rect').width / 2
            y = result[0].get('rect').y + result[0].get('rect').height / 2
            poco_instance = gr.get_value("pocoInstance")
            x_coordinate = float(x) / g_Context.image_size[1]
            y_coordinate = float(y) / g_Context.image_size[0]
            poco_instance.click([x_coordinate, y_coordinate])
        else:
            raise Exception("[click image] click image error !")
    except Exception:
        raise Exception("[click image] click image error !")


def click_regional_ocr_text(context, param1, param2):
    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    str_list = selector_str.split('=')
    regional_id = int(str_list[1])
    regional_ocr_result = list(filter(lambda item: item['regional_id'] == regional_id, g_Context.struct_ocr_result))
    flag = False
    param2_dict = dsl_helper.params_to_dic(param2)
    selector_str = param2_dict["selector"]
    for line in regional_ocr_result:
        try:
            if "fuzzyMatch" in param2_dict.keys() and re.search(selector_str, line['txt'], flags=0) is not None:
                log.info(f"[click regional ocr txt] click txt fuzzyMatch found: {line['txt']}")
                flag = True
            else:
                trim_param = selector_str.replace(" ", "")
                fixed_txt = paddle_fix_txt([line['txt']], True)
                line_param = trim_param.replace("-", "")
                line_txt = fixed_txt[0].replace("-", "")
                if trim_param == fixed_txt[0] or line_param == line_txt:
                    log.info(f"[click regional ocr txt] click txt found: {line['txt']}")
                    flag = True
            if flag is True:
                box = line['box']
                x = (box[0][0] + box[1][0]) / 2
                y = (box[0][1] + box[2][1]) / 2
                poco_instance = gr.get_value("pocoInstance")
                x_coordinate = float(x) / g_Context.image_size[1]
                y_coordinate = float(y) / g_Context.image_size[0]
                poco_instance.click([x_coordinate, y_coordinate])
                break
        except Exception:
            raise Exception("[click regional ocr text] click ocr text error !")
    if flag is False:
        raise Exception("[click regional ocr text] click ocr text is not found !")


def click_regional_ocr(context, param):
    try:
        param_dict = dsl_helper.params_to_dic(param)
        selector_str = param_dict["selector"]
        str_list = selector_str.split('=')
        regional_id = int(str_list[1])
        regional_ocr_result = list(filter(lambda item: item['regional_id'] == regional_id, g_Context.struct_ocr_result))
        box = regional_ocr_result[0]['regional_box']
        log.info(f"[click regional ocr] regional box found: {box}")
        x = (box[0][0] + box[1][0]) / 2
        y = (box[0][1] + box[2][1]) / 2
        poco_instance = gr.get_value("pocoInstance")
        x_coordinate = float(x) / g_Context.image_size[1]
        y_coordinate = float(y) / g_Context.image_size[0]
        poco_instance.click([x_coordinate, y_coordinate])
    except Exception:
        raise Exception("[click regional ocr] click regional box error !")
