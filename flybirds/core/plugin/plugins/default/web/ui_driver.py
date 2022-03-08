# -*- coding: utf-8 -*-
"""
android device core api implement.
"""

from playwright.sync_api import sync_playwright

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext

__open__ = ["UIDriver"]


class UIDriver:
    """Android Device Class"""

    name = "web_ui_driver"

    # def __init__(self):
    #     play_wright, browser = self.init_browser()
    #     self.play_wright = play_wright
    #     self.browser = browser

    @staticmethod
    def init_browser(browser_type='firefox', config_dict={"headless": False}):
        try:
            play_wright = sync_playwright().start()
            gr.set_value("playwright", play_wright)
            GlobalContext.ui_driver_instance = play_wright

            browser_type = getattr(play_wright, browser_type)
            browser = browser_type.launch(headless=config_dict["headless"])
            log.info(f"Init browser success! browser_type:[{browser_type}]")
            gr.set_value("browser", browser)

            return play_wright, browser
        except Exception as e:
            log.error('Init browser has error! Error msg is:', str(e))

    @staticmethod
    def close_browser():
        play_wright = gr.get_value('playwright')
        browser = gr.get_value('browser')
        page_obj = gr.get_value('plugin_page')

        if page_obj and hasattr(page_obj, 'context'):
            page_obj.context.close()
        if browser:
            browser.close()
        if play_wright:
            play_wright.stop()
