# -*- coding: utf-8 -*-
"""
This module defines the steps related to the UI element.
"""
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap


@step("text[{selector}]property[{param2}]is {param3}")
@ele_wrap
def text_attr_equal(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_equal(context, selector, param2, param3)


@step("element[{selector}]property[{param2}]is {param3}")
@ele_wrap
def ele_attr_equal(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_equal(context, selector, param2, param3)


@step("click[{selector}]")
@ele_wrap
def click_ele(context, selector=None):
    """
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.click_ele(context, selector)


@step("click text[{selector}]")
@ele_wrap
def click_text(context, selector=None):
    """
    Click on the text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_text(context, selector)


@step("click ocr text[{selector}]")
@ele_wrap
def click_ocr_text(context, selector=None):
    """
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_ocr_text(context, selector)


@step("click ocr regional[{selector}] text[{param2}]")
@ele_wrap
def click_ocr_regional_text(context, selector, param2):
    """
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    :param2 selector: locator string for text element (or None).
    """
    g_Context.step.click_regional_ocr_text(context, selector, param2)


@step("click ocr regional[{selector}]")
@ele_wrap
def click_regional_ocr(context, selector):
    """
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_regional_ocr(context, selector)


@step("click image[{selector}]")
@ele_wrap
def click_image(context, selector=None):
    """
    Click on the image
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_image(context, selector)


@step("click position[{x},{y}]")
@ele_wrap
def click_coordinates(context, x=None, y=None):
    """
    Click on the screen coordinates
    :param context: step context
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    g_Context.step.click_coordinates(context, x, y)


@step("in[{selector}]input[{param2}]")
@ele_wrap
def ele_input(context, selector=None, param2=None):
    """
    Enter the value param2 in the selector element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ele_input(context, selector, param2)


@step("in ocr[{selector}]input[{param2}]")
@ele_wrap
def ocr_text_input(context, selector=None, param2=None):
    """
    Enter the value param2 in the selector element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ocr_text_input(context, selector, param2)


@step("element[{selector}]position not change in[{param2}]seconds")
@ele_wrap
def position_not_change(context, selector=None, param2=None):
    """
    Check that the position of the selector element param1 has not changed
    within param2 seconds
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2:
    """
    g_Context.step.position_not_change(context, selector, param2)


@step("[{selector}]slide to {param2} distance[{param3}]")
@ele_wrap
def ele_swipe(context, selector=None, param2=None, param3=None):
    """
    Selector element param1 slides in the specified direction param2 and
    slides the specified distance param3
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param param3: slide distance
    """
    g_Context.step.ele_swipe(context, selector, param2, param3)


@step("slide to {param1} distance[{param2}]")
@ele_wrap
def full_screen_swipe(context, param1=None, param2=None):
    """
    Slide the full screen in the specified direction for the specified distance
    :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param param2: slide distance
    """
    g_Context.step.full_screen_swipe(context, param1, param2)


@step("exist text[{selector}]")
@ele_wrap
def wait_text_exist(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_text_exist(context, selector)


@step("ocr exist text[{selector}]")
@ele_wrap
def ocr_text_exist(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_exist(context, selector)


@step("ocr regional[{selector}] exist text[{param2}]")
@ele_wrap
def ocr_regional_text_exist(context, selector, param2):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_exist(context, selector, param2)


@step("ocr contain text[{selector}]")
@ele_wrap
def ocr_text_contain(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_contain(context, selector)


@step("ocr regional[{selector}] contain text[{param2}]")
@ele_wrap
def ocr_regional_text_contain(context, selector, param2):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_contain(context, selector, param2)


@step("page ocr complete find text[{selector}]")
@ele_wrap
def wait_ocr_text_appear(context, selector=None):
    """
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ocr_text_appear(context, selector)


@step("not exist text[{selector}]")
@ele_wrap
def text_not_exist(context, selector=None):
    """
    The specified text element string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.text_not_exist(context, selector)


@step("ocr not exist text[{selector}]")
@ele_wrap
def ocr_text_not_exist(context, selector=None):
    """
    The specified text string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_not_exist(context, selector)

@step("text[{selector}]disappear")
@ele_wrap
def wait_text_disappear(context, selector=None):
    """
    The specified text element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_text_disappear(context, selector)


@step("exist [{p_selector}] subNode [{c_selector}] element")
@ele_wrap
def find_child_from_parent(context, p_selector=None, c_selector=None):
    """
    The specified child selector element of the specified parent selector
    element exists in the page.
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param c_selector: locator string for selector child element (or None).
    """
    g_Context.step.find_child_from_parent(context, p_selector, c_selector)


@step("exist[{selector}]element")
@ele_wrap
def wait_ele_exit(context, selector=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_exit(context, selector)


@step("not exist element[{selector}]")
@ele_wrap
def ele_not_exit(context, selector=None):
    """
    The specified selector element string does not exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.ele_not_exit(context, selector)


@step("element[{selector}]disappear")
@ele_wrap
def wait_ele_disappear(context, selector=None):
    """
    The specified selector element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_disappear(context, selector)


@step("the text of element[{selector}]is[{param2}]")
@ele_wrap
def ele_text_equal(context, selector=None, param2=None):
    """
    Check if the value of the text of the selector element param1 is param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_equal(context, selector, param2)


@step("the text of element[{selector}]include[{param2}]")
@ele_wrap
def ele_text_container(context, selector=None, param2=None):
    """
   Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_container(context, selector, param2)


@step("page rendering complete appears element[{selector}]")
@ele_wrap
def wait_ele_appear(context, selector=None):
    """
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_appear(context, selector)


@step("existing element[{selector}]")
@ele_wrap
def exist_ele(context, selector=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.exist_ele(context, selector)


@step("in[{p_selector}]from {param2} find[{c_selector}]element")
@ele_wrap
def swipe_to_ele(context, p_selector=None, param2=None, c_selector=None):
    """
    Within the specified selector element Slide in the specified direction
     to find the selector element
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param c_selector: locator string for selector child element (or None).
    """
    g_Context.step.swipe_to_ele(context, p_selector, param2, c_selector)


@step("from {param1} find[{selector}]element")
@ele_wrap
def full_screen_swipe_to_ele_aaa(context, param1=None, selector=None):
    """
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_ele_aaa(context, param1, selector)


@step("from {param1} find[{selector}]text")
@ele_wrap
def full_screen_swipe_to_ocr_txt(context, param1=None, selector=None):
    """
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_ocr_txt(context, param1, selector)


@step("from {param1} find[{selector}]image")
@ele_wrap
def full_screen_swipe_to_img(context, param1=None, selector=None):
    """
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_img(context, param1, selector)


@step("clear [{selector}] and input[{param2}]")
@ele_wrap
def ele_clear_input(context, selector=None, param2=None):
    """
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ele_clear_input(context, selector, param2)


@step("from [{selector}] select [{param2}]")
@ele_wrap
def ele_select(context, selector=None, param2=None):
    """
    Select the value param2 from the dropdown box element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: text or value of select option
    """
    g_Context.step.ele_select(context, selector, param2)


@step(
    "the text of element [{p_selector}] subNode [{c_selector}] is [{param3}]")
@ele_wrap
def find_text_from_parent(context, p_selector=None, c_selector=None,
                          param3=None):
    """
    check the text of the child element in the parent element is param3
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param c_selector: locator string for selector child element (or None).
    :param param3: expected value.
    """
    g_Context.step.find_text_from_parent(context, p_selector, c_selector,
                                         param3)

@step("exist image [{param}]")
def img_exist(context, param):
    g_Context.step.img_exist(context, param)


@step("not exist image [{param}]")
def img_not_exist(context, param):
    g_Context.step.img_not_exist(context, param)

