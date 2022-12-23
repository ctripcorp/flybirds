# -*- coding: utf-8 -*-
"""
app base step class
"""
import flybirds.core.plugin.plugins.default.step.app as step_app
import flybirds.core.plugin.plugins.default.step.attr as step_attr
import flybirds.core.plugin.plugins.default.step.click as step_click
import flybirds.core.plugin.plugins.default.step.common as step_common
import flybirds.core.plugin.plugins.default.step.page_show_adjust \
    as step_adjust
import flybirds.core.plugin.plugins.default.step.record as step_record
import flybirds.core.plugin.plugins.default.step.swipe as step_swipe
import flybirds.core.plugin.plugins.default.step.verify as step_verify
from flybirds.core.plugin.plugins.default.step.app \
    import (to_app_home, app_login, app_logout)
from flybirds.core.plugin.plugins.default.step.input \
    import (ele_input, ocr_text_input)
from flybirds.core.plugin.plugins.default.step.position import (
    position_not_change
)


class AppBaseStep:
    """APP Base Step Class"""

    name = "app_base_step"

    def init_device(self, context, param=None):
        step_app.init_device(context, param)

    def change_ocr_lang(self, context, param=None):
        step_common.change_ocr_lang(context, lang=param)

    def img_exist(self, context, param):
        step_verify.img_exist(context, param)

    def img_not_exist(self, context, param):
        step_verify.img_not_exist(context, param)

    def connect_device(self, context, param):
        step_app.connect_device(context, param)

    def start_app(self, context, param):
        step_app.start_app(context, param)

    def restart_app(self, context):
        step_app.restart_app(context)

    def stop_app(self, context):
        step_app.stop_app(context)

    def text_attr_equal(self, context, selector, param2, param3):
        step_attr.text_attr_equal(context, selector, param2, param3)

    def ele_attr_equal(self, context, selector, param2, param3):
        step_attr.ele_attr_equal(context, selector, param2, param3)

    def click_ele(self, context, selector):
        step_click.click_ele(context, selector)

    def click_text(self, context, selector):
        step_click.click_text(context, selector)

    def click_coordinates(self, context, x, y):
        step_click.click_coordinates(context, x, y)

    def click_ocr_text(self, context, selector):
        step_click.click_ocr_text(context, selector)

    def click_regional_ocr_text(self, context, selector, param2):
        step_click.click_regional_ocr_text(context, selector, param2)

    def click_regional_ocr(self, context, selector):
        step_click.click_regional_ocr(context, selector)

    def click_image(self, context, selector):
        step_click.click_image(context, selector)

    def sleep(self, context, param):
        step_common.sleep(context, param)

    def screenshot(self, context):
        step_common.screenshot(context)

    def ocr(self, context, param=None):
        step_common.ocr(context, param)

    def prev_fail_scenario_relevance(self, context, param1, param2):
        step_common.prev_fail_scenario_relevance(context, param1, param2)

    def ele_input(self, context, selector, param2):
        ele_input(context, selector, param2)

    def ocr_text_input(self, context, selector, param2):
        ocr_text_input(context, selector, param2)

    def swipe_to_ele(self, context, p_selector, param2, c_selector):
        step_adjust.swipe_to_ele(context, p_selector, param2, c_selector)

    def full_screen_swipe_to_ele_aaa(self, context, param1, selector):
        step_adjust.full_screen_swipe_to_ele_aaa(context, param1, selector)

    def full_screen_swipe_to_ocr_txt(self, context, param1, selector):
        step_adjust.full_screen_swipe_to_ocr_txt(context, param1, selector)

    def full_screen_swipe_to_img(self, context, param1, selector):
        step_adjust.full_screen_swipe_to_img(context, param1, selector)

    def position_not_change(self, context, selector, param2):
        position_not_change(context, selector, param2)

    def start_screen_record_timeout(self, context, param):
        step_record.start_screen_record_timeout(context, param)

    def start_screen_record(self, context):
        step_record.start_screen_record(context)

    def stop_screen_record(self, context):
        step_record.stop_screen_record(context)

    def ele_swipe(self, context, selector, param2, param3):
        step_swipe.ele_swipe(context, selector, param2, param3)

    def full_screen_swipe(self, context, param1, param2):
        step_swipe.full_screen_swipe(context, param1, param2)

    def wait_text_exist(self, context, selector):
        step_verify.wait_text_exist(context, selector)

    def ocr_text_exist(self, context, selector):
        step_verify.ocr_txt_exist(context, selector)

    def ocr_regional_text_exist(self, context, selector, param2):
        step_verify.ocr_regional_txt_exist(context, selector, param2)

    def ocr_text_contain(self, context, selector):
        step_verify.ocr_txt_contain(context, selector)

    def ocr_regional_text_contain(self, context, selector, param2):
        step_verify.ocr_regional_txt_contain(context, selector, param2)

    def ocr_text_not_exist(self, context, selector):
        step_verify.ocr_txt_not_exist(context, selector)

    def text_not_exist(self, context, selector):
        step_verify.text_not_exist(context, selector)

    def wait_text_disappear(self, context, selector):
        step_verify.wait_text_disappear(context, selector)

    def wait_ele_exit(self, context, selector):
        step_verify.wait_ele_exit(context, selector)

    def ele_not_exit(self, context, selector):
        step_verify.ele_not_exit(context, selector)

    def wait_ele_disappear(self, context, selector):
        step_verify.wait_ele_disappear(context, selector)

    def wait_ocr_text_appear(self, context, param):
        step_verify.wait_ocr_text_appear(context, param)

    def ele_text_equal(self, context, selector, param2):
        step_verify.ele_text_equal(context, selector, param2)

    def ele_text_container(self, context, selector, param2):
        step_verify.ele_text_container(context, selector, param2)

    def wait_ele_appear(self, context, selector):
        step_verify.wait_ele_appear(context, selector)

    def exist_ele(self, context, selector):
        step_verify.exist_ele(context, selector)

    def to_app_home(self, context):
        to_app_home(context)

    def app_login(self, context, param1, param2):
        app_login(context, param1, param2)

    def app_logout(self, context):
        app_logout(context)
