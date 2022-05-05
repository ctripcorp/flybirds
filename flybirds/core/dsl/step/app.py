# -*- coding: utf-8 -*-
"""
This module defines the steps related to the app.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap


@step("install app[{selector}]")
@ele_wrap
def install_app(context, selector=None):
    g_Context.step.install_app(context, selector)


@step("delete app[{selector}]")
@ele_wrap
def uninstall_app(context, selector=None):
    """
    uninstall app
    """
    g_Context.step.uninstall_app(context, selector)


@step("start app[{selector}]")
@ele_wrap
def start_app(context, selector=None):
    g_Context.step.start_app(context, selector)


@step("restart app")
def restart_app(context):
    g_Context.step.restart_app(context)


@step("close app")
def stop_app(context):
    g_Context.step.stop_app(context)
