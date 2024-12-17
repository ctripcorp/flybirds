# -*- coding: utf-8 -*-
"""
This module defines the steps related to the UI element.
"""
from behave import step

from flybirds.core.exceptions import ErrorFlag, ActionType
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap, VerifyStep, RetryType, FlybirdsReportTagInfo


@step("text[{selector}]property[{param2}]is {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.equ, "value": "param3"}, verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def text_attr_equal(context, selector=None, param2=None, param3=None):
    """
    文案[{selector}]的属性[{param2}]为{param3}
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_equal(context, selector, param2, param3)


@step("text[{selector}]property[{param2}]include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def text_attr_container(context, selector=None, param2=None, param3=None):
    """
    文案[{selector}]的属性[{param2}]包含{param3}
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_container(context, selector, param2, param3)


@step("text[{selector}]property[{param2}]not include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.not_contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def text_attr_not_container(context, selector=None, param2=None, param3=None):
    """
    文案[{selector}]的属性[{param2}]不包含{param3}
    Check if the value of the attribute param2 of the text element param1 in
     the page is param3

    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.text_attr_not_container(context, selector, param2, param3)


@step("element[{selector}]property[{param2}]is {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.equ, "value": "param3"}, verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def ele_attr_equal(context, selector=None, param2=None, param3=None):
    """
    元素[{selector}]的属性[{param2}]为{param3}
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_equal(context, selector, param2, param3)


@step("element[{selector}]property[{param2}]include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def ele_attr_container(context, selector=None, param2=None, param3=None):
    """
    元素[{selector}]的属性[{param2}]包含{param3}
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_container(context, selector, param2, param3)


@step("element[{selector}]property[{param2}]not include {param3}")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "param2", "name": "属性"}]},
                       verify={"type": ErrorFlag.not_contains, "value": "param3"},
                       verify_function="ele_verify_attr_error_parse")
@VerifyStep()
@ele_wrap
def ele_attr_not_container(context, selector=None, param2=None, param3=None):
    """
    元素[{selector}]的属性[{param2}]不包含{param3}
    Check if the value of the attribute param2 of the selector element param1
     in the page is param3

    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: attribute Name
    :param param3: expected Value
    """
    g_Context.step.ele_attr_not_container(context, selector, param2, param3)


@step("mouse hover[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.hover)
@ele_wrap
def hover_ele(context, selector=None):
    """
    鼠标悬浮[{selector}]
    Hover on the selector element
    
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.hover_ele(context, selector)


@step("click[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_ele(context, selector=None):
    """
    点击[{selector}]
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """

    g_Context.step.click_ele(context, selector)


@step("if [{selector}] exist then click")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_param_if_ele_exist(context, selector=None):
    """
    如果[{selector}]存在则点击该元素
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param: locator string for selector element (or None).
    """

    g_Context.step.click_exist_param(context, selector)


@step("click text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文本元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_text(context, selector=None):
    """
    点击文案[{selector}]
    Click on the text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_text(context, selector)


@step("click ocr text[{selector}]")
@ele_wrap
def click_ocr_text(context, selector=None):
    """
    点击扫描文案[{selector}]
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_ocr_text(context, selector)


@step("click ocr regional[{selector}] text[{param2}]")
@ele_wrap
def click_ocr_regional_text(context, selector, param2):
    """
    点击区域[{selector}]中扫描文案[{param2}]
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
    点击区域[{selector}]
    Click on the ocr text element
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_regional_ocr(context, selector)


@step("click image[{selector}]")
@ele_wrap
def click_image(context, selector=None):
    """
    点击图片[{selector}]
    Click on the image
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.click_image(context, selector)


@step("click position[{x},{y}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "point", "value": "x", "name": "x坐标"}, {"type": "point", "value": "y", "name": "y坐标"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_coordinates(context, x=None, y=None):
    """
    点击屏幕位置[{x},{y}]
    Click on the screen coordinates
    :param context: step context
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    g_Context.step.click_coordinates(context, x, y)


@step("in[{selector}]input[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "path", "text": "param2", "name": "文本"}]},
                       verify_function="common_error_parse",
                       action=ActionType.input)
@ele_wrap
def ele_input(context, selector=None, param2=None):
    """
    在[{selector}]中输入[{param2}]
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
    在扫描文字[{selector}]中输入[{param2}]
    Enter the value param2 in the selector element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ocr_text_input(context, selector, param2)


@step("element[{selector}]position not change in[{param2}]seconds")
@VerifyStep()
@ele_wrap
def position_not_change(context, selector=None, param2=None):
    """
    元素[{selector}]位置[{param2}]秒内未变动
    Check that the position of the selector element param1 has not changed
    within param2 seconds
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2:
    """
    g_Context.step.position_not_change(context, selector, param2)


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
    [{selector}]向{param2}滑动[{param3}]
    Selector element param1 slides in the specified direction param2 and
    slides the specified distance param3
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param param3: slide distance
    """
    g_Context.step.ele_swipe(context, selector, param2, param3)


@step("[{selector}]slide to[{left},{top}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "position", "value": "left", "name": "左"},
             {"type": "position", "value": "top", "name": "上部"}]}, verify_function="common_error_parse",
                       action=ActionType.swipe)
@ele_wrap
def ele_direction_swipe(context, selector=None, left=None, top=None):
    """
    [{selector}]滑动[{left},{top}]
    Selector element param1 slides in the specified direction param2 and
    slides the specified distance param3
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param top: equal to y-coord
    :param left: equal to x-coord
    """
    g_Context.step.ele_swipe_to(context, selector, left, top)


@step("slide to {param1} distance[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "direction", "value": "param1", "name": "方向"},
             {"type": "distance", "value": "param2", "name": "距离"}]}, verify_function="common_error_parse",
                       action=ActionType.swipe)
@ele_wrap
def full_screen_swipe(context, param1=None, param2=None):
    """
    全屏向{param1}滑动[{param2}]", "向{param1}滑动[{param2}]
    Slide the full screen in the specified direction for the specified distance
    :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param param2: slide distance
    """

    g_Context.step.full_screen_swipe(context, param1, param2)


@step("exist text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def wait_text_exist(context, selector=None):
    """
    存在[{selector}]的文案
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_text_exist(context, selector)


@step("exist page text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def wait_page_text_exist(context, selector=None):
    """
    页面存在文案[{selector}]
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_page_text_exist(context, selector)


@step("ocr exist text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_exist(context, selector=None):
    """
    扫描存在[{selector}]的文案
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_exist(context, selector)


@step("ocr regional[{selector}] exist text[{param2}]")
@VerifyStep()
@ele_wrap
def ocr_regional_text_exist(context, selector, param2):
    """
    扫描区域[{selector}]中存在[{param2}]的文案
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_exist(context, selector, param2)


@step("ocr contain text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_contain(context, selector=None):
    """
    扫描包含[{selector}]的文案
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_contain(context, selector)


@step("ocr regional[{selector}] contain text[{param2}]")
@VerifyStep()
@ele_wrap
def ocr_regional_text_contain(context, selector, param2):
    """
    扫描区域[{selector}]中包含[{param2}]的文案
    The specified text element string exists in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    :param param2: locator string for text element (or None).
    """
    g_Context.step.ocr_regional_text_contain(context, selector, param2)


@step("page ocr complete find text[{selector}]")
@VerifyStep()
@ele_wrap
def wait_ocr_text_appear(context, selector=None):
    """
    页面扫描完成出现文字[{selector}]
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ocr_text_appear(context, selector)


@step("not exist text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify={"type": ErrorFlag.not_exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def text_not_exist(context, selector=None):
    """
    不存在[{selector}]的文案
    The specified text element string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.text_not_exist(context, selector)


@step("ocr not exist text[{selector}]")
@VerifyStep()
@ele_wrap
def ocr_text_not_exist(context, selector=None):
    """
    扫描不存在[{selector}]的文案
    The specified text string does not exist in the page
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.ocr_text_not_exist(context, selector)


@step("text[{selector}]disappear")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文本"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_text_disappear(context, selector=None):
    """
    文案[{selector}]消失
    The specified text element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for text element (or None).
    """
    g_Context.step.wait_text_disappear(context, selector)


@step("exist [{p_selector}] subNode [{c_selector}] element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "path", "value": "c_selector", "name": "子元素"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
def find_child_from_parent(context, p_selector=None, c_selector=None):
    """
    存在[{p_selector}]的[{c_selector}]的元素
    The specified child selector element of the specified parent selector
    element exists in the page.
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param c_selector: locator string for selector child element (or None).
    """
    g_Context.step.find_child_from_parent(context, p_selector, c_selector)


@step("exist[{selector}]element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist, "name": "存在"}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
def wait_ele_exit(context, selector=None):
    """
    存在[{selector}]的元素
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_exit(context, selector)


@step("not exist element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.not_exist, "name": "不存在"}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
@RetryType('timeout')
def ele_not_exit(context, selector=None):
    """
    不存在[{selector}]的元素
    The specified selector element string does not exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.ele_not_exit(context, selector)


@step("element[{selector}]disappear")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_ele_disappear(context, selector=None):
    """
    元素[{selector}]消失
    The specified selector element string disappears from the page within
     a specified period of time
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_disappear(context, selector)


@step("the text of element[{selector}]is[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_equal(context, selector=None, param2=None):
    """
    [{selector}]的文案为[{param2}]
    Check if the value of the text of the selector element param1 is param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_equal(context, selector, param2)


@step("the text of element[{selector}]include[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_container(context, selector=None, param2=None):
    """
    [{selector}]的文案包含[{param2}]
   Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_container(context, selector, param2)


@step("the text of element[{selector}]not include[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_not_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_text_not_container(context, selector=None, param2=None):
    """
    [{selector}]的文案不包含[{param2}]
   Check if the value of the text of the selector element param1 include param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: expected value
    """
    g_Context.step.ele_text_not_container(context, selector, param2)


@step("page rendering complete appears element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.disappear)
@ele_wrap
def wait_ele_appear(context, selector=None):
    """
    页面渲染完成出现元素[{selector}]
    Wait for the page to finish rendering and the selector element param1
     to appear
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.wait_ele_appear(context, selector)


@step("existing element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist}, verify_function="ele_verify_error_parse")
@VerifyStep()
@ele_wrap
def exist_ele(context, selector=None):
    """
    存在元素[{selector}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.exist_ele(context, selector)


@step("the element[{selector}]value is[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_exist_value(context, selector=None, param2=None):
    """
    元素[{selector}]的value为[{param2}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: element value.
    """
    g_Context.step.ele_exist_value(context, selector, param2)
    # g_Context.step.exist_ele(context, selector)


@step("the element[{selector}]value contains[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_value(context, selector=None, param2=None):
    """
    元素[{selector}]的value包含[{param2}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: element value.
    """
    g_Context.step.ele_contain_value(context, selector, param2)


@step("the element[{selector}]value not contains[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_not_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_not_contain_value(context, selector=None, param2=None):
    """
    元素[{selector}]的value不包含[{param2}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: element value.
    """
    g_Context.step.ele_not_contain_value(context, selector, param2)


@step("witch contain [{param1}] element [{selector}] value is[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param1", "name": "文本"},
             {"type": "attr", "value": "param2", "name": "属性"},
             {"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_value(context, param1=None, selector=None, param2=None):
    """
    参数含有[{param1}]的元素[{selector}]的文案为[{param2}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param1: element value.
    :param param2: element value.
    """
    g_Context.step.ele_contain_param_value(context, param1, selector, param2)


@step("witch contain [{param1}] element [{selector}] value contain [{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param1", "name": "文本"},
             {"type": "attr", "value": "param2", "name": "属性"},
             {"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_contains, "value": "param2"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_contain_value(context, param1=None, selector=None, param2=None):
    """
    参数含有[{param1}]的元素[{selector}]的文案包含[{param2}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param1: element value.
    :param param2: element value.
    """
    g_Context.step.ele_contain_param_contain_value(context, param1, selector, param2)


@step("contain [{param}] by [{selector}] exist")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.exist, "value": "param"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_exist(context, param=None, selector=None):
    """
    存在包含参数[{param}]的元素[{selector}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param: element value.
    """
    g_Context.step.ele_contain_param_exist(context, param, selector)


@step("contain [{param}] by [{selector}] not exist")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.not_exist, "value": "param"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_not_exist(context, param=None, selector=None):
    """
    不存在包含参数[{param}]的元素[{selector}]
    The specified selector element string exists in the page
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param: element value.
    """
    g_Context.step.ele_contain_param_not_exist(context, param, selector)


@step("the [{param}] contained by the element [{selector}] has attribute [{attr_name}] with value [{attr_value}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param", "name": "文本"},
             {"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "attr_name", "name": "属性"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "attr_value"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_attr_exist(context, param=None, selector=None, attr_name=None, attr_value=None):
    """
    包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值为[{attr_value}]
    The specified selector element string exists in the page
    :param context: step context
    :param param: element value.
    :param selector: locator string for selector element (or None).
    :param attr_name: attribute name
    :param attr_value: attribute value
    """
    g_Context.step.ele_contain_param_attr_exist(context, param, selector, attr_name, attr_value)


@step("the [{param}] contained by the element [{selector}] element value is [{attr_value}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param", "name": "文本"},
             {"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": ErrorFlag.text_equ, "value": "attr_value"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_attr_exist(context, param=None, selector=None, attr_value=None):
    """
    包含参数[{param}]的元素[{selector}]的value为[{attr_value}]
    The specified selector element string exists in the page
    :param context: step context
    :param param: element value.
    :param selector: locator string for selector element (or None).
    :param attr_name: attribute name
    :param attr_value: attribute value
    """
    g_Context.step.ele_with_param_value_equal(context, param, selector, attr_value)


@step("the [{param}] contained by the element [{selector}] has attribute [{attr_name}] contain value [{attr_value}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param", "name": "文本"},
             {"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "attr_name", "name": "属性"}]},
                       verify={"type": ErrorFlag.text_contains, "value": "attr_value"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_attr_contain(context, param=None, selector=None, attr_name=None, attr_value=None):
    """
    包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值包含[{attr_value}]
    The specified selector element string exists in the page
    :param context: step context
    :param param: element value.
    :param selector: locator string for selector element (or None).
    :param attr_name: attribute name
    :param attr_value: attribute value
    """
    g_Context.step.ele_contain_param_attr_contain(context, param, selector, attr_name, attr_value)


@step("the [{param}] contained by the element [{selector}] has attribute [{attr_name}] not contain value [{attr_value}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "text", "value": "param", "name": "文本"},
             {"type": "path", "value": "selector", "name": "元素"},
             {"type": "attr", "value": "attr_name", "name": "属性"}]},
                       verify={"type": ErrorFlag.text_not_contains, "value": "attr_value"},
                       verify_function="ele_verify_text_error_parse")
@VerifyStep()
@ele_wrap
def ele_contain_param_attr_not_contain(context, param=None, selector=None, attr_name=None, attr_value=None):
    """
    包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值不包含[{attr_value}]
    The specified selector element string exists in the page
    :param context: step context
    :param param: element value.
    :param selector: locator string for selector element (or None).
    :param attr_name: attribute name
    :param attr_value: attribute value
    """
    g_Context.step.ele_contain_param_attr_not_contain(context, param, selector, attr_name, attr_value)


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
    在[{p_selector}]中向{param2}查找[{c_selector}]的元素
    Within the specified selector element Slide in the specified direction
     to find the selector element
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param param2: slide direction (top/bottom/left/right)
    :param c_selector: locator string for selector child element (or None).
    """
    g_Context.step.swipe_to_ele(context, p_selector, param2, c_selector)


@step("from {param1} find[{selector}]element")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify={"type": "exist", "name": "存在"})
@VerifyStep()
@ele_wrap
def full_screen_swipe_to_ele_aaa(context, param1=None, selector=None):
    """
    向{param1}查找[{selector}]的元素
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_ele_aaa(context, param1, selector)


@step("from {param1} find[{selector}]text")
@VerifyStep()
@ele_wrap
def full_screen_swipe_to_ocr_txt(context, param1=None, selector=None):
    """
    向{param1}扫描[{selector}]的文案
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_ocr_txt(context, param1, selector)


@step("from {param1} find[{selector}]image")
@VerifyStep()
@ele_wrap
def full_screen_swipe_to_img(context, param1=None, selector=None):
    """
    向{param1}查找[{selector}]的图像
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param param1: slide direction (top/bottom/left/right)
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.full_screen_swipe_to_img(context, param1, selector)


@step("move element[{selector}]to view")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.move)
@ele_wrap
def scroll_ele_into_view(context, selector=None):
    """
    移动元素[{selector}]至可视区域
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.scroll_ele_into_view(context, selector)


@step("upload image to element[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.upload)
@ele_wrap
def scroll_ele_into_view(context, selector=None):
    """
    上传图片至元素[{selector}]
    Full screen swipe in the specified direction to find the specified
     selector element
     :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.upload_image_to_ele(context, selector)


@step("clear [{selector}] and input[{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "text", "value": "param2", "name": "文本"}]},
                       verify_function="common_error_parse",
                       action=ActionType.input)
@ele_wrap
def ele_clear_input(context, selector=None, param2=None):
    """
    在[{selector}]中清空并输入[{param2}]
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: string to be input
    """
    g_Context.step.ele_clear_input(context, selector, param2)


@step("clear input[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify_function="common_error_parse",
                       action=ActionType.clear)
@ele_wrap
def clear_input(context, selector=None):
    """
    清空输入框[{selector}]
    Empty the selector element param1 and enter the value param2
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.clear_input(context, selector)


@step("from [{selector}] select [{param2}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"},
             {"type": "value", "value": "param2", "name": "值"}]},
                       verify_function="common_error_parse",
                       action=ActionType.select)
@ele_wrap
def ele_select(context, selector=None, param2=None):
    """
    在[{selector}]中选择[{param2}]
    Select the value param2 from the dropdown box element param1
    :param context: step context
    :param selector: locator string for selector element (or None).
    :param param2: text or value of select option
    """
    g_Context.step.ele_select(context, selector, param2)


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
    [{p_selector}]的[{c_selector}]文案为[{param3}]
    check the text of the child element in the parent element is param3
    :param context: step context
    :param p_selector: locator string for parent selector element (or None).
    :param c_selector: locator string for selector child element (or None).
    :param param3: expected value.
    """
    g_Context.step.find_text_from_parent(context, p_selector, c_selector,
                                         param3)


@step("exist image [{param}]")
@VerifyStep()
def img_exist(context, param):
    """
    存在图像[{param}]
    Check image exist
    :param context: step context
    :param param: image url
    """
    g_Context.step.img_exist(context, param)


@step("not exist image [{param}]")
@VerifyStep()
def img_not_exist(context, param):
    """
     不存在图像[{param}]
    Check image not exist
    :param context: step context
    :param param: image url
    """
    g_Context.step.img_not_exist(context, param)


@step("touch[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def touch_ele(context, selector=None):
    """
    点触[{selector}]
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.ele_touch(context, selector)


@step("touch text[{selector}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "文案"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def touch_text(context, selector=None):
    """
    点触文本[{selector}]
    Click on the selector element
    :param context: step context
    :param selector: locator string for selector element (or None).
    """
    g_Context.step.touch_text(context, selector)


@step("click ele [{selector}] position[{x},{y}]")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}, {"type": "point", "value": "x", "name": "x坐标"},
             {"type": "point", "value": "y", "name": "y坐标"}]},
                       verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def click_ele_point(context, selector, x=None, y=None):
    """
    点击元素[{selector}]位置[{x},{y}]
    Click on the screen coordinates
    :param context: step context
    :param selector: locator string for selector element (or None)
    :param x: Coordinate x-axis
    :param y: Coordinate y-axis.
    """
    g_Context.step.click_ele_point(context, selector, int(float(x)), int(float(y)))


@step("click[{selector}] and cancel dialog")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def close_dialog(context, selector):
    """
    点击[{selector}]并取消弹窗
    Close the dialog box
    :param context: step context
    """
    g_Context.step.close_dialog(context)
    g_Context.step.click_ele(context, selector)


@step("click[{selector}] and accept dialog")
@FlybirdsReportTagInfo(group="element", selectors={
    "path": [{"type": "path", "value": "selector", "name": "元素"}]}, verify_function="common_error_parse",
                       action=ActionType.press)
@ele_wrap
def accept_dialog(context, selector):
    """
    点击[{selector}]并接受弹窗
    Close the dialog box
    :param context: step context
    """
    g_Context.step.accept_dialog(context)
    g_Context.step.click_ele(context, selector)
