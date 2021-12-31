# -*- coding: utf-8 -*-
"""
Get element attributes
"""
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
from flybirds.core.plugin.plugins.default.ui_driver.poco import poco_manage


def get_ele_attr(
        poco,
        selector_str,
        optional,
        attr_name,
        deal_method=None,
        params_deal_module=None,
):
    """
    get the specified attribute of the element, and after the attribute is
    obtained,you can choose whether to process it through a custom method.
    """
    poco_ele.wait_exists(poco, selector_str, optional)
    poco_object = poco_manage.create_poco_object_by_dsl(
        poco, selector_str, optional
    )
    ele_attr = poco_object.attr(attr_name)
    if not (deal_method is None):
        deal_method = getattr(params_deal_module, deal_method)
        ele_attr = deal_method(ele_attr)
    return ele_attr
