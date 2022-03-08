# -*- coding: utf-8 -*-
"""
web step implements class
"""

from playwright.sync_api import sync_playwright

import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext as g_context

__open__ = ["Step"]


class Step:
    """Web Step Class"""

    name = "web_step"

    @classmethod
    def jump_to_page(cls, context, param):
        log.info(f'web jump_to_page. param: {param}')
        plugin_page = g_context.page
        page = plugin_page()
        page.navigate(context, param)

    @classmethod
    def screenshot(cls, context):
        log.info('web screenshot.')

        with sync_playwright() as play_wright:
            step_index = context.cur_step_index - 1
            cls.screen_link_to_behave(play_wright, context.scenario,
                                      step_index, "screen_")

    @classmethod
    def prev_fail_scenario_relevance(self, context, param1, param2):
        pass

    @classmethod
    def start_screen_record(cls, context):
        log.info('web start_screen_record.')

        with sync_playwright() as play_wright:
            step_index = context.cur_step_index - 1
            # screen_record.link_record(context.scenario, step_index)
            cls.record_link(play_wright, context.scenario, step_index)

    # @staticmethod
    # def screen_link_to_behave(play_wright, scenario, step_index, tag=None):
    #     """
    #     screenshot address and linked to the <scr> tag
    #     The label information is placed in the description of the scene,
    #     and the json report is processed after all the runs are finished,
    #     and the <scr> information in the description is converted into embeddings
    #     information in the step.
    #     """
    #     feature_name = file_helper.valid_file_name(scenario.feature.name)
    #     scenario_name = file_helper.valid_file_name(scenario.name)
    #
    #     if len(scenario.steps) > step_index >= 0:
    #         file_name = None
    #         if not (tag is None):
    #             file_name = tag
    #         file_name += (
    #                 scenario_name
    #                 + uuid_helper.create_short_uuid()
    #                 + str(int(round(time.time() * 1000)))
    #                 + ".png"
    #         )
    #
    #         # TODO 需要将web 的 get_screen_save_dir  保存到gr中去,
    #         #  否则current_screen_dir不正确： current_screen_dir path :web测试
    #         # screen_shot_dir = gr.get_screen_save_dir()
    #         screen_shot_dir = None
    #         if not (screen_shot_dir is None):
    #             current_screen_dir = os.path.join(screen_shot_dir,
    #                                               feature_name)
    #         else:
    #             current_screen_dir = os.path.join(feature_name)
    #         file_helper.create_dirs_path_object(current_screen_dir)
    #
    #         src_path = "../screenshot/{}/{}".format(feature_name, file_name)
    #         log.info("screen_link_to_behave: {}".format(src_path))
    #         data = (
    #             'embeddingsTags, stepIndex={}, <image class ="screenshot"'
    #             ' width="375" src="{}" />'.format(step_index, src_path)
    #         )
    #         scenario.description.append(data)
    #
    #         log.info(f"screen_shot_dir path :{screen_shot_dir}")
    #         log.info(f"current_screen_dir path :{current_screen_dir}")
    #         path = os.path.join(current_screen_dir, file_name)
    #         Step.web_screenshot(play_wright, path)
    #         # page.screenshot(path=f'{path}.png')
    #
    # @staticmethod
    # def web_screenshot(play_wright, path):
    #     browser_type = play_wright.firefox
    #     browser = browser_type.launch(headless=False
    #                                   )
    #     page = browser.new_page()
    #     page.goto("https://www.baidu.com/")
    #     # 等待页面加载完全后截图
    #     print(page.title())
    #     page.wait_for_selector("text=百度一下")
    #     page.screenshot(path=f'{path}')
    #     browser.close()
    #
    # @staticmethod
    # def record_link(play_wright, scenario, step_index):
    #     """
    #     Associate screenshots to report
    #     """
    #     support = True
    #     log.info(
    #         "link_record support: {}, step_index: {},"
    #         " len(scenario.steps): {}, if: {}".format(
    #             str(support),
    #             str(step_index),
    #             str(len(scenario.steps)),
    #             str(len(scenario.steps) > step_index >= 0),
    #         )
    #     )
    #     if not support:
    #         data = "embeddingsTags, stepIndex={}, " \
    #                "<label>the device does not " \
    #                "support screen recording</label>".format(step_index)
    #         scenario.description.append(data)
    #         return
    #     feature_name = file_helper.valid_file_name(scenario.feature.name)
    #     scenario_name = file_helper.valid_file_name(scenario.name)
    #     if len(scenario.steps) > step_index >= 0:
    #         file_name = (
    #                 scenario_name
    #                 + uuid_helper.create_short_uuid()
    #                 + str(int(round(time.time() * 1000)))
    #                 + ".mp4"
    #         )
    #         # TODO
    #         # screen_shot_dir = gr.get_screen_save_dir()
    #         # current_screen_dir = os.path.join(screen_shot_dir, feature_name)
    #         current_screen_dir = os.path.join(feature_name)
    #         file_helper.create_dirs_path_object(current_screen_dir)
    #
    #         src_path = "../screenshot/{}/{}".format(feature_name, file_name)
    #         data = (
    #             'embeddingsTags, stepIndex={}, <video controls width="375">'
    #             '<source src="{}" type="video/mp4"></video>'.format(
    #                 step_index, src_path
    #             )
    #         )
    #         scenario.description.append(data)
    #         src_path = os.path.join(current_screen_dir, file_name)
    #         log.info(f'web record_link src_path: {src_path}')
    #         Step.web_record(play_wright, src_path)
    #
    # @staticmethod
    # def web_record(play_wright, src_path):
    #     browser_type = play_wright.firefox
    #     browser = browser_type.launch(headless=True)
    #
    #     context = browser.new_context(record_video_dir='videos')
    #     page = context.new_page()
    #
    #     page.goto("https://www.baidu.com/", wait_until='networkidle')
    #     page.click('#kw')
    #     page.fill('#kw', '12306')
    #     page.wait_for_timeout(1000)
    #     page.click('#su')
    #
    #     video = page.video
    #     path = video.path()
    #     print(f'web_record path: {path}')
    #
    #     context.close()
    #     # 将视频另存为
    #     video.save_as(src_path)
    #     browser.close()
