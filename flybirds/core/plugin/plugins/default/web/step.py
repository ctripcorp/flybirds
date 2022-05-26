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
from flybirds.core.plugin.plugins.default.web.interception import \
    Interception as request_op

__open__ = ["Step"]


class Step:
    """Web Step Class"""

    name = "web_step"

    @classmethod
    def jump_to_page(cls, context, param):
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
        return True

    @classmethod
    def cur_page_is(cls, context, param):
        page = gr.get_value("plugin_page")
        page.cur_page_equal(context, param)

    @classmethod
    def has_page_changed(cls, context):
        return True

    @classmethod
    def click_ele(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_click(context, selector)

    @classmethod
    def click_text(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.click_text(context, selector)

    @classmethod
    def click_coordinates(cls, context, x, y):
        ele = gr.get_value("plugin_ele")
        ele.click_coordinates(context, x, y)

    @classmethod
    def ele_text_container(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.ele_text_include(context, selector, param_2)

    @classmethod
    def wait_text_exist(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.find_text(context, selector)

    @classmethod
    def text_not_exist(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.find_no_text(context, selector)

    @classmethod
    def ele_text_equal(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.ele_text_equal(context, selector, param_2)

    @classmethod
    def exist_ele(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_exist(context, selector)

    @classmethod
    def wait_ele_exit(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_exist(context, selector)

    @classmethod
    def ele_not_exit(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_not_exist(context, selector)

    @classmethod
    def wait_ele_appear(cls, context, selector):
        """
         page rendering complete appears element[{param}]
        """
        ele = gr.get_value("plugin_ele")
        ele.wait_for_ele(context, selector)

    @classmethod
    def ele_input(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.ele_input_text(context, selector, param_2)

    @classmethod
    def ele_clear_input(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.clear_and_input(context, selector, param_2)

    @classmethod
    def ele_swipe(cls, context, selector, param_2, param_3):
        ele = gr.get_value("plugin_ele")
        ele.ele_slide(context, selector, param_2, param_3)

    @classmethod
    def full_screen_swipe(cls, context, param_1, param_2):
        ele = gr.get_value("plugin_ele")
        ele.full_screen_slide(context, param_1, param_2)

    @classmethod
    def ele_select(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.ele_select(context, selector, param_2)

    @classmethod
    def full_screen_swipe_to_ele_aaa(cls, context, param_1, selector):
        """
        from {param1} find[{param2}]element
        """
        ele = gr.get_value("plugin_ele")
        ele.find_full_screen_slide(context, param_1, selector)

    @classmethod
    def ele_attr_equal(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_equal(context, selector, param2, param3)

    @classmethod
    def text_attr_equal(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_text_attr_equal(context, selector, param2, param3)

    @classmethod
    def find_child_from_parent(cls, context, p_selector, c_selector):
        ele = gr.get_value("plugin_ele")
        ele.is_parent_exist_child(context, p_selector, c_selector)

    @classmethod
    def find_text_from_parent(cls, context, p_selector, c_selector, param3):
        ele = gr.get_value("plugin_ele")
        ele.find_text_from_parent(context, p_selector, c_selector, param3)

    @classmethod
    def swipe_to_ele(cls, context, p_selector, param2, c_selector):
        ele = gr.get_value("plugin_ele")
        ele.is_parent_exist_child(context, p_selector, c_selector)

    @classmethod
    def to_app_home(cls, context):
        to_app_home(context)

    @classmethod
    def app_login(cls, context, param1, param2):
        app_login(context, param1, param2)

    @classmethod
    def app_logout(cls, context):
        app_logout(context)

    # -------------------------------------------------------------------------
    # request interception
    # -------------------------------------------------------------------------
    @staticmethod
    def add_request_body(context, service_str):
        request_op.add_some_interception_request_body(service_str)

    @staticmethod
    def remove_request_body(context, service_str):
        request_op.remove_some_interception_request_body(service_str)

    @staticmethod
    def clear_all_request_body(context):
        request_op.clear_interception_request_body()

    # -------------------------------------------------------------------------
    # request service listening
    # -------------------------------------------------------------------------
    @staticmethod
    def add_request_mock(context, service_str, mock_case_id_str):
        request_op.add_some_interception_mock(service_str, mock_case_id_str)

    @staticmethod
    def remover_request_mock(context, service_str):
        request_op.remove_some_interception_mock(service_str)

    @staticmethod
    def clear_all_request_mock(context):
        request_op.clear_interception_mock()

    # -------------------------------------------------------------------------
    # compare service requests
    # -------------------------------------------------------------------------
    @staticmethod
    def request_compare_from_path(context, operation, target_data_path):
        request_op.request_compare(operation, target_data_path)

    @staticmethod
    def request_query_str_compare_from_path(context, operation,
                                            target_data_path):
        request_op.request_query_string_compare(operation, target_data_path)

    @staticmethod
    def request_compare_value(context, operation, target_json_path,
                              expect_value):
        request_op.request_compare_value(operation, target_json_path,
                                         expect_value)
