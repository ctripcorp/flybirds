# -*- coding: utf-8 -*-
"""
web step implements class
"""

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.step.common as step_common
import flybirds.utils.flybirds_log as log
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
    def click_ele(cls, context, param):
        page = gr.get_value("plugin_page")
        page.click_ele(context, param)

    @classmethod
    def click_text(cls, context, param):
        page = gr.get_value("plugin_page")
        page.click_text(context, param)

    @classmethod
    def click_coordinates(cls, context, x, y):
        page = gr.get_value("plugin_page")
        page.click_coordinates(context, x, y)

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
