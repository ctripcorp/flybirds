# -*- coding: utf-8 -*-
"""
 point_helper unit test
"""
from unittest import TestCase
from unittest import main

from flybirds.utils import point_helper


class PointHelperTest(TestCase):
    """
    PointHelper  test
    """

    def test_search_direction_switch(self):
        direct = '上'
        direction = point_helper.search_direction_switch(direct)
        self.assertEqual(direction, '下')


if __name__ == "__main__":
    main()
