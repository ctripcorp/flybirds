# -*- coding: utf-8 -*-
"""
plugin load and destroy
"""

from flybird.core.global_context import GlobalContext

__import__("flybird.core.plugin.loader")


def load(context):
    """
    load plugin
    """
    GlobalContext.process("plugin_processor", context)


def destroy(context):
    """
     destroy plugin
    """
    raise Exception("not implement destroy")


# start load
load(None)
