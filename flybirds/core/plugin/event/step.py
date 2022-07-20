# -*- coding: utf-8 -*-
"""
when run step will trigger this event
"""

from flybirds.core.global_context import GlobalContext
from flybirds.utils import flybirds_log as log
from flybirds.utils import launch_helper
import flybirds.core.global_resource as gr


def step_init(context, step):
    """
    adjust the order of the current steps for use in associated screenshots
    """
    # adjust the order of the current steps for use in associated screenshots
    context.cur_step_index += 1


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    before step
    """

    name = "OnBefore"
    order = 5

    @staticmethod
    def can(context, step):
        return True

    @staticmethod
    def run(context, step):
        """
        exe before step
        """
        log.info(step)
        step_init(context, step)
        log.info(f"run step:{step.name}")
        # # if there is a hook custom behavior, call the related function
        # before_step_extend = launch_helper.get_hook_file("before_step_extend")
        # if before_step_extend is not None:
        #     before_step_extend(context, step)


class OnUserBefore:  # pylint: disable=too-few-public-methods
    """
    before step
    """

    name = "OnUserBefore"
    order = 50

    @staticmethod
    def can(context, step):
        return True

    @staticmethod
    def run(context, step):
        """
        exe before step
        """
        # if there is a hook custom behavior, call the related function
        before_step_extend = launch_helper.get_hook_file("before_step_extend")
        if before_step_extend is not None:
            before_step_extend(context, step)


class OnWebBefore:  # pylint: disable=too-few-public-methods
    """
    before step
    """

    name = "OnWebBefore"
    order = 15

    @staticmethod
    def can(context, step):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() == "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context, step):
        """
        exe before step
        """
        if hasattr(GlobalContext, "get_global_cache"):
            if GlobalContext.get_global_cache("web_console") is not None:
                GlobalContext.set_global_cache("web_console", None)


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    after step
    """

    name = "OnAfter"
    order = 100

    @staticmethod
    def can(context, step):
        return True

    @staticmethod
    def run(context, step):
        """
        exe after step
        """
        # hook extend by tester
        after_step_extend = launch_helper.get_hook_file("after_step_extend")
        if after_step_extend is not None:
            after_step_extend(context, step)


# join step event to global processor
var = GlobalContext.join("before_step_processor", OnBefore, 1)
var4 = GlobalContext.join("before_step_processor", OnUserBefore, 1)

var1 = GlobalContext.join("after_step_processor", OnAfter, 1)
