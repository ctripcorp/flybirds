# -*- coding: utf-8 -*-
"""
parse json report
"""
import os
import re
import shutil
import traceback
from json import JSONDecodeError

from flybirds.utils import file_helper
from flybirds.utils import flybirds_log as log


def parse_json_data(report_dir, rerun_report_dir=None, is_parallel=False):
    """
    Parse the screenshot address in the behave json report,
    and use it when converting
    the follow-up cucumber json report into an html report
    """
    rerun_features = None
    not_aggregation = False

    if rerun_report_dir is not None:
        # get the array of all rerun json under the rerun_report_dir
        rerun_features = get_rerun_feature(rerun_report_dir, is_parallel)
        log.info(
            "parse_json_data move_rerun_screen, report_dir_path: "
            f"{report_dir}, rerun_report_dir_path: {rerun_report_dir}"
        )
        # move_rerun_screen(report_dir, rerun_report_dir)
        # copy_rerun_screen(report_dir, rerun_report_dir)

    if isinstance(rerun_features, list) and len(rerun_features) > 0:
        not_aggregation = True

    for file_item in os.listdir(report_dir):
        if re.search(r"\.json", str(file_item)) is not None:
            # noinspection PyBroadException
            try:
                file_path = os.path.join(report_dir, file_item)
                report_json = file_helper.get_json_from_file_path(file_path)
                if isinstance(report_json, list):
                    cur_json = []
                    cur_features = []
                    if not_aggregation:
                        report_json.extend(rerun_features)
                        not_aggregation = False
                    for feature in report_json:
                        parse_feature(feature, rerun_report_dir)
                        if (
                                isinstance(feature.get("elements"), list)
                                and len(feature.get("elements")) > 0
                        ):
                            if is_parallel and feature.get('metadata') is None:
                                browser_name = file_item.split('.')[1]
                                feature["metadata"] = [
                                    {"name": "Browser",
                                     "value": browser_name
                                     }
                                ]
                            cur_features.append(feature)
                    cur_json.extend(cur_features)

                    file_helper.store_json_to_file_path(
                        cur_json, file_path, "w"
                    )
            except JSONDecodeError:
                log.warn('[parse_json_data] has error: Invalid json.')
            except Exception:
                log.warn(
                    f"error processing image address in {file_item}",
                    traceback.format_exc(),
                )


def parse_feature(feature, rerun_report_dir):
    """
    parse feature: exclude the data with status=rerun
    """
    if isinstance(feature.get("elements"), list):
        cur_scenarios = []
        for scenario in feature.get("elements"):
            if scenario["type"] == "background":
                continue
            if scenario["status"] == "rerun":
                if rerun_report_dir is None:
                    scenario["status"] = "failed"
                else:
                    continue
            if isinstance(scenario.get("description"), list):
                desc_new_array = []
                for desc_item in scenario["description"]:
                    if desc_item is None:
                        continue
                    desc_item = desc_item.strip()
                    if desc_item == "initialization description_":
                        continue
                    elif desc_item.startswith("embeddingsTags, stepIndex="):
                        split_array = desc_item.split(",")
                        step_index = int(
                            split_array[1].strip().split("=", 1)[1].strip()
                        )
                        data = split_array[2].strip()
                        if (
                                isinstance(scenario["steps"], list)
                                and len(scenario["steps"]) > step_index
                        ):
                            images_dict = {
                                "mime_type": "text/html",
                                "data": data,
                            }
                            if (
                                    "embeddings"
                                    in scenario["steps"][step_index].keys()
                            ):
                                scenario["steps"][step_index][
                                    "embeddings"
                                ].append(images_dict)
                            else:
                                scenario["steps"][step_index]["embeddings"] = [
                                    images_dict
                                ]
                    else:
                        desc_new_array.append(desc_item)
                scenario["description"] = desc_new_array

            cur_scenarios.append(scenario)
        feature["elements"] = cur_scenarios


def get_rerun_feature(report_dir, is_parallel):
    """
    Get all the results of rerun after failure
    """
    if report_dir is None:
        return None
    result = []
    try:
        for file_item in os.listdir(report_dir):
            if re.search(r"\.json", str(file_item)) is not None:
                # noinspection PyBroadException
                try:
                    file_path = os.path.join(report_dir, file_item)
                    report_json = file_helper.get_json_from_file_path(
                        file_path
                    )
                    if isinstance(report_json, list):
                        for feature in report_json:
                            if is_parallel and feature.get('metadata') is None:
                                browser_name = file_item.split('.')[1]
                                feature["metadata"] = [
                                    {"name": "Browser",
                                     "value": browser_name
                                     }
                                ]
                    if isinstance(report_json, list) and len(report_json) > 0:
                        result.extend(report_json)
                except Exception:
                    log.warn(
                        f"summarize a single rerun feature: {file_item} error",
                        traceback.format_exc(),
                    )
    except Exception as e:
        log.warn(
            "An error occurred when re-run "
            f"the feature result: {str(e)}",
            traceback.format_exc(),
        )
    return result


def move_rerun_screen(report_dir, rerun_report_dir=None):
    """
    Some screenshots and other resources that failed after re-running
     are moved to the resources generated during
    the first formal operation, which is
    conducive to the integration of reports
    """
    try:
        if rerun_report_dir is None:
            return
        origin_screen_dir = os.path.join(report_dir, "screenshot")
        rerun_screen_dir = os.path.join(rerun_report_dir, "screenshot")
        if os.path.exists(rerun_screen_dir):
            if not os.path.exists(origin_screen_dir):
                file_helper.create_dirs(origin_screen_dir)
            for dir_item in os.listdir(rerun_screen_dir):
                shutil.move(
                    os.path.join(rerun_screen_dir, dir_item), origin_screen_dir
                )
    except Exception as e:
        log.warn(
            "An error occurred when copying the failed screenshot information"
            f" to the report screenshot directory: {str(e)}",
            traceback.format_exc(),
        )


def copy_rerun_screen(report_dir, rerun_report_dir=None):
    """
    copy rerun screen
    """
    origin_screen_dir = os.path.join(report_dir, "screenshot")
    rerun_screen_dir = os.path.join(rerun_report_dir, "screenshot")
    copy_file(rerun_screen_dir, origin_screen_dir)


def copy_file(source_dir, target_dir):
    """
    copy dir
    """
    for s_f in os.listdir(source_dir):
        source_f = os.path.join(source_dir, s_f)
        print("sourceF", source_f)
        target_f = os.path.join(target_dir, s_f)
        if os.path.isfile(source_f):
            shutil.copy(source_f, target_f)
            log.info(
                "Copy the failed screenshot to the report screenshot"
                f" directory: {source_f}"
            )
        if os.path.isdir(source_f):
            if os.path.exists(target_f):
                copy_file(source_f, target_f)
            else:
                os.mkdir(target_f)
                copy_file(source_f, target_f)
