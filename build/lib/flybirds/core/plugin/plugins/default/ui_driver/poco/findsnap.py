# -*- coding: utf-8 -*-
"""
Snapshots API
"""
import re

from flybirds.core.global_context import GlobalContext as g_context

__SOURCE__ = None
__IS_NEED_REFRESH__ = False


def clear_snap():
    """
    clear snapshot
    """
    global __SOURCE__
    __SOURCE__ = None


def get_snap():
    """
    Get snapshot
    """
    global __SOURCE__
    return __SOURCE__


def get_refresh_status():
    """
    Get if need refresh  snapshot status
    :return: 'False' or 'True'
    """
    global __IS_NEED_REFRESH__
    return __IS_NEED_REFRESH__


def fix_refresh_status(status):
    """
    Modify whether the snapshot status needs to be refreshed
    """
    global __IS_NEED_REFRESH__
    __IS_NEED_REFRESH__ = status


def refresh_snap():
    """
    Take screenshot
    """
    poco = g_context.element.ui_driver_init()
    frozen_poco = poco.freeze()
    global __SOURCE__
    __SOURCE__ = frozen_poco.agent.hierarchy.dump()


def snap_find(source, config):
    """
    find elements from snapshots
    text: text
    name: name, id
    textMatches: Regular
    """
    print("config", config)
    text = config.get("text")
    name = config.get("name")
    textMatches = config.get("textMatches")
    elements = []

    def find(data):
        if data:
            if name:
                isMatch = data.get("name") == name
            elif text:
                isMatch = (
                    data.get("payload").get("text") or ""
                ).strip().replace(u"\u200b", "") == text.strip().replace(
                    u"\u200b", ""
                )
            elif textMatches:
                matchResult = re.search(
                    textMatches, data.get("payload").get("text") or ""
                )
                isMatch = not (matchResult is None)
            else:
                print("nothing to find")
            children = data.get("children") or []
            if isMatch:
                elements.append(data)
            elif children:
                nextEle = []
                if isinstance(
                    children,
                    (
                        frozenset,
                        list,
                        set,
                        tuple,
                    ),
                ):
                    nextEle = children
                else:
                    nextEle.append(children)
                for child in nextEle:
                    find(child)
            return elements
        else:
            print("not find data")

    return __SOURCE__ and find(__SOURCE__) or None
    # return source and find(source) or None
