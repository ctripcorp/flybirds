# -*- coding: utf-8 -*-
"""
Step implement of element input.
"""
import flybirds.core.global_resource as gr
import flybirds.utils.dsl_helper as dsl_helper

from flybirds.core.global_context import GlobalContext as g_Context


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
