# -*- coding: utf-8 -*-
"""
it is triggered when behave before all
"""
import json
import traceback
from typing import Dict, Any

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.exceptions import get_error_type
from flybirds.core.global_context import GlobalContext
import flybirds.utils.flybirds_log as logger

playwright_send = None
playwright_send_return_as_dict = None
playwright_send_no_reply = None


async def send(self, method: str, params: Dict = None) -> Any:
    selector = None
    method = method
    try:
        if params is not None and params.get("selector") is not None:
            selector = params.get("selector")
        if method is not None and method == "goto":
            if params is not None and params.get("url") is not None:
                selector = params.get("url")
        result = await playwright_send(self, method, params)
        return result
    except Exception as e:
        try:
            get_error_type(e, selector, method)
        except Exception as set_error:
            logger.info(f"set error failed")
        raise e


async def send_return_as_dict(self, method: str, params: Dict = None) -> Any:
    selector = None
    method = method
    try:
        if params is not None and params.get("selector") is not None:
            selector = params.get("selector")
        result = await playwright_send_return_as_dict(self, method, params)
        return result
    except Exception as e:
        try:
            get_error_type(e, selector, method)
        except Exception as set_error:
            logger.info(f"set error failed")
        raise e


def send_no_reply(self, method: str, params: Dict = None) -> None:
    selector = None
    method = method
    try:
        if params is not None and params.get("selector") is not None:
            selector = params.get("selector")
        playwright_send_no_reply(self, method, params)
    except Exception as e:
        try:
            get_error_type(e, selector, method)

        except Exception as set_error:
            logger.info(f"set error failed")

        raise e


class OnWebPlaywrightHook:  # pylint: disable=too-few-public-methods
    """
    load user config data event
    """

    name = "OnWebPlaywrightHook"
    order = 30

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() == "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        execute load config and set to global context
        """
        try:
            global playwright_send
            global playwright_send_return_as_dict
            global playwright_send_no_reply
            from playwright._impl._connection import Channel
            playwright_send = Channel.send
            Channel.send = send
            playwright_send_return_as_dict = Channel.send_return_as_dict
            Channel.send_return_as_dict = send_return_as_dict
            playwright_send_no_reply = Channel.send_no_reply
            Channel.send_no_reply = send_no_reply
        except Exception as e_out:
            log.info("hook === playwright error", traceback.format_exc())
            raise e_out


var = GlobalContext.insert("config_processor", OnWebPlaywrightHook, 1)
