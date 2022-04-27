# -*- coding: utf-8 -*-
"""
Poco manage api
"""
import flybirds.core.plugin.plugins.default.ui_driver.poco.parse_path as parse
import flybirds.core.plugin.plugins.default.ui_driver.poco.parse_selector \
    as msd
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_selector as pc
from flybirds.core.global_context import GlobalContext as g_context


def poco_init():
    """
    Get the poco object used by the initialization global
    """
    return g_context.element.ui_driver_init()


def create_poco_object_by_dsl(poco, select_dsl_str, optional):
    """
    get the poco element of optional parameter structure and selector structure
    :param poco:
    :param select_dsl_str:
    :param optional:
    :return:
    """
    poco_object = None
    if optional is not None and "path" in optional.keys() \
            and optional["path"] == "true":
        poco_object = parse.create_path_poco(poco, select_dsl_str)
    elif (
            optional is not None and
            "multiSelector" in optional.keys()
            and optional["multiSelector"] == "true"
    ):
        poco_object = pc.create_poco_object(
            poco, msd.create_multi_selector(select_dsl_str)
        )
    else:
        poco_object = pc.create_poco_object(
            poco, msd.create_single_selector(select_dsl_str)
        )
    return poco_object
