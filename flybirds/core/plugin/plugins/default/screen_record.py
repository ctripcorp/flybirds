# -*- coding: utf-8 -*-
"""
Screen recording related.
"""
import datetime
import os
import time
import shutil
import ffmpeg
import airtest
from airtest.core.android.adb import ADB

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.snippet as cmd_helper
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.exceptions import ScreenRecordException
from flybirds.core.global_context import GlobalContext as g_context

airtest_adb_path = ADB.builtin_adb_path()


class ScreenRecord:
    def __init__(self):
        self.support = False
        self.start_time = None
        self.end_time = None
        self.process = None
        # 0 Just created 1 Reset state 2 Start recording
        self.status = 0

        self.use_airtest_record = gr.get_frame_config_value(
            "use_airtest_record", False
        )

        self.airtest_record_mode = gr.get_frame_config_value("airtest_record_mode")

        if self.use_airtest_record is False:
            self.record_support()
        else:
            self.support = True

        log.info("use_airtest_record: {}".format(self.use_airtest_record))

        self.dev = gr.get_value("deviceInstance")
        if self.use_airtest_record:
            # Use airtest to record screen
            self.recording_file = "/sdcard/test.mp4"
            self.output_file = "screen.mp4"
            self.output_ffmpeg_file = None
            self.airtest_version_high = False

            airtest_version = airtest.__version__
            v1 = tuple(map(int, airtest_version.split('.')))
            v2 = tuple(map(int, "1.2.9".split('.')))
            if v1 >= v2:
                self.airtest_version_high = True
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
        try:
            proc.communicate(timeout=10)
            proc_code = proc.poll()
        except Exception as e:
            log.error(
                "Screen record support {} not end in 10 seconds, innerError:{}".format(
                    cmd, str(e)
                )
            )
            proc_code = 1

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

            if self.airtest_version_high:
                self.output_ffmpeg_file = os.path.join(
                    "screen_%s.mp4" % (time.strftime("%Y%m%d%H%M%S", time.localtime())))
                self.dev.start_recording(max_time=max_time, bit_rate=bit_rate, bit_rate_level=bit_rate_level,
                                         mode=self.airtest_record_mode, output=self.output_ffmpeg_file)
                if self.airtest_record_mode == 'yosemite':
                    if self.dev.yosemite_recorder.recording_file is not None:
                        device_id = gr.get_device_id()
                        copy_target_file = self.dev.yosemite_recorder.recording_file
                        dirs = get_all_dir(copy_target_file)

                        target_exist_code = len(dirs) - 1
                        for i, dir_path in enumerate(reversed(dirs)):
                            if dir_path != '':
                                cmd = "{} -s {} shell ls {}".format(airtest_adb_path, device_id, dir_path)
                                check_exists_code = execute_cmd(cmd, False)

                                if check_exists_code == 0:
                                    target_exist_code = len(dirs) - 1 - i
                                    break

                        if target_exist_code < len(dirs) - 1:
                            for i, dir_path in enumerate(dirs):
                                if dir_path != '':
                                    if i > target_exist_code:
                                        if i == len(dirs) - 1:
                                            cmd = "{} -s {} shell touch {}".format(airtest_adb_path, device_id,
                                                                                   dir_path)
                                        else:
                                            cmd = "{} -s {} shell mkdir -p {}".format(airtest_adb_path, device_id,
                                                                                      dir_path)
                                        execute_cmd(cmd, False)
            else:
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
            self.dev.stop_recording(output=self.output_file, is_interrupted=True)
            # self.dev.adb.pull(self.recording_file, self.output_file)
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

        copy_target_file = None

        if self.use_airtest_record:
            if self.airtest_version_high:
                if self.airtest_record_mode == 'ffmpeg':
                    source_file = self.output_ffmpeg_file
                    target_file = save_path
                    shutil.copy(source_file, target_file)

                    if not os.path.exists(target_file):
                        shutil.copy(source_file, target_file)
                    return
                elif self.airtest_record_mode == 'yosemite':
                    copy_target_file = self.dev.yosemite_recorder.recording_file
            else:
                copy_target_file = self.recording_file
        else:
            copy_target_file = self.recording_file

        cmd = "{} -s {} pull {} {}".format(airtest_adb_path,
                                           device_id, copy_target_file,
                                           save_path
                                           )
        execute_cmd(cmd, True)

    def clear_record(self):
        """
        Delete the existing screen recording file
        """
        device_id = gr.get_device_id()

        copy_target_file = None

        if self.use_airtest_record:
            if self.airtest_version_high:
                if self.airtest_record_mode == 'ffmpeg':
                    try:
                        if self.output_ffmpeg_file is not None:
                            os.remove(self.output_ffmpeg_file)
                    except Exception as e:
                        pass
                    return
                elif self.airtest_record_mode == 'yosemite':
                    if self.dev.yosemite_recorder.recording_file is not None:
                        # reset methond
                        copy_target_file = self.dev.yosemite_recorder.recording_file
                    else:
                        # destroy methond
                        copy_target_file = self.recording_file
            else:
                copy_target_file = self.recording_file
        else:
            copy_target_file = self.recording_file

        cmd = "{} -s {} shell rm -r {}".format(airtest_adb_path, device_id,
                                               copy_target_file)
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
        if self.use_airtest_record and self.airtest_record_mode != 'ffmpeg':
            target = 'tmp.mp4'
            try:
                log.info("crop_record start")
                screen_size = gr.get_device_size()
                source = src_path
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
            finally:
                if os.path.exists(target):
                    os.remove(target)


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
        gr.set_value("record_url", src_path)
        log.info(
            f'default screen_record [link_record] src_path: {src_path}')

        try:
            screen_record.copy_record(src_path)
            if gr.get_platform().lower() == "android":
                screen_record.crop_record(src_path)
        except Exception as e:
            log.error(
                "Screen record copy error "
                "innerError:{}".format(
                    str(e)
                )
            )

        try:
            g_context.set_global_cache('current_record_path', src_path)
        except:
            pass


def get_all_dir(file_path):
    if not file_path:
        return []

    dir_path = file_path[:file_path.rfind('/')]
    dirs = get_all_dir(dir_path)
    dirs.append(file_path)
    return dirs


def execute_cmd(cmd, outerr):
    proc_code = 5
    # sub process start time
    start_time = datetime.datetime.now()
    proc = cmd_helper.create_sub_process(cmd)
    message = ""
    try:
        proc.communicate(timeout=30)
    except Exception as e:
        message = "cp screenshot {} not end " \
                  "in 30 seconds," \
                  " innerError:{}".format(cmd, str(e))
    proc_code = proc.poll()

    # time out
    while proc.poll() is None:
        end_time = datetime.datetime.now()
        diff = end_time - start_time
        if diff.seconds > (60 * 2):
            log.warn("execute cmd:{} running timeout", cmd)
            if proc.poll() is None:
                # proc_code=5 means kill sub process
                proc_code = 5
            break

    if int(proc_code) == 0:
        log.info("execute cmd:{} success", cmd)
    else:
        log.warn(
            "execute cmd:{} not copy_success message: {}".format(cmd, message)
        )
        if proc is not None:
            proc.terminate()

        if outerr:
            raise ScreenRecordException(message)

    proc.terminate()
    return proc_code
