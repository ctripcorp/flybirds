# -*- coding: utf-8 -*-
"""
uuid helper
"""
import os
import random
import time
import uuid


def create_uuid():
    """
    Generate random string
    """
    return uuid.uuid4()


def create_short_uuid():
    """
    Generate random integer
    """
    result = str(random.randint(0, 999999999))
    return result


def create_short_timestamp_uuid():
    """
    Generate short uuid plus timestamp
    """
    short_uuid = create_short_uuid()
    return "{}{}".format(short_uuid, time.time())


def report_name(feature, browser_type):
    # name_of_feature.chrome.1495298685509.json
    if '/' in feature:
        feature = feature.split('/')[-1]
    elif os.sep in feature:
        feature = feature.split(os.sep)[-1]
    feature_name = remove_suffix(feature, '.feature')
    millis = int(round(time.time() * 1000))
    return f"{feature_name}.{browser_type}.{millis}.json"


def remove_suffix(s: str, suffix: str) -> str:
    # suffix='' should not call self[:-0].
    if suffix and s.endswith(suffix):
        return s[:-len(suffix)]
    else:
        return s[:]


def remove_prefix(s: str, prefix: str) -> str:
    if s.startswith(prefix):
        return s[len(prefix):]
    else:
        return s[:]
