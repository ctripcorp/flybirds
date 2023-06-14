# -*- coding: utf-8 -*-
"""
web step implements class
"""
from PIL import Image
import io
import os
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.step.common as step_common
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.step.app \
    import to_app_home, app_login, app_logout
from flybirds.core.plugin.plugins.default.step.record import \
    stop_screen_record
from flybirds.core.plugin.plugins.default.web.interception import \
    Interception as request_op
from flybirds.core.exceptions import FlybirdsException
from flybirds.utils import dsl_helper, uuid_helper

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
            raise FlybirdsException(message)

        # Bring the target page to the front and return its URL
        target_url = target.url
        target.bring_to_front()

    @classmethod
    def return_pre_page(cls, context):
        page = gr.get_value("plugin_page")
        page.return_pre_page(context)

    @classmethod
    def sleep(cls, context, param):
        page = gr.get_value("plugin_page")
        page.sleep(context, param)

    @classmethod
    def add_cookies(cls, context, name, value, url):
        page = gr.get_value("plugin_page")
        page.add_cookies(name, value, url)

    @classmethod
    def get_cookie(cls, context):
        page = gr.get_value("plugin_page")
        page.get_cookie(context)

    @classmethod
    def get_local_storage(cls, context):
        page = gr.get_value("plugin_page")
        page.get_local_storage(context)

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

    @staticmethod
    def picture_compare_from_path(context, target_element, compared_picture_path):
        # default threshold value
        threshold = 0.95

        # Convert parameter string to dictionary
        param_dict = dsl_helper.params_to_dic(target_element, "target_element")

        # Get path from dictionary
        target_element = param_dict["target_element"]

        if "threshold" in param_dict.keys():
            threshold = param_dict["threshold"]

            try:
                threshold = float(threshold)
            except ValueError:
                message = f'[threshold] is not int or float value'
                raise FlybirdsException(message)

        ele = gr.get_value("plugin_ele")
        locator, timeout = ele.wait_for_ele(context, target_element)
        target_image = locator.screenshot()
        target_image_io = Image.open(io.BytesIO(target_image))

        file_path = os.path.join(os.getcwd(), compared_picture_path)
        directory = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        uuid = uuid_helper.create_uuid()

        old_filename = f"{os.path.splitext(filename)[0]}_{uuid}_old.png"
        target_image_path = os.path.join(directory, old_filename)
        target_image_io.save(target_image_path)
        request_op.compare_images(context,target_image_path, compared_picture_path, threshold)


    @staticmethod
    def dom_ele_compare_from_path(context, target_ele, compared_text_path):
        # Convert parameter string to dictionary
        param_dict = dsl_helper.params_to_dic(target_ele, "target_element")

        # Get path from dictionary
        target_element = param_dict["target_element"]

        ele = gr.get_value("plugin_ele")
        locator, timeout = ele.wait_for_ele(context, target_element)
        target_text = locator.inner_text()

        request_op.compare_dom_element_text(target_text, compared_text_path)

    @staticmethod
    def call_external_party_api(context, method, url, data, headers):
        request_op.call_external_party_api(method, url, data, headers)
