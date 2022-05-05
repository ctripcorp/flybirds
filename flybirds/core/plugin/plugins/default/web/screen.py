# -*- coding: utf-8 -*-
"""
web screen impl
"""

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.screen import BaseScreen

__open__ = ["Screen"]


class Screen(BaseScreen):
    """
    web screen impl
    """
    name = "web_screen"

    @staticmethod
    def screen_shot(path):
        log.info(f"[web screen_shot] screen shot start. path is:{path}")
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web_screenshot] get page object has error!')
        page_obj.page.screenshot(path=f'{path}')
        log.info("[web screen_shot] screen shot end!")
