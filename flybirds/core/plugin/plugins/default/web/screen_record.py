# -*- coding: utf-8 -*-
"""
web screen record
"""

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log

__open__ = ["ScreenRecordInfo"]


class ScreenRecordInfo:
    name = "web_screen_record"
    instantiation_timing = "plugin"

    def __init__(self):
        self.support = True
        self.start_time = None
        self.end_time = None
        self.process = None
        # 0 Just created 1 Reset state 2 Start recording
        self.status = 0

    @staticmethod
    def stop_record():
        log.info("[web stop_record] start")
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'context')):
            log.error('[web stop_record] get page object has error!')

        if gr.get_web_info_value("browserExit") is not None and \
                gr.get_web_info_value("browserExit") is False:
            page_obj.page.close()
        else:
            page_obj.context.close()

    @staticmethod
    def copy_record(src_path):
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web copy_record] get page object has error!')

        video = page_obj.page.video
        path = video.path()
        log.info(f'[web copy_record] web_record path: {path}')
        # Save video as
        video.save_as(src_path)
        video.delete()
