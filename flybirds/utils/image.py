import os
import platform
import cv2
import numpy as np
import paddle
from PIL import Image, ImageDraw, ImageFont
import math


def get_output_tensors(args, mode, predictor):
    output_names = predictor.get_output_names()
    output_tensors = []
    if mode == "rec" and args.rec_algorithm in ["CRNN", "SVTR_LCNet"]:
        output_name = 'softmax_0.tmp_0'
        if output_name in output_names:
            return [predictor.get_output_handle(output_name)]
        else:
            for output_name in output_names:
                output_tensor = predictor.get_output_handle(output_name)
                output_tensors.append(output_tensor)
    else:
        for output_name in output_names:
            output_tensor = predictor.get_output_handle(output_name)
            output_tensors.append(output_tensor)
    return output_tensors


def get_infer_gpuid():
    sysstr = platform.system()
    if sysstr == "Windows":
        return 0

    if not paddle.fluid.core.is_compiled_with_rocm():
        cmd = "env | grep CUDA_VISIBLE_DEVICES"
    else:
        cmd = "env | grep HIP_VISIBLE_DEVICES"
    env_cuda = os.popen(cmd).readlines()
    if len(env_cuda) == 0:
        return 0
    else:
        gpu_id = env_cuda[0].strip().split("=")[1]
        return int(gpu_id[0])


def draw_e2e_res(dt_boxes, strs, img_path):
    src_im = cv2.imread(img_path)
    for box, str in zip(dt_boxes, strs):
        box = box.astype(np.int32).reshape((-1, 1, 2))
        cv2.polylines(src_im, [box], True, color=(255, 255, 0), thickness=2)
        cv2.putText(
            src_im,
            str,
            org=(int(box[0, 0, 0]), int(box[0, 0, 1])),
            fontFace=cv2.FONT_HERSHEY_COMPLEX,
            fontScale=0.7,
            color=(0, 255, 0),
            thickness=1)
    return src_im


def draw_text_det_res(dt_boxes, img):
    for box in dt_boxes:
        box = np.array(box).astype(np.int32).reshape(-1, 2)
        cv2.polylines(img, [box], True, color=(255, 255, 0), thickness=2)
    return img


def resize_img(img, input_size=600):
    """
    resize img and limit the longest side of the image to input_size
    """
    img = np.array(img)
    im_shape = img.shape
    im_size_max = np.max(im_shape[0:2])
    im_scale = float(input_size) / float(im_size_max)
    img = cv2.resize(img, None, None, fx=im_scale, fy=im_scale)
    return img


def draw_ocr(image,
             boxes,
             txts=None,
             scores=None,
             drop_score=0.5,
             font_path="./doc/fonts/simfang.ttf"):
    """
    Visualize the results of OCR detection and recognition
    args:
        image(Image|array): RGB image
        boxes(list): boxes with shape(N, 4, 2)
        txts(list): the texts
        scores(list): txxs corresponding scores
        drop_score(float): only scores greater than drop_threshold will be visualized
        font_path: the path of font which is used to draw text
    return(array):
        the visualized img
    """
    if scores is None:
        scores = [1] * len(boxes)
    box_num = len(boxes)
    for i in range(box_num):
        if scores is not None and (scores[i] < drop_score or
                                   math.isnan(scores[i])):
            continue
        box = np.reshape(np.array(boxes[i]), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
    if txts is not None:
        img = np.array(resize_img(image, input_size=1920))
        txt_img = text_visual(
            txts,
            scores,
            img_h=img.shape[0],
            img_w=1080,
            threshold=drop_score,
            font_path=font_path)
        img = np.concatenate([np.array(img), np.array(txt_img)], axis=1)
        return img
    return image


def create_font(txt, sz, font_path="./doc/fonts/simfang.ttf"):
    font_size = int(sz[1] * 0.99)
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    length = font.getsize(txt)[0]
    if length > sz[0]:
        font_size = int(font_size * sz[0] / length)
        font = ImageFont.truetype(font_path, font_size, encoding="utf-8")
    return font


def str_count(s):
    """
    Count the number of Chinese characters,
    a single English character and a single number
    equal to half the length of Chinese characters.
    args:
        s(string): the input of string
    return(int):
        the number of Chinese characters
    """
    import string
    count_zh = count_pu = 0
    s_len = len(s)
    en_dg_count = 0
    for c in s:
        if c in string.ascii_letters or c.isdigit() or c.isspace():
            en_dg_count += 1
        elif c.isalpha():
            count_zh += 1
        else:
            count_pu += 1
    return s_len - math.ceil(en_dg_count / 2)


def text_visual(texts,
                scores,
                img_h=400,
                img_w=600,
                threshold=0.,
                font_path="./doc/simfang.ttf"):
    """
    create new blank img and draw txt on it
    args:
        texts(list): the text will be draw
        scores(list|None): corresponding score of each txt
        img_h(int): the height of blank img
        img_w(int): the width of blank img
        font_path: the path of font which is used to draw text
    return(array):
    """
    if scores is not None:
        assert len(texts) == len(
            scores), "The number of txts and corresponding scores must match"

    def create_blank_img():
        blank_img = np.ones(shape=[img_h, img_w], dtype=np.int8) * 255
        blank_img[:, img_w - 1:] = 0
        blank_img = Image.fromarray(blank_img).convert("RGB")
        draw_txt = ImageDraw.Draw(blank_img)
        return blank_img, draw_txt

    blank_img, draw_txt = create_blank_img()

    font_size = 40
    txt_color = (0, 0, 0)
    font = ImageFont.truetype(font_path, font_size, encoding="utf-8")

    gap = font_size + 5
    txt_img_list = []
    count, index = 1, 0
    for idx, txt in enumerate(texts):

        if scores[idx] < threshold or math.isnan(scores[idx]):
            index -= 1
            continue
        first_line = True
        while str_count(txt) >= img_w // font_size - 4:
            tmp = txt
            txt = tmp[:img_w // font_size - 4]
            if first_line:
                new_txt = str(index) + ': ' + txt
                first_line = False
            else:
                new_txt = '    ' + txt
            draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
            txt = tmp[img_w // font_size - 4:]
            if count >= img_h // gap - 1:
                txt_img_list.append(np.array(blank_img))
                blank_img, draw_txt = create_blank_img()
                count = 0
            count += 1
        if first_line:
            new_txt = str(index) + ': ' + txt
        else:
            new_txt = "  " + txt
        draw_txt.text((0, gap * count), new_txt, txt_color, font=font)
        # whether add new blank img or not
        if count >= img_h // gap - 1 and idx + 1 < len(texts):
            txt_img_list.append(np.array(blank_img))
            blank_img, draw_txt = create_blank_img()
            count = 0
        count += 1
        index += 1
    txt_img_list.append(np.array(blank_img))
    if len(txt_img_list) == 1:
        blank_img = np.array(txt_img_list[0])
    else:
        blank_img = np.concatenate(txt_img_list, axis=1)
    return np.array(blank_img)


def base64_to_cv2(b64str):
    import base64
    data = base64.b64decode(b64str.encode('utf8'))
    data = np.frombuffer(data, np.uint8)
    data = cv2.imdecode(data, cv2.IMREAD_COLOR)
    return data


def draw_boxes(image, boxes, scores=None, drop_score=0.5):
    if scores is None:
        scores = [1] * len(boxes)
    for (box, score) in zip(boxes, scores):
        if score < drop_score:
            continue
        box = np.reshape(np.array(box), [-1, 1, 2]).astype(np.int64)
        image = cv2.polylines(np.array(image), [box], True, (255, 0, 0), 2)
    return image


def get_rotate_crop_image(img, points):
    '''
    img_height, img_width = img.shape[0:2]
    left = int(np.min(points[:, 0]))
    right = int(np.max(points[:, 0]))
    top = int(np.min(points[:, 1]))
    bottom = int(np.max(points[:, 1]))
    img_crop = img[top:bottom, left:right, :].copy()
    points[:, 0] = points[:, 0] - left
    points[:, 1] = points[:, 1] - top
    '''
    assert len(points) == 4, "shape of points must be 4*2"
    img_crop_width = int(
        max(
            np.linalg.norm(points[0] - points[1]),
            np.linalg.norm(points[2] - points[3])))
    img_crop_height = int(
        max(
            np.linalg.norm(points[0] - points[3]),
            np.linalg.norm(points[1] - points[2])))
    pts_std = np.float32([[0, 0], [img_crop_width, 0],
                          [img_crop_width, img_crop_height],
                          [0, img_crop_height]])
    M = cv2.getPerspectiveTransform(points, pts_std)
    dst_img = cv2.warpPerspective(
        img,
        M, (img_crop_width, img_crop_height),
        borderMode=cv2.BORDER_REPLICATE,
        flags=cv2.INTER_CUBIC)
    dst_img_height, dst_img_width = dst_img.shape[0:2]
    if dst_img_height * 1.0 / dst_img_width >= 1.5:
        dst_img = np.rot90(dst_img)
    return dst_img


def get_minarea_rect_crop(img, points):
    bounding_box = cv2.minAreaRect(np.array(points).astype(np.int32))
    points = sorted(list(cv2.boxPoints(bounding_box)), key=lambda x: x[0])

    index_a, index_b, index_c, index_d = 0, 1, 2, 3
    if points[1][1] > points[0][1]:
        index_a = 0
        index_d = 1
    else:
        index_a = 1
        index_d = 0
    if points[3][1] > points[2][1]:
        index_b = 2
        index_c = 3
    else:
        index_b = 3
        index_c = 2

    box = [points[index_a], points[index_b], points[index_c], points[index_d]]
    crop_img = get_rotate_crop_image(img, np.array(box))
    return crop_img


def check_gpu(use_gpu):
    if use_gpu and not paddle.is_compiled_with_cuda():
        use_gpu = False
    return use_gpu

