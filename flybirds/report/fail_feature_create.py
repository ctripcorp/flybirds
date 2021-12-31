# -*- coding: utf-8 -*-
"""
fail scenario create rerun
"""
import json
import os
import re
import shutil
import subprocess

from flybirds.core.config_manage import FlowBehave
from flybirds.report import json_format_deal
from flybirds.report.rerun_params import get_rerun_params
from flybirds.utils import file_helper
from flybirds.utils import flybirds_log as log
from flybirds.utils import language_helper as lge
from flybirds.utils import uuid_helper


class FailScenarioSum:
    """
    Information on all failed scenarios
    """

    def __init__(self):
        self.fail_scenarios = {}

    def add_scenario(self, feature_name, scenario_name, description):
        """
        Add the failure scenario to the current failure set, the key is the
        only one
        """
        scenario_key = str(uuid_helper.create_uuid())
        while scenario_key in list(self.fail_scenarios):
            log.info(
                "When adding a failure scenario, the generated uuid is "
                "duplicated！"
            )
            scenario_key = str(uuid_helper.create_uuid())
        scenario_value = FailScenarioInfo(
            feature_name, scenario_name, description
        )
        self.fail_scenarios[scenario_key] = json.dumps(scenario_value.__dict__)
        return scenario_key

    def serialize_to_file(self, rerun_root_dir):
        """
        Serialize all the information associated with the failure scenario
        and save it in a file
        """
        file_helper.store_json_to_file_path(
            self.fail_scenarios,
            os.path.join(rerun_root_dir, "fail_relevance.json"),
            "w+",
        )


class FailScenarioInfo:
    """
    Some information about the failure scenario, which can be associated with
    the failure information in the report when re-run
    """

    def __init__(self, feature_name, scenario_name, description):
        self.feature_name = feature_name
        self.scenario_name = scenario_name
        if not isinstance(description, list):
            self.description = []
        else:
            self.description = description


def rerun_launch(need_rerun_args, report_dir_path, run_args):
    """
    start to rerun
    """
    # Determine whether the failed scenario needs to be re-run
    flow_behave_config = FlowBehave({}, None)
    rerun_report_dir_path = None
    # rerun_feature_path_array = []
    max_fail_rerun_count = flow_behave_config.max_fail_rerun_count

    if not need_rerun_args:
        need_rerun = flow_behave_config.fail_rerun
    else:
        need_rerun = need_rerun_args
    if need_rerun:
        max_retry_count = flow_behave_config.max_retry_count
        run_count = 1
        rerun_dir_path = report_dir_path
        count_satisfy = create_rerun(
            report_dir_path,
            rerun_dir_path,
            run_count,
            max_fail_rerun_count,
        )
        # The number of failures is not higher than the limited value and
        # needs to be re-run
        if count_satisfy:
            while max_retry_count > 0:
                log.info(
                    (
                        f"Number of failed retries{run_count}, start to "
                        f"generate feature files that failed to rerun, "
                        f"report root directory{report_dir_path}"
                    )
                )
                rerun_dir_path = report_dir_path
                try:
                    if run_count > 1:
                        count_satisfy = create_rerun(
                            rerun_report_dir_path,
                            rerun_dir_path,
                            run_count,
                            max_fail_rerun_count,
                        )
                    rerun_feature_path = (
                        f"{report_dir_path}{os.sep}rerun" f"{run_count}"
                    )
                    # rerun_feature_path_array.append(rerun_feature_path)
                    log.info(
                        f"count_satisfy: {count_satisfy}, max_retry_count: "
                        f"{max_retry_count}, run_count: {run_count}"
                    )
                    if count_satisfy:
                        rerun_params = get_rerun_params(
                            run_count,
                            rerun_feature_path,
                            max_retry_count,
                            report_dir_path,
                            run_args,
                        )
                        rerun_cmd_str = rerun_params.get("rerun_cmd_str")
                        rerun_report_dir_path = rerun_params.get(
                            "rerun_report_dir_path"
                        )
                        if rerun_cmd_str is not None:
                            rerun_behave_process = subprocess.Popen(
                                rerun_cmd_str,
                                cwd=os.getcwd(),
                                shell=True,
                                stdout=None,
                            )
                            rerun_behave_process.wait()
                            rerun_behave_process.communicate()
                            # Re-run of the failed scenario ends
                            # Number of reruns -1, actual number of runs +1
                            max_retry_count = max_retry_count - 1
                            run_count = run_count + 1
                            # Failed to rerun result move
                            log.info(
                                f"move_rerun_screen, report_dir_path: "
                                f"{report_dir_path}, rerun_report_dir_path:"
                                f" {rerun_report_dir_path}"
                            )
                            json_format_deal.copy_rerun_screen(
                                report_dir_path, rerun_report_dir_path
                            )
                        else:
                            log.info(
                                "Failure to re-run parameters not obtained"
                            )
                            break
                    else:
                        log.info(
                            f"Number of failed retry runs: {run_count}, "
                            f"do you need to rerun the task:{count_satisfy}, "
                            "failed retry task is not executed"
                        )
                        break
                except Exception as e:
                    log.error(f"behave failed retry error: {e}")
                    break
        else:
            log.info(
                f"Do you need to rerun the task: {count_satisfy}, the failed "
                f"retry task was not executed"
            )
        log.info(
            f"Start processing the json report under the directory "
            f"{report_dir_path}"
        )
    # if rerun_report_dir_path is not None:
    json_format_deal.parse_json_data(report_dir_path, rerun_report_dir_path)


def create_rerun(report_dir, rerun_dir, run_count, max_fail_count=1.0):
    """
    Feature to re-run after creation failure
    Some information after failure (such as screenshots) falls into the file
    , and this information is
    associated in the next run
    """
    result = True
    sum_count = 0
    fail_count = 0

    rerun_root_dir = f"{rerun_dir}{os.sep}rerun{run_count}"
    if not file_helper.create_dirs(rerun_root_dir):
        file_helper.clear_dirs(rerun_root_dir)

    fail_scenario_static = FailScenarioSum()

    rerun_feature_index = run_count
    exist_scenario_name = []

    # Second level file index
    # rerun_feature_second_index = 1

    sum_count, fail_count, fail_scenario_static, rerun_root_dir = \
        process_loop_block(report_dir, rerun_feature_index, sum_count,
                           fail_count,
                           exist_scenario_name, fail_scenario_static,
                           run_count,
                           rerun_root_dir)
    if sum_count <= 0 or fail_count <= 0:
        log.info(
            "Feature sum_count rerun after creation"
            " failure <= 0 or fail_count <= 0",
            sum_count <= 0 or fail_count <= 0,
        )
        result = False
    elif (
        isinstance(max_fail_count, float)
        and (fail_count / sum_count) > max_fail_count
    ):
        log.info(
            "Feature to rerun after creation failure "
            "(fail_count / sum_count)> max_fail_count",
            (fail_count / sum_count) > max_fail_count,
        )
        result = False
    elif isinstance(max_fail_count, int) and fail_count > max_fail_count:
        log.info(
            "Feature fail_count> max_fail_count to"
            " rerun after creation failure",
            fail_count > max_fail_count,
        )
        result = False

    fail_scenario_static.serialize_to_file(rerun_root_dir)
    copy_behave_need_file(rerun_root_dir)
    return result


def process_loop_block(report_dir, rerun_feature_index, sum_count, fail_count,
                       exist_scenario_name, fail_scenario_static, run_count,
                       rerun_root_dir):
    for file_item in os.listdir(report_dir):
        if re.search(r"\.json", str(file_item)) is not None:
            # noinspection PyBroadException
            try:
                file_path = os.path.join(report_dir, file_item)
                report_json = file_helper.get_json_from_file_path(file_path)
                if isinstance(report_json, list):
                    for feature in report_json:
                        cur_feature_array = get_init_feature_array(
                            rerun_feature_index, feature.get("language")
                        )
                        rerun_feature_location = feature["location"]
                        rerun_match_obj = re.match(
                            r"(.*\/)*([^.]+).feature", rerun_feature_location
                        )

                        # Because the path of the failed file should be
                        # displayed in the report,
                        # the failure case is named using the original feature,
                        # not integrated into one file

                        rerun_feature_name = (
                            f"flybirdsARFeature" f"{rerun_feature_index}"
                        )
                        if rerun_match_obj is not None:
                            rerun_feature_name = rerun_match_obj.group(2)
                        log.info(f"rerun_feature_name: {rerun_feature_name}")
                        if isinstance(feature.get("elements", None), list):
                            for scenario in feature["elements"]:
                                if scenario["type"] == "background":
                                    continue
                                sum_count += 1
                                if scenario["status"] == "failed":
                                    fail_count += 1
                                    if isinstance(scenario["tags"], list):
                                        cur_tags = ""
                                        for tag_item in scenario["tags"]:
                                            cur_tags += f" @{tag_item}"
                                        cur_feature_array.append(
                                            f" {cur_tags}\n"
                                        )
                                    rerun_scenario_name = scenario["name"]
                                    while (
                                            rerun_scenario_name
                                            in exist_scenario_name
                                    ):
                                        rerun_scenario_name += str(range(9))
                                    exist_scenario_name.append(
                                        rerun_scenario_name
                                    )
                                    log.info(
                                        "exist_scenario_name: "
                                        f"{str(exist_scenario_name)}"
                                    )
                                    f_language = feature.get("language")
                                    scenario_key = lge.parse_keyword(
                                        "scenario", f_language
                                    )

                                    cur_feature_array.append(
                                        f"  {scenario_key}: "
                                        f"{rerun_scenario_name}\n"
                                    )

                                    relevance_key = (
                                        fail_scenario_static.add_scenario(
                                            feature["name"],
                                            scenario["name"],
                                            scenario["description"],
                                        )
                                    )
                                    if relevance_key:
                                        g_step_name = lge.parse_glb_str(
                                            "information association of failed"
                                            " operation",
                                            feature.get("language"),
                                        )
                                        then_key = lge.parse_keyword(
                                            "then", feature.get("language")
                                        )
                                        f_d = f"{then_key} {g_step_name}\n"
                                        l_f_d = f_d.format(
                                            run_count, relevance_key
                                        )
                                        cur_feature_array.append(l_f_d)

                                    if isinstance(scenario["steps"], list):
                                        for step in scenario["steps"]:
                                            keyword = step["keyword"]
                                            name = step["name"]
                                            cur_feature_array.append(
                                                f"    {keyword} {name}\n"
                                            )
                                    cur_feature_array.append("\n")
                                    scenario["status"] = "rerun"
                                    print(
                                        "rerun_feature_name",
                                        rerun_feature_name,
                                        "cur_feature_array",
                                        cur_feature_array,
                                    )
                                    file_helper.array_to_file(
                                        os.path.join(
                                            rerun_root_dir,
                                            f"{rerun_feature_name}.feature",
                                        ),
                                        cur_feature_array,
                                    )

                    file_helper.store_json_to_file_path(
                        report_json, file_path, "w"
                    )
            except Exception as e:
                raise Exception(
                    f"{file_item} Parsing is an error, innerError: {str(e)}"
                ) from e

    return sum_count, fail_count, fail_scenario_static, rerun_root_dir


def get_init_feature_array(index, language):
    """
    generate failed info
    """

    feature_des = []
    feature_des.append(f"# language: {language}\n\n")
    f_l = lge.parse_keyword("feature", language)
    r_f = lge.parse_glb_str("rerun failed scenario", language)
    feature_des.append(f"{f_l}:{r_f}{index}\n\n")

    return feature_des


def copy_behave_need_file(rerun_root_dir):
    """
    copy step.py and environment.py and other behave files to feature path
    """
    file_helper.create_dirs(os.path.join(rerun_root_dir, "steps"))
    file_helper.clear_dirs(os.path.join(rerun_root_dir, "steps"))
    shutil.copy(
        os.path.join(os.getcwd(), "features", "steps", "steps.py"),
        os.path.join(rerun_root_dir, "steps", "steps.py"),
    )
    shutil.copy(
        os.path.join(os.getcwd(), "features", "environment.py"),
        os.path.join(rerun_root_dir, "environment.py"),
    )
    shutil.copy(
        os.path.join(os.getcwd(), "features", "__init__.py"),
        os.path.join(rerun_root_dir, "__init__.py"),
    )


def set_rerun_info(user_data, gr):
    """
    set rerun info
    """
    last_fail_scenario_info_obj = {}
    # get rerun info, add into report
    if (
        "flybirdsAutoRerun" in user_data.keys()
        and user_data["flybirdsAutoRerun"] == "Yes"
    ):
        log.info("this is rerun case execute")
        rerun_info_array = user_data["flybirdsAutoRerunInfo"].split(",")
        if len(rerun_info_array) > 0:
            for item_rerun_info in rerun_info_array:
                rerun_info = item_rerun_info.strip()
                print("rerun_info", rerun_info)
                if (
                    "flybirdsAutoRerunInfo" in user_data.keys()
                    and os.path.exists(rerun_info)
                ):
                    try:
                        last_fail_scenario_info = (
                            file_helper.get_json_from_file(rerun_info)
                        )
                        last_fail_scenario_info_obj = dict(
                            last_fail_scenario_info_obj,
                            **last_fail_scenario_info,
                        )
                    except Exception as e:
                        log.info(
                            f"rerun case get exception info "
                            f"failed。innerError: {str(e)}"
                        )
            gr.set_value("rerunFailInfo", last_fail_scenario_info_obj)

    log.info(f"user data，count:{len(user_data)}")
