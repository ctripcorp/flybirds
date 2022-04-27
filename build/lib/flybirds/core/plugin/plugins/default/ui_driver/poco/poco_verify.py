# -*- coding: utf-8 -*-
"""
Poco Element verification
"""
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_attr as pa
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_text as pt
import flybirds.utils.verify_helper as verify_helper


def ele_text_is(
    poco,
    selector_str,
    target_str,
    optional,
    deal_method=None,
    params_deal_module=None,
):
    """
    determine whether the element is the expected value
    """
    ele_str = pt.get_ele_text_replace_space(
        poco, selector_str, optional, deal_method, params_deal_module
    )
    verify_helper.text_equal(target_str, ele_str)


def ele_text_contains(
    poco,
    selector_str,
    target_str,
    optional,
    deal_method=None,
    params_deal_module=None,
):
    """
    determine whether the element contains
    """
    ele_str = pt.get_ele_text_replace_space(
        poco, selector_str, optional, deal_method, params_deal_module
    )
    verify_helper.text_container(target_str, ele_str)


def ele_attr_is(
    poco,
    selector_str,
    optional,
    target_attr,
    target_attr_value,
    deal_method,
    params_deal_module,
):
    """
    determine whether the specified attribute of the element is the expected
    value.
    """
    ele_attr = pa.get_ele_attr(
        poco,
        selector_str,
        optional,
        target_attr,
        deal_method,
        params_deal_module,
    )
    verify_helper.attr_equal(target_attr_value, ele_attr)
