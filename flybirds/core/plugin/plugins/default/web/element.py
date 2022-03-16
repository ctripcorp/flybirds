# -*- coding: utf-8 -*-
"""
web Element core api implement
"""

__open__ = ["Element"]

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.utils.verify_helper as verify_helper


class Element:
    """Android Element Class"""

    name = "web_element"
    instantiation_timing = "plugin"

    def __init__(self):
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web Element init] get page object has error!')
        self.page = page_obj.page

    def get_ele_text(self, param):
        locator = self.page.locator(param)
        e_text = locator.inner_text()
        if e_text is None or e_text.strip() == '':
            e_text = locator.get_attribute('value')
            if e_text is None or e_text.strip() == '':
                e_text = ""
        return e_text

    def ele_text_include(self, context, param_1, param_2):
        e_text = self.get_ele_text(param_1)
        verify_helper.text_container(str(param_2).strip(), e_text)
