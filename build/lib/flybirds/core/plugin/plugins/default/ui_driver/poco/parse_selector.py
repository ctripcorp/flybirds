# -*- coding: utf-8 -*-
"""
Convert selector
"""
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan


def create_multi_selector(multi_str, default="name"):
    """
    description of the poco multi-condition selection element
    is converted into a dictionary for use by poco
    :param multi_str:
    :param default:
    :return:
    """
    # get current language
    language = g_Context.get_current_language()
    split_str = lan.parse_glb_str("and", language)

    selector_array = multi_str.split(split_str)
    result = {}
    for item in selector_array:
        if "=" in item:
            item_split = item.split("=", 1)
            key = item_split[0].strip()
            result[key] = item_split[1].strip()
        else:
            result[default] = item.strip()
    return result


def create_single_selector(single_str, default="name"):
    """
    description of the poco single condition selection element
    is converted into a dictionary for use by poco
    """
    result = {}
    if "=" in single_str:
        single_split = single_str.split("=", 1)
        key = single_split[0].strip()
        result[key] = single_split[1].strip()
    else:
        result[default] = single_str.strip()
    return result
