# -*- coding: utf-8 -*-
"""
This module defines the steps related to the page.
"""

from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params


@step("go to url[{param}]")
def jump_to_page(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.jump_to_page(context, param_1)


@step("return to previous page")
def return_pre_page(context):
    g_Context.step.return_pre_page(context)


@step("go to home page")
def to_app_home(context):
    g_Context.step.to_app_home(context)


@step("logon account[{param1}]password[{param2}]")
def app_login(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.app_login(context, param_1, param_2)


@step("logout")
def app_logout(context):
    g_Context.step.app_logout(context)
