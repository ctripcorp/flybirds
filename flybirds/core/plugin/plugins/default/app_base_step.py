# -*- coding: utf-8 -*-
"""
app base step class
"""
import flybirds.core.plugin.plugins.default.step.app as step_app
import flybirds.core.plugin.plugins.default.step.attr as step_attr
import flybirds.core.plugin.plugins.default.step.click as step_click
import flybirds.core.plugin.plugins.default.step.common as step_common
import flybirds.core.plugin.plugins.default.step.page_show_adjust as step_adjust
import flybirds.core.plugin.plugins.default.step.record as step_record
import flybirds.core.plugin.plugins.default.step.swipe as step_swipe
import flybirds.core.plugin.plugins.default.step.verify as step_verify
from flybirds.core.plugin.plugins.default.step.input import ele_input
from flybirds.core.plugin.plugins.default.step.position import (
    position_not_change
)


class AppBaseStep:
    """APP Base Step Class"""

    name = "app_base_step"

    def init_device(self, context, param=None):
        step_app.init_device(context, param)

    def connect_device(self, context, param):
        step_app.connect_device(context, param)

    def start_app(self, context, param):
        step_app.start_app(context, param)

    def restart_app(self, context):
        step_app.restart_app(context)

    def stop_app(self, context):
        step_app.stop_app(context)

    def text_attr_equal(self, context, param1, param2, param3):
        step_attr.text_attr_equal(context, param1, param2, param3)

    def ele_attr_equal(self, context, param1, param2, param3):
        step_attr.ele_attr_equal(context, param1, param2, param3)

    def click_ele(self, context, param):
        step_click.click_ele(context, param)

    def click_text(self, context, param):
        step_click.click_text(context, param)

    def click_coordinates(self, context, x, y):
        step_click.click_coordinates(context, x, y)

    def sleep(self, context, param):
        step_common.sleep(context, param)

    def screenshot(self, context):
        step_common.screenshot(context)

    def prev_fail_scenario_relevance(self, context, param1, param2):
        step_common.prev_fail_scenario_relevance(context, param1, param2)

    def ele_input(self, context, param1, param2):
        ele_input(context, param1, param2)

    def swipe_to_ele(self, context, param1, param2, param3):
        step_adjust.swipe_to_ele(context, param1, param2, param3)

    def full_screen_swipe_to_ele_aaa(self, context, param1, param2):
        step_adjust.full_screen_swipe_to_ele_aaa(context, param1, param2)

    def position_not_change(self, context, param1, param2):
        position_not_change(context, param1, param2)

    def start_screen_record_timeout(self, context, param):
        step_record.start_screen_record_timeout(context, param)

    def start_screen_record(self, context):
        step_record.start_screen_record(context)

    def stop_screen_record(self, context):
        step_record.stop_screen_record(context)

    def ele_swipe(self, context, param1, param2, param3):
        step_swipe.ele_swipe(context, param1, param2, param3)

    def full_screen_swipe(self, context, param1, param2):
        step_swipe.full_screen_swipe(context, param1, param2)

    def wait_text_exist(self, context, param):
        step_verify.wait_text_exist(context, param)

    def text_not_exist(self, context, param):
        step_verify.text_not_exist(context, param)

    def wait_text_disappear(self, context, param):
        step_verify.wait_text_disappear(context, param)

    def wait_ele_exit(self, context, param):
        step_verify.wait_ele_exit(context, param)

    def ele_not_exit(self, context, param):
        step_verify.ele_not_exit(context, param)

    def wait_ele_disappear(self, context, param):
        step_verify.wait_ele_disappear(context, param)

    def ele_text_equal(self, context, param1, param2):
        step_verify.ele_text_equal(context, param1, param2)

    def ele_text_container(self, context, param1, param2):
        step_verify.ele_text_container(context, param1, param2)

    def wait_ele_appear(self, context, param):
        step_verify.wait_ele_appear(context, param)

    def exist_ele(self, context, param):
        step_verify.exist_ele(context, param)
