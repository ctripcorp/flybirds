# -*- coding: utf-8 -*-
"""
report generate
"""
import traceback

from flybirds.core.launch_cycle.run_manage import RunManage
from flybirds.utils.flybirds_log import logger
from flybirds.report.gen_factory import GenFactory


class OnGenerate:
    """
    generate event class
    """

    name = "OnGenerate"
    order = 200

    @staticmethod
    def can(context):
        """
        only local need gen report
        """
        run_at = context.get("run_at")
        if run_at is not None and run_at != "local":
            logger.info("not run at local,skip generate html report")
            return False
        else:
            return True
        report_path = context["report_dir_path"]
        gen_type = context["report_format"]
        if report_path is not None and report_path != "" and gen_type is \
                not None and gen_type != "":
            return True
        else:
            logger.info("skip generate html report maybe no report path "
                        "or no report generate type")
            return False

    @staticmethod
    def run(context):
        """
        generate logical
        """
        try:
            report_path = context["report_dir_path"]
            gen_type = context["report_format"]
            GenFactory.gen(gen_type, report_path)
        except Exception:
            logger.error(
                f"report task execute error: {traceback.format_exc()}")


# add event to processor
RunManage.join("after_run_processor", OnGenerate, 1)
