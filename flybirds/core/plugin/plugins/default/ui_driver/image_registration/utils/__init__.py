#! usr/bin/python
# -*- coding:utf-8 -*-
import math
import cv2
import numpy as np
from typing import Union


def generate_result(rect, confi):
    """Format the result: 定义图像识别结果格式."""
    ret = {
        'rect': rect,
        'confidence': confi,
    }
    return ret


def keypoint_distance(kp1, kp2):
    """求两个keypoint的两点之间距离"""
    if isinstance(kp1, cv2.KeyPoint):
        kp1 = kp1.pt
    elif isinstance(kp1, (list, tuple)):
        kp1 = kp1
    else:
        raise ValueError('kp1需要时keypoint或直接是坐标, kp1={}'.format(kp1))

    if isinstance(kp2, cv2.KeyPoint):
        kp2 = kp2.pt
    elif isinstance(kp2, (list, tuple)):
        kp2 = kp2
    else:
        raise ValueError('kp2需要时keypoint或直接是坐标, kp1={}'.format(kp2))

    x = kp1[0] - kp2[0]
    y = kp1[1] - kp2[1]
    return math.sqrt((x ** 2) + (y ** 2))


def keypoint_angle(kp1, kp2):
    """求两个keypoint的夹角 """
    k = [
        (kp1.angle - 180) if kp1.angle >= 180 else kp1.angle,
        (kp2.angle - 180) if kp2.angle >= 180 else kp2.angle
    ]
    if k[0] == k[1]:
        return 0
    else:
        return abs(k[0] - k[1])


def get_keypoint_from_matches(kp, matches, mode):
    res = []
    if mode == 'query':
        for match in matches:
            res.append(kp[match.queryIdx])
    elif mode == 'train':
        for match in matches:
            res.append(kp[match.trainIdx])

    return res


def keypoint_origin_angle(kp1, kp2):
    """
    以kp1为原点,计算kp2的旋转角度
    """
    origin_point = kp1.pt
    train_point = kp2.pt

    point = (abs(origin_point[0] - train_point[0]), abs(origin_point[1] - train_point[1]))

    x_quadrant = (1, 4)
    y_quadrant = (3, 4)
    if origin_point[0] > train_point[0]:
        x_quadrant = (2, 3)

    if origin_point[1] > train_point[1]:
        y_quadrant = (1, 2)
    point_quadrant = list(set(x_quadrant).intersection(set(y_quadrant)))[0]

    x, y = point[::-1]
    angle = math.degrees(math.atan2(x, y))
    if point_quadrant == 4:
        angle = angle
    elif point_quadrant == 3:
        angle = 180 - angle
    elif point_quadrant == 2:
        angle = 180 + angle
    elif point_quadrant == 1:
        angle = 360 - angle

    return angle


def _mapping_angle_distance(distance, origin_angle, angle):
    """

    Args:
        distance: 距离
        origin_angle: 对应原点的角度
        angle: 旋转角度

    """
    _angle = origin_angle + angle
    _y = distance * math.cos((math.pi * _angle) / 180)
    _x = distance * math.sin((math.pi * _angle) / 180)
    return round(_x, 3), round(_y, 3)


def rectangle_transform(point, size, mapping_point, mapping_size, angle):
    """
    根据point,找出mapping_point映射的矩形顶点坐标

    Args:
        point: 坐标在矩形中的坐标
        size: 矩形的大小(h, w)
        mapping_point: 映射矩形的坐标
        mapping_size: 映射矩形的大小(h, w)
        angle: 旋转角度

    Returns:

    """
    h, w = size[0], size[1]
    _h, _w = mapping_size[0], mapping_size[1]

    h_scale = _h / h
    w_scale = _w / w

    tl = keypoint_distance((0, 0), point)  # 左上
    tr = keypoint_distance((w, 0), point)  # 右上
    bl = keypoint_distance((0, h), point)  # 左下
    br = keypoint_distance((w, h), point)  # 右下

    # x = np.float32([point[1], point[1], (h - point[1]), (h - point[1])])
    # y = np.float32([point[0], (w - point[0]), point[0], (w - point[0])])
    # A, B, C, D = cv2.phase(x, y, angleInDegrees=True)
    A = math.degrees(math.atan2(point[0], point[1]))
    B = math.degrees(math.atan2((w - point[0]), point[1]))
    C = math.degrees(math.atan2(point[0], (h - point[1])))
    D = math.degrees(math.atan2((w - point[0]), (h - point[1])))

    new_tl = _mapping_angle_distance(tl, A, angle=angle)
    new_tl = (-new_tl[0] * w_scale, -new_tl[1] * h_scale)
    new_tl = (mapping_point[0] + new_tl[0], mapping_point[1] + new_tl[1])

    new_tr = _mapping_angle_distance(tr, B, angle=angle)
    new_tr = (new_tr[0] * w_scale, -new_tr[1] * h_scale)
    new_tr = (mapping_point[0] + new_tr[0], mapping_point[1] + new_tr[1])

    new_bl = _mapping_angle_distance(bl, C, angle=angle)
    new_bl = (-new_bl[0] * w_scale, new_bl[1] * h_scale)
    new_bl = (mapping_point[0] + new_bl[0], mapping_point[1] + new_bl[1])

    new_br = _mapping_angle_distance(br, D, angle=angle)
    new_br = (new_br[0] * w_scale, new_br[1] * h_scale)
    new_br = (mapping_point[0] + new_br[0], mapping_point[1] + new_br[1])

    return [new_tl, new_tr, new_bl, new_br]
