# coding=utf-8
"""
behave hook and our plugin load from here
"""
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.life_cycle import load

__import__("flybirds.core.plugin.life_cycle")


def before_all(context):
    """
    behave hook before running
    """
    log.info('################## [web] before_all start! ##################')
    # start load
    log.info(f'[web] before_all context: {context.config.userdata}')
    load(context)
    # plugin load
    GlobalContext.process("config_processor", context)
    GlobalContext.process("before_run_processor", context)


def after_all(context):
    """
    behave global hook after running
    """
    log.info('################## [web] after_all start! ##################')
    GlobalContext.process("after_run_processor", context)


def before_feature(context, feature):
    """
    feature hook before running
    """
    log.info(
        '################ [web] before_feature start! ##################')
    GlobalContext.process("before_feature_processor", context, feature)


def after_feature(context, feature):
    """
    feature hook after running
    """
    log.info(
        '################ [web] after_feature start! ##################')
    GlobalContext.process("after_feature_processor", context, feature)


def before_scenario(context, scenario):
    """
    scene before running hook
    """
    log.info(
        '################ [web] before_scenario start! ##################')
    GlobalContext.process("before_scenario_processor", context, scenario)


def after_scenario(context, scenario):
    """
    scenario post-run hook
    """
    log.info(
        '################ [web] after_scenario start! ##################')
    GlobalContext.process("after_scenario_processor", context, scenario)


def before_step(context, step):
    """
    statement hook before run
    """
    log.info(
        '################ [web] before_step start! ##################')
    GlobalContext.process("before_step_processor", context, step)


def after_step(context, step):
    """
    statement run hook
    """
    log.info(
        '################ [web] after_step start! ##################')
    GlobalContext.process("after_step_processor", context, step)


def before_tag(context, tag):
    """
    tag front hook
    """
    log.info(
        '################ [web] before_tag start! ##################')
    GlobalContext.process("before_tag_processor", context, tag)


def after_tag(context, tag):
    """
    tag post hook
    """
    log.info(
        '################ [web] after_tag start! ##################')
    GlobalContext.process("after_tag_processor", context, tag)
