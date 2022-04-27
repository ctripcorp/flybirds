# -*- coding: utf-8 -*-
"""
Element position api
"""
import time

from poco.exceptions import PocoNoSuchNodeException

import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
from flybirds.core.plugin.plugins.default.ui_driver.poco import poco_manage
import flybirds.utils.snippet as snippet
from flybirds.core.exceptions import FlybirdPositionChanging


def position_change(poco, select_str, optional, o_position):
    """
    determine whether the position of the element has changed within the
    specified time.
    """
    result = False
    timeout = optional["timeout"]
    current_wait_second = 1
    while (not result) and (timeout > 0):
        try:
            poco_target = poco_manage.create_poco_object_by_dsl(
                poco, select_str, optional
            )
            if poco_target.exists():
                t_position = poco_target.get_position()
                if not snippet.list_comparator(o_position, t_position):
                    result = True
            if result:
                break
        except Exception:
            pass
        time.sleep(current_wait_second)
        timeout -= current_wait_second
        current_wait_second += 1
    return result


def position_not_change(poco, select_str, optional, dur_time, verify_count):
    """
    determine the position of the element has not changed
    """
    poco_ele.wait_exists(poco, select_str, optional)
    prev_position = None

    log_time = dur_time * verify_count

    result = False
    while verify_count > 0 and (not result):
        verify_count -= 1
        try:
            if prev_position is None:
                prev_position = poco_manage.create_poco_object_by_dsl(
                    poco, select_str, optional
                ).get_position()
        except Exception:
            time.sleep(dur_time)
            continue

        time.sleep(dur_time)

        try:
            poco_target = poco_manage.create_poco_object_by_dsl(
                poco, select_str, optional
            )
            cur_position = poco_target.get_position()
            if snippet.list_comparator(prev_position, cur_position):
                result = True
            else:
                prev_position = cur_position
            if result:
                break
        except PocoNoSuchNodeException:
            result = True
        except Exception:
            prev_position = None
    if not result:
        message = "during {}s time, {} position is changing".format(
            log_time, select_str
        )
        raise FlybirdPositionChanging(message)
