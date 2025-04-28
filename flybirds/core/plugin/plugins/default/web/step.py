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
from flybirds.core.exceptions import FlybirdsException, ErrorName

from flybirds.core.global_context import GlobalContext

__open__ = ["Step"]


class Step:
    """Web Step Class"""

    name = "web_step"

    @classmethod
    def excute_js_page(cls, context, param):
        page = gr.get_value("plugin_page")
        page.evaluatejs(context, param)

    @classmethod
    def jump_to_page(cls, context, param):
        # plugin_page = g_context.page
        # page = plugin_page()
        page = gr.get_value("plugin_page")
        page.navigate(context, param)

    @classmethod
    def set_web_page_size(cls, context, width, height):
        page = gr.get_value("plugin_page")
        page.set_web_page_size(context, width, height)

    @classmethod
    def switch_target_page(cls, context, title, url):
        # Get the current page from global registry
        page = gr.get_value("plugin_page")

        # Get all pages from the current page's context
        pages = page.context.pages

        # Set the target page to the first page by default
        target = pages[0]

        # Loop through all pages to find the target page
        for item_page in pages:
            # Check if the URL matches the target URL
            if url:
                item_page_url_value = item_page.url
                if item_page_url_value[-1] == '/':
                    item_page_url_value = item_page_url_value[:-1]

                if url == item_page.url or url == item_page_url_value:
                    target = item_page
                    break

            # Check if the title matches the target title
            if title:
                item_page_title = item_page.title()
                if title == item_page_title:
                    target = item_page
                    break

        # If the target page is not found, log an error message
        else:
            message = f'Url or title could not match any tab page in this browser.'
            raise FlybirdsException(message, error_name=ErrorName.PageNotFoundError)

        # Bring the target page to the front and return its URL
        target_url = target.url
        target.bring_to_front()
        ele = gr.get_value("plugin_ele")
        # need to fix plugin_ele and plugin_page, both pages mount page objects
        ele.page = target
        page.page = target

    @classmethod
    def switch_to_latest_page(cls, context):
        # Get the current page from global registry
        page = gr.get_value("plugin_page")

        # Get latestPage from the current page's context
        pages = page.context.pages

        page_count = len(pages)
        latest_page = pages[page_count - 1]

        latest_page.bring_to_front()
        ele = gr.get_value("plugin_ele")
        ele.page = latest_page
        page.page = latest_page

    @classmethod
    def return_pre_page(cls, context):
        page = gr.get_value("plugin_page")
        page.return_pre_page(context)

    @classmethod
    def page_go_forward(cls, context):
        page = gr.get_value("plugin_page")
        page.page_go_forward(context)

    @classmethod
    def sleep(cls, context, param):
        page = gr.get_value("plugin_page")
        page.sleep(context, param)

    @classmethod
    def add_header(cls, context, name, value):
        page = gr.get_value("plugin_page")
        page.add_header(context, name, value)

    @classmethod
    def add_cookies(cls, context, name, value, url):
        page = gr.get_value("plugin_page")
        page.add_cookies(name, value, url)

    @classmethod
    def get_cookie(cls, context):
        page = gr.get_value("plugin_page")
        page.get_cookie(context)

    @classmethod
    def add_local_storage(cls, context, name, value):
        page = gr.get_value("plugin_page")
        page.add_local_storage(context, name, value)

    @classmethod
    def get_local_storage(cls, context):
        page = gr.get_value("plugin_page")
        page.get_local_storage(context)

    @classmethod
    def add_session_storage(cls, context, name, value):
        page = gr.get_value("plugin_page")
        page.add_session_storage(context, name, value)

    @classmethod
    def get_session_storage(cls, context):
        page = gr.get_value("plugin_page")
        page.get_session_storage(context)

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
    def hover_ele(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_hover(context, selector)

    @classmethod
    def click_ele(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_click(context, selector)

    @classmethod
    def click_exist_param(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.click_exist_param_web(context, selector)

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
    def ele_text_not_container(cls, context, selector, param_2):
        ele = gr.get_value("plugin_ele")
        ele.ele_text_not_include(context, selector, param_2)

    @classmethod
    def wait_text_exist(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.find_text(context, selector)

    @classmethod
    def wait_page_text_exist(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.find_page_text(context, selector)

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
    def ele_exist_value(cls, context, selector, param):
        ele = gr.get_value("plugin_ele")
        ele.ele_exist_value(context, selector, param)

    @classmethod
    def ele_contain_value(cls, context, selector, param):
        ele = gr.get_value("plugin_ele")
        ele.ele_contain_value(context, selector, param)

    @classmethod
    def ele_not_contain_value(cls, context, selector, param):
        ele = gr.get_value("plugin_ele")
        ele.ele_not_contain_value(context, selector, param)

    @classmethod
    def ele_contain_param_value(cls, context, param1, selector, param2):
        params = param1.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.ele_text_equal(context, selector, param2)

    @classmethod
    def ele_with_param_value_equal(cls, context, param, selector, attr_value):
        params = param.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.ele_with_param_value_equal_attr(context, selector, attr_value)

    @classmethod
    def ele_contain_param_contain_value(cls, context, param1, selector, param2):
        params = param1.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.ele_text_include(context, selector, param2)

    @classmethod
    def ele_contain_param_exist(cls, context, param1, selector):
        params = param1.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.ele_exist(context, selector)

    @classmethod
    def ele_contain_param_not_exist(cls, context, param1, selector):
        params = param1.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.ele_not_exist(context, selector)

    @classmethod
    def ele_contain_param_attr_exist(cls, context, param, selector, attr_name, attr_value):
        params = param.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_equal(context, selector, attr_name, attr_value)

    @classmethod
    def ele_contain_param_attr_contain(cls, context, param, selector, attr_name, attr_value):
        params = param.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_container(context, selector, attr_name, attr_value)

    @classmethod
    def ele_contain_param_attr_not_contain(cls, context, param, selector, attr_name, attr_value):
        params = param.split(',')
        for param in params:
            selector = selector.replace('{}', param, 1)
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_not_container(context, selector, attr_name, attr_value)

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
    def clear_input(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.clear_input(context, selector)

    @classmethod
    def ele_swipe(cls, context, selector, param_2, param_3):
        ele = gr.get_value("plugin_ele")
        ele.ele_slide(context, selector, param_2, param_3)

    @classmethod
    def ele_swipe_to(cls, context, selector, param_left, param_top):
        ele = gr.get_value("plugin_ele")
        ele.ele_swipe_to(context, selector, param_left, param_top)

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
    def scroll_ele_into_view(cls, context, selector):
        """
        from {param1} find[{param2}]element
        """
        ele = gr.get_value("plugin_ele")
        ele.find_full_screen_slide(context, None, selector)

    @classmethod
    def upload_image_to_ele(cls, context, selector):
        """
        from {param1} find[{param2}]element
        """
        ele = gr.get_value("plugin_ele")
        ele.upload_image(context, selector)

    @classmethod
    def ele_attr_equal(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_equal(context, selector, param2, param3)

    @classmethod
    def ele_attr_container(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_container(context, selector, param2, param3)

    @classmethod
    def ele_attr_not_container(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_ele_attr_not_container(context, selector, param2, param3)

    @classmethod
    def text_attr_equal(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_text_attr_equal(context, selector, param2, param3)

    @classmethod
    def text_attr_container(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_text_attr_container(context, selector, param2, param3)

    @classmethod
    def text_attr_not_container(cls, context, selector, param2, param3):
        ele = gr.get_value("plugin_ele")
        ele.is_text_attr_not_container(context, selector, param2, param3)

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

    @staticmethod
    def clear_all_request_record(context):
        request_op.clear_all_request_record()

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
        request_op.request_compare(operation, target_data_path, ['_removed', '_changed'])

    @staticmethod
    def request_compare_from_path_exceptions_removed(context, operation, target_data_path):
        request_op.request_compare(operation, target_data_path, ['_removed', '_changed', '_add'])
   
    @staticmethod
    def page_not_requested(context, operation):
        request_op.page_not_requested(operation)

    @staticmethod
    def page_requests_some_interfaces(context, operation):
        request_op.page_requests_some_interfaces(operation)

    @staticmethod
    def page_wait_interface_request_finished(context, operation):
        request_op.page_wait_interface_request_finished(operation)

    @staticmethod
    def request_query_str_compare_from_path(context, operation,
                                            target_data_path):
        request_op.request_query_string_compare(operation, target_data_path)

    @staticmethod
    def request_compare_value(context, operation, target_json_path,
                              expect_value):
        request_op.request_compare_value(operation, target_json_path,
                                         expect_value)

    @staticmethod
    def request_compare_value_is_none(context, operation, target_json_path):
        request_op.request_compare_value_is_none(operation, target_json_path,)

    @staticmethod
    def request_compare_includes_value(context, operation, target_json_path,
                                       expect_value):
        request_op.request_compare_includes_value(operation, target_json_path,
                                                  expect_value)

    @staticmethod
    def request_compare_not_includes_value(context, operation, target_json_path,
                                           expect_not_contain_value):
        request_op.request_compare_not_includes_value(operation, target_json_path,
                                                      expect_not_contain_value)

    @staticmethod
    def picture_compare_from_path(context, target_element, compared_picture_path):
        request_op.compare_images(context, target_element, compared_picture_path)

    @staticmethod
    def dom_ele_compare_from_path(context, target_ele, compared_text_path):
        request_op.compare_dom_element_text(context, target_ele, compared_text_path)

    @staticmethod
    def call_external_party_api(context, method, url, data, headers):
        request_op.call_external_party_api(method, url, data, headers)

    @staticmethod
    def open_web_mock(context, service_str, mock_case_id_str):
        request_mock_key_value = GlobalContext.get_global_cache("request_mock_key_value")
        if request_mock_key_value is None:
            request_mock_key_value = []
            GlobalContext.set_global_cache("request_mock_key_value", request_mock_key_value)
        request_op.open_web_mock(service_str, mock_case_id_str, request_mock_key_value)

    @staticmethod
    def remove_web_mock(context):
        request_mock_key_value = GlobalContext.get_global_cache("request_mock_key_value")
        if request_mock_key_value is not None:
            del request_mock_key_value
        GlobalContext.set_global_cache("request_mock_key_value", None)

    @classmethod
    def ele_touch(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.ele_touch(context, selector)

    @classmethod
    def touch_text(cls, context, selector):
        ele = gr.get_value("plugin_ele")
        ele.touch_text(context, selector)

    @classmethod
    def click_ele_point(cls, context, selector, x, y):
        ele = gr.get_value("plugin_ele")
        ele.ele_click_point(context, selector, x, y)

    @staticmethod
    def open_web_request_mock(context, service_str, path_list, mock_case_id_str):
        request_mock_key_value = GlobalContext.get_global_cache("request_mock_request_key_value")
        if request_mock_key_value is None:
            request_mock_key_value = []
            GlobalContext.set_global_cache("request_mock_request_key_value", request_mock_key_value)
        request_op.open_web_request_mock(service_str, mock_case_id_str, path_list, request_mock_key_value)

    @staticmethod
    def close_dialog(context):
        ele = gr.get_value("plugin_ele")
        ele.close_dialog(context)

    @staticmethod
    def accept_dialog(context):
        ele = gr.get_value("plugin_ele")
        ele.accept_dialog(context)
