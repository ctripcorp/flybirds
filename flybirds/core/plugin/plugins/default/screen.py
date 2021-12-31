# -*- coding: utf-8 -*-
"""
Device screenshot method.
"""
import os
import time
import traceback
from base64 import b64decode

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.global_context import GlobalContext as g_context
from flybirds.core.plugin.plugins.default.ios_snapshot import get_screen


def screen_shot(path):
    """
    Take a screenshot and save
    """
    log.info(f"screen shot start------path :{path}")
    # poco = g_context.element.ui_driver_init()
    poco = g_context.ui_driver_instance
    screen_size = gr.get_device_size()
    cur_platform = g_context.platform
    try:
        if cur_platform is not None and cur_platform.strip().lower() == "ios":
            b64img, fmt = get_screen()
        else:
            b64img, fmt = poco.snapshot(width=screen_size[1])

        open(path, "wb").write(b64decode(b64img))
    except Exception as e:
        log.warn(
            "Screenshot failed path: {}, error: {}".format(path, str(e)),
            traceback.format_exc(),
        )

    log.info("screen shot end------")


def screen_link_to_behave(scenario, step_index, tag=None):
    """
    screenshot address and linked to the <scr> tag
    The label information is placed in the description of the scene,
    and the json report is processed after all the runs are finished,
    and the <scr> information in the description is converted into embeddings
    information in the step.
    """
    feature_name = file_helper.valid_file_name(scenario.feature.name)
    scenario_name = file_helper.valid_file_name(scenario.name)

    if len(scenario.steps) > step_index >= 0:
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
            current_screen_dir = os.path.join(screen_shot_dir, feature_name)
        else:
            current_screen_dir = os.path.join(feature_name)
        file_helper.create_dirs_path_object(current_screen_dir)

        src_path = "../screenshot/{}/{}".format(feature_name, file_name)
        log.info("screen_link_to_behave: {}".format(src_path))
        data = (
            'embeddingsTags, stepIndex={}, <image class ="screenshot"'
            ' width="375" src="{}" />'.format(step_index, src_path)
        )
        scenario.description.append(data)

        log.info(f"screen_shot_dir path :{screen_shot_dir}")
        screen_shot(os.path.join(current_screen_dir, file_name))
