# -*- coding: utf-8 -*-
"""
test_fail_feature_create unit test
"""
from unittest import TestCase
from unittest import main

from flybird.report import fail_feature_create


class FailFeatureCreateTest(TestCase):
    """
    FailFeatureCreate  test
    """

    def test_create_rerun(self):
        report_dir = r'report\c08beb92-7ccd-4af5-9297-71958f37db45'
        rerun_dir = r'report\c08beb92-7ccd-4af5-9297-71958f37db45'
        run_count = 1
        max_fail_count = 1.0
        result = fail_feature_create.create_rerun(report_dir, rerun_dir,
                                                  run_count,
                                                  max_fail_count)

        self.assertEqual(result, False)


if __name__ == "__main__":
    main()
