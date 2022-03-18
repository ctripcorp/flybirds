# -*- coding: utf-8 -*-
"""
web step implements class
"""

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.step.common as step_common
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.step.app \
    import to_app_home, app_login, app_logout
from flybirds.core.plugin.plugins.default.step.record import \
    stop_screen_record

__open__ = ["Step"]


class Step:
    """Web Step Class"""

    name = "web_step"

    @classmethod
    def jump_to_page(cls, context, param):
        log.info(f'web jump_to_page. param: {param}')
        # plugin_page = g_context.page
        # page = plugin_page()
        page = gr.get_value("plugin_page")
        page.navigate(context, param)

    @classmethod
    def return_pre_page(cls, context):
        page = gr.get_value("plugin_page")
        page.return_pre_page(context)

    @classmethod
    def sleep(cls, context, param):
        page = gr.get_value("plugin_page")
        page.sleep(context, param)

    @classmethod
    def screenshot(cls, context):
        log.info('web Step screenshot.')
        step_common.screenshot(context)

    @classmethod
    def prev_fail_scenario_relevance(cls, context, param1, param2):
        """
        Related operations for the previous failure scenario
        """
        step_common.prev_fail_scenario_relevance(context, param1, param2)

    @classmethod
    def stop_screen_record(cls, context):
        log.info('web Step stop_screen_record.')
        stop_screen_record(context)

    @classmethod
    def unblock_page(cls, context):
        """
            解除当前页面限制
        """
        return True

    @classmethod
    def cur_page_is(cls, context, param):
        """
        当前页面是[param]
        """
        page = gr.get_value("plugin_page")
        page.cur_page_equal(context, param)

    @classmethod
    def has_page_changed(cls, context):
        """
        当前页面已不是上一个指定页面
        """
        return True

    # ################ element step  ##############
    @classmethod
    def click_ele(cls, context, param):
        ele = gr.get_value("plugin_ele")
        ele.ele_click(context, param)

    @classmethod
    def click_text(cls, context, param):
        ele = gr.get_value("plugin_ele")
        ele.ele_click(context, param)

    @classmethod
    def click_coordinates(cls, context, x, y):
        ele = gr.get_value("plugin_ele")
        ele.click_coordinates(context, x, y)

    @classmethod
    def ele_text_container(cls, context, param_1, param_2):
        """
        "[{param1}]的文案包含[{param2}]
        """
        ele = gr.get_value("plugin_ele")
        ele.ele_text_include(context, param_1, param_2)

    @classmethod
    def wait_text_exist(cls, context, param):
        """
        存在\[([\s\S]*)\]的文案
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.find_text(context, param)

    @classmethod
    def text_not_exist(cls, context, param):
        """
        bu存在\[([\s\S]*)\]的文案
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.find_no_text(context, param)

    @classmethod
    def ele_text_equal(cls, context, param_1, param_2):
        """
        /^\[([\s\S]*)\]的文案为\[([\s\S]*)\]$/,
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.ele_text_equal(context, param_1, param_2)

    @classmethod
    def exist_ele(cls, context, param):
        """
        /^存在元素[p]$/,
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.get_ele_locator(context, param)

    @classmethod
    def wait_ele_exit(cls, context, param):
        """
      存在[{param}]的元素
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.get_ele_locator(context, param)

    @classmethod
    def ele_not_exit(cls, context, param):
        """
      不存在[{param}]的元素
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.ele_not_exist(context, param)

    @classmethod
    def wait_ele_appear(cls, context, param):
        """
       页面渲染完成出现元素
        """
        # element
        ele = gr.get_value("plugin_ele")
        ele.wait_for_ele(context, param)

    @classmethod
    def ele_input(cls, context, param_1, param_2):
        """
       在[{param1}]中输入[{param2}]
        """
        ele = gr.get_value("plugin_ele")
        ele.ele_input_text(context, param_1, param_2)

    @classmethod
    def ele_clear_input(cls, context, param_1, param_2):
        """
       在[{param1}]中清空并输入
        """
        ele = gr.get_value("plugin_ele")
        ele.clear_and_input(context, param_1, param_2)

    @classmethod
    def ele_swipe(cls, context, param_1, param_2, param_3):
        """
        [{param1}]向{param2}滑动[{param3}]
        """
        ele = gr.get_value("plugin_ele")
        ele.ele_slide(context, param_1, param_2, param_3)

    @classmethod
    def full_screen_swipe(cls, context, param_1, param_2):
        """
       全屏向{param1}滑动[{param2}]
        """
        ele = gr.get_value("plugin_ele")
        ele.full_screen_slide(context, param_1, param_2)

    @classmethod
    def ele_select(cls, context, param_1, param_2):
        """
        在[param1]中选择[param2]
        """
        ele = gr.get_value("plugin_ele")
        ele.ele_select(context, param_1, param_2)

    @classmethod
    def full_screen_swipe_to_ele_aaa(cls, context, param_1, param_2):
        """
        向{param1}查找[{param2}]的元素
        """
        ele = gr.get_value("plugin_ele")
        ele.find_full_screen_slide(context, param_1, param_2)

    @classmethod
    def to_app_home(cls, context):
        to_app_home(context)

    @classmethod
    def app_login(cls, context, param1, param2):
        app_login(context, param1, param2)

    @classmethod
    def app_logout(cls, context):
        app_logout(context)
