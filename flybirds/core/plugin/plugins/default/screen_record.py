# -*- coding: utf-8 -*-
"""
Screen recording related.
"""
import datetime
import os
import time
import shutil
import ffmpeg

from airtest.core.android.adb import ADB

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.snippet as cmd_helper
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.exceptions import ScreenRecordException

airtest_adb_path = ADB.builtin_adb_path()


class ScreenRecord:
    def __init__(self):
        self.support = False
        self.start_time = None
        self.end_time = None
        self.process = None
        # 0 Just created 1 Reset state 2 Start recording
        self.status = 0

        self.record_support()
        self.use_airtest_record = gr.get_frame_config_value(
            "use_airtest_record", False
        )
        log.info("use_airtest_record: {}".format(self.use_airtest_record))

        self.dev = gr.get_value("deviceInstance")
        if self.use_airtest_record:
            # Use airtest to record screen
            self.recording_file = "/sdcard/test.mp4"
            self.output_file = "screen.mp4"
        else:
            self.recording_file = "/sdcard/flybirds.mp4"

    def reset(self):
        """
        Reset object
        """
        self.start_time = None
        self.end_time = None
        self.status = 1
        if not (self.process is None):
            proc_code = self.process.poll()
            if proc_code is None:
                self.process.terminate()
                time.sleep(2)
        self.clear_record()

    def destroy(self):
        """
        Destroy all recorded video processes after the task runs
        """
        if not (self.process is None):
            proc_code = self.process.poll()
            if proc_code is None:
                self.process.terminate()
                time.sleep(2)
        self.clear_record()

    def record_support(self):
        device_id = gr.get_device_id()

        cmd = "{} -s {} shell screenrecord --help".format(airtest_adb_path,
                                                          device_id)
        proc = cmd_helper.create_sub_process(cmd)
        proc.communicate(timeout=10)
        proc_code = proc.poll()

        if int(proc_code) == 0:
            self.support = True
            log.info(
                "record_support message:  proc_code:{}, support: {}".format(
                    str(proc_code), self.support
                )
            )
        proc.terminate()

    def start_record(self, timeout, bit_rate_level=1, bit_rate=None):
        """
        Start recording
        """
        log.info("start_record")
        log.info("bit_rate_level: {}".format(bit_rate_level))
        if bit_rate_level > 5:
            bit_rate_level = 5
        if self.use_airtest_record:
            if not bit_rate:
                screen_size = gr.get_device_size()
                bit_rate = screen_size[0] * screen_size[1] * bit_rate_level
            max_time = timeout
            log.info(
                "record use_airtest max_time: {}, bit_rate: {}".format(
                    max_time, bit_rate
                )
            )
            self.dev.start_recording(max_time, bit_rate)
        else:
            if not self.support:
                return
            self.reset()
            device_id = gr.get_device_id()
            screen_size = gr.get_device_size()
            if not bit_rate:
                bit_rate = screen_size[0] * screen_size[1] * bit_rate_level
            if ":" in device_id:
                cmd = "{} -s {} shell screenrecord --bugreport " \
                      "--size {}x{} --time-limit {} --bit-rate {} " \
                      "--verbose sdcard/flybirds.mp4".format(airtest_adb_path,
                                                             device_id,
                                                             screen_size[0],
                                                             screen_size[1],
                                                             timeout, bit_rate)
            else:
                cmd = "{} -s {} shell screenrecord" \
                      " --size {}x{} " \
                      "--time-limit {} " \
                      "--bit-rate {}" \
                      " --verbose " \
                      "sdcard/flybirds.mp4".format(airtest_adb_path, device_id,
                                                   screen_size[0],
                                                   screen_size[1], timeout,
                                                   bit_rate)

            proc = cmd_helper.create_sub_process(cmd)
            message = ""
            try:
                out, err = proc.communicate(timeout=10)
                if out:
                    message = "Recording start {}".format(
                        out.decode(encoding="UTF-8")
                    )
                if err:
                    message = "Recording start error {}".format(
                        err.decode(encoding="UTF-8")
                    )
            except Exception as e:
                message = "Recording start /sdcard/flybirds.mp4 , " \
                          f"innerError:{str(e)}"
            log.debug("start_record message: {}".format(message))
            time.sleep(1)
            self.process = proc
            self.status = 2
            self.start_time = time.time()

    def stop_record(self):
        """
        Stop the current screen recording
        """
        log.info("stop_record")
        if self.use_airtest_record:
            log.info("stop_record use_airtest_record")
            self.dev.stop_recording(output=self.output_file)
            self.dev.adb.pull(self.recording_file, self.output_file)
        else:
            if not self.support:
                return
            proc = self.process
            if proc is None:
                return "No recording service"

            message = ""
            # proc.wait()
            proc_code = proc.poll()
            if proc_code is None:
                proc.terminate()
                time.sleep(2)
                message = "Stop recording"
            else:
                message = "Recording is over，code={}".format(proc_code)
            self.end_time = time.time()
            self.status = 3
            out, err = proc.communicate()
            if out:
                message += " Screen recording {}".format(
                    out.decode(encoding="UTF-8")
                )
                log.debug(
                    "stop_record out message: {}, proc_code: {}".format(
                        message, str(proc_code)
                    )
                )
            if err:
                message += " Screen recording error {}".format(
                    err.decode(encoding="UTF-8")
                )
                log.warn(
                    "stop_record err "
                    "ScreenRecordException: {}, proc_code: {}".format(
                        message, str(proc_code)
                    )
                )
                raise ScreenRecordException(message)
            log.info(
                "stop_record message: {}, proc_code: {}".format(
                    message, str(proc_code)
                )
            )
            return message

    def copy_record(self, save_path):
        """
        Copy the screen recording from the mobile phone to the current client
        """
        device_id = gr.get_device_id()
        cmd = "{} -s {} pull {} {}".format(airtest_adb_path,
                                           device_id, self.recording_file,
                                           save_path
                                           )
        # sub process start time
        start_time = datetime.datetime.now()
        proc = cmd_helper.create_sub_process(cmd)
        message = ""
        try:
            proc.communicate(timeout=30)
        except Exception as e:
            message = "cp screenshot {} not end " \
                      "in 30 seconds," \
                      " innerError:{}".format(self.recording_file, str(e))
        proc_code = proc.poll()

        # time out
        while proc.poll() is None:
            end_time = datetime.datetime.now()
            diff = end_time - start_time
            if diff.seconds > (60 * 2):
                log.warn("copy record running timeout")
                if proc.poll() is None:
                    # proc_code=5 means kill sub process
                    proc_code = 5
                break

        if int(proc_code) == 0:
            log.info("copy record success")
        else:
            log.warn(
                "copy_record not copy_success message: {}".format(message)
            )
            if proc is not None:
                proc.terminate()

            raise ScreenRecordException(message)

        proc.terminate()

    def clear_record(self):
        """
        Delete the existing screen recording file
        """
        device_id = gr.get_device_id()
        cmd = "{} -s {} shell rm -r {}".format(airtest_adb_path, device_id,
                                               self.recording_file)
        proc = cmd_helper.create_sub_process(cmd)
        # message = ""
        try:
            proc.communicate(timeout=15)
        except Exception as e:
            log.error(
                "Screen record deletion {} not end in "
                "15 seconds, innerError:{}".format(
                    self.recording_file, str(e)
                )
            )
        proc_code = proc.poll()
        if int(proc_code) == 0:
            log.info("clear record success")
        proc.terminate()

    def crop_record(self, src_path):
        if self.use_airtest_record:
            try:
                log.info("crop_record start")
                screen_size = gr.get_device_size()
                source = src_path
                target = 'tmp.mp4'
                shutil.copy(source, target)
                stream = ffmpeg.input(target)
                stream = ffmpeg.crop(stream, 0, 0, screen_size[0], screen_size[1])
                stream = ffmpeg.output(stream, source)
                stream = ffmpeg.overwrite_output(stream)
                ffmpeg.run(stream)
                os.remove(target)
                log.info("crop_record finish success")
            except Exception as e:
                log.error(
                    "Screen record crop error "
                    "innerError:{}".format(
                        str(e)
                    )
                )


def link_record(scenario, step_index):
    """
    Associate screenshots to report
    """
    screen_record = gr.get_value("screenRecord")
    log.info(
        "link_record support: {}, step_index: {},"
        " len(scenario.steps): {}, if: {}".format(
            str(screen_record.support),
            str(step_index),
            str(len(scenario.steps)),
            str(len(scenario.steps) > step_index >= 0),
        )
    )
    if not screen_record.support:
        data = "embeddingsTags, stepIndex={}, " \
               "<label>the device does not " \
               "support screen recording</label>".format(step_index)
        scenario.description.append(data)
        return
    feature_name = file_helper.valid_file_name(scenario.feature.name)
    scenario_name = file_helper.valid_file_name(scenario.name)
    if len(scenario.steps) > step_index >= 0:
        file_name = (
                scenario_name
                + uuid_helper.create_short_uuid()
                + str(int(round(time.time() * 1000)))
                + ".mp4"
        )
        screen_shot_dir = gr.get_screen_save_dir()
        if not (screen_shot_dir is None):
            current_screen_dir = os.path.join(screen_shot_dir, feature_name)
        else:
            current_screen_dir = os.path.join(feature_name)
        file_helper.create_dirs_path_object(current_screen_dir)

        src_path = "../screenshot/{}/{}".format(feature_name, file_name)
        data = (
            'embeddingsTags, stepIndex={}, <video controls width="375">'
            '<source src="{}" type="video/mp4"></video>'.format(
                step_index, src_path
            )
        )
        scenario.description.append(data)
        src_path = os.path.join(current_screen_dir, file_name)
        log.info(
            f'default screen_record [link_record] src_path: {src_path}')
        screen_record.copy_record(src_path)
        if gr.get_platform().lower() == "android":
            screen_record.crop_record(src_path)

