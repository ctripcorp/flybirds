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
    """Web Element Class"""

    name = "web_element"
    instantiation_timing = "plugin"

    def __init__(self):
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web Element init] get page object has error!')
        self.page = page_obj.page

    def get_ele_locator(self, selector):
        if selector is None:
            message = f"[get_ele_locator] the param[{selector}] is None."
            raise FlybirdsVerifyEleException(message=message)
        param_temp = handle_str(selector)
        param_dict = params_to_dic(param_temp)
        selector_str = param_dict["selector"]

        if "timeout" in param_dict.keys():
            timeout = param_dict["timeout"]
        else:
            timeout = gr.get_frame_config_value("wait_ele_timeout", 30)

        ele_locator = self.page.locator(selector_str)
        return ele_locator, float(timeout) * 1000

    def get_ele_text(self, param):
        locator, timeout = self.get_ele_locator(param)
        e_text = locator.inner_text(timeout=timeout)
        if e_text is None or e_text.strip() == '':
            e_text = locator.get_attribute('value')
            if e_text is None or e_text.strip() == '':
                e_text = ""
        return e_text

    def ele_click(self, context, param):
        locator, timeout = self.get_ele_locator(param)
        locator.click(timeout=timeout)

    def click_text(self, context, param):
        if 'text=' not in param:
            param = "text=" + param
        locator, timeout = self.get_ele_locator(param)
        locator.click(timeout=timeout)

    def click_coordinates(self, context, x, y):
        self.page.mouse.click(float(x), float(y))

    def ele_text_include(self, context, param_1, param_2):
        e_text = self.get_ele_text(param_1)
        verify_helper.text_container(param_2, e_text)

    def find_text(self, context, param):
        param_temp = handle_str(param)
        param_dict = params_to_dic(param_temp)
        selector_str = param_dict["selector"]

        p_content = self.page.content()
        if selector_str in p_content:
            log.info(f'find_text: [{selector_str}] is success!')
        else:
            message = f"expect to find the text [{selector_str}] in the " \
                      f"page, but not actually find it"
            raise FlybirdVerifyException(message)

    def find_no_text(self, context, param):
        param_temp = handle_str(param)
        param_dict = params_to_dic(param_temp)
        selector_str = param_dict["selector"]

        p_content = self.page.content()
        if selector_str in p_content:
            message = f"except text [{selector_str}] not exists in page, " \
                      f"but actual has find it."
            raise FlybirdVerifyException(message)

    def ele_text_equal(self, context, param_1, param_2):
        e_text = self.get_ele_text(param_1)
        verify_helper.text_equal(param_2, e_text)

    def ele_exist(self, context, param):
        locator, timeout = self.get_ele_locator(param)
        locator.element_handle(timeout=timeout)

    def ele_not_exist(self, context, param):
        try:
            self.ele_exist(context, param)
            ele_exists = True
        except Exception:
            ele_exists = False

        if ele_exists:
            message = f"except element [{param}] not exists in page, " \
                      f"but actual has find it."
            raise FlybirdVerifyException(message)

    def wait_for_ele(self, context, param):
        locator, timeout = self.get_ele_locator(param)
        locator.wait_for(timeout=timeout, state='visible')

    def ele_input_text(self, context, param_1, param_2):
        locator, timeout = self.get_ele_locator(param_1)
        locator.click(timeout=timeout)
        locator.fill(param_2, timeout=timeout)
        return self.page.wait_for_timeout(100)

    def clear_and_input(self, context, param_1, param_2):
        locator, timeout = self.get_ele_locator(param_1)
        locator.click(timeout=timeout)
        locator.fill('', timeout=timeout)
        locator.fill(param_2, timeout=timeout)
        return self.page.wait_for_timeout(100)

    def ele_slide(self, context, param_1, param_2, param_3):
        locator, timeout = self.get_ele_locator(param_1)
        box = locator.bounding_box(timeout=timeout)
        x = box["x"] + box["width"] / 2
        y = box["y"] + box["height"] / 2
        # get scroll direction
        language = g_Context.get_current_language()
        direct = lan.get_glb_key(param_2, language)

        fun = direct_dict.get(direct, direct_default)
        to_x, to_y = fun(x, y, float(param_3))

        self.page.evaluate(f"window.scrollTo({to_x}, {to_y})")

    def full_screen_slide(self, context, param_1, param_2):
        # get scroll direction
        language = g_Context.get_current_language()
        direct = lan.get_glb_key(param_1, language)

        fun = direct_dict.get(direct, direct_default)
        to_x, to_y = fun(0, 0, float(param_2))

        self.page.evaluate(f"window.scrollBy({to_x}, {to_y})")

    def ele_select(self, context, selector, option_str):
        locator, timeout = self.get_ele_locator(selector)
        try:
            # select by text
            locator.select_option(label=option_str, timeout=timeout)
            log.info(f'[ele_select] select option[{option_str}] success.')
        except FlybirdsVerifyEleException as fe:
            raise fe
        except Exception:
            # select by value
            log.warn(f'[ele_select] retry select option[{option_str}].')
            locator.select_option(option_str, timeout=timeout)

    def find_full_screen_slide(self, context, param1, param2):
        locator, timeout = self.get_ele_locator(param2)
        locator.scroll_into_view_if_needed(timeout=timeout)

    def get_ele_attr(self, selector, attr_name, params_deal_module=None,
                     deal_method=None):
        locator, timeout = self.get_ele_locator(selector)
        ele_attr = locator.get_attribute(attr_name, timeout=timeout)
        if deal_method is not None:
            deal_method = getattr(params_deal_module, deal_method)
            ele_attr = deal_method(ele_attr)
        return ele_attr

    def is_ele_attr_equal(self, context, selector, attr_name, target_val):
        param2_dict = params_to_dic(attr_name, "attrName")
        target_attr = param2_dict["attrName"]

        deal_method = None
        params_deal_module = None
        if "dealMethod" in param2_dict.keys():
            deal_method = param2_dict["dealMethod"]
            params_deal_module = gr.get_value("projectScript").params_deal

        ele_attr = self.get_ele_attr(selector, target_attr, params_deal_module,
                                     deal_method)
        verify_helper.attr_equal(target_val, ele_attr)

    def is_text_attr_equal(self, context, text_selector, attr_name,
                           target_val):
        if 'text=' not in text_selector:
            text_selector = "text=" + text_selector
        self.is_ele_attr_equal(context, text_selector, attr_name, target_val)

    def is_parent_exist_child(self, context, parent_selector, child_selector):
        parent_locator, p_timeout = self.get_ele_locator(parent_selector)

        child_temp = handle_str(child_selector)
        child_dict = params_to_dic(child_temp)
        child_str = child_dict["selector"]

        if "timeout" in child_dict.keys():
            c_timeout = child_dict["timeout"]
        else:
            c_timeout = gr.get_frame_config_value("wait_ele_timeout", 30)
        c_timeout = float(c_timeout) * 1000

        sub_locator = parent_locator.locator(child_str)
        sub_locator.element_handle(timeout=p_timeout)
        return sub_locator, c_timeout

    def find_text_from_parent(self, context, parent_selector, child_selector,
                              target_text):
        sub_locator, c_timeout = self.is_parent_exist_child(context,
                                                            parent_selector,
                                                            child_selector)
        e_text = sub_locator.inner_text(timeout=c_timeout)
        if e_text is None or e_text.strip() == '':
            e_text = sub_locator.get_attribute('value', timeout=c_timeout)
        verify_helper.text_equal(target_text, e_text)
