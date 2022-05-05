# -*- coding: utf-8 -*-
import base64
import json
import os

import flybirds.utils.file_helper as file_helper
import flybirds.utils.flybirds_log as log


def get_rerun_params(
        run_count, rerun_feature_path, max_retry_count, report_dir_path,
        run_args
):
    if run_args is not None:
        use_define = run_args.get("use_define")
        env_config = run_args.get("env_config")
        report_format = run_args.get("report_format")

        rerun_report_path = "{}{}rerun{}{}result{}report.json".format(
            report_dir_path,
            os.sep,
            run_count,
            os.sep,
            os.sep,
        )
        #   create and clear report path
        rerun_report_dir_path = rerun_report_path[
                                0: rerun_report_path.rfind(os.sep)
                                ]
        file_helper.create_dirs(rerun_report_dir_path)
        file_helper.clear_dirs(rerun_report_dir_path)
        rerun_report_path = "-o {}".format(rerun_report_path)
        log.info("reruned case report path: {}".format(rerun_report_path))

        rerun_cmd_array = [
            "behave",
            rerun_feature_path,
            report_format,
            rerun_report_path,
        ]

        # create and clear screenshot path
        rerun_screen_shot_dir = "{}{}screenshot".format(
            rerun_report_dir_path, os.sep
        )
        file_helper.create_dirs(rerun_screen_shot_dir)
        file_helper.clear_dirs(rerun_screen_shot_dir)
        rerun_user_data_screen_dir = "screenShotDir={}".format(
            str(
                base64.b64encode(rerun_screen_shot_dir.encode("utf-8")),
                "utf-8",
            )
        )
        screen_data_index = -1
        for use_data_index in range(len(use_define)):
            if use_define[use_data_index].startswith("screenShotDir="):
                screen_data_index = use_data_index
                break
        if screen_data_index != -1:
            use_define[screen_data_index] = rerun_user_data_screen_dir
        else:
            use_define.extend(
                [
                    "--define",
                    rerun_user_data_screen_dir,
                ]
            )
        log.info(
            "reruned case screenshot path: {}".format(rerun_screen_shot_dir)
        )

        is_rerun = "flybirdsAutoRerun={}".format(
            str(
                base64.b64encode("Yes".encode("utf-8")),
                "utf-8",
            )
        )
        run_path_array = []
        if run_count > 1:
            for item_count in range(1, run_count + 1):
                run_path_array.append(
                    str(
                        os.path.join(
                            report_dir_path,
                            "rerun" + str(item_count),
                            "fail_relevance.json",
                        )
                    )
                )
            re_run_info = "flybirdsAutoRerunInfo={}".format(
                str(
                    base64.b64encode(",".join(run_path_array).encode("utf-8")),
                    "utf-8",
                )
            )
        else:
            re_run_info = "flybirdsAutoRerunInfo={}".format(
                str(
                    base64.b64encode(
                        str(
                            os.path.join(
                                report_dir_path,
                                "rerun" + str(run_count),
                                "fail_relevance.json",
                            )
                        ).encode("utf-8")
                    ),
                    "utf-8",
                )
            )
        use_define.extend(["--define", is_rerun])
        use_define.extend(["--define", re_run_info])
        rerun_cmd_array.extend(
            [
                "--define maxRetryCount={}".format(
                    str(
                        base64.b64encode(str(max_retry_count).encode("utf-8")),
                        "utf-8",
                    )
                )
            ]
        )
        if len(use_define) > 0:
            rerun_cmd_array.extend(use_define)
        if not (env_config is None):
            rerun_cmd_array.extend(
                [
                    "--define es={}".format(
                        str(
                            base64.b64encode(
                                json.dumps(env_config).encode("utf-8")
                            ).decode("utf-8")
                        )
                    )
                ]
            )

        rerun_cmd_array.append(
            "--no-color --no-capture --no-capture-stderr --no-skipped"
        )
        rerun_cmd_str = " ".join(rerun_cmd_array)
        log.info("rerun behave execute: {}".format(rerun_cmd_str))
        return {
            "rerun_cmd_str": rerun_cmd_str,
            "rerun_report_dir_path": rerun_report_dir_path,
        }
    else:
        return None
