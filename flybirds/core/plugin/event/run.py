# -*- coding: utf-8 -*-
"""
when behave start run hook will trigger this
"""
import traceback

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.driver import ui_driver
from flybirds.core.global_context import GlobalContext
from flybirds.utils import launch_helper


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    before event
    """

    name = "OnBefore"
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

            # get device screen size
            context.config_manage.device_info.screen_size = (
                ui_driver.air_bdd_screen_size(poco_instance)
            )
            log.info(
                f"device {context.config_manage.device_info.device_id} "
                f"get device"
                f" screen size {context.config_manage.device_info.screen_size}"
            )
        else:
            log.info(
                f"initialization device not obtained:{device_id} or platform"
            )

    @staticmethod
    def init_ocr_driver(context):
        """
        init ocr
        """
        ocr_instance = ui_driver.init_ocr()
        gr.set_value("ocrInstance", ocr_instance)
        context.ocr_instance = ocr_instance
        GlobalContext.ocr_driver_instance = ocr_instance
        log.info("ocr object initialize complete")

    @staticmethod
    def run(context):
        """
        event logical which try to connect device, init screen
        record, lunch login if it need
        """
        try:
            log.info("init device and screen config")
            OnBefore.init_ui_driver(context)
            OnBefore.init_ocr_driver(context)
            # get the global object used to record the screen
            screen_record = GlobalContext.screen_record()
            gr.set_value("screenRecord", screen_record)
            context.screen_record = screen_record
            log.info("screen recording context initialization completed")
            if not screen_record.support:
                log.info("the device does not support screen recording")

            launch_helper.login()

            # startup method selection
            launch_helper.app_start("before_run_page")

        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    after event
    """

    name = "OnAfter"
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
