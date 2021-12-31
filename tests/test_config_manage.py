# -*- coding: utf-8 -*-
"""
config_manage unit test
"""
from unittest import TestCase
from unittest import main

from flybirds.core.config_manage import FrameConfig, ConfigManage


class FrameConfigTest(TestCase):
    """
    FrameConfig init test
    """

    def test_frame_info(self):
        user_data = {}
        frame_info = FrameConfig(user_data, None)
        self.assertEqual(frame_info.page_render_timeout, 65)

    def test_config_manage(self):
        user_data = {}
        config_manage = ConfigManage(user_data)
        self.assertEqual(config_manage.frame_info.wait_ele_timeout, 15)
        self.assertEqual(config_manage.flow_behave.max_fail_rerun_count, 1.0)
        self.assertEqual(config_manage.flow_behave.scenario_fail_page,
                         "restartApp")


if __name__ == "__main__":
    main()
