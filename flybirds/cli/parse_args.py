# -*- coding: utf-8 -*-
"""
process args
"""
import base64
import json
import os

import flybirds.utils.flybirds_log as log
import flybirds.utils.uuid_helper as uuid_helper
from flybirds.core.tag_expression import TagExpression
from flybirds.utils import file_helper


def default_report_path():
    """
    Generate the default report directory
    """
    report_path = "report{}{}{}report.json".format(
        os.sep, uuid_helper.create_uuid(), os.sep
    )
    return report_path


def parse_args(
        feature_path, tag, report_format, report_path, define, rerun, es,
        to_html, run_at
):
    """
    process args
    :return:
    """
    log.info(
        f"flybirds cmd info: {feature_path} {tag} {report_format} {report_path}"
        f" {define} {rerun} {es} {to_html} {run_at}"
    )
    use_define = []
    tags = []
    need_rerun = False

    # process define
    if define:
        for define_item in define:
            use_define.append("--define")
            use_item_array = define_item.strip().split("=", 1)
            use_item_key = use_item_array[0]
            use_item_value = use_item_array[1]
            use_item = "{}={}".format(
                use_item_key,
                str(
                    base64.b64encode(use_item_value.encode("utf-8")),
                    "utf-8",
                ),
            )
            use_define.append(use_item)

    # process rerun
    if rerun:
        need_rerun = rerun

    # create and clear report path
    report_dir_path = report_path[0: report_path.rfind(os.sep)]
    file_helper.create_dirs(report_dir_path)
    file_helper.clear_dirs(report_dir_path)
    report_path = "-o {}".format(report_path)
    log.info("report path: {}".format(report_path))

    # args cmd_array
    cmd_array = ["behave", feature_path, report_format, report_path]

    # process es
    if not (es is None):
        cmd_array.extend(
            [
                "--define es={}".format(
                    str(
                        base64.b64encode(
                            json.dumps(es).encode("utf-8")
                        ).decode("utf-8")
                    )
                )
            ]
        )

    # process tag
    if not (tag is None):
        # tag deal
        tags.append(tag)
        temp_tags = TagExpression(tags)
        tag_array = str(temp_tags).split(" ")
        behave_tag_array = ["--tags={}".format(item) for item in tag_array]
        cmd_array.extend(behave_tag_array)

    # create and clear screenshot ptah
    screen_shot_dir = "{}{}screenshot".format(report_dir_path, os.sep)
    file_helper.create_dirs(screen_shot_dir)
    file_helper.clear_dirs(screen_shot_dir)
    user_data_screen_dir = "screenShotDir={}".format(
        str(base64.b64encode(screen_shot_dir.encode("utf-8")), "utf-8")
    )

    use_define.extend(["--define", user_data_screen_dir])
    log.info("screenshot path: {}".format(screen_shot_dir))

    if run_at is None:
        run_at = 'local'
    run_at_base = str(base64.b64encode(run_at.encode('utf-8')), 'utf-8')
    use_define.extend(["--define", f"run_at={run_at_base}"])

    if len(use_define) > 0:
        cmd_array.extend(use_define)

    cmd_array.append(
        "--no-color --no-capture --no-capture-stderr --no-skipped"
    )
    cmd_str = " ".join(cmd_array)
    log.info("the assembled behave execution command: {}".format(cmd_str))
    return {
        "cmd_str": cmd_str,
        "need_rerun": need_rerun,
        "report_dir_path": report_dir_path,
        "use_define": use_define,
        "env_config": es,
        "report_format": report_format,
        "html": to_html,
        "run_at": run_at
    }
