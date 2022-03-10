# -*- coding: utf-8 -*-
# @Time : 2022/3/7 19:18
# @Author : hyx
# @File : page.py
# @desc : web page implement
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.utils import dsl_helper
from flybirds.utils.dsl_helper import is_number

__open__ = ["Page"]


class Page:
    """Web Page Class"""

    name = "web_page"
    instantiation_timing = "plugin"

    def __init__(self):
        page, context = Page.init_page()
        self.page = page
        self.context = context

    @staticmethod
    def init_page():
        browser = gr.get_value('browser')
        context = browser.new_context(record_video_dir="videos")
        page = context.new_page()
        return page, context

    def navigate(self, context, param):
        param_dict = dsl_helper.params_to_dic(param, "urlKey")
        url_key = param_dict["urlKey"]
        schema_url_value = gr.get_page_schema_url(url_key)

        self.page.goto(schema_url_value)

    def sleep(self, context, param):
        if is_number(param):
            self.page.wait_for_timeout(float(param) * 1000)
        else:
            log.warn(f"default wait for timeout!")
            self.page.wait_for_timeout(3 * 1000)

    def click_ele(self, context, param):
        self.page.locator(param).click(timeout=15000)

    def click_text(self, context, param):
        self.page.locator(param).click(timeout=15000)

    def click_coordinates(self, context, x, y):
        self.page.mouse.click(x, y)
