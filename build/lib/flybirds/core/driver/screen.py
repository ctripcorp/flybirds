# -*- coding: utf-8 -*-
"""
screen proxy
"""
from flybirds.core.global_context import GlobalContext


def screen_shot(path):
    GlobalContext.screen.screen_shot(path)


def screen_link_to_behave(scenario, step_index, tag=None):
    GlobalContext.screen.screen_link_to_behave(scenario, step_index, tag)
