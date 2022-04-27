# -*- coding: utf-8 -*-
"""
This module defines the steps related to the app.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params


@step("install app[{param}]")
def install_app(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.install_app(context, param_1)


@step("delete app[{param}]")
def uninstall_app(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.uninstall_app(context, param_1)


@step("start app[{param}]")
def start_app(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.start_app(context, param_1)


@step("restart app")
def restart_app(context):
    g_Context.step.restart_app(context)


@step("close app")
def stop_app(context):
    g_Context.step.stop_app(context)
