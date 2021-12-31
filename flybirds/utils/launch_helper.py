# -*- coding: utf-8 -*-

"""
lunch help
"""
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.core.driver.app as app
import flybirds.core.driver.element as ake
import time


def login():
    """
    use user login
    """
    need_login = gr.get_flow_behave_value("before_run_login", False)
    log.info("before_run_login:{}".format(need_login))
    if need_login:
        schema_goto_module = gr.get_value("projectScript").app_operation
        login = getattr(schema_goto_module, "login")
        if not (login is None):
            login_user = gr.get_app_config_value("default_user")
            login_password = gr.get_app_config_value("default_password")
            log.info(
                "Login，user：{} password：{}".format(login_user, login_password)
            )
            login(login_user, login_password)


def app_start(page_name):
    """
    device start at init
    """
    device_id = gr.get_device_id()
    package_name = gr.get_app_package_name()
    page_value = gr.get_flow_behave_value(page_name, None)
    log.info("device_id:{},".format(device_id))
    log.info("page_name:{},".format(page_name))
    log.info("package_name:{}".format(package_name))
    if not (package_name is None or page_value is None or device_id is None):
        if "restartApp" == page_value:
            app.shut_app(package_name)
            wait_time = gr.get_frame_config_value("app_start_time", 6)
            app.wake_app(package_name, wait_time)
            log.info("complete restartApp and sleep {}".format(wait_time))
        elif "startApp" == page_value:
            wait_time = gr.get_frame_config_value("app_start_time", 6)
            app.wake_app(package_name, wait_time)
            log.info("complete startApp and sleep {}".format(wait_time))
        elif "stopApp" == page_value:
            app.shut_app(package_name)
            log.info("stop app before running")
        elif "backupPage" == page_value:
            ake.key_event("4")


def get_runtime_data(scenario):
    """
    get run data
    """
    client_id = gr.get_app_config_value("unique_tag")
    device_id = gr.get_device_id()
    run_id = gr.get_app_config_value("run_id")
    build_id = gr.get_app_config_value("build_id")
    pkg_version = gr.get_app_config_value("pkg_version")
    run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    location = scenario.feature.location
    data = (
        "client_id: {}, device_id: {}, run_id: {}, build_id: {}"
        ", pkg_version: {}, run_time: {}, location: {}".format(
            client_id,
            device_id,
            run_id,
            build_id,
            pkg_version,
            run_time,
            location,
        )
    )
    return data


def get_hook_file(filename):
    """
    get use hook data
    """
    project_script = gr.get_value("projectScript")
    if hasattr(project_script, "dsl_hook") and hasattr(
        project_script.dsl_hook, filename
    ):
        file_extend = getattr(project_script.dsl_hook, filename)
        return file_extend
    else:
        return None
