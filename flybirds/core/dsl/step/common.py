# -*- coding: utf-8 -*-
"""
This module defines the common steps.
"""

from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params


@step("wait[{param}]seconds")
def sleep(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.sleep(context, param_1)


@step("screenshot")
def screenshot(context):
    g_Context.step.screenshot(context)


@step("information association of failed operation,"
      " run the {param1} time :[{param2}]"
      )
def prev_fail_scenario_relevance(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.prev_fail_scenario_relevance(context, param_1, param_2)
