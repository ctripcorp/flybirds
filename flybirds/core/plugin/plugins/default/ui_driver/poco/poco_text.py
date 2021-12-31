# -*- coding: utf-8 -*-
"""
Text apis
"""
import re
import time

import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage as pm


def get_ele_text_replace_space(
        poco, selector_str, optional, deal_method_name, params_deal_module
):
    """
    get the text of the element, and after the text is obtained,
    you can choose whether to process it by a custom method
    """
    pattern = re.compile(r"\s+")
    poco_ele.wait_exists(poco, selector_str, optional)
    poco_object = pm.create_poco_object_by_dsl(
        poco, selector_str, optional
    )
    ele_str = poco_object.get_text()
    if ele_str is None:
        ele_str = poco_object.attr('label')
    handled_ele_str = re.sub(pattern, "", ele_str.replace(u"\u200b", ""))
    if not (deal_method_name is None):
        deal_method = getattr(params_deal_module, deal_method_name)
        handled_ele_str = deal_method(handled_ele_str)
        handled_ele_str = re.sub(pattern, "", handled_ele_str)
    return handled_ele_str


def get_ele_text(
        poco, selector_str, optional, deal_method_name, params_deal_module
):
    """
    get the text of the element, and after the text is obtained,
    you can choose whether to process it by a custom method
    """
    poco_ele.wait_exists(poco, selector_str, optional)
    poco_object = pm.create_poco_object_by_dsl(
        poco, selector_str, optional
    )
    ele_str = poco_object.get_text()
    if ele_str is None:
        ele_str = poco_object.attr('label')
    ele_str = ele_str.replace(u"\u200b", "")
    if not (deal_method_name is None):
        deal_method = getattr(params_deal_module, deal_method_name)
        ele_str = deal_method(ele_str)
    return ele_str


def text_change(poco, select_str, optional, o_text):
    """
    determine whether the copy of the element has changed within the specified
    time.
    """
    result = False
    timeout = optional["timeout"]
    current_wait_second = 1
    while (not result) and (timeout > 0):
        try:
            poco_target = pm.create_poco_object_by_dsl(
                poco, select_str, optional
            )
            if poco_target.exists():
                t_text = poco_target.get_text()
                if t_text is None:
                    t_text = poco_target.attr('label')
                if not (o_text == t_text):
                    result = True
            if result:
                break
        except Exception:
            pass
        time.sleep(current_wait_second)
        timeout -= current_wait_second
        current_wait_second += 1
    return result
