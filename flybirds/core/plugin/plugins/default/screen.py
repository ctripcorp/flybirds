# -*- coding: utf-8 -*-
"""
Device screenshot method.
"""
import os
import time
import traceback
from baseImage import Image
from base64 import b64decode
from .ui_driver import SIFT

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.core.plugin.plugins.default.ios_snapshot import get_screen


class BaseScreen:

    @staticmethod
    def screen_shot(path):
        """
        Take a screenshot and save
        """
        log.info(f"[screen_shot] screen shot start. path is:{path}")
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
        log.info("[screen_shot] screen shot end!")

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
            log.info(f"[screen_link_to_behave] screen_shot_dir path :"
                     f"{screen_shot_dir} and "
                     f"current_screen_dir path: {current_screen_dir}")
            file_helper.create_dirs_path_object(current_screen_dir)

            src_path = "../screenshot/{}/{}".format(feature_name, file_name)
            log.info("[screen_link_to_behave] src_path: {}".format(src_path))
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
        log.info(f"[image ocr path] image path is:{img_path}")
        ocr = g_Context.ocr_driver_instance
        g_Context.ocr_result = ocr.ocr(img_path, cls=True)
        g_Context.image_size = Image(img_path).size
        log.info(f"[image ocr path] image size is:{g_Context.image_size}")
        for line in g_Context.ocr_result:
            log.info(f"[image ocr result] scan line info is:{line}")
            # box = line[0]
            # log.info(f"[image ocr result] scan box info is:{box}")
            # x = (box[0][0] + box[1][0]) / 2
            # y = (box[0][1] + box[2][1]) / 2
            # log.info(f"[image ocr result] scan box xy info is:{x},{y}")
            # txt = line[1][0]
            # log.info(f"[image ocr result] scan txt info is:{txt}")
            # score = line[1][1]
            # log.info(f"[image ocr result] scan score info is:{score}")


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



