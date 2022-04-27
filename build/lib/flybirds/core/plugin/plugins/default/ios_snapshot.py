# -*- coding: utf-8 -*-
"""
Overriding poco snapshot
"""
import base64
import os
import time

from airtest import aircv
from airtest.core.helper import G
from airtest.core.settings import Settings as ST

import flybirds.core.global_resource as gr


def get_screen():
    save_path = snapshot()
    return base64.b64encode(open(save_path, 'rb').read()), 'png'


def snapshot(filename=None, msg="", quality=None, max_size=None):
    """
    Take the screenshot of the target device and save it to the file.
    """
    if not quality:
        quality = ST.SNAPSHOT_QUALITY
    if not max_size and ST.IMAGE_MAXSIZE:
        max_size = ST.IMAGE_MAXSIZE
    if filename:
        if not os.path.isabs(filename):
            log_dir = ST.LOG_DIR or "."
            filename = os.path.join(log_dir, filename)
        screen = G.DEVICE.snapshot(filename, quality=quality,
                                   max_size=max_size)
        return try_log_screen(screen, quality=quality, max_size=max_size)
    else:
        return try_log_screen(quality=quality, max_size=max_size)


def try_log_screen(screen=None, quality=None, max_size=None):
    """
    Save screenshot to file

    Args:
        screen: screenshot to be saved
        quality: The image quality, default is ST.SNAPSHOT_QUALITY
        max_size: the maximum size of the picture, e.g 1200

    Returns:
       filepath
    """
    if not ST.LOG_DIR:
        ST.LOG_DIR = gr.get_screen_save_dir()
    if not ST.SAVE_IMAGE:
        return
    if not quality:
        quality = ST.SNAPSHOT_QUALITY
    if not max_size:
        max_size = ST.IMAGE_MAXSIZE
    if screen is None:
        screen = G.DEVICE.snapshot(quality=quality)
    filename = "%(time)d.jpg" % {'time': time.time() * 1000}
    filepath = os.path.join(ST.LOG_DIR, filename)
    if screen is not None:
        aircv.imwrite(filepath, screen, quality, max_size=max_size)
        return filepath
    return None
