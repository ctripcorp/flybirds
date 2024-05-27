import traceback
import importlib

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.driver import ui_driver
from flybirds.core.global_context import GlobalContext
from flybirds.utils import launch_helper


class OnScreenRecordBefore:  # pylint: disable=too-few-public-methods
    """
    before event
    """

    name = "@OnScreenRecordBefore001@"
    order = 16

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
            log.info("init screen config")
            # get the global object used to record the screen
            screen_record = GlobalContext.screen_record()
            gr.set_value("screenRecord", screen_record)
            context.screen_record = screen_record
            log.info("screen recording context initialization completed")
            if not screen_record.support:
                log.info("the device does not support screen recording")
        except Exception as init_error:
            log.info("global initialization error", traceback.format_exc())
            raise init_error


var2 = GlobalContext.join("before_run_processor", OnScreenRecordBefore, 1)
