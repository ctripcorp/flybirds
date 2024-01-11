# -*- coding: utf-8 -*-
"""
log helper
"""
import logging
from flybirds.core.global_context import GlobalContext
import flybirds.core.global_resource as gr

# create logger
logger = logging.getLogger("flybirds_log")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)


def debug_debug(*args, level):
    try:
        if gr.get_value("debug", False):
            if hasattr(GlobalContext, "debug_console"):
                data = ""
                for arg in args:
                    if isinstance(arg, str):
                        data = data + arg
                GlobalContext.debug_console.set_case_step_log(data, level)
    except Exception as e:
        print(e)


def debug(*args):
    """
    log debug
    """
    debug_debug(*args, level=2)
    for arg in args:
        logger.debug(arg)


def info(*args):
    """
    log info
    """
    debug_debug(*args, level=0)
    for arg in args:
        logger.info(arg)


def warn(*args):
    """
    warn log
    """
    debug_debug(*args, level=3)
    for arg in args:
        logger.warning(arg)


def error(*args):
    """
    error log
    """
    debug_debug(*args, level=1)
    for arg in args:
        logger.error(arg)
