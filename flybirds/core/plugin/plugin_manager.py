# -*- coding: utf-8 -*-
"""
plugin load mannger
"""
import os
import sys
from imp import find_module, load_module, acquire_lock, release_lock

import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.plugin_proxy import PluginProxy


def append_prex(name, sub_pkg):
    """
    append default pkg
    """
    return "flybirds.core.plugin.plugins." + sub_pkg + "." + name


def append_event_prex(name, sub_pkg):
    """
    append default pkg
    """
    return "flybirds.core.plugin." + sub_pkg + "." + name


def append_config_prex(name, parent_pkg):
    """
    combine pkg and py file name as import module key
    """
    return parent_pkg + "." + name


def find_exsit_name(plugins, name, group):
    """
    get  name from plugins pth list
    """
    for index, item in enumerate(plugins):
        if (
                item[0] is not None
                and item[0] == name
                and item[3] is not None
                and item[3] == group
        ):
            return index + 1
    return 0


class PluginModule:
    """
    plugin  add find and remove func
    """

    name = "base"

    def __init__(self, plugins=(), config=None):
        if config is not None:
            self.c_config = config
        self.__plugins = []
        if plugins:
            self.add_plugins(plugins)

    def __iter__(self):
        return iter(self.plugins)

    def add_plugin(self, plug):
        """
        plugin add
        """
        self.__plugins.append(plug)

    def add_plugins(self, plugins):
        """
        plugin add list
        """
        for plug in plugins:
            self.add_plugin(plug)

    def del_plugin(self, plug):
        """
        plugin del
        """
        if plug in self.__plugins:
            self.__plugins.remove(plug)

    def del_plugins(self, plugins):
        """
        plugin del list
        """
        for plug in plugins:
            self.del_plugin(plug)

    def get_plugins(self, name=None):
        """
        plugin get list
        """
        plugins = []
        for plugin in self.__plugins:
            if name is None or plugin.name == name:
                plugins.append(plugin)
        return plugins

    def _load_plugin(self, plug):
        """
        regist plugin to list
        """
        loaded = False
        for plg in self.plugins:
            if plg.name == plug.name:
                loaded = True
                break
        if not loaded:
            self.add_plugin(plug)

    def _get_plugins(self):
        """
        property get func
        """
        return self.__plugins

    def _set_plugins(self, plugins):
        """
        property set func
        """
        self.__plugins = []
        self.add_plugins(plugins)

    plugins = property(
        _get_plugins,
        _set_plugins,
        None,
    )


# lock = Lock()


class DirectoryPluginManager(PluginModule):
    """
    Plugin manager that loads plugins from plugin directories.
    """

    name = "directory_loader"

    def __init__(self, plugins=(), config=None):
        default_directory = os.path.join(os.path.dirname(__file__), "plugins")
        if config is None:
            config = {}
        self.directories = config.get("directories", (default_directory,))
        PluginModule.__init__(self, plugins, config)

    def find_default_run_event_dir(self, plugins, group):
        """
        get default event plugin path list
        """
        base_dir = os.path.dirname(__file__)
        base_dir_list = (base_dir,)
        for dir_name in base_dir_list:
            try:
                dir_name = (
                    f"{dir_name}/event/"
                    f"{GlobalContext.platform}"
                )
                for f_p in os.listdir(dir_name):
                    if f_p.endswith(".py") and f_p != "__init__.py":
                        exsit_index = find_exsit_name(plugins, f_p[:-3], group)
                        if exsit_index == 0:
                            name = append_event_prex(
                                f_p[:-3],
                                "event."
                                f"{GlobalContext.platform}",
                            )
                            plugins.append((f_p[:-3], name, dir_name, group))
            except OSError:
                continue

        for dir_name in base_dir_list:
            try:
                dir_name = f"{dir_name}/event"
                for f_p in os.listdir(dir_name):
                    if f_p.endswith(".py") and f_p != "__init__.py":
                        exsit_index = find_exsit_name(plugins, f_p[:-3], group)
                        if exsit_index == 0:
                            event_pkg = "event"
                            plugins.append(
                                (
                                    f_p[:-3],
                                    append_event_prex(f_p[:-3], event_pkg),
                                    dir_name,
                                    group,
                                )
                            )
            except OSError:
                continue

    def find_default_dir(self, plugins, group):
        """
        get default platform plugin pth list
        """
        for d_n in self.directories:
            try:
                d_n = d_n + "/default/" + GlobalContext.platform
                for f_p in os.listdir(d_n):
                    if f_p.endswith(".py") and f_p != "__init__.py":
                        exsit_index = find_exsit_name(plugins, f_p[:-3], group)
                        if exsit_index == 0:
                            name = append_prex(
                                f_p[:-3],
                                f"{GlobalContext.active_plugin}"
                                f".{GlobalContext.platform}",
                            )
                            plugins.append((f_p[:-3], name, d_n, group))
            except OSError:
                log.info(f"do not exist path: {d_n}")
                continue

    @staticmethod
    def find_config_dir(plugins, group):
        """
        get user config platform pth list which level is higher than
        find_default_dir
        """
        plugin_info = getattr(GlobalContext, "plugin_info")
        if plugin_info is not None and plugin_info.__contains__(
                GlobalContext.platform
        ):
            active_plug_info = plugin_info.get(GlobalContext.platform)
            all_plugin = []

            for name, value in vars(GlobalContext).items():
                if (
                        value is not None
                        and not hasattr(value, "__call__")
                        and isinstance(value, PluginProxy)
                ):
                    all_plugin.append(name)

            for plugin_key in all_plugin:
                if (
                        active_plug_info is not None
                        and active_plug_info.__contains__(plugin_key)
                ):
                    py_config = active_plug_info.get(plugin_key)
                    if py_config is not None:
                        py_path = py_config.get("path")
                        py_ns = py_config.get("ns")
                        DirectoryPluginManager.add_plugin_path(
                            py_path, py_ns, plugin_key, plugins, group
                        )

    @staticmethod
    def add_plugin_path(py_path, py_ns, plugin_key, plugins, group):
        """
        add path to plugin
        """
        if (
                py_path is not None
                and py_path != ""
                and py_ns is not None
                and py_ns != ""
        ):
            py_name = os.path.basename(os.path.realpath(py_path))
            py_dir = os.path.dirname(os.path.realpath(py_path))
            if find_exsit_name(plugins, py_name[:-3], group) == 0:
                plugins.append(
                    (
                        plugin_key,
                        append_config_prex(py_name[:-3], py_ns),
                        py_dir,
                        group,
                    )
                )

    def load_plugins(self):
        """
        Load plugins by iterating files in plugin directories.
        """
        plugins = []
        self.find_default_run_event_dir(plugins, "event")
        DirectoryPluginManager.find_config_dir(plugins, "driver")
        self.find_default_dir(plugins, "driver")

        fh = None
        mod = None
        for (p_key, name, dir, group) in plugins:
            try:
                acquire_lock()
                fh, filename, desc = find_module(p_key, [dir])
                old = sys.modules.get(name)
                if old is not None:
                    del sys.modules[name]

                mod = load_module(name, fh, filename, desc)

                if hasattr(mod, "__open__"):
                    attrs = [getattr(mod, x) for x in mod.__open__]
                    for plug in attrs:
                        if hasattr(plug, "instantiation_timing") and \
                                plug.instantiation_timing == "plugin":
                            plugin_instance = plug
                        else:
                            plugin_instance = plug()
                        setattr(GlobalContext, p_key, plugin_instance)
            finally:
                if fh:
                    fh.close()
                release_lock()
