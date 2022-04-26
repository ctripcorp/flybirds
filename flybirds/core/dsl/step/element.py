# -*- coding: utf-8 -*-
"""
This module defines the steps related to the UI element.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import get_params


@step("text[{param1}]property[{param2}]is {param3}")
def text_attr_equal(context, param1=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param param1: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.text_attr_equal(context, param_1, param_2, param_3)


@step("element[{param1}]property[{param2}]is {param3}")
def ele_attr_equal(context, param1=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.ele_attr_equal(context, param_1, param_2, param_3)


@step("click[{param}]")
def click_ele(context, param=None):
    """
    Click on the selector element
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.click_ele(context, param_1)


@step("click text[{param}]")
def click_text(context, param=None):
    """
    Click on the text element
    :param context: step context
    :param param: locator string for text element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.click_text(context, param_1)


@step("click position[{x},{y}]")
def click_coordinates(context, x=None, y=None):
    """
    Click on the screen coordinates
    :param context: step context
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    param_x, param_y = get_params(context, (x, "param1"), (y, "param2"))
    g_Context.step.click_coordinates(context, param_x, param_y)


@step("in[{param1}]input[{param2}]")
def ele_input(context, param1=None, param2=None):
    """
    Enter the value param2 in the selector element param1
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: string to be input
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_input(context, param_1, param_2)


@step("element[{param1}]position not change in[{param2}]seconds")
def position_not_change(context, param1=None, param2=None):
    """
    Check that the position of the selector element param1 has not changed
    within param2 seconds
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2:
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.position_not_change(context, param_1, param_2)


@step("[{param1}]slide to {param2} distance[{param3}]")
def ele_swipe(context, param1=None, param2=None, param3=None):
    """
    Selector element param1 slides in the specified direction param2 and
    slides the specified distance param3
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param param3: slide distance
    """
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.ele_swipe(context, param_1, param_2, param_3)


@step("slide to {param1} distance[{param2}]")
def full_screen_swipe(context, param1=None, param2=None):
    """
    Slide the full screen in the specified direction for the specified distance
    :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param param2: slide distance
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.full_screen_swipe(context, param_1, param_2)


@step("exist text[{param}]")
def wait_text_exist(context, param=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param param: locator string for text element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_text_exist(context, param_1)


@step("not exist text[{param}]")
def text_not_exist(context, param=None):
    """
    The specified text element string does not exist in the page
    :param context: step context
    :param param: locator string for text element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.text_not_exist(context, param_1)


@step("text[{param}]disappear")
def wait_text_disappear(context, param=None):
    """
    The specified text element string disappears from the page within
     a specified period of time
    :param context: step context
    :param param: locator string for text element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_text_disappear(context, param_1)


@step("exist [{param1}] subNode [{param2}] element")
def find_child_from_parent(context, param1=None, param2=None):
    """
    The specified child selector element of the specified parent selector
    element exists in the page.
    :param context: step context
    :param param1: locator string for parent selector element (or None).
    :param param2: locator string for selector child element (or None).
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.find_child_from_parent(context, param_1, param_2)


@step("exist[{param}]element")
def wait_ele_exit(context, param=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_exit(context, param_1)


@step("not exist element[{param}]")
def ele_not_exit(context, param=None):
    """
    The specified selector element string does not exists in the page
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.ele_not_exit(context, param_1)


@step("element[{param}]disappear")
def wait_ele_disappear(context, param=None):
    """
    The specified selector element string disappears from the page within
     a specified period of time
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_disappear(context, param_1)


@step("the text of element[{param1}]is[{param2}]")
def ele_text_equal(context, param1=None, param2=None):
    """
    Check if the value of the text of the selector element param1 is param2
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: expected value
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_text_equal(context, param_1, param_2)


@step("the text of element[{param1}]include[{param2}]")
def ele_text_container(context, param1=None, param2=None):
    """
    Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: expected value
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_text_container(context, param_1, param_2)


@step("page rendering complete appears element[{param}]")
def wait_ele_appear(context, param=None):
    """
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.wait_ele_appear(context, param_1)


@step("existing element[{param}]")
def exist_ele(context, param=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param param: locator string for selector element (or None).
    """
    (param_1,) = get_params(context, (param, "param"))
    g_Context.step.exist_ele(context, param_1)


@step("in[{param1}]from {param2} find[{param3}]element")
def swipe_to_ele(context, param1=None, param2=None, param3=None):
    """
    Within the specified selector element Slide in the specified direction
     to find the selector element
    :param context: step context
    :param param1: locator string for parent selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param param3: locator string for selector child element (or None).
    """
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.swipe_to_ele(context, param_1, param_2, param_3)


@step("from {param1} find[{param2}]element")
def full_screen_swipe_to_ele_aaa(context, param1=None, param2=None):
    """
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param param2: locator string for selector element (or None).
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.full_screen_swipe_to_ele_aaa(context, param_1, param_2)


@step("clear [{param1}] and input[{param2}]")
def ele_clear_input(context, param1=None, param2=None):
    """
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: string to be input
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_clear_input(context, param_1, param_2)


@step("from [{param1}] select [{param2}]")
def ele_select(context, param1=None, param2=None):
    """
    Select the value param2 from the dropdown box element param1
    :param context: step context
    :param param1: locator string for selector element (or None).
    :param param2: text or value of select option
    """
    param_1, param_2 = get_params(
        context, (param1, "param1"), (param2, "param2")
    )
    g_Context.step.ele_select(context, param_1, param_2)


@step("the text of element [{param1}] subNode [{param2}] is [{param3}]")
def find_text_from_parent(context, param1=None, param2=None, param3=None):
    """
    check the text of the child element in the parent element is param3
    :param context: step context
    :param param1: locator string for parent selector element (or None).
    :param param2: locator string for selector child element (or None).
    :param param3: expected value.
    """
    param_1, param_2, param_3 = get_params(
        context, (param1, "param1"), (param2, "param2"), (param3, "param3")
    )
    g_Context.step.find_text_from_parent(context, param_1, param_2, param_3)
