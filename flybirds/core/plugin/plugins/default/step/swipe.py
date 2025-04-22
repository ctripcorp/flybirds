# -*- coding: utf-8 -*-
"""
Element swipe
"""
import re

from airtest.core.android.touch_methods.base_touch import BaseTouch, DownEvent, SleepEvent, MoveEvent, UpEvent
from airtest.core.android.touch_methods.touch_proxy import AdbTouchImplementation, MinitouchImplementation
from airtest.core.api import text, time
from airtest.utils.snippet import (on_method_ready)

import flybirds.core.global_resource as g_res
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap as findsnap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage as pm
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_swipe as ps
import flybirds.utils.dsl_helper as dsl_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.point_helper as point_helper
from flybirds.core.exceptions import FlybirdNotFoundException
from flybirds.core.global_context import GlobalContext
from flybirds.utils import language_helper


def ele_swipe(context, param1, param2, param3):
    poco_instance = gr.get_value("pocoInstance")

    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    optional = {}
    if "path" in param1_dict.keys():
        optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    param3_dict = dsl_helper.params_to_dic(param3, "swipeNumber")

    start_point = [0.5, 0.5]
    if "startX" in param3_dict.keys():
        start_point[0] = float(param3_dict["startX"])
    if "startY" in param3_dict.keys():
        start_point[1] = float(param3_dict["startY"])

    screen_size = gr.get_device_size()
    direction = param2.strip()
    if g_res is None or not g_res.get_app_config_value("finger_direction_switch", False):
        direction = point_helper.search_direction_switch(param2.strip())

    distance = float(param3_dict["swipeNumber"])

    duration = None
    if gr.get_frame_config_value("use_swipe_duration", False):
        duration = gr.get_frame_config_value("swipe_duration", 1)
    if "duration" in param3_dict.keys():
        duration = float(param3_dict["duration"])

    ready_time = gr.get_frame_config_value("swipe_ready_time", 1)
    if "readyTime" in param3_dict.keys():
        ready_time = float(param3_dict["readyTime"])

    ps.air_bdd_ele_swipe(
        poco_instance,
        selector_str,
        optional,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time,
    )


def full_screen_swipe(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")

    param2_dict = dsl_helper.params_to_dic(param2, "swipeNumber")

    start_point = [0.5, 0.5]
    if "startX" in param2_dict.keys():
        start_point[0] = float(param2_dict["startX"])
    if "startY" in param2_dict.keys():
        start_point[1] = float(param2_dict["startY"])

    screen_size = gr.get_device_size()
    # direction = param1.strip()
    # if g_res is None or not g_res.get_app_config_value("finger_direction_switch", False):
    #     direction = point_helper.search_direction_switch(param1.strip())
    direction = point_helper.search_direction_switch(param1.strip())
    distance = float(param2_dict["swipeNumber"])

    duration = None
    if gr.get_frame_config_value("use_swipe_duration", False):
        duration = gr.get_frame_config_value("swipe_duration", 1)
    if "duration" in param2_dict.keys():
        duration = float(param2_dict["duration"])

    ready_time = gr.get_frame_config_value("swipe_ready_time", 1)
    if "readyTime" in param2_dict.keys():
        ready_time = float(param2_dict["readyTime"])

    ps.air_bdd_full_screen_swipe(
        poco_instance,
        start_point,
        screen_size,
        direction,
        distance,
        duration,
        ready_time,
    )


class FlyBirdsEvent:

    def __init__(self):
        pass

    @staticmethod
    def on_search(event_obj):
        poco = gr.get_value("pocoInstance")
        optional = {"timeout": 20}
        selector = event_obj["selector"]
        try:
            search_poco_object = pm.create_poco_object_by_dsl(
                poco, selector, optional
            )
            search_result = search_poco_object.exists()
            if search_result:
                log.info(f"Element found successfully: {selector}")
                return True
            log.info(f"Element not found: {selector}")
            return False
        except Exception as e:
            log.info(f"Element not found: {selector}, error: {e}")
            return False

    @staticmethod
    def on_click(event_obj):

        poco = gr.get_value("pocoInstance")
        optional = {}
        selector = event_obj["selector"]
        try:
            poco_object = pm.create_poco_object_by_dsl(
                poco, selector, optional
            )
            search_result = poco_object.exists()
            if search_result is False:
                # find selector in poco domtree
                if "element=" in selector:
                    data = poco.agent.hierarchy.dump()
                    result = find_payload_with_resource_id(data, selector)
                    if result is None:
                        log.info(f"Element not found: {selector}")
                        return False
                    else:
                        x, y = result.get("pos")
                        poco.click([x, y])
                        log.info(f"Element found successfully and clicked: {selector}")
                        return True
                else:
                    return False
            poco_object.click()
            log.info(f"Element found successfully and clicked: {selector}")
            return True
        except Exception as e:
            log.info(f"Element not found: {selector}, error: {e}")
            return False

    @staticmethod
    def on_input(event_obj):
        selector = event_obj["selector"]
        input_str = event_obj["param"]
        poco = gr.get_value("pocoInstance")
        optional = {"timeout": 20}
        try:
            poco_object = pm.create_poco_object_by_dsl(
                poco, selector, optional
            )
            if poco_object.exists() is False:
                log.info(f"Element not found when input {input_str} into : {selector}")
                return False
            poco_object.click()
            text(input_str)
            # GlobalContext.element.str_input(input_str)
            log.info(f"{selector} input {input_str} successfully")
            return True
        except Exception as e:
            log.info(f"Element not found when input {input_str} into : {selector}, error: {e}")
            return False


def handle_str(un_handle_str):
    res = re.match(r"([\S\s]+),\s*[0-9_]+\s*", un_handle_str)
    if res is not None:
        return res.group(1)
    else:
        return un_handle_str


def find_payload_with_resource_id(data, target_resource_id):
    if "=" in target_resource_id:
        target_resource_id = target_resource_id.split("=")[1]
    if isinstance(data, dict):
        if data.get("payload", {}).get("name") == target_resource_id:
            return data["payload"]
        if data.get("payload", {}).get("text") == target_resource_id:
            return data["payload"]
        for key, value in data.items():
            result = find_payload_with_resource_id(value, target_resource_id)
            if result:
                return result
    elif isinstance(data, list):
        for item in data:
            result = find_payload_with_resource_id(item, target_resource_id)
            if result:
                return result
    return None


# 新滑动方法滑动的同时检测元素是否存在
def full_screen_swipe_new(context, direction, selector):
    screen_size = gr.get_device_size() or [1080, 1920]
    handled_selector_temp = handle_str(selector)
    selector_dict = dsl_helper.params_to_dic(handled_selector_temp)
    selector = selector_dict.get("selector")
    if selector_dict.get("distance") is not None and float(selector_dict.get("distance")) > 1:
        distance = int(selector_dict.get("distance"))
    else:
        distance = 6000
    # search_optional = {}
    # if "path" in selector_dict.keys():
    #     search_optional["path"] = selector_dict["path"]
    # elif "multiSelector" in selector_dict.keys():
    #     search_optional["multiSelector"] = selector_dict["multiSelector"]
    # 起始参数放入全局缓存
    event_obj = {
        "context": context,
        "selector": selector,
        "direction": direction,
        "action": FlyBirdsEvent.on_search}
    tuple_from_xy, tuple_to_xy = build_swipe_search_point(direction, screen_size, selector_dict, distance)
    # 每次移动距离
    duration = 100
    # 移动次数
    steps = int(distance / duration)
    time.sleep(1)
    log.info(f"swipe {direction} to found {selector}")
    gr.get_value("deviceInstance").touch_proxy.swipe(tuple_from_xy, tuple_to_xy, duration=duration, steps=steps,
                                                     event_obj=event_obj)


# 滑动查找并点击
def full_screen_swipe_click(context, selector, direction):
    screen_size = gr.get_device_size() or [1080, 1920]
    handled_selector_temp = handle_str(selector)
    selector_dict = dsl_helper.params_to_dic(handled_selector_temp)
    selector = selector_dict.get("selector")
    duration = 100
    if selector_dict.get("distance") is not None and float(selector_dict.get("distance")) > 1:
        distance = int(selector_dict.get("distance"))
    else:
        distance = 6000
    event_obj = {
        "context": context,
        "selector": selector,
        "direction": direction,
        "action": FlyBirdsEvent.on_click}
    tuple_from_xy, tuple_to_xy = build_swipe_search_point(direction, screen_size, selector_dict, distance)
    steps = int(distance / duration)
    time.sleep(1)
    log.info(f"swipe {direction} to found {selector} then click")
    gr.get_value("deviceInstance").touch_proxy.swipe(tuple_from_xy, tuple_to_xy, duration=duration, steps=steps,
                                                     event_obj=event_obj)


# 滑动查找并输入
def full_screen_swipe_input(context, selector, param, direction):
    screen_size = gr.get_device_size() or [1080, 1920]
    handled_selector_temp = handle_str(selector)
    selector_dict = dsl_helper.params_to_dic(handled_selector_temp)
    selector = selector_dict.get("selector")
    if selector_dict.get("distance") is not None and float(selector_dict.get("distance")) > 1:
        distance = int(selector_dict.get("distance"))
    else:
        distance = 6000
    duration = 100
    event_obj = {
        "context": context,
        "selector": selector,
        "param": param,
        "direction": direction,
        "action": FlyBirdsEvent.on_input}
    tuple_from_xy, tuple_to_xy = build_swipe_search_point(direction, screen_size, selector_dict, distance)
    steps = int(distance / duration)
    time.sleep(1)
    log.info(f"swipe {direction} to found {selector} then input {param}")
    gr.get_value("deviceInstance").touch_proxy.swipe(tuple_from_xy, tuple_to_xy, duration=duration, steps=steps,
                                                     event_obj=event_obj)


@on_method_ready('install_and_setup')
def swipe(self, tuple_from_xy, tuple_to_xy, duration=0.8, steps=5, event_obj=None):
    """
    Perform swipe event.

    Args:
        tuple_from_xy: start point
        tuple_to_xy: end point
        duration: time interval for swipe duration, default is 0.8
        steps: size of swipe step, default is 5
        event_obj: event object

    Returns:
        None

    """
    # 兼容老的滑动逻辑
    if event_obj is None:
        origin_swipe(self, tuple_from_xy, tuple_to_xy, duration=duration, steps=steps)
        return
    swipe_events = [DownEvent(tuple_from_xy, pressure=50), SleepEvent(0.1)]
    swipe_events += __swipe_move(tuple_from_xy, tuple_to_xy, duration=duration, steps=steps)
    # swipe_events.append(UpEvent())
    self.perform(swipe_events, event_obj=event_obj)


# 重新滑动事件方法
def __swipe_move(tuple_from_xy, tuple_to_xy, duration=0.8, steps=5):
    """
    Return a sequence of swipe motion events (only MoveEvent)

    minitouch protocol example::

        d 0 0 0 50
        c
        m 0 20 0 50
        c
        u 0
        c

    Args:
        tuple_from_xy: start point
        tuple_to_xy: end point
        duration: time interval for swipe duration, default is 0.8
        steps: size of swipe step, default is 5

    Returns:
        [MoveEvent(from_x, from_y), ..., MoveEvent(to_x, to_y)]
    """
    from_x, from_y = tuple_from_xy
    to_x, to_y = tuple_to_xy

    ret = []
    # interval = float(duration) / (steps + 1)

    for i in range(1, steps):
        ret.append(MoveEvent((from_x + (to_x - from_x) * i / steps,
                              from_y + (to_y - from_y) * i / steps)))
        ret.append(SleepEvent(0.5))
    ret += [MoveEvent((to_x, to_y), pressure=50), SleepEvent(0.5)]
    return ret


# 根据motion_events进行滑动操作
@on_method_ready('install_and_setup')
def perform(self, motion_events, interval=0.02, event_obj=None):
    """
    Perform a sequence of motion events including: UpEvent, DownEvent, MoveEvent, SleepEvent

    Args:
        motion_events: a list of MotionEvent instances
        interval: minimum interval between events
        event_obj: event object, such as on_search, on_click, on_input

    Returns:
        None
    """
    # 兼容老的滑动逻辑
    if event_obj is None:
        origin_perform(self, motion_events)
        return
    search_result = False
    event_count = 0
    for event in motion_events:
        # 每循环10次事件执行下action对应操作

        if event_count % 10 == 0 and event_obj is not None:
            search_result = event_obj["action"](event_obj)
            if search_result:
                break

        if isinstance(event, SleepEvent):
            time.sleep(event.seconds)
        else:
            cmd = event.getcmd(transform=self.transform_xy)
            self.handle(cmd)
            time.sleep(interval)
        event_count += 1

    if search_result is False:
        message = "{} swipe not find {}".format(
            event_obj["direction"], event_obj["selector"])
        raise FlybirdNotFoundException(message, {event_obj["selector"]})
    if gr.get_frame_config_value("use_snap", False):
        findsnap.fix_refresh_status(True)


# 重写坐标转换方法，解决滑动时坐标转换问题
def transform_xy(self, x, y):
    """
    Transform coordinates (x, y) according to the device display

    Args:
        x: coordinate x
        y: coordinate y

    Returns:
        transformed coordinates (x, y)

    """
    return x, y


def build_swipe_search_point(direction, screen_size, selector_dict, move_distance=6000):
    """
    build the start and end coordinate point of the sliding data
    """
    start_x = None
    start_y = None
    # get current language
    language = GlobalContext.get_current_language()
    direction = direction.strip()
    pw, ph = screen_size
    start_point = [0.5 * pw, 0.5 * ph]
    end_point = [0.5 * pw, 0.5 * ph]
    if "startX" in selector_dict.keys():
        start_x = float(selector_dict["startX"])
        if start_x > 1:
            start_x = start_x / screen_size[0]
    if "startY" in selector_dict.keys():
        start_y = float(selector_dict["startY"])
        if start_y > 1:
            start_y = start_y / screen_size[1]
    # 滑动距离默认为当前手机分辨率2个屏幕距离
    if direction == "left" or direction == language_helper.parse_glb_str("left", language):
        if start_x is None:
            start_x = 0.666
        if start_y is None:
            start_y = 0.5
        start_point = [start_x * pw, start_y * ph]
        end_point = [start_x * pw - move_distance, start_y * ph]
    if direction == "right" or direction == language_helper.parse_glb_str("right", language):
        if start_x is None:
            start_x = 0.333
        if start_y is None:
            start_y = 0.5
        start_point = [start_x * pw, start_y * ph]
        end_point = [start_x * pw + move_distance, start_y * ph]
    if direction == "up" or direction == language_helper.parse_glb_str("up", language):
        if start_x is None:
            start_x = 0.5
        if start_y is None:
            start_y = 0.333
        start_point = [start_x * pw, start_y * ph]
        end_point = [start_x * pw, start_y * ph + move_distance]
    if direction == "down" or direction == language_helper.parse_glb_str("down", language):
        if start_x is None:
            start_x = 0.5
        if start_y is None:
            start_y = 0.666
        start_point = [start_x * pw, start_y * ph]
        end_point = [start_x * pw, start_y * ph - move_distance]
    # 设置默认触屏起始坐标
    log.info("start_point: %s, end_point: %s, move_distance: %s" % (start_point, end_point, move_distance))
    return start_point, end_point


def adb_swipe(self, p1, p2, duration=0.5, event_obj=None, *args, **kwargs):
    duration *= 1000
    self.base_touch.swipe(p1, p2, duration=duration, event_obj=event_obj)


def min_swipe(self, p1, p2, duration=0.5, steps=5, fingers=1, event_obj=None):
    p1 = self.ori_transformer(p1)
    p2 = self.ori_transformer(p2)
    if fingers == 1:
        self.base_touch.swipe(p1, p2, duration=duration, steps=steps, event_obj=event_obj)
    elif fingers == 2:
        self.base_touch.two_finger_swipe(p1, p2, duration=duration, steps=steps, event_obj=event_obj)
    else:
        raise Exception("param fingers should be 1 or 2")


# 兼容老版滑动方法
origin_swipe = BaseTouch.swipe
origin_perform = BaseTouch.perform
origin_adb_touch_swipe = AdbTouchImplementation.swipe
origin_adb_min_swipe = MinitouchImplementation.swipe

# 重写poco滑动方法
BaseTouch.swipe = swipe
BaseTouch.perform = perform
AdbTouchImplementation.swipe = adb_swipe
MinitouchImplementation.swipe = min_swipe
