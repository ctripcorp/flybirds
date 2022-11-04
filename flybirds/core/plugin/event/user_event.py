# -*- coding: utf-8 -*-
"""
when behave start run hook will trigger this
"""

from flybirds.core.global_context import GlobalContext
from flybirds.utils import launch_helper


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    user defined before all hook
    """

    name = "On_Before_User_Hook"
    order = 50

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        """
        user defined before all hook
        """
        # hook extend by tester
        before_all_extend = launch_helper.get_hook_file("before_all_extend")
        if before_all_extend is not None:
            before_all_extend(context)


var = GlobalContext.join("before_run_processor", OnBefore, 1)
