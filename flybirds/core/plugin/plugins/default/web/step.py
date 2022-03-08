# -*- coding: utf-8 -*-
"""
web step implements class
"""

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext as g_context

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
    def screenshot(cls, context):
        log.info('web Step screenshot.')
        g_context.screen.screen_shot(context)

    @classmethod
    def prev_fail_scenario_relevance(cls, context, param1, param2):
        pass

    @classmethod
    def start_screen_record(cls, context):
        log.info('web start_screen_record.')
        screen_record_obj = gr.get_value("screenRecord")
        screen_record_obj.screen_record(context)
