# -*- coding: utf-8 -*-
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan


def get_swipe_search_start_point(direction, start_x=None, start_y=None):
    """
    Get the start coordinate point of the sliding operation
    """
    # get current language
    language = g_Context.get_current_language()
    direct_left = lan.parse_glb_str("left", language)
    direct_right = lan.parse_glb_str("right", language)
    direct_up = lan.parse_glb_str("up", language)
    direct_down = lan.parse_glb_str("down", language)

    start_point = [None, None]
    if start_x is None:
        if direction == direct_left:
            start_point[0] = 0.666
        elif direction == direct_right:
            start_point[0] = 0.333
        else:
            start_point[0] = 0.5
    else:
        start_point[0] = start_x
    if start_y is None:
        if direction == direct_up:
            start_point[1] = 0.666
        elif direction == direct_down:
            start_point[1] = 0.333
        else:
            start_point[1] = 0.5
    else:
        start_point[1] = start_y
    return start_point


def search_direction_switch(direction):
    """
    To find in a certain direction,
    you have to slide in a certain direction
    to change the direction parameter
    """
    # get current language
    language = g_Context.get_current_language()
    direct_left = lan.parse_glb_str("left", language)
    direct_right = lan.parse_glb_str("right", language)
    direct_up = lan.parse_glb_str("up", language)
    direct_down = lan.parse_glb_str("down", language)

    direction = direction.strip()
    if direction == direct_left:
        direction = direct_right
    elif direction == direct_right:
        direction = direct_left
    elif direction == direct_up:
        direction = direct_down
    elif direction == direct_down:
        direction = direct_up
    return direction
