# -*- coding: utf-8 -*-
"""
Device screenshot method.
"""
import os
import time
import traceback
from baseImage import Image, Rect
from base64 import b64decode
from .ui_driver import SIFT

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.core.plugin.plugins.default.ios_snapshot import get_screen
from flybirds.core.exceptions import FlybirdsException


class BaseScreen:

    @staticmethod
    def screen_shot(path):
        """
        Take a screenshot and save
        """
        log.debug(f"[screen_shot] screen shot start. path is:{path}")
        cur_platform = g_Context.platform
        try:
            if cur_platform is None:
                log.error('[screen_shot] get cur_platform is None!')
                raise Exception("[screen_shot] get cur_platform is None!")

            poco = g_Context.ui_driver_instance
            screen_size = gr.get_device_size()
            if cur_platform.strip().lower() == "ios":
                b64img, fmt = get_screen()
            else:
                b64img, fmt = poco.snapshot(width=screen_size[1])

            open(path, "wb").write(b64decode(b64img))
        except Exception as e:
            log.warn(
                "Screenshot failed path: {}, error: {}".format(path, str(e)),
                traceback.format_exc(),
            )
        log.debug("[screen_shot] screen shot end!")

    @staticmethod
    def screen_link_to_behave(scenario, step_index, tag=None, link=True):
        """
        screenshot address and linked to the <scr> tag
        The label information is placed in the description of the scene,
        and the json report is processed after all the runs are finished,
        and the <scr> information in the description is converted into
        embeddings information in the step.
        """
        feature_name = file_helper.valid_file_name(scenario.feature.name)
        scenario_name = file_helper.valid_file_name(scenario.name)

        step_len = len(scenario.steps)
        if scenario is not None and hasattr(scenario, "background_steps") and \
                len(scenario.background_steps) > 0:
            step_len = step_len + len(scenario.background_steps)

        if step_len > step_index >= 0:
            file_name = None
            if not (tag is None):
                file_name = tag
            file_name += (
                    scenario_name
                    + uuid_helper.create_short_uuid()
                    + str(int(round(time.time() * 1000)))
                    + ".png"
            )

            screen_shot_dir = gr.get_screen_save_dir()
            if not (screen_shot_dir is None):
                current_screen_dir = os.path.join(screen_shot_dir,
                                                  feature_name)
            else:
                current_screen_dir = os.path.join(feature_name)
            log.debug(f"[screen_link_to_behave] screen_shot_dir path :"
                     f"{screen_shot_dir} and "
                     f"current_screen_dir path: {current_screen_dir}")
            file_helper.create_dirs_path_object(current_screen_dir)

            src_path = "../screenshot/{}/{}".format(feature_name, file_name)
            log.debug("[screen_link_to_behave] src_path: {}".format(src_path))
            data = (
                'embeddingsTags, stepIndex={}, <image class ="screenshot"'
                ' width="375" src="{}" />'.format(step_index, src_path)
            )
            if link is True:
                scenario.description.append(data)
            screen_path = os.path.join(current_screen_dir, file_name)
            g_Context.screen.screen_shot(screen_path)
            return screen_path

    @staticmethod
    def image_ocr(img_path):
        """
        Take a screenshot and ocr
        """
        log.debug(f"[image ocr path] image path is:{img_path}")
        ocr = g_Context.ocr_driver_instance

        if ocr is None:
            message = "\n----------------------------------------------------\n" \
                      "OCR engine is not start, please check following steps:\n"\
                      "1. In windows platform, you need to download OCR requirement file from " \
                      "https://github.com/ctripcorp/flybirds/blob/main/requirements_ml.txt\n" \
                      "2. run command `pip install -r requirements_ml.txt`\n" \
                      "3. Configure `ocrLang` option in flybirds_config.json, detail languages refer to \n" \
                      "https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#ocr-opencv\n" \
                      "----------------------------------------------------\n "
            raise FlybirdsException(message)

        g_Context.ocr_result = ocr.ocr(img_path, cls=True)
        g_Context.image_size = Image(img_path).size
        log.debug(f"[image ocr path] image size is:{g_Context.image_size}")


    @staticmethod
    def image_verify(img_source_path, img_search_path):
        """
        Take a screenshot and verify image
        """
        match = SIFT()
        img_source = Image(img_source_path)
        img_search = Image(img_search_path)

        result = match.find_all_results(img_source, img_search)
        return result

    @staticmethod
    def white_screen_detect(img_path):
        match = SIFT()
        img = Image(img_path)
        start_time = time.time()
        width = img.size[1]
        height = img.size[0]
        range_height = height / 100
        point_y = 0
        white_percent = 0
        while point_y + range_height <= height:
            new_img = img.crop(rect=Rect(0, point_y, width, range_height))
            kp_src, des_src = match.get_keypoint_and_descriptor(new_img)
            point_y += range_height
            if len(kp_src) < 3:
                white_percent += 1
        log.info(f"detect use time:{time.time() - start_time}")
        return white_percent



