# -*- coding: utf-8 -*-
"""
report gen
"""
import os
import subprocess

from flybirds.report.gen_factory import GenFactory
from flybirds.utils.flybirds_log import logger

STATIC_DIR = os.path.dirname(__file__)


class CucumberGen:
    """
    cucumber gen
    """
    name = "cucumber"

    @staticmethod
    def gen(report_path, platform):
        """
        report gen
        """

        report_js_path = os.path.dirname(STATIC_DIR)

        gen_path = os.path.join(report_js_path, "node_report",
                                "report.js")

        cmd_str = f'node "{gen_path}" {report_path} {report_path} {platform}'
        logger.info(f"report cmd:{cmd_str}")

        report_process = subprocess.Popen(
            cmd_str, cwd=os.getcwd(), shell=True, stdout=None
        )

        report_process.wait()
        report_process.communicate()


GenFactory.add(CucumberGen)
