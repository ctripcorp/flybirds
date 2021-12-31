# -*- coding: utf-8 -*-
"""
uuid helper
"""
import uuid
import time
import random


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
