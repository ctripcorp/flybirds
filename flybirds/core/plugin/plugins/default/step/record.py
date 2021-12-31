# -*- coding: utf-8 -*-
"""
Screen record.
"""
import flybirds.core.global_resource as gr


def start_screen_record_timeout(context, param):
    screen_record = gr.get_value("screenRecord")
    timeout = float(param)
    screen_record.start_record(timeout)


def start_screen_record(context):
    screen_record = gr.get_value("screenRecord")
    timeout = gr.get_frame_config_value("screen_record_time", 60)
    screen_record.start_record(timeout)


def stop_screen_record(context):
    screen_record = gr.get_value("screenRecord")
    screen_record.stop_record()
    step_index = context.cur_step_index - 1
    screen_record.link_record(context.scenario, step_index)
