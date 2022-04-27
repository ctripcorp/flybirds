# -*- coding: utf-8 -*-
"""
device prepare
"""
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.core.driver.device as device_manage
from flybirds.core.global_context import GlobalContext


class OnPrepare:
    """
    prepare
    """
    name = "On_Device_Prepare"
    order = 15

    @staticmethod
    def init_device(context):
        """
        init device instance
        """
        # get device id
        device_id = gr.get_device_id()
        log.info(f"device_id information:{device_id}")
        if device_id is not None:
            device_instance = device_manage.device_connect(device_id)
            gr.set_value("deviceInstance", device_instance)
            context.device_instance = device_instance
            log.info(f"initialize the device complete:{device_id}")
        else:
            log.info("native device must have device id")
            raise Exception("miss device id")

    @staticmethod
    def can(context):
        """
        only native android can be run
        """
        if gr.get_platform() is not None \
                and (gr.get_platform().lower() == "android"
                     or gr.get_platform().lower()
                     == "ios"):
            return True
        else:
            return False

    @staticmethod
    def run(context):
        """
        install app
        """
        log.info("device prepare")
        OnPrepare.init_device(context)


class OnPCPrepare:
    """
    prepare
    """
    name = "On_PC_Prepare"
    order = 13

    @staticmethod
    def init_device(context):
        """
        prepare device pc connector
        """
        # get device id
        device_id = gr.get_device_id()
        log.info(f"device_id information:{device_id}")
        web_driver_agent = gr.get_web_driver_agent()
        log.info(f"web_driver_agent:{web_driver_agent}")
        if device_id is not None and web_driver_agent is not None and \
                web_driver_agent != "":
            if hasattr(GlobalContext.device, "pc_init"):
                pc_instance = GlobalContext.device.pc_init(device_id,
                                                           web_driver_agent)
                GlobalContext.connector = pc_instance
            log.info(f"initialize the pc connector complete:{device_id}")
        else:
            log.info("ios device must have device id and webDriverAgent")
            raise Exception("miss device id or web_driver_agent")

    @staticmethod
    def can(context):
        """
        only native ios can be run
        """
        if gr.get_platform() is not None \
                and gr.get_platform().lower() == "ios":
            return False
        else:
            return False

    @staticmethod
    def run(context):
        """
        device connect
        """
        log.info("device prepare")
        OnPCPrepare.init_device(context)


# add android prepare into global context
var = GlobalContext.join("before_run_processor", OnPCPrepare, 1)
var1 = GlobalContext.join("before_run_processor", OnPrepare, 1)
