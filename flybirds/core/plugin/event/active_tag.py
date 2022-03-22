# -*- coding: utf-8 -*-
# @Time : 2022/3/22 17:12
# @Author : hyx
# @File : active_tag.py
# @desc :
import os
import sys

from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values

from flybirds.core.global_context import GlobalContext
from flybirds.utils import flybirds_log as log

# -- MATCHES ANY TAGS: @use.with_{category}={value}
# NOTE: active_tag_value_provider provides category values for active tags.
# TODO 写入其他py文件
active_tag_value_provider = {
    "python": 'true',
    "browser": os.environ.get("BEHAVE_BROWSER", "chrome"),
    "os": sys.platform,
    "foo": '1',
}
active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


class OnBeforeAll:
    """
    prepare
    """
    name = "OnBeforeAll"
    order = 0

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        """
          SETUP ACTIVE-TAG MATCHER (with userdata)
          USE: behave -D browser=safari ...
        """
        log.info(f'[before_all] user_data:{context.config.userdata}')
        setup_active_tag_values(active_tag_value_provider,
                                context.config.userdata)


class OnBeforeFeature:
    """
    prepare OnBeforeFeature
    """
    name = "OnBeforeFeature"
    order = 5

    @staticmethod
    def can(context, feature):
        return True

    @staticmethod
    def run(context, feature):
        log.info(f'[before_feature] feature.tags:{feature.tags}')
        if active_tag_matcher.should_exclude_with(feature.tags):
            feature.skip(reason=active_tag_matcher.exclude_reason)


class OnBeforeScenario:
    """
    before run scenario will trigger this
    """
    name = "OnBeforeScenario"
    order = 5

    @staticmethod
    def can(context, scenario):
        return True

    @staticmethod
    def run(context, scenario):
        log.info(
            f'[before_scenario] scenario.effective_tags:{scenario.effective_tags}')
        # -- NOTE: scenario.effective_tags := scenario.tags + feature.tags
        if active_tag_matcher.should_exclude_with(scenario.effective_tags):
            scenario.skip(reason=active_tag_matcher.exclude_reason)


var_all = GlobalContext.join("before_run_processor", OnBeforeAll, 1)
var_2 = GlobalContext.join("before_feature_processor", OnBeforeFeature, 1)
var_3 = GlobalContext.join("before_scenario_processor", OnBeforeScenario, 1)
