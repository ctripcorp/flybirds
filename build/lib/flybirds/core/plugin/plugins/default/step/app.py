# -*- coding: utf-8 -*-
"""
app step implement
"""
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext as g_Context


def init_device(context, param=None):
    device_id = param
    g_Context.device.device_connect(device_id)
    gr.set_value("deviceid", device_id)
    log.info("device connected:{}".format(device_id))

    # Get the globally defined poco object
    poco_instance = g_Context.element.ui_driver_init()
    gr.set_value("pocoInstance", poco_instance)
    context.poco_instance = poco_instance
    log.info("poco initial complete")


def connect_device(context, param):
    g_Context.device.device_connect(param)


def install_app(context, param):
    g_Context.app.install_app(param)


def uninstall_app(context, param):
    g_Context.app.uninstall_app(param)


def start_app(context, param):
    g_Context.app.wake_app(param, 10)
    gr.set_value("packageName", param)
    # Modal box error detection
    poco_ele.detect_error()


def restart_app(context):
    package_name = gr.get_app_package_name()
    g_Context.app.shut_app(package_name)
    wait_time = gr.get_frame_config_value("app_start_time", 6)
    g_Context.app.wake_app(package_name, wait_time)


def stop_app(context):
    package_name = gr.get_app_package_name()
    g_Context.app.shut_app(package_name)


def return_pre_page(context):
    g_Context.element.key_event("4")


def to_app_home(context):
    schema_goto_module = gr.get_value("projectScript").app_operation
    to_home = getattr(schema_goto_module, "to_home")
    to_home()


def app_login(context, param1, param2):
    schema_goto_module = gr.get_value("projectScript").app_operation
    login = getattr(schema_goto_module, "login")
    login(param1, param2)


def app_logout(context):
    schema_goto_module = gr.get_value("projectScript").app_operation
    logout = getattr(schema_goto_module, "logout")
    logout()
