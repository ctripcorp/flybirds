# -*- coding: utf-8 -*-
"""
ios screen imp
"""
from flybirds.core.plugin.plugins.default import screen

__open__ = ["Screen"]


class Screen:
    """
    screen imp
    """
    name = "ios_screen"

    def screen_shot(self, path):
        screen.screen_shot(path)

    def screen_link_to_behave(self, scenario, step_index, tag=None):
        screen.screen_link_to_behave(scenario, step_index, tag)
