# -*- coding: utf-8 -*-
"""
load event
"""
import base64

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.config_manage import DeviceConfig
from flybirds.core.config_manage import PluginConfig
from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.plugin_manager import DirectoryPluginManager


class PluginManager:  # pylint: disable=too-few-public-methods
    """
    plugin load management
    """

    name = "PluginManager"
    order = 1

    @staticmethod
    def run(context):
        """
        load plugin from pkg
        """
        # initialize the global object module
        gr.init_glb()
        # get user-specified parameter value or custom parameter
        user_data = {}
        if context is not None and context.config is not None:
            user_data = (
                context.config.userdata
                if isinstance(context.config.userdata, dict)
                else {}
            )
            for key, value in user_data.items():
                user_data[key] = str(base64.b64decode(value), "utf-8")

        log.info(f'[loader] user_data: {user_data}')
        gr.set_value("userData", user_data)

        p_info = PluginConfig(user_data).plugin_info
        if p_info is not None and p_info.__contains__("active"):
            GlobalContext.active_plugin = p_info.get("active")

        GlobalContext.plugin_info = p_info.get(GlobalContext.active_plugin)

        if GlobalContext.plugin_info is None:
            raise Exception(
                f"not exist this plugin {GlobalContext.active_plugin}"
            )
        if user_data.get('platform'):
            GlobalContext.platform = user_data.get('platform')
        else:
            GlobalContext.platform = DeviceConfig(user_data, None).platform
        log.info(
            f"[loader] run platform: {GlobalContext.platform}")
        plugin_manager = DirectoryPluginManager()
        plugin_manager.load_plugins()

        return plugin_manager


# add plugin load event to global processor
GlobalContext.join("plugin_processor", PluginManager, 1)
