# -*- coding: utf-8 -*-
"""
load event
"""
import base64

from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.plugin_manager import DirectoryPluginManager
from flybirds.core.config_manage import PluginConfig
from flybirds.core.config_manage import DeviceConfig


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
        user_data = {}
        if context is not None and context.config is not None:
            user_data = (
                context.config.userdata
                if isinstance(context.config.userdata, dict)
                else {}
            )
            for key, value in user_data.items():
                user_data[key] = str(base64.b64decode(value), "utf-8")

        p_info = PluginConfig(user_data).plugin_info
        if p_info is not None and p_info.__contains__("active"):
            GlobalContext.active_plugin = p_info.get("active")

        GlobalContext.plugin_info = p_info.get(GlobalContext.active_plugin)

        if GlobalContext.plugin_info is None:
            raise Exception(
                f"not exist this plugin {GlobalContext.active_plugin}"
            )

        GlobalContext.platform = DeviceConfig(user_data, None).platform
        plugin_manager = DirectoryPluginManager()
        plugin_manager.load_plugins()

        return plugin_manager


# add plugin load event to global processor
GlobalContext.join("plugin_processor", PluginManager, 1)
