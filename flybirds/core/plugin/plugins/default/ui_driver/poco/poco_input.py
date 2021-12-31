# -*- coding: utf-8 -*-
"""
Poco element input
"""
from airtest.core.api import text, time

import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.ui_driver.poco import poco_manage


def air_bdd_input(
        poco, select_dsl_str, optional, input_str, after_input_wait=None
):
    """
    input text
    :param poco:
    :param select_dsl_str:
    :param input_str:
    :param optional:
    :param after_input_wait:
    :return:
    """
    poco_ele.wait_exists(poco, select_dsl_str, optional)
    poco_object = poco_manage.create_poco_object_by_dsl(
        poco, select_dsl_str, optional
    )
    try:
        poco_object.set_text(input_str)
    except Exception as input_error:
        log.info(f"air_bdd_input has error:{str(input_error)}")
        poco_object.click()
        text(input_str)
    if not (after_input_wait is None):
        time.sleep(after_input_wait)
