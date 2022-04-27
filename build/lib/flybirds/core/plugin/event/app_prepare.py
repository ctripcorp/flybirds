# -*- coding: utf-8 -*-
"""
app or other prepare
"""
import traceback
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext
import flybirds.core.driver.device as device
from flybirds.core.driver import app


class OnPrepare:
    """
    prepare
    """
    name = "On_App_Prepare"
    order = 21
    _app_name = "installer.apk"

    @staticmethod
    def check_config():
        """
        only local and has package path
        """
        run_info = gr.get_run_info()
        has_local = False
        has_pkg_path = False
        is_rerun = False
        if run_info is not None and run_info.run_at is not None \
                and run_info.run_at.lower() == "local":
            has_local = True

        if run_info is not None and run_info.is_rerun is not None:
            is_rerun = run_info.is_rerun

        package_path = gr.get_app_config_value("package_path")
        if package_path is not None and package_path.strip() != "":
            has_pkg_path = True
        else:
            has_pkg_path = False
        if has_local is True and has_pkg_path is True and is_rerun is False:
            return True
        else:
            return False

    @staticmethod
    def is_web_url(package_path):
        return package_path.startswith(("http:", "https:"))

    @staticmethod
    def check_app():
        """
        check whether app is installed
        """
        has_install = False
        over_install = gr.get_app_config_value("overwrite_installation")
        if over_install is True:
            return True

        pkg_name = gr.get_app_package_name()
        cmd_package_installed = "pm list packages"
        cmd_result = device.use_shell(cmd_package_installed)
        if cmd_result is not None:
            lines = cmd_result.splitlines()
            for line in lines:
                if line is not None and line:
                    ls = line.split(":")
                    if len(ls) == 2 and pkg_name == ls[1].strip():
                        log.info(f"app {pkg_name} has already be installed")
                        has_install = True
        if has_install is True:
            return False
        else:
            return True

    @staticmethod
    def can(context):
        """
        only native android can be run
        """
        if gr.get_platform() is not None and gr.get_platform().lower() \
                == "android":
            # check config
            config_check = OnPrepare.check_config()
            if config_check is True:
                return OnPrepare.check_app()
            else:
                return False
        else:
            return False

    @staticmethod
    def run(context):
        """
        install app
        """
        try:
            if hasattr(context, "installer_path"):
                installer = context.installer_path
                log.info(f"install app start, path:{installer}")
                app.install_app(installer)

                log.info("install end")
            else:
                raise Exception("not find any installer path")
        except Exception:
            log.info("fail to install app")
            exception_str = traceback.format_exc()
            if exception_str is not None and exception_str.find(
                    "INSTALL_FAILED_VERSION_DOWNGRADE") > 0:
                raise Exception(
                    "A higher version of the app is already installed on "
                    "the device, please uninstall it before installing")
            else:
                raise Exception(exception_str)


# add android prepare into global context
var = GlobalContext.join("before_run_processor", OnPrepare, 1)
