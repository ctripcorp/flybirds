# -*- coding: utf-8 -*-
"""
Element verification
"""
import re

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele\
    as poco_ele
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_findsnap\
    as poco_find_snap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_verify\
    as poco_verify
import flybirds.utils.dsl_helper as dsl_helper


def wait_text_exist(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    config = None
    use_snap = gr.get_frame_config_value("use_snap", False)
    if "fuzzyMatch" in param_dict.keys():
        if use_snap:
            config = {"textMatches": selector_str}
        else:
            selector_str = "textMatches=" + selector_str
    else:
        if use_snap:
            config = {"text": selector_str}
        else:
            selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)
    if use_snap and config:
        poco_find_snap.find_ele_by_snap(poco_instance, config, optional)
    else:
        poco_ele.wait_exists(poco_instance, selector_str, optional)


def text_not_exist(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    if "fuzzyMatch" in param_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}

    poco_ele.not_exist(poco_instance, selector_str, optional)


def wait_text_disappear(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    if "fuzzyMatch" in param_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_disappear", 10
        )

    poco_ele.wait_disappear(poco_instance, selector_str, optional)


def wait_ele_exit(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    config = None
    use_snap = gr.get_frame_config_value("use_snap", False)
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    elif use_snap:
        config = {"name": selector_str}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)
    if use_snap and config:
        print("Use snap to determine the existence of elements")
        poco_find_snap.find_ele_by_snap(poco_instance, config, optional)
    else:
        poco_ele.wait_exists(poco_instance, selector_str, optional)


def ele_not_exit(context, param):
    poco_instance = gr.get_value("pocoInstance")
    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]

    poco_ele.not_exist(poco_instance, selector_str, optional)


def wait_ele_disappear(context, param):
    poco_instance = gr.get_value("pocoInstance")
    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_disappear", 10
        )

    poco_ele.wait_disappear(poco_instance, selector_str, optional)


def ele_text_equal(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")
    pattern = re.compile(r"\s+")
    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    optional = {}
    config = None
    # use snap
    # use_snap = gr.get_frame_config_value("use_snap", False)
    if "path" in param1_dict.keys():
        optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    params_deal_module = None
    deal_method = None
    param2_dict = dsl_helper.params_to_dic(param2, "tText")
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal
    target_str = param2_dict["tText"]
    handled_target_str = re.sub(pattern, "", target_str.replace(u"\u200b", ""))
    handled_selector_str = re.sub(
        pattern, "", selector_str.replace(u"\u200b", "")
    )
    if not (deal_method is None):
        deal_method_fun = getattr(params_deal_module, deal_method)
        handled_target_str = deal_method_fun(handled_target_str)
        pattern = re.compile(r"\s+")
        handled_target_str = re.sub(pattern, "", handled_target_str)
    if False:
        config = {"name": selector_str, "expect_text": target_str}
        poco_find_snap.verify_ele_by_snap(poco_instance, config, optional)
    else:
        poco_verify.ele_text_is(
            poco_instance,
            handled_selector_str,
            handled_target_str,
            optional,
            deal_method,
            params_deal_module,
        )


def ele_text_container(context, param1, param2):
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

    deal_method = None
    params_deal_module = None
    param2_dict = dsl_helper.params_to_dic(param2, "tText")
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal
    target_str = param2_dict["tText"]
    pattern = re.compile(r"\s+")
    handled_target_str = re.sub(pattern, "", target_str.replace(u"\u200b", ""))
    if not (deal_method is None):
        deal_method_fun = getattr(params_deal_module, deal_method)
        handled_target_str = deal_method_fun(handled_target_str)
        pattern = re.compile(r"\s+")
        handled_target_str = re.sub(pattern, "", handled_target_str)

    poco_verify.ele_text_contains(
        poco_instance,
        selector_str,
        handled_target_str,
        optional,
        deal_method,
        params_deal_module,
    )


def wait_ele_appear(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "page_render_timeout", 30
        )

    poco_ele.wait_exists(poco_instance, selector_str, optional)


def exist_ele(context, param):
    """
    Compatible with the old version of the statement, it will be discarded in
    the future.
    """
    poco_instance = gr.get_value("pocoInstance")

    params_array = param.split(",")
    selector_str = params_array[0]
    optional = {}
    if len(params_array) >= 2:
        optional["timeout"] = float(params_array[1])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_timeout", 10
        )
    poco_ele.wait_exists(poco_instance, selector_str, optional)
