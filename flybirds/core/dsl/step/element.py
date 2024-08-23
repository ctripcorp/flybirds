# -*- coding: utf-8 -*-
"""
This module defines the steps related to the UI element.
"""
from behave import step

from flybirds.core.exceptions import ErrorFlag, ActionType
from flybirds.core.global_context import GlobalContext as g_Context
import flybirds.core.global_resource as gr
from flybirds.utils import dsl_helper
from flybirds.utils.dsl_helper import ele_wrap, VerifyStep, RetryType, FlybirdsReportTagInfo


# 文案[{selector}]的属性[{param2}]为{param3}
@step("text[{selector}]property[{param2}]is {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.equ, "value": "param3"}, verify_function="ele_verify_attr_error_parse")
@VerifyStep()
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


# 文案[{selector}]的属性[{param2}]包含{param3}
@step("text[{selector}]property[{param2}]include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def text_attr_container(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_container(context, selector, param2, param3)


# 文案[{selector}]的属性[{param2}]不包含{param3}
@step("text[{selector}]property[{param2}]not include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.not_contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def text_attr_not_container(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_not_container(context, selector, param2, param3)


# 元素[{selector}]的属性[{param2}]为{param3}
@step("element[{selector}]property[{param2}]is {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.equ, "value": "param3"}, verify_function="ele_verify_attr_error_parse")
@VerifyStep()
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


# 元素[{selector}]的属性[{param2}]包含{param3}
@step("element[{selector}]property[{param2}]include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def ele_attr_container(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_container(context, selector, param2, param3)


# 元素[{selector}]的属性[{param2}]不包含{param3}
@step("element[{selector}]property[{param2}]not include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.not_contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def ele_attr_not_container(context, selector=None, param2=None, param3=None):
    """
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_not_container(context, selector, param2, param3)


# 鼠标悬浮[{selector}]
@step("mouse hover[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.hover)
@ele_wrap
def hover_ele(context, selector=None):
    """
    Hover on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.hover_ele(context, selector)


# 点击[{selector}]
@step("click[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_ele(context, selector=None):
    """
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """

    g_Context.step.click_ele(context, selector)


# 点击文案[{selector}]
@step("click text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文本元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_text(context, selector=None):
    """
    Click on the text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_text(context, selector)


# 点击扫描文案[{selector}]
@step("click ocr text[{selector}]")
@ele_wrap
def click_ocr_text(context, selector=None):
    """
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_ocr_text(context, selector)


# 点击区域[{selector}]中扫描文案[{param2}]
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


# 点击区域[{selector}]
@step("click ocr regional[{selector}]")
@ele_wrap
def click_regional_ocr(context, selector):
    """
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_regional_ocr(context, selector)


# 点击图片[{selector}]
@step("click image[{selector}]")
@ele_wrap
def click_image(context, selector=None):
    """
    Click on the image
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_image(context, selector)


# 点击屏幕位置[{x},{y}]
@step("click position[{x},{y}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "point", "value": "x", "name": "x坐标"}, {"type": "point", "value": "y", "name": "y坐标"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_coordinates(context, x=None, y=None):
    """
    Click on the screen coordinates
    :param context: step context
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    g_Context.step.click_coordinates(context, x, y)


# 在[{selector}]中输入[{param2}]
@step("in[{selector}]input[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "path", "text": "param2", "name": "文本"}]},
                       verify_function="common_error_parse",
                       action=ActionType.input)
@ele_wrap
def ele_input(context, selector=None, param2=None):
    """
    Enter the value param2 in the selector element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ele_input(context, selector, param2)


# 在扫描文字[{selector}]中输入[{param2}]
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


# 元素[{selector}]位置[{param2}]秒内未变动
@step("element[{selector}]position not change in[{param2}]seconds")
@VerifyStep()
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


# [{selector}]向{param2}滑动[{param3}]
@step("[{selector}]slide to {param2} distance[{param3}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "direction", "value": "param2", "name": "方向"},
             {"type": "distance", "value": "param3", "name": "距离"}]},
                       verify_function="common_error_parse",
                       action=ActionType.swipe)
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


# [{selector}]滑动[{left},{top}]
@step("[{selector}]slide to[{left},{top}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "position", "value": "left", "name": "左"},
             {"type": "position", "value": "top", "name": "上部"}]}, verify_function="common_error_parse",
                       action=ActionType.swipe)
@ele_wrap
def ele_direction_swipe(context, selector=None, left=None, top=None):
    """
    Selector element param1 slides in the specified direction param2 and
    slides the specified distance param3
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param top: equal to y-coord
    :param left: equal to x-coord
    """
    g_Context.step.ele_swipe_to(context, selector, left, top)


# 全屏向{param1}滑动[{param2}]", "向{param1}滑动[{param2}]
@step("slide to {param1} distance[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "direction", "value": "param1", "name": "方向"},
             {"type": "distance", "value": "param2", "name": "距离"}]}, verify_function="common_error_parse",
                       action=ActionType.swipe)
@ele_wrap
def full_screen_swipe(context, param1=None, param2=None):
    """
    Slide the full screen in the specified direction for the specified distance
    :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param param2: slide distance
    """

    g_Context.step.full_screen_swipe(context, param1, param2)


# 存在[{selector}]的文案
@step("exist text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def wait_text_exist(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    try:
        gr.get_frame_config_value("wait_ele_timeout", 10)
        g_Context.step.wait_text_exist(context, selector)
    except Exception:
        # use fuzzy match
        selector = ".*" + selector + ".*" + ",fuzzyMatch = true"
        g_Context.step.wait_text_exist(context, selector)


# 页面存在文案[{selector}]
@step("exist page text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def wait_page_text_exist(context, selector=None):
    g_Context.step.wait_page_text_exist(context, selector)


# 扫描存在[{selector}]的文案
@step("ocr exist text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_exist(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_exist(context, selector)


# 扫描区域[{selector}]中存在[{param2}]的文案
@step("ocr regional[{selector}] exist text[{param2}]")
@VerifyStep()
@ele_wrap
def ocr_regional_text_exist(context, selector, param2):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_exist(context, selector, param2)


# 扫描包含[{selector}]的文案
@step("ocr contain text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_contain(context, selector=None):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_contain(context, selector)


# 扫描区域[{selector}]中包含[{param2}]的文案
@step("ocr regional[{selector}] contain text[{param2}]")
@VerifyStep()
@ele_wrap
def ocr_regional_text_contain(context, selector, param2):
    """
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_contain(context, selector, param2)


# 页面扫描完成出现文字[{selector}]
@step("page ocr complete find text[{selector}]")
@VerifyStep()
@ele_wrap
def wait_ocr_text_appear(context, selector=None):
    """
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ocr_text_appear(context, selector)


# 不存在[{selector}]的文案
@step("not exist text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.not_exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def text_not_exist(context, selector=None):
    """
    The specified text element string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.text_not_exist(context, selector)


# 扫描不存在[{selector}]的文案
@step("ocr not exist text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_not_exist(context, selector=None):
    """
    The specified text string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_not_exist(context, selector)


# 文案[{selector}]消失
@step("text[{selector}]disappear")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文本"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_text_disappear(context, selector=None):
    """
    The specified text element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_text_disappear(context, selector)


# 存在[{p_selector}]的[{c_selector}]的元素
@step("exist [{p_selector}] subNode [{c_selector}] element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "path", "value": "c_selector", "name": "子元素"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
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


# 存在[{selector}]的元素
@step("exist[{selector}]element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist, "name": "存在"}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
def wait_ele_exit(context, selector=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_exit(context, selector)


# 不存在[{selector}]的元素
@step("not exist element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.not_exist, "name": "不存在"}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def ele_not_exit(context, selector=None):
    """
    The specified selector element string does not exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.ele_not_exit(context, selector)


# 元素[{selector}]消失
@step("element[{selector}]disappear")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_ele_disappear(context, selector=None):
    """
    The specified selector element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_disappear(context, selector)


# [{selector}]的文案为[{param2}]
@step("the text of element[{selector}]is[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_equal(context, selector=None, param2=None):
    """
    Check if the value of the text of the selector element param1 is param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_equal(context, selector, param2)


# [{selector}]的文案包含[{param2}]
@step("the text of element[{selector}]include[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_container(context, selector=None, param2=None):
    """
   Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_container(context, selector, param2)


# [{selector}]的文案不包含[{param2}]
@step("the text of element[{selector}]not include[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_not_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_not_container(context, selector=None, param2=None):
    """
   Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_not_container(context, selector, param2)


# 页面渲染完成出现元素[{selector}]
@step("page rendering complete appears element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_ele_appear(context, selector=None):
    """
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_appear(context, selector)


# 存在元素[{selector}]
@step("existing element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
def exist_ele(context, selector=None):
    """
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.exist_ele(context, selector)


# 在[{p_selector}]中向{param2}查找[{c_selector}]的元素
@step("in[{p_selector}]from {param2} find[{c_selector}]element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "p_selector", "name": "元素"},
             {"type": "path", "value": "c_selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist, f"{ErrorFlag.fource}": "c_selector"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
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


# 向{param1}查找[{selector}]的元素
@step("from {param1} find[{selector}]element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": "exist", "name": "存在"})
@VerifyStep()
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


# 向{param1}扫描[{selector}]的文案
@step("from {param1} find[{selector}]text")
@VerifyStep()
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


# 向{param1}查找[{selector}]的图像
@step("from {param1} find[{selector}]image")
@VerifyStep()
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


# 移动元素[{selector}]至可视区域
@step("move element[{selector}]to view")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.move)
@ele_wrap
def scroll_ele_into_view(context, selector=None):
    """
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.scroll_ele_into_view(context, selector)


# 在[{selector}]中清空并输入[{param2}]
@step("clear [{selector}] and input[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "text", "value": "param2", "name": "文本"}]},
                       verify_function="common_error_parse",
                       action=ActionType.input)
@ele_wrap
def ele_clear_input(context, selector=None, param2=None):
    """
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ele_clear_input(context, selector, param2)


# 清空输入框[{selector}]
@step("clear input[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify_function="common_error_parse",
                       action=ActionType.clear)
@ele_wrap
def clear_input(context, selector=None):
    """
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.clear_input(context, selector)


# 在[{selector}]中选择[{param2}]
@step("from [{selector}] select [{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "value", "value": "param2", "name": "值"}]},
                       verify_function="common_error_parse",
                       action=ActionType.select)
@ele_wrap
def ele_select(context, selector=None, param2=None):
    """
    Select the value param2 from the dropdown box element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: text or value of select option
    """
    g_Context.step.ele_select(context, selector, param2)


# [{p_selector}]的[{c_selector}]文案为[{param3}]
@step(
    "the text of element [{p_selector}] subNode [{c_selector}] is [{param3}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "p_selector", "name": "元素"},
             {"type": "path", "value": "c_selector", "name": "子元素"}]},
                       verify={"type": ErrorFlag.equ, "value": "param3"}, verify_function="ele_verify_text_error_parse")
@VerifyStep()
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


# 存在图像[{param}]
@step("exist image [{param}]")
@VerifyStep()
def img_exist(context, param):
    g_Context.step.img_exist(context, param)


# 不存在图像[{param}]
@step("not exist image [{param}]")
@VerifyStep()
def img_not_exist(context, param):
    g_Context.step.img_not_exist(context, param)


# 点触[{selector}]
@step("touch[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def touch_ele(context, selector=None):
    """
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.ele_touch(context, selector)


# 点触文本[{selector}]
@step("touch text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def touch_text(context, selector=None):
    """
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.touch_text(context, selector)


# 点击元素[{selector}]位置[{x},{y}]
@step("click ele [{selector}] position[{x},{y}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "point", "value": "x", "name": "x坐标"},
             {"type": "point", "value": "y", "name": "y坐标"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_ele_point(context, selector, x=None, y=None):
    """
    Click on the screen coordinates
    :param context: step context
    :param selector: locator string for selector element (or None)
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    g_Context.step.click_ele_point(context, selector, int(float(x)), int(float(y)))


# 点击[{selector}]并取消弹窗
@step("click[{selector}] and cancel dialog")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def close_dialog(context, selector):
    """
    Close the dialog box
    :param context: step context
    """
    g_Context.step.close_dialog(context)
    g_Context.step.click_ele(context, selector)


# 点击[{selector}]并接受弹窗
@step("click[{selector}] and accept dialog")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def accept_dialog(context, selector):
    """
    Close the dialog box
    :param context: step context
    """
    g_Context.step.accept_dialog(context)
    g_Context.step.click_ele(context, selector)
