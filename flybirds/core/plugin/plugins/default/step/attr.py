# -*- coding: utf-8 -*-
"""
Step implement of element attribute.
"""
import flybirds.core.global_resource as gr
import flybirds.utils.dsl_helper as dsl_helper
from flybirds.core.global_context import GlobalContext as g_Context


def text_attr_equal(context, param1, param2, param3):
    """
    text attribute comparison
    """
    poco_instance = gr.get_value("pocoInstance")

    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    if "fuzzyMatch" in param1_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    param2_dict = dsl_helper.params_to_dic(param2, "attrName")

    target_attr = param2_dict["attrName"]

    target_attr_value = param3.strip()

    deal_method = None
    params_deal_module = None
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal
    g_Context.element.ele_attr_is(
        poco_instance,
        selector_str,
        optional,
        target_attr,
        target_attr_value,
        deal_method,
        params_deal_module,
    )


def ele_attr_equal(context, param1, param2, param3):
    """
    Element attribute comparison
    """
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

    param2_dict = dsl_helper.params_to_dic(param2, "attrName")

    target_attr = param2_dict["attrName"]

    target_attr_value = param3.strip()

    deal_method = None
    params_deal_module = None
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal

    g_Context.element.ele_attr_is(
        poco_instance,
        selector_str,
        optional,
        target_attr,
        target_attr_value,
        deal_method,
        params_deal_module,
    )
