# -*- coding: utf-8 -*-
"""
This module defines the steps related to the UI element.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params


@step("text[{param1}]property[{param2}]is {param3}")
def text_attr_equal(context, param1=None, param2=None, param3=None):
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.text_attr_equal(context, param_1, param_2, param_3)


@step("element[{param1}]property[{param2}]is {param3}")
def ele_attr_equal(context, param1=None, param2=None, param3=None):
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.ele_attr_equal(context, param_1, param_2, param_3)


@step("click[{param}]")
def click_ele(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.click_ele(context, param_1)


@step("click text[{param}]")
def click_text(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.click_text(context, param_1)


@step("click position[{x},{y}]")
def click_coordinates(context, x=None, y=None):
    param_x, param_y = get_params(context, (x, "param1"), (y, "param2"))
    g_Context.step.click_coordinates(context, param_x, param_y)


@step("in[{param1}]input[{param2}]")
def ele_input(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_input(context, param_1, param_2)


@step("element[{param1}]position not change in[{param2}]seconds")
def position_not_change(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.position_not_change(context, param_1, param_2)


@step("[{param1}]slide to {param2} distance[{param3}]")
def ele_swipe(context, param1=None, param2=None, param3=None):
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.ele_swipe(context, param_1, param_2, param_3)


@step("slide to {param1} distance[{param2}]")
def full_screen_swipe(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.full_screen_swipe(context, param_1, param_2)


@step("exist text[{param}]")
def wait_text_exist(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_text_exist(context, param_1)


@step("not exist text[{param}]")
def text_not_exist(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.text_not_exist(context, param_1)


@step("text[{param}]disappear")
def wait_text_disappear(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_text_disappear(context, param_1)


@step("exist[{param}]element")
def wait_ele_exit(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_exit(context, param_1)


@step("not exist element[{param}]")
def ele_not_exit(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.ele_not_exit(context, param_1)


@step("element[{param}]disappear")
def wait_ele_disappear(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_disappear(context, param_1)


@step("the text of element[{param1}]is[{param2}]")
def ele_text_equal(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_text_equal(context, param_1, param_2)


@step("the text of element[{param1}]include[{param2}]")
def ele_text_container(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_text_container(context, param_1, param_2)


@step("page rendering complete appears element[{param}]")
def wait_ele_appear(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_appear(context, param_1)


@step("existing element[{param}]")
def exist_ele(context, param=None):
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.exist_ele(context, param_1)


@step("in[{param1}]from {param2} find[{param3}]element")
def swipe_to_ele(context, param1=None, param2=None, param3=None):
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.swipe_to_ele(context, param_1, param_2, param_3)


@step("from {param1} find[{param2}]element")
def full_screen_swipe_to_ele_aaa(context, param1=None, param2=None):
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.full_screen_swipe_to_ele_aaa(context, param_1, param_2)
