# coding=utf-8
"""
behave hook and our plugin load from here
"""
from flybirds.core.global_context import GlobalContext

__import__("flybirds.core.plugin.life_cycle")


def before_all(context):
    """
    behave hook before running
    """
    # plugin load
    GlobalContext.process("config_processor", context)
    GlobalContext.process("before_run_processor", context)


def after_all(context):
    """
    behave global hook after running
    """
    GlobalContext.process("after_run_processor", context)


def before_feature(context, feature):
    """
    feature hook before running
    """

    GlobalContext.process("before_feature_processor", context, feature)


def after_feature(context, feature):
    """
    feature hook after running
    """

    GlobalContext.process("after_feature_processor", context, feature)


def before_scenario(context, scenario):
    """
    scene before running hook
    """
    GlobalContext.process("before_scenario_processor", context, scenario)


def after_scenario(context, scenario):
    """
    scenario post-run hook
    """
    GlobalContext.process("after_scenario_processor", context, scenario)


def before_step(context, step):
    """
    statement hook before run
    """
    GlobalContext.process("before_step_processor", context, step)


def after_step(context, step):
    """
    statement run hook
    """
    GlobalContext.process("after_step_processor", context, step)


def before_tag(context, tag):
    """
    tag front hook
    """
    GlobalContext.process("before_tag_processor", context, tag)


def after_tag(context, tag):
    """
    tag post hook
    """
    GlobalContext.process("after_tag_processor", context, tag)
