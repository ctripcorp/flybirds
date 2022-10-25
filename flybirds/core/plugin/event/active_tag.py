# -*- coding: utf-8 -*-
# @Time : 2022/3/22 17:12
# @Author : hyx
# @File : active_tag.py
# @desc : active_tag
import sys

import six
from behave.tag_matcher import ActiveTagMatcher, setup_active_tag_values

import flybirds.core.global_resource as gr
from flybirds.core.global_context import GlobalContext
from flybirds.utils import flybirds_log as log


def bool_to_string(value):
    """Converts a boolean active-tag value into its normalized
    string representation.

    :param value:  Boolean value to use (or value converted into bool).
    :returns: Boolean value converted into a normalized string.
    """
    return str(bool(value)).lower()


# -----------------------------------------------------------------------------
# DEFAULT SUPPORTED: ACTIVE-TAGS
# -----------------------------------------------------------------------------
def default_active_tag_value_provider():
    platform = GlobalContext.platform if GlobalContext.platform is not None \
        else 'android'
    cur_browser = gr.get_value("cur_browser", 'chromium')
    log.info(f'default_active_tag_provider :{platform} {cur_browser}')
    return {
        "python2": bool_to_string(six.PY2),
        "python3": bool_to_string(six.PY3),
        "os": sys.platform.lower(),
        "platform": platform,
        "deviceType": 'ivd',
        "cur_browser": cur_browser,
    }


def active_tag_init():
    """
      # -- MATCHES ANY TAGS: @use.with_{category}={value}
     # NOTE:
         active_tag_value_provider provides category values for active tags.
     """
    # get custom active_tag
    # tag_provider_module = gr.get_value("projectScript").tag_provider
    # tag_value_provider = getattr(tag_provider_module,
    #                              "ACTIVE_TAG_VALUE_PROVIDER")
    # if tag_value_provider is None:
    #     tag_value_provider = {}
    # log.info(f'tag_value_provider :{tag_value_provider}')

    # get default active_tag
    default_active_tag = default_active_tag_value_provider().copy()
    if default_active_tag is None:
        default_active_tag = {}
    active_tag_value_provider = default_active_tag
    active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)
    gr.set_value("active_tag_matcher", active_tag_matcher)
    return active_tag_value_provider


def merge(dict1, dict2):
    res = {**dict1, **dict2}
    return res


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
          SETUP ACTIVE-TAG MATCHER (with user_data)
          USE: behave -D browser=safari ...
        """
        log.info(f'[active_before_all] user_data:{context.config.userdata}')
        GlobalContext.set_global_cache('userdata', context.config.userdata)
        active_tag_value_provider = active_tag_init()
        log.info(f'[active_before_all] active_tag_provider:'
                 f'{active_tag_value_provider}')
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
        active_tag_matcher = gr.get_value("active_tag_matcher")
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
            f'[before_scenario] scenario.effective_tags:'
            f'{scenario.effective_tags}')
        active_tag_matcher = gr.get_value("active_tag_matcher")
        # -- NOTE: scenario.effective_tags := scenario.tags + feature.tags
        if active_tag_matcher.should_exclude_with(scenario.effective_tags):
            scenario.skip(reason=active_tag_matcher.exclude_reason)


var_all = GlobalContext.join("before_run_processor", OnBeforeAll, 1)
var_2 = GlobalContext.join("before_feature_processor", OnBeforeFeature, 1)
var_3 = GlobalContext.join("before_scenario_processor", OnBeforeScenario, 1)
