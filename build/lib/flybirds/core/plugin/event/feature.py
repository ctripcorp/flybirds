# -*- coding: utf-8 -*-
"""
when run behave feature will trigger the before and after event
"""
from flybirds.core.global_context import GlobalContext
from flybirds.utils import launch_helper


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    feature before processor
    """

    name = "OnBefore"
    order = 5

    @staticmethod
    def can(context, feature):
        return True

    @staticmethod
    def run(context, feature):
        """
        run before processor and run user defined hook func
        """
        # thread local set feature language
        GlobalContext.set_current_language(feature.language)

        # hook extend by tester
        before_feature_extend = launch_helper.get_hook_file(
            "before_feature_extend"
        )
        if before_feature_extend is not None:
            before_feature_extend(context, feature)


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    feature after processor
    """

    name = "OnAfter"
    order = 100

    @staticmethod
    def can(context, feature):
        return True

    @staticmethod
    def run(context, feature):
        """
        run after processor and run user defined hook func
        """
        # thread local release feature language
        GlobalContext.del_current_language()
        # hook extend by tester
        after_feature_extend = launch_helper.get_hook_file(
            "after_feature_extend"
        )
        if after_feature_extend is not None:
            after_feature_extend(context, feature)


# register event to global processor wait to be triggered
var = GlobalContext.join("before_feature_processor", OnBefore, 1)
var1 = GlobalContext.join("after_feature_processor", OnAfter, 1)
