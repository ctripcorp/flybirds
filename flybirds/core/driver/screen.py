# -*- coding: utf-8 -*-
"""
screen proxy
"""
from flybirds.core.global_context import GlobalContext


def screen_shot(path, file_name):
    GlobalContext.screen.screen_shot(path, file_name)


def screen_link_to_behave(scenario, step_index, tag=None):
    result = GlobalContext.screen.screen_link_to_behave(scenario, step_index, tag)
    return result
