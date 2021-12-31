# -*- coding: utf-8 -*-
"""
app file prepare
"""
import os
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext
from flybirds.utils import file_helper
from flybirds.utils import download_helper


class OnPrepare:
    """
    prepare
    """
    name = "OnFilePrepare"
    order = 20
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
            log.info("not have package path")
            has_pkg_path = False
        if has_local is True and has_pkg_path is True and is_rerun is False:
            return True
        else:
            return False

    @staticmethod
    def is_web_url(package_path):
        return package_path.startswith(("http:", "https:"))

    @staticmethod
    def check_apk_file(context):
        package_path = gr.get_app_config_value("package_path")
        if OnPrepare.is_web_url(package_path):
            d_apk_path = os.path.join(os.getcwd(), "download",
                                      OnPrepare._app_name)
            if os.path.exists(d_apk_path):
                context.installer_path = d_apk_path
                return False
            else:
                return True
        else:
            if os.path.isfile(package_path):
                if os.path.exists(package_path):
                    context.installer_path = package_path
                    return False
                else:
                    raise Exception(
                        f"cannot find your package in path:{package_path}")
            else:
                new_package_path = os.path.join(package_path,
                                                OnPrepare._app_name)
                if os.path.exists(new_package_path):
                    context.installer_path = new_package_path
                    return False
                else:
                    raise Exception(
                        f"cannot find your package in path:{new_package_path}")

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
                return OnPrepare.check_apk_file(context)
            else:
                return False
        else:
            return False

    @staticmethod
    def run(context):
        """
        install app
        """
        # download app
        log.info("install file prepare")

        package_path = gr.get_app_config_value("package_path")
        log.info(f"package path:{package_path}")
        installer = None
        if OnPrepare.is_web_url(package_path):
            base_path = os.path.join(os.getcwd(), "download")
            file_helper.create_dirs(base_path)
            d_apk_path = os.path.join(os.getcwd(), "download",
                                      OnPrepare._app_name)
            log.info("download start")
            download_helper.downlaod(package_path, d_apk_path)
            log.info("download end")
            installer = d_apk_path
        else:
            if os.path.isfile(package_path):
                installer = package_path
            else:
                installer = os.path.join(package_path,
                                         OnPrepare._app_name)
        if os.path.exists(installer) is not True:
            raise Exception(
                f"not exist path :{installer}")
        else:
            context.installer_path = installer


# add android prepare into global context
var = GlobalContext.join("before_run_processor", OnPrepare, 1)
