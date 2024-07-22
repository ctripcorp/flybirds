# -*- coding: utf-8 -*-
"""
tag event
"""
from behave.model import Tag

from flybirds.core.global_context import GlobalContext
from flybirds.core.use_external.config import Config
from flybirds.utils import launch_helper
from flybirds.utils import flybirds_log as log
import os
from flybirds.utils import file_helper


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    before tag
    """

    name = "OnBefore"
    order = 5

    @staticmethod
    def can(context, tag):
        return True

    @staticmethod
    def run(context, tag):
        """
        exe before
        """
        log.info(tag)
        if tag is not None and tag.startswith("elementLocator"):
            ele_config = tag.split('=')[-1]
            ele_locator = Config.get_ele_locator()
            if ele_locator is not None:
                ele_locator_path = os.path.join(
                    os.getcwd(), "config", "elementLocator", ele_config)
                if os.path.exists(ele_locator_path):
                    ele_locator.spec_ele_locator = file_helper.get_json_from_file(
                        ele_locator_path)
        # hook extend by tester
        before_tag_extend = launch_helper.get_hook_file("before_tag_extend")
        if before_tag_extend is not None:
            before_tag_extend(context, tag)


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    after tag
    """

    name = "OnAfter"
    order = 100

    @staticmethod
    def can(context, tag):
        return True

    @staticmethod
    def run(context, tag):
        """
        exe after tag
        """
        # hook extend by tester
        after_tag_extend = launch_helper.get_hook_file("after_tag_extend")
        if after_tag_extend is not None:
            after_tag_extend(context, tag)


# add tag event into global processor
var = GlobalContext.join("before_tag_processor", OnBefore, 1)
var1 = GlobalContext.join("after_tag_processor", OnAfter, 1)
