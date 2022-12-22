# -*- coding: utf-8 -*-
"""
Swipe apis
"""
import time

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap as findsnap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage as pm
import flybirds.utils.point_helper as point_helper
from flybirds.core.exceptions import FlybirdNotFoundException
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan
from flybirds.core.plugin.plugins.default.step.verify import ocr, ocr_txt_contain, img_exist
import flybirds.utils.flybirds_log as log


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
    # get current language
    language = g_Context.get_current_language()
    direct_left = lan.parse_glb_str("left", language)
    direct_right = lan.parse_glb_str("right", language)

    if not (ready_time is None):
        time.sleep(ready_time)
    if start_point[0] > 1:
        start_point[0] = start_point[0] / screen_size[0]
    if start_point[1] > 1:
        start_point[1] = start_point[1] / screen_size[1]
    if distance > 1:
        if direction == direct_left or direction == direct_right:
            distance /= screen_size[0]
        else:
            distance /= screen_size[1]
    air_bdd_direction_swipe(poco, start_point, direction, distance, duration)


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
    poco_ele.wait_exists(poco, container_dsl_str, optional)

    if not (ready_time is None):
        time.sleep(ready_time)

    poco_object = pm.create_poco_object_by_dsl(
        poco, container_dsl_str, optional
    )
    target_position = poco_object.get_position()
    target_size = poco_object.get_size()
    if start_point[0] > 1:
        start_point[0] = (
                                 (target_position[0] * screen_size[0])
                                 - (target_size[0] / 2 * screen_size[0])
                                 + start_point[0]
                         ) / screen_size[0]
    else:
        start_point[0] = (
                target_position[0]
                - target_size[0] / 2
                + target_size[0] * start_point[0]
        )
    if start_point[1] > 1:
        start_point[1] = (
                                 (target_position[1] * screen_size[1])
                                 - (target_size[1] / 2 * screen_size[1])
                                 + start_point[1]
                         ) / screen_size[1]
    else:
        start_point[1] = (
                target_position[1]
                - target_size[1] / 2
                + target_size[1] * start_point[1]
        )

    # get current language
    language = g_Context.get_current_language()
    direct_left = lan.parse_glb_str("left", language)
    direct_right = lan.parse_glb_str("right", language)

    max_x = target_position[0] - target_size[0] / 2 + target_size[0] - 2 / screen_size[0]
    max_y = target_position[1] - target_size[1] / 2 + target_size[1] - 2 / screen_size[1]

    min_x = target_position[0] - target_size[0] / 2 + 2 / screen_size[0]
    min_y = target_position[1] - target_size[1] / 2 + 2 / screen_size[1]

    if distance > 1:
        if direction == direct_left or direction == direct_right:
            distance /= screen_size[0]
            if distance > max_x:
                distance = max_x
            if distance < min_x:
                distance = min_x
        else:
            distance /= screen_size[1]
            if distance > max_y:
                distance = max_y
            if distance < min_y:
                distance = min_y
    else:
        if direction == direct_left or direction == direct_right:
            distance *= target_size[0]
            if distance > max_x:
                distance = max_x
            if distance < min_x:
                distance = min_x
        else:
            distance *= target_size[1]
            if distance > max_y:
                distance = max_y
            if distance < min_y:
                distance = min_y

    air_bdd_direction_swipe(poco, start_point, direction, distance, duration)


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
    # get current language
    language = g_Context.get_current_language()
    direct_left = lan.parse_glb_str("left", language)
    direct_right = lan.parse_glb_str("right", language)
    direct_up = lan.parse_glb_str("up", language)
    direct_down = lan.parse_glb_str("down", language)

    end_point = [start_point[0], start_point[1]]
    if direction == direct_left:
        end_point[0] -= distance
        if end_point[0] < 0.0:
            end_point[0] = 0
            start_point[0] = distance
    elif direction == direct_right:
        end_point[0] += distance
        if end_point[0] > 1.0:
            end_point[0] = 1
            start_point[0] = 1 - distance
    elif direction == direct_up:
        end_point[1] -= distance
        if end_point[1] < 0:
            end_point[1] = 0
            start_point[1] = distance
    elif direction == direct_down:
        end_point[1] += distance
        if end_point[1] > 1:
            end_point[1] = 1
            start_point[1] = 1 - distance
    air_bdd_percent_point_swipe(poco, start_point, end_point, duration)


def air_bdd_percent_point_swipe(poco, start_point, end_point, duration=None):
    """
    swipe from the start point to the end point
    :param poco:
    :param start_point:
    :param end_point:
    :param duration:
    :return:
    """
    if duration is None:
        poco.swipe(start_point, end_point)
    else:
        poco.swipe(start_point, end_point, duration=duration)
    if gr.get_frame_config_value("use_snap", False):
        findsnap.fix_refresh_status(True)


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
    direction = point_helper.search_direction_switch(direction)
    start_point = point_helper.get_swipe_search_start_point(
        direction, start_x, start_y
    )

    if distance is None:
        distance = 0.3

    log_count = swipe_count
    searched = False
    while swipe_count >= 0:
        print("swipe_count", swipe_count)
        try:
            search_poco_object = pm.create_poco_object_by_dsl(
                poco, search_dsl_str, search_optional
            )
            if search_poco_object.exists():
                searched = True
                break
        except Exception:
            pass
        if swipe_count == 0:
            break
        air_bdd_full_screen_swipe(
            poco, start_point, screen_size, direction, distance, duration
        )
        swipe_count -= 1
    if not searched:
        message = "swipe to {} {} times，not find {}".format(
            direction, log_count, search_dsl_str
        )
        raise FlybirdNotFoundException(message, {})
    if gr.get_frame_config_value("use_snap", False):
        findsnap.fix_refresh_status(True)


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
    poco_ele.wait_exists(poco, container_dsl_str, container_optional)
    direction = point_helper.search_direction_switch(direction)
    start_point = point_helper.get_swipe_search_start_point(
        direction, start_x, start_y
    )

    if distance is None:
        distance = 0.3

    log_count = swipe_count
    searched = False
    while swipe_count >= 0:
        try:
            search_poco_object = pm.create_poco_object_by_dsl(
                poco, search_dsl_str, search_optional
            )
            if search_poco_object.exists():
                searched = True
                break
        except Exception:
            pass
        if swipe_count == 0:
            break
        air_bdd_ele_swipe(
            poco,
            container_dsl_str,
            container_optional,
            start_point,
            screen_size,
            direction,
            distance,
            duration,
        )
        swipe_count -= 1
    if not searched:
        message = "{} swipe to {} {} times，not find {}".format(
            container_dsl_str, direction, log_count, search_dsl_str
        )
        raise FlybirdNotFoundException(message, {})
    if gr.get_frame_config_value("use_snap", False):
        findsnap.fix_refresh_status(True)


def full_screen_swipe_search_ocr(
        context,
        poco,
        search_dsl_str,
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
    direction = point_helper.search_direction_switch(direction)
    start_point = point_helper.get_swipe_search_start_point(
        direction, start_x, start_y
    )

    if distance is None:
        distance = 0.3

    log_count = swipe_count
    searched = False
    while swipe_count >= 0:
        try:
            ocr(context)
            searched = ocr_txt_contain(context, search_dsl_str, islog=False)
            if searched is True:
                log.info("[full_screen_swipe_search_ocr]txt found")
                break
        except Exception:
            pass
        if swipe_count == 0:
            break
        air_bdd_full_screen_swipe(
            poco, start_point, screen_size, direction, distance, duration
        )
        swipe_count -= 1
    if not searched:
        for line in g_Context.ocr_result:
            log.info(f"[image ocr result] scan line info is:{line}")
        message = "swipe to {} {} times，not find {}".format(
            direction, log_count, search_dsl_str
        )
        raise FlybirdNotFoundException(message, {})


def full_screen_swipe_search_img(
        context,
        poco,
        search_dsl_str,
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
    direction = point_helper.search_direction_switch(direction)
    start_point = point_helper.get_swipe_search_start_point(
        direction, start_x, start_y
    )

    if distance is None:
        distance = 0.3

    log_count = swipe_count
    searched = False
    while swipe_count >= 0:
        try:
            searched = img_exist(context, search_dsl_str, islog=False)
            if searched is True:
                break
        except Exception:
            pass
        if swipe_count == 0:
            break
        air_bdd_full_screen_swipe(
            poco, start_point, screen_size, direction, distance, duration
        )
        swipe_count -= 1
    if not searched:
        step_index = context.cur_step_index - 1
        src_path = "../../../{}".format(search_dsl_str)
        data = (
            'embeddingsTags, stepIndex={}, <image class ="screenshot"'
            ' width="375" src="{}" />'.format(step_index, src_path)
        )
        context.scenario.description.append(data)

        message = "swipe to {} {} times，not find {}".format(
            direction, log_count, search_dsl_str
        )
        raise FlybirdNotFoundException(message, {})
