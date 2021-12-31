# -*- coding: utf-8 -*-
"""
launch init such as run args init
"""
from flybirds.core.launch_cycle.run_manage import RunManage


class LaunchInit:
    """
    launch init
    """

    name = "LaunchInit"
    order = 15

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        """
        command set default value
        """
        option = {
            "cmd_str": None,
            "need_rerun_args": None,
            "report_dir_path": None,
            "is_html": None,
            "run_at": None,
            "no_args": None
        }
        if context is not None:
            context.update(option)
        else:
            context = option
        run_args = context["run_args"]
        if run_args is not None:
            context["cmd_str"] = run_args.get("cmd_str")
            context["need_rerun_args"] = run_args.get("need_rerun")
            context["report_dir_path"] = run_args.get("report_dir_path")
            context["no_args"] = False
            is_html = run_args.get("html")
            run_at = run_args.get("run_at")

            if is_html is not None and is_html is False:
                context["report_format"] = None
            else:
                context["report_format"] = "cucumber"
            if run_at is not None and run_at != "":
                context["run_at"] = run_at
            else:
                context["run_at"] = "local"


# add event to processor, launch init should be first one
RunManage.insert("before_run_processor", LaunchInit, 1)
