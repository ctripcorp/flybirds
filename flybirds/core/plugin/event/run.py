# -*- coding: utf-8 -*-
"""
when behave start run hook will trigger this
"""
import traceback
import importlib

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.driver import ui_driver
from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.event.device_prepare import OnPrepare
from flybirds.utils import launch_helper


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    before event
    """

    name = "@OnAppDriveInitBeforeBefore@"
    order = 50

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() != "web"):
            return True
        else:
            return False

    @staticmethod
    def init_ui_driver(context):
        """
        init device
        """
        # get deviceid
        device_id = gr.get_device_id()
        if device_id is not None:

            # get the globally defined poco object
            poco_instance = ui_driver.init_driver()
            gr.set_value("pocoInstance", poco_instance)
            context.poco_instance = poco_instance
            GlobalContext.ui_driver_instance = poco_instance
            log.info("poco object initialization completed")

            try:
                # get device screen size
                context.config_manage.device_info.screen_size = (
                    ui_driver.air_bdd_screen_size(poco_instance)
                )
                gr.set_value("current_screen_size", context.config_manage.device_info.screen_size)
                log.info(
                    f"device {context.config_manage.device_info.device_id} "
                    f"get device"
                    f" screen size {context.config_manage.device_info.screen_size}"
                )
            except Exception as e:
                log.info(f"get device screen size error: {str(e)}")
                OnPrepare.init_device(context)
        else:
            log.info(
                f"initialization device not obtained:{device_id} or platform"
            )

    @staticmethod
    def init_ocr_driver(context):
        """
        init ocr
        """
        try:
            ocr_instance = ui_driver.init_ocr()
            gr.set_value("ocrInstance", ocr_instance)
            context.ocr_instance = ocr_instance
            GlobalContext.ocr_driver_instance = ocr_instance
            log.info("ocr object initialize complete")
        except Exception:
            pass

    @staticmethod
    def run(context):
        """
        event logical which try to connect device, init screen
        record, lunch login if it need
        """
        try:
            log.info("init device and screen config")
            OnBefore.init_ui_driver(context)

        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


class OnOcrBefore:  # pylint: disable=too-few-public-methods
    """
    before event
    """

    name = "@OnAppDriveOcrInitBeforeBefore@"
    order = 51

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() != "web"):
            return True
        else:
            return False

    @staticmethod
    def init_ocr_driver(context):
        """
        init ocr
        """
        try:
            ocr_instance = ui_driver.init_ocr()
            gr.set_value("ocrInstance", ocr_instance)
            context.ocr_instance = ocr_instance
            GlobalContext.ocr_driver_instance = ocr_instance
            log.info("ocr object initialize complete")
        except Exception:
            pass

    @staticmethod
    def run(context):
        """
        event logical which try to connect device, init screen
        record, lunch login if it need
        """
        try:
            log.info("init ocr config")
            try:
                importlib.import_module("paddleocr")
                OnBefore.init_ocr_driver(context)
            except Exception as e:
                log.info("paddleocr not installed")

        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    after event
    """

    name = "OnAppAfterAll"
    order = 100

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() != "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        close screen record
        """
        ui_driver.close_driver()

        # hook extend by tester
        after_all_extend = launch_helper.get_hook_file("after_all_extend")
        if after_all_extend is not None:
            after_all_extend(context)


class OnAppUserLoginBeforeAll:  # pylint: disable=too-few-public-methods
    """
    before event
    """

    name = "@OnAppUserLoginBeforeAll@"
    order = 56

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() != "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        event logical which try to connect device, init screen
        record, lunch login if it need
        """
        try:
            log.info("user before all")
            need_login = gr.get_flow_behave_value("before_run_login", False)
            log.info("before_run_login:{}".format(need_login))
            launch_helper.login()
            if need_login:
                # startup method selection
                launch_helper.app_start("before_run_page")
        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


class OnScreenRecordRelease:
    """
    after event
    """

    name = "OnScreenRecordRelease"
    order = 10

    @staticmethod
    def can(context):
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() != "web"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        close connector
        """
        try:
            log.info("release screen record")
            screen_record = gr.get_value("screenRecord")
            if screen_record is not None and hasattr(screen_record, "destroy"):
                screen_record.destroy()
        except Exception as clear_error:
            log.info(f"clear screen record error :{str(clear_error)}")


class OnRelease:
    """
    after event
    """

    name = "OnRelease"
    order = 13

    @staticmethod
    def can(context):

        if GlobalContext.connector is not None:
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        close connector
        """
        GlobalContext.connector.close()


# add event to global processor
var = GlobalContext.join("before_run_processor", OnBefore, 1)
var2 = GlobalContext.join("after_run_processor", OnScreenRecordRelease, 1)
var3 = GlobalContext.join("after_run_processor", OnRelease, 1)
var4 = GlobalContext.join("after_run_processor", OnAfter, 1)
var5 = GlobalContext.join("before_run_processor", OnAppUserLoginBeforeAll, 1)
var6 = GlobalContext.join("before_run_processor", OnOcrBefore, 1)
