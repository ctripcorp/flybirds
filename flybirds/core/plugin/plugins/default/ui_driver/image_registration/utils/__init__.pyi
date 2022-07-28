# from __future__ import annotations
from baseImage import Rect
from typing import Union, TypedDict, List, Tuple
import cv2


class ResultType(TypedDict):
    rect: Rect
    confidence: Union[int, float]
point_type = Tuple[Union[float, int], Union[float, int]]
keypoint_type = Union[cv2.KeyPoint, List[float, float], Tuple[float, float]]


def generate_result(rect: Rect, confi: Union[float, int]) -> ResultType: ...

def keypoint_distance(kp1: keypoint_type, kp2: keypoint_type) -> float: ...

def keypoint_angle(kp1: cv2.KeyPoint, kp2: cv2.KeyPoint) -> float:  ...

def get_keypoint_from_matches(kp: Tuple[cv2.KeyPoint, ...], matches: List[cv2.DMatch, ...], mode: str) -> List[cv2.KeyPoint]: ...

def keypoint_origin_angle(kp1: cv2.KeyPoint, kp2: cv2.KeyPoint) -> Union[int, float]:  ...

def _mapping_angle_distance(distance: float, origin_angle: Union[int, float], angle: Union[int, float]) -> Tuple[float, float]: ...

def rectangle_transform(point: point_type, size: point_type, mapping_point: point_type, mapping_size: point_type, angle: Union[float, int])\
        -> Tuple[point_type, point_type, point_type, point_type]: ...