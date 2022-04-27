# -*- coding: utf-8 -*-
"""
log helper
"""
import logging

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


def debug(*args):
    """
    log debug
    """
    for arg in args:
        logger.debug(arg)


def info(*args):
    """
    log info
    """
    for arg in args:
        logger.info(arg)


def warn(*args):
    """
    warn log
    """
    for arg in args:
        logger.warning(arg)


def error(*args):
    """
    error log
    """
    for arg in args:
        logger.error(arg)
