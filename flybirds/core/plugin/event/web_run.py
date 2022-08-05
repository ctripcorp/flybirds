# -*- coding: utf-8 -*-
# @Time : 2022/2/24 19:27
# @Author : hyx
# @File : web_run.py
# @desc : web_run
import traceback

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.driver import ui_driver
from flybirds.core.global_context import GlobalContext
from flybirds.utils import launch_helper


class OnBefore:
    name = "OnWebBefore"
    order = 51

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() == "web"):
            return True
        else:
            return False

    @staticmethod
    def init_ui_driver(context):
        """
        init browser
        """
        play_wright, browser = ui_driver.init_driver()
        context.play_wright = play_wright
        context.browser = browser
        GlobalContext.ui_driver_instance = play_wright
        log.info("playwright object initialization completed")

    @staticmethod
    def init_ui_page(context):
        # get the global object used to plugin page
        plugin_page = GlobalContext.page()
        gr.set_value("plugin_page", plugin_page)
        context.plugin_page = plugin_page

        # get the global object used to record the screen
        screen_record = GlobalContext.screen_record()
        gr.set_value("screenRecord", screen_record)
        context.screen_record = screen_record

        plugin_ele = GlobalContext.element()
        gr.set_value("plugin_ele", plugin_ele)
        context.plugin_ele = plugin_ele

        if gr.get_web_info_value("browserExit") is not None and \
                gr.get_web_info_value("browserExit") is False:
            gr.set_value("browser_context", plugin_page.page
                         .context)

        log.info("screen recording context initialization completed")
        if not screen_record.support:
            log.info("the device does not support screen recording")

    @staticmethod
    def run(context):
        try:
            log.info('[web run] OnBefore run event!')
            OnBefore.init_ui_driver(context)
            OnBefore.init_ui_page(context)

        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


class OnAfter:
    """
    after event
    """

    name = "OnWebAfter"
    order = 100

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() == "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        log.info('[web run] OnAfter run event!')
        # close browser
        ui_driver.close_driver()

        # hook extend by tester
        after_all_extend = launch_helper.get_hook_file("after_all_extend")
        if after_all_extend is not None:
            after_all_extend(context)


hook1 = GlobalContext.join("before_run_processor", OnBefore, 1)
hook2 = GlobalContext.join("after_run_processor", OnAfter, 1)
