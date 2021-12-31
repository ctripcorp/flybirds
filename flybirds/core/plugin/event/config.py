# -*- coding: utf-8 -*-
"""
it is triggered when behave before all
"""
import base64
import traceback
from flybirds.core.config_manage import ConfigManage, AppEnvConfig
from flybirds.core.script_config import ScriptImportManage
from flybirds.report.fail_feature_create import set_rerun_info
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext


class OnConfigLoad:  # pylint: disable=too-few-public-methods
    """
    load user config data event
    """

    name = "OnConfigLoad"
    order = 0

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        """
        execute load config and set to global context
        """
        try:
            log.info("start on before hook")
            # initialize the global object module
            gr.init_glb()
            # get user-specified parameter value or custom parameter
            user_data = (
                context.config.userdata
                if isinstance(context.config.userdata, dict)
                else {}
            )
            for key, value in user_data.items():
                user_data[key] = str(base64.b64decode(value), "utf-8")
            gr.set_value("userData", user_data)
            # obtain the failure case information and associate
            # it with the report later
            set_rerun_info(user_data, gr)
            # get configuration, user-defined priority and configuration file
            config_manage = ConfigManage(user_data)
            gr.set_value("configManage", config_manage)
            context.config_manage = config_manage
            log.info("configuration file read completed")
            log.ch.setLevel(gr.get_log_level())

            # config app runtime env
            app_env_config = AppEnvConfig(user_data, None)
            if app_env_config.env_config is not None:
                gr.set_value("appEnvConfig", app_env_config.env_config)
                context.app_env_config = app_env_config
                log.info(
                    "app operating environment variable "
                    "configuration is complete"
                )

            gr.set_value("run_info", config_manage.run_config)

            # get the custom python script of the project
            project_script = ScriptImportManage()
            gr.set_value("projectScript", project_script)
            context.project_script = project_script
            log.info("the python script in the project is read")

        except Exception as e_out:
            log.info("global initialization error", traceback.format_exc())
            raise e_out


var = GlobalContext.insert("config_processor", OnConfigLoad, 1)
