# -*- coding: utf-8 -*-
"""
web Element core api implement
"""

__open__ = ["Element"]

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.utils.verify_helper as verify_helper
from flybirds.core.exceptions import FlybirdVerifyException


class Element:
    """Android Element Class"""

    name = "web_element"
    instantiation_timing = "plugin"

    def __init__(self):
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web Element init] get page object has error!')
        self.page = page_obj.page

    def get_ele_locator(self, param):
        params_array = param.split(",")
        selector_str = params_array[0]
        selector = self.page.query_selector(selector_str)
        if selector is None:
            message = f"The element [{param}] does not exist."
            raise FlybirdVerifyException(message)
        return self.page.locator(selector_str)

    def get_ele_text(self, param):
        try:
            locator = self.get_ele_locator(param)
            e_text = locator.inner_text()
            if e_text is None or e_text.strip() == '':
                e_text = locator.get_attribute('value')
                if e_text is None or e_text.strip() == '':
                    e_text = ""
            return e_text
        except FlybirdVerifyException as e:
            raise e

    def ele_text_include(self, context, param_1, param_2):
        try:
            e_text = self.get_ele_text(param_1)
            verify_helper.text_container(param_2, e_text)
        except FlybirdVerifyException as e:
            raise e

    def find_text(self, context, param):
        p_content = self.page.content()
        if param in p_content:
            log.info(f'fif_ind_text: [{param}] is success!')
        else:
            message = f"expect to find the text [{param}] in the page, " \
                      f"but not actually find it"
            raise FlybirdVerifyException(message)

    def find_no_text(self, context, param):
        p_content = self.page.content()
        if param in p_content:
            message = f"except text [{param}] not exists in page, " \
                      f"but actual has find it."
            raise FlybirdVerifyException(message)

    def ele_text_equal(self, context, param_1, param_2):
        try:
            e_text = self.get_ele_text(param_1)
            verify_helper.text_equal(param_2, e_text)
        except FlybirdVerifyException as e:
            raise e

    def ele_not_exist(self, context, param):
        try:
            self.get_ele_locator(param)
            ele_exists = True
        except FlybirdVerifyException:
            ele_exists = False

        if ele_exists:
            message = f"except element [{param}] not exists in page, " \
                      f"but actual has find it."
            raise FlybirdVerifyException(message)

    def wait_for_ele(self, context, param):
        params_array = param.split(",")
        selector_str = params_array[0]
        self.page.wait_for_selector(selector_str, state='visible')

    def ele_input_text(self, context, param_1, param_2):
        try:
            locator = self.get_ele_locator(param_1)
            locator.fill(param_2)
            return self.page.wait_for_timeout(100)
        except FlybirdVerifyException as e:
            raise e

    def clear_and_input(self, context, param_1, param_2):
        try:
            locator = self.get_ele_locator(param_1)
            locator.fill('')
            locator.fill(param_2)
            return self.page.wait_for_timeout(100)
        except FlybirdVerifyException as e:
            raise e
