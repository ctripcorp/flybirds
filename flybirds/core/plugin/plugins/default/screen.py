# -*- coding: utf-8 -*-
"""
Device screenshot method.
"""
import os
import time
import traceback
from operator import itemgetter
from flybirds.utils.image import draw_ocr
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
from paddleocr.tools.infer.utility import draw_boxes
from PIL import Image as Img


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

            if tag == "fail_" and len(g_Context.ocr_result) >= 1:
                ocr = g_Context.ocr_driver_instance
                result = ocr.ocr(screen_path, cls=True)
                image = Img.open(screen_path).convert('RGB')
                boxes = [line[0] for line in result]
                im_show = draw_boxes(image, boxes)
                im_show = Img.fromarray(im_show)
                im_show.save(screen_path)

            return screen_path

    @staticmethod
    def image_ocr(img_path, right_gap_max=None, left_gap_max=None, height_gap_max=None, skip_height_max=None):
        """
        Take a screenshot and ocr
        """
        log.debug(f"[image ocr path] image path is:{img_path}")
        ocr = g_Context.ocr_driver_instance

        if ocr is None:
            message = "\n----------------------------------------------------\n" \
                      "OCR engine is not start, please check following steps:\n" \
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
        regional_box, txts = BaseScreen.struct_ocr_result(g_Context.ocr_result, right_gap_max,
                                                          left_gap_max, height_gap_max, skip_height_max)
        boxes = [regional_box[key] for key in regional_box]
        image = Img.open(img_path).convert('RGB')
        if os.path.exists('./fonts/simfang.ttf'):
            im_show = draw_ocr(image, boxes, txts, font_path='./fonts/simfang.ttf')
        else:
            log.warn("draw ocr required ttf file is not found!")
            im_show = draw_boxes(image, boxes)
        im_show = Img.fromarray(im_show)
        im_show.save(img_path)



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

    @staticmethod
    def struct_ocr_result(result, right_gap_max=None, left_gap_max=None, height_gap_max=None, skip_height_max=None):
        struct_ocr = []
        index = 0
        txt_list = []
        if right_gap_max is None:
            right_gap_max = g_Context.image_size[0] * 0.3
        else:
            right_gap_max = g_Context.image_size[0] * right_gap_max
        if left_gap_max is None:
            left_gap_max = g_Context.image_size[0] * 0.3
        else:
            left_gap_max = g_Context.image_size[0] * left_gap_max
        if height_gap_max is None:
            height_gap_max = g_Context.image_size[1] * 0.07
        else:
            height_gap_max = g_Context.image_size[1] * height_gap_max
        if skip_height_max is None:
            skip_height_max = g_Context.image_size[1] * 0.12
        else:
            skip_height_max = g_Context.image_size[1] * skip_height_max
        # remove system time icon
        result = list((n for n in result if n[0][0][1] > skip_height_max
                       and n[1][0] != "0"))
        for line in result:
            struct_dic = {
                "box": None, "txt": None, "height": None,
                "right_box": None, "right_txt": None,
                "left_box": None, "left_txt": None,
                "bottom_box": None, "bottom_txt": None,
                "top_box": None, "top_txt": None,
                "regional_id": None, "regional_box": None,
            }
            box = line[0]
            struct_dic["box"] = box
            struct_dic["txt"] = line[1][0]
            struct_dic["height"] = box[2][1] - box[0][1]

            right_result = BaseScreen.right_box_cal(right_gap_max, height_gap_max, box, result)
            if right_result is not None:
                struct_dic["right_box"] = right_result[0]
                struct_dic["right_txt"] = right_result[1]

            left_result = BaseScreen.left_box_cal(left_gap_max, height_gap_max, box, result)
            if left_result is not None:
                struct_dic["left_box"] = left_result[0]
                struct_dic["left_txt"] = left_result[1]

            bottom_result = BaseScreen.bottom_box_cal(index, height_gap_max, box, result)
            if bottom_result is not None:
                struct_dic["bottom_box"] = bottom_result[0]
                struct_dic["bottom_txt"] = bottom_result[1]

            top_result = BaseScreen.top_box_cal(index, height_gap_max, box, result)
            if top_result is not None:
                struct_dic["top_box"] = top_result[0]
                struct_dic["top_txt"] = top_result[1]

            struct_ocr.append(struct_dic)
            index += 1

        regional_box = BaseScreen.regional_division(struct_ocr)
        struct_ocr_result = sorted(struct_ocr, key=itemgetter('regional_id'))
        ocr_regional_result = []
        for key in regional_box:
            dic_list = list(filter(lambda item: item['regional_id'] == key, struct_ocr_result))
            txts = []
            for dic in dic_list:
                txts.append(dic["txt"])
            txts = ','.join(txts)
            txt_list.append(txts)
            regional_result = {"id": key, "box": regional_box[key], "txts": txts}
            log.info(regional_result)
            ocr_regional_result.append(regional_result)
        g_Context.ocr_regional_result = ocr_regional_result
        g_Context.struct_ocr_result = struct_ocr_result
        return regional_box, txt_list

    @staticmethod
    def right_box_cal(gap_max, height_gap_max, box, result):
        right_index = 0
        box_list = []
        while right_index < len(result):
            right_line = result[right_index]
            right_box = right_line[0]
            right_txt = right_line[1][0]
            height_gap = (right_box[0][1] + right_box[3][1]) / 2 - (box[0][1] + box[3][1]) / 2
            box_gap = right_box[0][0] - box[1][0]
            if gap_max > box_gap > 0 and height_gap_max * 1.5 > height_gap > -height_gap_max * 1.5:
                matched = {"right_box": right_box, "right_txt": right_txt, "box_gap": box_gap}
                box_list.append(matched)
            right_index += 1
        if len(box_list) > 0:
            matched_min = min(box_list, key=itemgetter('box_gap'))
            return [matched_min["right_box"], matched_min["right_txt"]]
        return None

    @staticmethod
    def left_box_cal(gap_max, height_gap_max, box, result):
        left_index = 0
        box_list = []
        while left_index < len(result):
            left_line = result[left_index]
            left_box = left_line[0]
            left_txt = left_line[1][0]
            height_gap = (left_box[0][1] + left_box[3][1]) / 2 - (box[0][1] + box[3][1]) / 2
            box_gap = box[0][0] - left_box[1][0]
            if gap_max > box_gap > 0 and height_gap_max * 1.5 > height_gap > -height_gap_max * 1.5:
                matched = {"left_box": left_box, "left_txt": left_txt, "box_gap": box_gap}
                box_list.append(matched)
            left_index += 1
        if len(box_list) > 0:
            matched_min = min(box_list, key=itemgetter('box_gap'))
            return [matched_min["left_box"], matched_min["left_txt"]]
        return None

    @staticmethod
    def bottom_box_cal(index, height_gap_max, box, result):
        next_line_index = index + 1
        box_list = []
        while next_line_index < len(result):
            next_line = result[next_line_index]
            bottom_box = next_line[0]
            bottom_txt = next_line[1][0]
            height_gap = bottom_box[0][1] - box[2][1]
            wide_length_flag = BaseScreen.wide_gap_detect(bottom_box, box)
            if height_gap_max >= height_gap >= -height_gap_max and wide_length_flag is True:
                matched = {"bottom_box": bottom_box, "bottom_txt": bottom_txt, "height_gap": height_gap}
                box_list.append(matched)
            next_line_index += 1
        if len(box_list) > 0:
            matched_min = min(box_list, key=itemgetter('height_gap'))
            return [matched_min["bottom_box"], matched_min["bottom_txt"]]
        return None

    @staticmethod
    def top_box_cal(index, height_gap_max, box, result):
        before_index = index - 1
        box_list = []
        while before_index >= 0:
            before_line = result[before_index]
            top_box = before_line[0]
            top_txt = before_line[1][0]
            height_gap = top_box[2][1] - box[0][1]
            wide_length_flag = BaseScreen.wide_gap_detect(top_box, box)
            if height_gap_max >= height_gap >= -height_gap_max and wide_length_flag is True:
                matched = {"top_box": top_box, "top_txt": top_txt, "height_gap": height_gap}
                box_list.append(matched)
            before_index -= 1
        if len(box_list) > 0:
            matched_min = min(box_list, key=itemgetter('height_gap'))
            return [matched_min["top_box"], matched_min["top_txt"]]
        return None

    @staticmethod
    def wide_gap_detect(next_box, box):
        mid_gap = (next_box[0][0] + next_box[1][0]) / 2 - (box[0][0] + box[1][0]) / 2
        left_gap = next_box[0][0] - box[0][0]
        right_gap = next_box[1][0] - box[1][0]
        wide_gap = g_Context.image_size[0] * 0.05
        if wide_gap >= mid_gap >= -wide_gap \
                or wide_gap >= left_gap >= -wide_gap \
                or wide_gap >= right_gap >= -wide_gap:
            return True
        else:
            return False

    @staticmethod
    def regional_division(original_list):
        # 计算区域属性：区域ID
        regional_dic = {}
        regional_index = 0
        box_used = []
        index = 0
        # calculate regional id
        for box_dic in original_list:
            if box_dic["box"] in box_used:
                continue
            dic_used = [box_dic]
            if box_dic["regional_id"] is None:
                box_dic["regional_id"] = regional_index
            for dic in dic_used:
                BaseScreen.right_box_check(dic, regional_index, dic_used, original_list)
                BaseScreen.left_box_check(dic, regional_index, dic_used, original_list)
                BaseScreen.bottom_box_check(dic, regional_index, dic_used, original_list)
                BaseScreen.top_box_check(dic, regional_index, dic_used, original_list)
            for dic in dic_used:
                if dic["box"] not in box_used:
                    box_used.append(dic["box"])
            regional_index += 1
        # calculate regional box
        while index < regional_index:
            dic_list = list(filter(lambda item: item['regional_id'] == index, original_list))
            box_list = []
            for dic in dic_list:
                box = dic["box"]
                box_dic = {"00": box[0][0], "01": box[0][1], "10": box[1][0], "11": box[1][1],
                           "20": box[2][0], "21": box[2][1], "30": box[3][0], "31": box[3][1]}
                box_list.append(box_dic)
            if len(box_list) > 0:
                box_0 = [min(box_list, key=itemgetter('00')), min(box_list, key=itemgetter('01'))]
                box_1 = [max(box_list, key=itemgetter('10')), min(box_list, key=itemgetter('11'))]
                box_2 = [max(box_list, key=itemgetter('20')), max(box_list, key=itemgetter('21'))]
                box_3 = [min(box_list, key=itemgetter('30')), max(box_list, key=itemgetter('31'))]
                regional_box = [[box_0[0]["00"], box_0[1]["01"]],
                                [box_1[0]["10"], box_1[1]["11"]],
                                [box_2[0]["20"], box_2[1]["21"]],
                                [box_3[0]["30"], box_3[1]["31"]],
                                ]
                regional_dic[index] = regional_box
                BaseScreen.update_regional_box(original_list, index, regional_box)
            index += 1
        return regional_dic

    @staticmethod
    def update_regional_id(original_list, box, regional_index):
        for line in original_list:
            if line["box"] == box:
                line["regional_id"] = regional_index

    @staticmethod
    def update_regional_box(original_list, regional_id, regional_box):
        for line in original_list:
            if line["regional_id"] == regional_id:
                line["regional_box"] = regional_box

    @staticmethod
    def right_box_check(box_dic, regional_index, dic_used, original_list):
        right_box = box_dic["right_box"]
        right_used_box = []
        while right_box is not None and right_box not in right_used_box:
            right_used_box.append(right_box)
            BaseScreen.update_regional_id(original_list, right_box, regional_index)
            next_dic = list(filter(lambda item: item['box'] == right_box, original_list))
            right_box = next_dic[0]["right_box"]
            if next_dic[0] not in dic_used:
                dic_used.append(next_dic[0])

    @staticmethod
    def left_box_check(box_dic, regional_index, dic_used, original_list):
        left_box = box_dic["left_box"]
        left_used_box = []
        while left_box is not None and left_box not in left_used_box:
            left_used_box.append(left_box)
            BaseScreen.update_regional_id(original_list, left_box, regional_index)
            next_dic = list(filter(lambda item: item['box'] == left_box, original_list))
            left_box = next_dic[0]["left_box"]
            if next_dic[0] not in dic_used:
                dic_used.append(next_dic[0])

    @staticmethod
    def bottom_box_check(box_dic, regional_index, dic_used, original_list):
        bottom_box = box_dic["bottom_box"]
        bottom_used_box = []
        while bottom_box is not None and bottom_box not in bottom_used_box:
            bottom_used_box.append(bottom_box)
            BaseScreen.update_regional_id(original_list, bottom_box, regional_index)
            next_dic = list(filter(lambda item: item['box'] == bottom_box, original_list))
            bottom_box = next_dic[0]["bottom_box"]
            if next_dic[0] not in dic_used:
                dic_used.append(next_dic[0])

    @staticmethod
    def top_box_check(box_dic, regional_index, dic_used, original_list):
        top_box = box_dic["top_box"]
        top_used_box = []
        while top_box is not None and top_box not in top_used_box:
            top_used_box.append(top_box)
            BaseScreen.update_regional_id(original_list, top_box, regional_index)
            next_dic = list(filter(lambda item: item['box'] == top_box, original_list))
            top_box = next_dic[0]["top_box"]
            if next_dic[0] not in dic_used:
                dic_used.append(next_dic[0])
