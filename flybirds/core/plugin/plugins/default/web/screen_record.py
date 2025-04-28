# -*- coding: utf-8 -*-
"""
web screen record
"""
import json
import os

from flybirds.core.global_context import GlobalContext

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log

__open__ = ["ScreenRecordInfo"]


def read_har_file(file_path):
    with open(file_path, "r", encoding='utf-8') as file:
        har_data = json.load(file)
    return har_data


def filter_non_200_requests(har_data):
    non_200_requests = []
    for entry in har_data['log']['entries']:
        response_status = entry['response']['status']
        if response_status != 200:
            non_200_requests.append(entry)
    return non_200_requests


def save_to_new_har_file(original_har_data, non_200_requests, output_file_path):
    new_har_data = {
        "log": {
            "version": original_har_data['log']['version'],
            "creator": original_har_data['log']['creator'],
            "pages": original_har_data['log'].get('pages', []),  # 如果存在pages字段则保留
            "entries": non_200_requests
        }
    }
    with open(output_file_path, "w", encoding='utf-8') as file:
        json.dump(new_har_data, file, indent=4)


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
        scenario_status = gr.get_value("scenario_status", True)
        log.info(f'[web stop_record] scenario_status: {scenario_status}')
        if page_obj is None or (not hasattr(page_obj, 'context')):
            log.error('[web stop_record] get page object has error!')
        try:
            # if case failed, export web trace
            export_web_trace_path = GlobalContext.get_global_cache('export_web_trace_path')
            if page_obj.context.tracing is not None and export_web_trace_path and scenario_status is not True:
                if page_obj.context.tracing is not None:
                    log.info(f'[web stop_record] export_web_trace_path: {export_web_trace_path}')
                    page_obj.context.tracing.stop(path=export_web_trace_path)
        except Exception as e:
            log.error(f'[web stop_record] get tracing has error! Error msg is: {str(e)}')
        if gr.get_web_info_value("browserExit") is not None and \
                gr.get_web_info_value("browserExit") is False:
            page_obj.page.close()
        else:
            page_obj.context.close()
            log.info("[web stop_record] close browser")
            try:
                har_path = GlobalContext.get_global_cache('export_har_path')
                if scenario_status is True and har_path is not None and os.path.isfile(har_path):
                    os.remove(har_path)
                    log.info(f'[web stop_record] remove har_path: {har_path}')
                    return
                if har_path is not None and os.path.isfile(har_path):
                    har_data = read_har_file(har_path)
                    non_200_requests = filter_non_200_requests(har_data)
                    log.info(f'[web stop_record] export_bad_request')
                    save_to_new_har_file(har_data, non_200_requests, har_path)
                else:
                    log.error('[web stop_record] har_path is None')
            except Exception as e:
                log.error(f'[web stop_record] close browser has error! Error msg is: {str(e)}')

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
