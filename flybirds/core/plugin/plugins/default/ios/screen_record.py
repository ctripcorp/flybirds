# -*- coding: utf-8 -*-
"""
ios screen record
"""
import os
import time
from flybirds.core import global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.plugin.plugins.default.screen_record import ScreenRecord
import inspect
__open__ = ["ScreenRecordInfo"]


class ScreenRecordInfo(ScreenRecord):
    name = "ios_screen_record"
    instantiation_timing = "plugin"

    def __init__(self):
        log.info(
         "ios start_record")
        ScreenRecord.__init__(self)
        

    def reset(self):
        """
        Reset object
        """
        self.start_time = None
        self.end_time = None
        self.status = 1


    def record_support(self):
        if hasattr(self.dev, "start_recording"):
            log.info("The current Airtest version iOS screen recording is supported，can set configuration useAirtestRecord ot true")

    def start_record(self, timeout, bit_rate_level=1, bit_rate=None):
        """
        Start recording
        """
        log.info(
        "ios start_record")
        """
               Start recording
               """
        log.info("bit_rate_level: {}".format(bit_rate_level))

        if bit_rate_level > 5:
            bit_rate_level = 5
        if self.use_airtest_record:
            self.reset()

            if not bit_rate:
                screen_size = gr.get_device_size()
                bit_rate = screen_size[0] * screen_size[1] * bit_rate_level
            max_time = timeout
            log.info(
                "record use_airtest max_time: {}, bit_rate: {}".format(
                    max_time, bit_rate
                )
            )

            self.output_ffmpeg_file = os.path.join(
                "screen_%s.mp4" % (time.strftime("%Y%m%d%H%M%S", time.localtime())))
            log.info(
                "ios-record-default {}, output_ffmpeg_file: {}".format(
                    max_time, self.output_ffmpeg_file
                )
            )
            if hasattr(self.dev, "start_recording"):

                # 使用inspect.signature获取函数的签名对象
                sig = inspect.signature(self.dev.start_recording)
                # 打印实例的__call__方法的参数信息
                argspec = inspect.getfullargspec(self.dev.start_recording)

                param_list = sig.parameters.keys()
                if 'mode' in param_list:
                    log.info("start_recording has mode parameter")
                    self.dev.start_recording(max_time, mode=self.airtest_record_mode,
                                             output=self.output_ffmpeg_file)
                elif 'write_mode' in param_list:
                    log.info("start_recording have write_mode parameter")
                    self.dev.start_recording(max_time, write_mode=self.airtest_record_mode,
                                             output=self.output_ffmpeg_file)
                else:
                    log.info("start_recording")
                    self.dev.start_recording(max_time, output=self.output_ffmpeg_file)
            else:
                log.info("The current Airtest version does not support iOS screen recording, please upgrade")
                # self.dev.start_recording(max_time, output=self.output_ffmpeg_file)

        else:
            if not self.support:
                return
            self.reset()
            self.status = 2
            self.start_time = time.time()



    def stop_record(self):
        """
        Stop the current screen recording
        """
        log.info("stop_record")
        if self.use_airtest_record:
            log.info("ios stop_record use_airtest_record")
            save_path = self.dev.stop_recording()
        else:
            if not self.support:
                return
            proc = self.process
            if proc is None:
                return "No recording service"
            self.end_time = time.time()
            self.status = 3

