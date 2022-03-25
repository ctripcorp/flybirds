# -*- coding: utf-8 -*-
# @Time : 2022/3/23 12:06
# @Author : hyx
# @File : tag_provider.py
# @desc : Custom tag_provider
import os

import six

from flybirds.utils.feature_tag import bool_to_string

# -----------------------------------------------------------------------------
# Custom: ACTIVE-TAGS
# Note:
# 1. The following configuration is a demo, users can configure it
# according to their needs
# 2. When the key of the tag is the same as the key of the default tag,
# the value will override the value of the default tag.
# -----------------------------------------------------------------------------
ACTIVE_TAG_VALUE_PROVIDER = {
    "python2": bool_to_string(six.PY2),
    "browser": os.environ.get("BEHAVE_BROWSER", "chrome"),
    "foo": '1'

}
