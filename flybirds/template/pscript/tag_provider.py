# -*- coding: utf-8 -*-
# @Time : 2022/3/23 12:06
# @Author : hyx
# @File : tag_provider.py
# @desc :
import os
import sys

import six


def bool_to_string(value):
    """Converts a boolean active-tag value into its normalized
    string representation.

    :param value:  Boolean value to use (or value converted into bool).
    :returns: Boolean value converted into a normalized string.
    """
    return str(bool(value)).lower()


ACTIVE_TAG_VALUE_PROVIDER = {
    "python": bool_to_string(six.PY3),
    "browserT": os.environ.get("BEHAVE_BROWSER", "chrome"),
    "os": sys.platform,
    "foo": '1',
}
