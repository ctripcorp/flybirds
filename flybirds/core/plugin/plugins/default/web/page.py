# -*- coding: utf-8 -*-
# @Time : 2022/3/7 19:18
# @Author : hyx
# @File : page.py
# @desc : web page implement
import flybirds.core.global_resource as gr
from flybirds.utils import dsl_helper

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
