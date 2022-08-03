#! usr/bin/python
# -*- coding:utf-8 -*-
import math
import cv2


def generate_result(rect, confi):
    """Format the result: Define the image recognition result format."""
    ret = {
        'rect': rect,
        'confidence': confi,
    }
    return ret


def keypoint_distance(kp1, kp2):
    """Find the distance between two keypoints"""
    if isinstance(kp1, cv2.KeyPoint):
        kp1 = kp1.pt
    elif isinstance(kp1, (list, tuple)):
        kp1 = kp1
    else:
        raise ValueError('When kp1 needs keypoint or direct coordinates, kp1={}'.format(kp1))

    if isinstance(kp2, cv2.KeyPoint):
        kp2 = kp2.pt
    elif isinstance(kp2, (list, tuple)):
        kp2 = kp2
    else:
        raise ValueError('When kp2 needs keypoint or direct coordinates, kp1={}'.format(kp2))

    x = kp1[0] - kp2[0]
    y = kp1[1] - kp2[1]
    return math.sqrt((x ** 2) + (y ** 2))


def get_keypoint_from_matches(kp, matches, mode):
    res = []
    if mode == 'query':
        for match in matches:
            res.append(kp[match.queryIdx])
    elif mode == 'train':
        for match in matches:
            res.append(kp[match.trainIdx])

    return res


def _mapping_angle_distance(distance, origin_angle, angle):
    """

    Args:
        distance: distance
        origin_angle: The angle corresponding to the origin
        angle: Rotation angle

    """
    _angle = origin_angle + angle
    _y = distance * math.cos((math.pi * _angle) / 180)
    _x = distance * math.sin((math.pi * _angle) / 180)
    return round(_x, 3), round(_y, 3)


def rectangle_transform(point, size, mapping_point, mapping_size, angle):
    """
    According to the point, find the rectangle vertex coordinates mapped by mapping_point

    Args:
         point: the coordinates of the coordinates in the rectangle
         size: the size of the rectangle (h, w)
         mapping_point: the coordinates of the mapping rectangle
         mapping_size: the size of the mapping rectangle (h, w)
         angle: rotation angle

    Returns:

    """
    h, w = size[0], size[1]
    _h, _w = mapping_size[0], mapping_size[1]

    h_scale = _h / h
    w_scale = _w / w

    tl = keypoint_distance((0, 0), point)  # upper left
    tr = keypoint_distance((w, 0), point)  # top right
    bl = keypoint_distance((0, h), point)  # lower left
    br = keypoint_distance((w, h), point)  # lower right

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
