# -*- coding: utf-8 -*-
"""
This module contains the UI elements Core APIs.
"""

from flybirds.core.global_context import GlobalContext as g_context

"""
UI elements Operations
"""


def str_input(input_str, after_input_wait=None):
    """
    Input text on the target device. Text input widget must be active first.
    :param input_str: text to input, unicode is supported
    :param after_input_wait: waiting time after input
    :return:
    """
    g_context.element.str_input(input_str, after_input_wait=after_input_wait)


def key_event(key_code):
    """
      Perform key event on the device.
    * ``iOS``: Only supports home/volumeUp/volumeDown::
    :param key_code:  platform specific key name
    :return: None
    """
    g_context.element.key_event(key_code)


"""
poco UI object Operations
"""


def ui_driver_init():
    """init ui driver"""
    return g_context.element.ui_driver_init()


def get_ele_attr(
    poco,
    selector_str,
    optional,
    attr_name,
    deal_method=None,
    params_deal_module=None,
):
    """
    Get the specified attribute of the element, and after the attribute is
    obtained, you can choose whether to process it through a custom method.
    """
    return g_context.element.get_ele_attr(
        poco,
        selector_str,
        optional,
        attr_name,
        deal_method=deal_method,
        params_deal_module=params_deal_module,
    )


def air_bdd_click(
    poco,
    select_dsl_str,
    optional,
    verify_dsl_str=None,
    verify_optional=None,
    verify_action=None,
):
    """
    Click the element. optional parameters to determine whether the clicked
    page is rendered.
    """
    g_context.element.air_bdd_click(
        poco,
        select_dsl_str,
        optional,
        verify_dsl_str=verify_dsl_str,
        verify_optional=verify_optional,
        verify_action=verify_action,
    )


def verify_click_end(
    poco, verify_dsl_str, verify_optional, verify_action, o_position, o_text
):
    """
    verify_click_end
    """
    g_context.element.verify_click_end(
        poco,
        verify_dsl_str,
        verify_optional,
        verify_action,
        o_position,
        o_text,
    )


def wait_exists(poco, selector_str, optional):
    """
     determine whether the element exists within the optional
    :param poco: ui driver
    :param selector_str: the string of selector
    :param optional:
    :return: None
    """
    g_context.element.wait_exists(poco, selector_str, optional)


def not_exist(poco, selector_str, optional):
    """
    determine whether the element does not exist
    :param poco: ui driver
    :param selector_str: the string of selector
    :param optional:
    :return: None
    """
    g_context.element.not_exist(poco, selector_str, optional)


def wait_disappear(poco, selector_str, optional):
    """
    determine whether the element disappears within the optional
    :param poco: ui driver
    :param selector_str:
    :param optional:
    :return: None
    """
    g_context.element.wait_disappear(poco, selector_str, optional)


def detect_error():
    """
    detect errors
    """
    g_context.element.detect_error()


def find_ele_by_snap(poco, config, optional):
    """
    Determine whether the element exists in the snapshot within optional
    :param poco: ui driver
    :param config:
    :param optional:
    :return: None
    """
    g_context.element.find_ele_by_snap(poco, config, optional)


def verify_ele_by_snap(poco, config, optional):
    """
     use snapshots to judge element text
    :param poco: ui driver
    :param config:
    :param optional:
    :return:None
    """
    g_context.element.verify_ele_by_snap(poco, config, optional)


def air_bdd_input(
    poco, select_dsl_str, optional, input_str, after_input_wait=None
):
    """
    Input text
    :return:
    """
    g_context.element.air_bdd_input(
        poco,
        select_dsl_str,
        optional,
        input_str,
        after_input_wait=after_input_wait,
    )


def create_poco_object_by_dsl(poco, select_dsl_str, optional):
    """
    get the poco element of optional parameter structure and selector structure
    :param poco:
    :param select_dsl_str:
    :param optional:
    :return: ui driver instance
    """
    return g_context.element.create_poco_object_by_dsl(
        poco, select_dsl_str, optional
    )


def position_change(poco, select_str, optional, o_position):
    """
    determine whether the position of the element has changed within the
    specified time
    :return: 'False' or 'True'
    """
    return g_context.element.position_change(
        poco, select_str, optional, o_position
    )


def position_not_change(poco, select_str, optional, dur_time, verify_count):
    """
    determine the position of the element has not changed
    """
    g_context.element.position_not_change(
        poco, select_str, optional, dur_time, verify_count
    )


def air_bdd_screen_size(poco_instance):
    """
    get the screen size of the device in use
    :param poco_instance: ui  driver
    :return: tuple: float number indicating the screen physical resolution
    in pixels
    """
    return g_context.element.air_bdd_screen_size(poco_instance)


def create_poco_object(poco, select_dic={}):
    """
    create page elements corresponding to pocoUi elements
    :param poco:
    :param select_dic: Constraints for constructing pocoObject
    :return:
    """
    return g_context.element.create_poco_object(poco, select_dic)


def create_parent(poco_object):
    """
    create the parent element of the pocoUi element
    :param poco_object:
    :return:
    """
    return g_context.element.create_parent(poco_object)


def create_first_child(poco_object, select_dic={}):
    """
    create the first child element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    return g_context.element.create_first_child(
        poco_object, select_dic=select_dic
    )


def create_first_offspring(poco_object, select_dic={}):
    """
    create the first descendant element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    return g_context.element.create_first_offspring(
        poco_object, select_dic=select_dic
    )


def create_first_sibling(poco_object, select_dic={}):
    """
    create the first sibling element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    return g_context.element.create_first_sibling(
        poco_object, select_dic=select_dic
    )


def select_child(poco_object, target_index, select_dic={}):
    """
    select the child element of the pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any child elements or the number of child elements is less than
    target_index,an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return g_context.element.select_child(
        poco_object, target_index, select_dic=select_dic
    )


def select_offspring(poco_object, target_index, select_dic={}):
    """
    select which descendant element of pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any descendant elements or the number of descendant elements is less than
    target_index, an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return g_context.element.select_offspring(
        poco_object, target_index, select_dic=select_dic
    )


def select_sibling(poco_object, target_index, select_dic={}):
    """
    select which sibling element of pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any sibling elements or the number of sibling elements is less than
    target_index, an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return g_context.element.select_sibling(
        poco_object, target_index, select_dic=select_dic
    )


def air_bdd_full_screen_swipe(
    poco,
    start_point,
    screen_size,
    direction,
    distance,
    duration,
    ready_time=None,
):
    """
    In the full screen range, slide from the specified starting point in one
    direction up, down, left, and right to specify the distance.
    """
    g_context.element.air_bdd_full_screen_swipe(
        poco,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time=ready_time,
    )


def air_bdd_ele_swipe(
    poco,
    container_dsl_str,
    optional,
    start_point,
    screen_size,
    direction,
    distance,
    duration,
    ready_time=None,
):
    """
    Slides a specified distance up, down, left, or right from a specified
    starting point within a sliding element.
    """
    g_context.element.air_bdd_ele_swipe(
        poco,
        container_dsl_str,
        optional,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time=ready_time,
    )


def air_bdd_direction_swipe(
    poco, start_point, direction, distance, duration=None
):
    """
    swipe the specified distance from the starting point to one of up, down,
    left, and right.
    :param poco:
    :param start_point:
    :param direction:
    :param distance:
    :param duration:
    :return:
    """
    g_context.element.air_bdd_direction_swipe(
        poco, start_point, direction, distance, duration=duration
    )


def air_bdd_percent_point_swipe(poco, start_point, end_point, duration=None):
    """
    swipe from the start point to the end point
    :param poco:
    :param start_point:
    :param end_point:
    :param duration:
    :return:
    """
    g_context.element.air_bdd_percent_point_swipe(
        poco, start_point, end_point, duration=duration
    )


def full_screen_swipe_search(
    poco,
    search_dsl_str,
    search_optional,
    swipe_count,
    direction,
    screen_size,
    start_x=None,
    start_y=None,
    distance=None,
    duration=None,
):
    """
    Full screen swipe to find
    """
    g_context.element.full_screen_swipe_search(
        poco,
        search_dsl_str,
        search_optional,
        swipe_count,
        direction,
        screen_size,
        start_x=start_x,
        start_y=start_y,
        distance=distance,
        duration=duration,
    )


def air_bdd_swipe_search(
    poco,
    container_dsl_str,
    container_optional,
    search_dsl_str,
    search_optional,
    swipe_count,
    screen_size,
    direction,
    start_x=None,
    start_y=None,
    distance=None,
    duration=None,
):
    """
    swipe in a certain direction in the full screen or within an element to
    find an element.
    """
    g_context.element.air_bdd_swipe_search(
        poco,
        container_dsl_str,
        container_optional,
        search_dsl_str,
        search_optional,
        swipe_count,
        screen_size,
        direction,
        start_x=start_x,
        start_y=start_y,
        distance=distance,
        duration=duration,
    )


def get_ele_text_replace_space(
    poco, selector_str, optional, deal_method_name, params_deal_module
):
    """
    get the text of the element, and after the text is obtained,
    you can choose whether to process it by a custom method
    """
    return g_context.element.get_ele_text_replace_space(
        poco, selector_str, optional, deal_method_name, params_deal_module
    )


def get_ele_text(
    poco, selector_str, optional, deal_method_name, params_deal_module
):
    """
    get the text of the element, and after the text is obtained,
    you can choose whether to process it by a custom method
    """
    return g_context.element.get_ele_text(
        poco, selector_str, optional, deal_method_name, params_deal_module
    )


def text_change(poco, select_str, optional, o_text):
    """
    determine whether the copy of the element has changed within the specified
    time.
    """
    return g_context.element.text_change(poco, select_str, optional, o_text)


def ele_text_is(
    poco,
    selector_str,
    target_str,
    optional,
    deal_method=None,
    params_deal_module=None,
):
    """
    determine whether the element is the expected value
    """
    g_context.element.ele_text_is(
        poco,
        selector_str,
        target_str,
        optional,
        deal_method=deal_method,
        params_deal_module=params_deal_module,
    )


def ele_text_contains(
    poco,
    selector_str,
    target_str,
    optional,
    deal_method=None,
    params_deal_module=None,
):
    """
    determine whether the element contains
    """
    g_context.element.ele_text_contains(
        poco,
        selector_str,
        target_str,
        optional,
        deal_method=deal_method,
        params_deal_module=params_deal_module,
    )


def ele_attr_is(
    poco,
    selector_str,
    optional,
    target_attr,
    target_attr_value,
    deal_method,
    params_deal_module,
):
    """
    determine whether the specified attribute of the element is the expected
    value.
    """
    g_context.element.ele_attr_is(
        poco,
        selector_str,
        optional,
        target_attr,
        target_attr_value,
        deal_method,
        params_deal_module,
    )
