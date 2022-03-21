# -*- coding: utf-8 -*-
"""
web Element core api implement
"""

__open__ = ["Element"]

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.utils.verify_helper as verify_helper
from flybirds.core.exceptions import FlybirdVerifyException, \
    FlybirdsVerifyEleException
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan
from flybirds.utils.dsl_helper import handle_str, params_to_dic


def direct_left(x, y, diff):
    to_x = x - diff
    to_y = y
    return to_x, to_y


def direct_right(x, y, diff):
    to_x = x + diff
    to_y = y
    return to_x, to_y


def direct_up(x, y, diff):
    to_x = x
    to_y = y - diff
    return to_x, to_y


def direct_down(x, y, diff):
    to_x = x
    to_y = y + diff
    return to_x, to_y


def direct_default(x, y, diff):
    to_x = x
    to_y = y - diff if y - diff > 0 else 0
    return to_x, to_y


direct_dict = {
    'left': direct_left,
    'right': direct_right,
    'up': direct_up,
    'down': direct_down
}


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
        if param is None:
            message = f"[get_ele_locator] the param[{param}] is None."
            raise FlybirdsVerifyEleException(message=message)

        param_temp = handle_str(param)
        param_dict = params_to_dic(param_temp)
        selector_str = param_dict["selector"]
        selector = self.page.query_selector(selector_str)
        if selector is None:
            raise FlybirdsVerifyEleException(selector=param)
        return self.page.locator(selector_str)

    def get_ele_text(self, param):
        locator = self.get_ele_locator(param)
        e_text = locator.inner_text()
        if e_text is None or e_text.strip() == '':
            e_text = locator.get_attribute('value')
            if e_text is None or e_text.strip() == '':
                e_text = ""
        return e_text

    def ele_click(self, context, param):
        locator = self.get_ele_locator(param)
        locator.click()

    def click_coordinates(self, context, x, y):
        self.page.mouse.click(x, y)

    def ele_text_include(self, context, param_1, param_2):
        e_text = self.get_ele_text(param_1)
        verify_helper.text_container(param_2, e_text)

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
        e_text = self.get_ele_text(param_1)
        verify_helper.text_equal(param_2, e_text)

    def ele_not_exist(self, context, param):
        try:
            self.get_ele_locator(param)
            ele_exists = True
        except FlybirdsVerifyEleException:
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
        locator = self.get_ele_locator(param_1)
        locator.fill(param_2)
        return self.page.wait_for_timeout(100)

    def clear_and_input(self, context, param_1, param_2):
        locator = self.get_ele_locator(param_1)
        locator.fill('')
        locator.fill(param_2)
        return self.page.wait_for_timeout(100)

    def ele_slide(self, context, param_1, param_2, param_3):
        locator = self.get_ele_locator(param_1)
        box = locator.bounding_box()
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        # get scroll direction
        language = g_Context.get_current_language()
        direct = lan.get_glb_key(param_2, language)

        fun = direct_dict.get(direct, direct_default)
        to_x, to_y = fun(x, y, param_3)

        self.page.evaluate(f"window.scrollTo({to_x}, {to_y})")

    def full_screen_slide(self, context, param_1, param_2):
        # get scroll direction
        language = g_Context.get_current_language()
        direct = lan.get_glb_key(param_1, language)

        fun = direct_dict.get(direct, direct_default)
        to_x, to_y = fun(0, 0, param_2)

        self.page.evaluate(f"window.scrollBy({to_x}, {to_y})")

    def ele_select(self, context, selector, option_str):
        locator = None
        try:
            locator = self.get_ele_locator(selector)
            # select by text
            locator.select_option(label=option_str)
            log.info(f'[ele_select] select option[{option_str}] success.')
        except FlybirdsVerifyEleException as fe:
            raise fe
        except Exception as e:
            # select by value
            log.warn(f'[ele_select] retry select option[{option_str}].')
            locator.select_option(option_str)

    def find_full_screen_slide(self, context, param1, param2):
        locator = self.get_ele_locator(param2)
        locator.scroll_into_view_if_needed()
