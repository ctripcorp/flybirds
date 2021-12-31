# -*- coding: utf-8 -*-
"""
dsl helper
"""
import re

import flybirds.utils.flybirds_log as log


# generate result_dic
def add_res_dic(dsl_params, functin_pattern, def_key):
    result_dic = {}
    match_obj = re.match(functin_pattern, dsl_params)
    if match_obj is not None:
        """
        senario：

        Flight, verifyEle=center_content_layout, verifyAction=position
        textMatches=shanghai.?
        .?economic.?, fuzzyMatch=true
        text=freshmode, timeout=15, swipeCount=40


        multi properities，example：text=freshmode, timeout=15, swipeCount=40
        Match from back to front, match back first,swipeCount=40
        match_obj_group_1（text=freshmode, timeout=15）
        f the conditions are still met, split again, Until the split to the
        last item: text=
        """
        group_1 = match_obj.group(1).strip().replace(u"\u200b", "")
        result_dic[match_obj.group(2)] = match_obj.group(3)
        match_obj_group_1 = re.match(functin_pattern, group_1)

        while match_obj_group_1 is not None:
            match_obj_group_1 = re.match(functin_pattern, group_1)
            if match_obj_group_1 is not None:
                group_1 = (
                    match_obj_group_1.group(1).strip().replace(u"\u200b", "")
                )
                result_dic[
                    match_obj_group_1.group(2)
                ] = match_obj_group_1.group(3)
            else:
                result_dic[def_key] = group_1
                break
        else:
            result_dic[def_key] = group_1

    else:
        result_dic[def_key] = dsl_params.strip().replace(u"\u200b", "")
    # print('result_dic44444', result_dic)
    return result_dic


# generate result_dic
def params_to_dic(dsl_params, def_key="selector"):
    """
    Convert the parameters in the dsl statement into dict format for use in
    subsequent processes
    """
    result_dic = {}
    functin_pattern = re.compile(r"([\S\s]+),\s*([a-zA-Z0-9_]+)\s*=\s*(\S+)")
    if isinstance(dsl_params, str):
        result_dic = add_res_dic(dsl_params, functin_pattern, def_key)
    log.info("result_dic: {}".format(result_dic))
    return result_dic


def split_must_param(dsl_params):
    """
    Get must and optional parameters
    """
    result = dsl_params.split(",", 1)
    result[0] = result[0].strip().replace(u"\u200b", "")
    result[1] = result[1].strip().replace(u"\u200b", "")
    return result


def get_params(context, *args):
    """
    Get param from context
    :param context: step context
    :param args: A tuple containing value and parameter name
    :return:
    """
    items = []
    for (val, param_name) in args:
        if val is not None:
            items.append(val)
        elif hasattr(context, param_name):
            items.append(getattr(context, param_name))
    return items


def return_value(value, def_value=None):
    """
    get global attribute value
    """
    if value is not None:
        return value
    return def_value
