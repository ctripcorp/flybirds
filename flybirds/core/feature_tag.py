# -*- coding: UTF-8 -*-
"""
Provides a knowledge database if some Python features are supported
in the current python version.
"""

import sys

import six

import flybirds.core.global_resource as gr


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
DEFAULT_ACTIVE_TAG_VALUE_PROVIDER = {
    "python2": bool_to_string(six.PY2),
    "python3": bool_to_string(six.PY3),
    "os": sys.platform.lower(),
    "deviceType": gr.get_platform()
}
