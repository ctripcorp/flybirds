# -*- coding: utf-8 -*-
"""
web UI driver core api implement.
"""

from playwright.sync_api import sync_playwright

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log

__open__ = ["UIDriver"]


class UIDriver:
    """web UI driver Class"""

    name = "web_ui_driver"

    @staticmethod
    def init_driver():
        try:
            play_wright = sync_playwright().start()
            gr.set_value("playwright", play_wright)
            browser_val = gr.get_value("cur_browser")
            browser_type = getattr(play_wright, browser_val)
            headless = gr.get_web_info_value("headless", True)
            browser = browser_type.launch(headless=headless)
            log.info(f"Init browser success! browser_type:[{browser_type}]")
            gr.set_value("browser", browser)

            return play_wright, browser
        except Exception as e:
            log.error('Init browser has error! Error msg is:', str(e))

    @staticmethod
    def close_driver():
        play_wright = gr.get_value('playwright')
        browser = gr.get_value('browser')
        page_obj = gr.get_value('plugin_page')

        if page_obj and hasattr(page_obj, 'context'):
            page_obj.context.close()
        if browser:
            browser.close()
        if play_wright:
            play_wright.stop()
