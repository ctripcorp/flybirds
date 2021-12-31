# -*- coding: utf-8 -*-

import os
import subprocess
import traceback
import operator

from flybirds.utils import flybirds_log as log
from flybirds.report.fail_feature_create import rerun_launch
from flybirds.utils.pkg_helper import load_pkg_by_ns


class RunManage:
    """
    run cycle manage class
    """

    def __init__(self):
        pass

    before_run_processor = []
    after_run_processor = []

    @staticmethod
    def load_pkg():
        """
        load report ref
        """
        load_pkg_by_ns("flybirds.core.launch_cycle")
        load_pkg_by_ns("flybirds.report.gen")

    @staticmethod
    def process(processors_name, *args):
        """
        processor executor
        """
        processors = getattr(RunManage, processors_name)
        if processors is not None and len(processors) > 0:
            sort_key = operator.attrgetter("order")
            processors.sort(key=sort_key)
            for processor in processors:
                if hasattr(processor, "can"):
                    can_run = processor.can(*args)
                    if can_run is True:
                        processor.run(*args)
                else:
                    processor.run(*args)

    @staticmethod
    def run(context):
        """
        run logical contains : before ,exe ,after
        """
        RunManage.load_pkg()
        RunManage.process("before_run_processor", context)
        RunManage.exe(context)
        RunManage.process("after_run_processor", context)

    @staticmethod
    def exe(context):
        """
        start behave process and rerun fail case
        """
        no_args = context.get("no_args")
        if no_args is not None and no_args is False:

            # noinspection PyBroadException
            try:
                run_args = context.get("run_args")
                cmd_str = context.get("cmd_str")
                need_rerun_args = context.get("need_rerun_args")
                report_dir_path = context.get("report_dir_path")

                behave_process = subprocess.Popen(
                    cmd_str, cwd=os.getcwd(), shell=True, stdout=None
                )

                behave_process.wait()
                behave_process.communicate()

                # Determine whether the failed scenario needs to be re-run
                rerun_launch(need_rerun_args, report_dir_path, run_args)

            except Exception:
                log.error(
                    f"behave task execute error: {traceback.format_exc()}")
        else:
            log.info("cannot run non-args")

    @staticmethod
    def join(processors_name, processor, replace=0):
        """
        add processor
        """
        if processor is not None and processor.name is not None:
            processors = getattr(RunManage, processors_name)
            indx = -1
            for i, item in enumerate(processors):
                if item.name is not None and item.name == processor.name:
                    indx = i
                    break
            if replace == 0:
                if indx >= 0:
                    return indx
            elif indx >= 0:
                processors[indx] = processor
                return indx
            processors.append(processor)

            return indx
        return -1

    @staticmethod
    def insert(processors_name, processor, replace=0):
        """
        insert process
        """
        if processor is not None and processor.name is not None:
            processors = getattr(RunManage, processors_name)
            indx = -1
            for i, item in enumerate(processors):
                if item.name is not None and item.name == processor.name:
                    indx = i
                    break
            if replace == 0:
                if indx >= 0:
                    return indx
            elif indx >= 0:
                del processors[indx]
            processors.insert(0, processor)

            return indx
        return -1


def run_script(run_args):
    log.info(f"received run_args: {run_args}")
    try:
        r_context = {
            "run_args": run_args
        }
        RunManage.run(r_context)
    except Exception:
        log.error(f"behave task run error: {traceback.format_exc()}")
