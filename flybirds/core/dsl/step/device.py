# -*- coding: utf-8 -*-
"""
This module defines the steps related to the device.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params, ele_wrap


@step("init device[{selector}]")
@ele_wrap
def init_device(context, selector=None):
    g_Context.step.init_device(context, selector)


@step("connect device[{selector}]")
@ele_wrap
def connect_device(context, selector=None):
    g_Context.step.connect_device(context, selector)


@step("start recording timeout[{param}]")
def start_screen_record_timeout(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.start_screen_record_timeout(context, param_1)


@step("start record")
def start_screen_record(context):
    g_Context.step.start_screen_record(context)


@step("stop record")
def stop_screen_record(context):
    g_Context.step.stop_screen_record(context)
