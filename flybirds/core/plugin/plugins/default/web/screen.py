# -*- coding: utf-8 -*-
"""
web screen imp
"""
import os
import time

import flybirds.core.global_resource as gr
import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log
import flybirds.utils.uuid_helper as uuid_helper

__open__ = ["Screen"]


class Screen:
    """
    screen imp
    """
    name = "web_screen"

    @classmethod
    def screen_shot(cls, context):
        log.info('web screenshot.')
        step_index = context.cur_step_index - 1
        cls.screen_link_to_behave(context.scenario, step_index, "screen_")

    @staticmethod
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

            # TODO 需要将web 的 get_screen_save_dir  保存到gr中去,
            #  否则current_screen_dir不正确： current_screen_dir path :web测试
            # screen_shot_dir = gr.get_screen_save_dir()
            screen_shot_dir = None
            if not (screen_shot_dir is None):
                current_screen_dir = os.path.join(screen_shot_dir,
                                                  feature_name)
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
            log.info(f"current_screen_dir path :{current_screen_dir}")
            path = os.path.join(current_screen_dir, file_name)
            Screen.web_screenshot(path)

    @staticmethod
    def web_screenshot(path):
        page_obj = gr.get_value("plugin_page")
        if page_obj is None or (not hasattr(page_obj, 'page')):
            log.error('[web_screenshot] get page object has error!')
        page_obj.page.screenshot(path=f'{path}')
