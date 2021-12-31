# -*- coding: utf-8 -*-
"""
snippet helper
"""
import os
import subprocess
import re
import flybirds.core.driver.device as device


def create_sub_process(cmd):
    """
    Create a child process that executes a specific command
    """
    proc = subprocess.Popen(
        cmd,
        cwd=os.getcwd(),
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        creationflags=0,
    )
    return proc


def list_comparator(o_list, t_list):
    """
    Determine whether two lists contain the same elements
    :param o_list:
    :param t_list:
    :return:
    """

    try:
        if sorted(o_list) == sorted(t_list):
            return True
    except Exception:
        return False
    else:
        return False


def chose_first_number(string):
    """
    Take out the first number in the statement
    :param string:
    :return:
    """
    return int(re.search(r"\d+", string).group(0))


def schema_goto(
    page_name,
    schema_url,
    schema_goto_module,
    deal_method=None,
    params_deal_module=None,
):
    """
    schema go to
    """
    if not (deal_method is None):
        deal_method = getattr(params_deal_module, deal_method)
        schema_url = deal_method(schema_url)

    schema_rule = getattr(schema_goto_module, "schema_deal_rule")
    schema_url = schema_rule(page_name, schema_url)
    cmd = "am start -a 'android.intent.action.VIEW' -d '" + schema_url + "'"
    device.use_shell(cmd)
