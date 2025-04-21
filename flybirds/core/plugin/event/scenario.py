# -*- coding: utf-8 -*-
"""
when behave run scenario will trigger this
"""
import os
import traceback
from urllib.parse import urlparse

import flybirds.core.global_resource as gr
import flybirds.utils.language_helper as lge
from flybirds.core.driver import screen
from flybirds.core.global_context import GlobalContext
from flybirds.core.plugin.plugins.default.screen_record import link_record
from flybirds.core.plugin.plugins.default.screen import BaseScreen
from flybirds.utils import flybirds_log as log
from flybirds.utils import launch_helper


def scenario_init(context, scenario):
    """
    init description and screen record
    """
    # initialize the description
    # the information added to the description will
    # take effect in this scenario
    log.info('[scenario_init] start!')
    GlobalContext.set_global_cache("verifyStepCount", 0)
    gr.set_value("mock_request_match_list", [])
    gr.set_value("current_page_dialog_action", None)
    scenario.description.append("initialization description_")
    gr.set_value('network_cache_map', {})
    gr.set_value("operate_record", {})
    # Initialize the sequence of steps to be executed
    # which is required for subsequent associated screenshots
    context.cur_step_index = 0
    # Whether to start recording screen
    # it is convenient to have screen recording information
    # associated in the report when it fails
    context.scenario_screen_record = False
    # Restart the app before running
    launch_helper.app_start("before_run_page")
    if gr.get_flow_behave_value("fail_screen_record", True):
        no_screen_record_step = True
        for step in scenario.all_steps:
            if step.name.strip().startswith(
                    lge.parse_glb_str(
                        "start record",
                        scenario.feature.language
                    )
            ) or step.name.strip().startswith(
                lge.parse_glb_str("stop record", scenario.feature.language)
            ):
                no_screen_record_step = False
                break
        if no_screen_record_step:
            try:
                screen_record = gr.get_value("screenRecord")
                if hasattr(screen_record, 'start_record'):
                    timeout = gr.get_flow_behave_value(
                        "scenario_screen_record_time", 120
                    )
                    screen_record.start_record(timeout)
                context.scenario_screen_record = True
            except Exception as scenario_error:
                log.error(
                    f"Running scene: An error occurred when starting to "
                    f"record the screen before {scenario.name}"
                    f", error: {str(scenario_error)}"
                )


def scenario_fail(context, scenario):
    """
    scenario fail handler
    """
    log.info(
        f"[scenario_fail] feature:{scenario.feature.name}, "
        f"scenario:{scenario.name} failed to run"
    )
    need_copy_record = 0
    gr.set_value("scenario_status", False)
    # the scene fails to output a log and take a screenshot
    for step in scenario.all_steps:
        if step.name.strip().startswith(
                lge.parse_glb_str("start record", scenario.feature.language)
        ) or (GlobalContext.get_global_cache("started_record") is not None and GlobalContext.get_global_cache(
            "started_record") is True):
            need_copy_record += 1
        elif step.name.strip().startswith(
                lge.parse_glb_str("stop record", scenario.feature.language)
        ):
            need_copy_record -= 1
        if step.status == "failed":
            info_log = f"[scenario_fail] step:{step.name}"
            log.info(info_log)
            log.error(f'[scenario_fail] step error msg:{step.error_message}')
            log.info("[scenario_fail] start to do failed screenshot")
            img_path = screen.screen_link_to_behave(
                scenario, context.cur_step_index - 1, "fail_"
            )
            try:
                white_percent = BaseScreen.white_screen_detect(img_path)
                data = ("<h4 style=\"color:DodgerBlue;\">failed screenshot analysis completed：{}% is white screen</h4>"
                        .format(white_percent))
                scenario.description.append(data)
                log.debug(f"[scenario_fail] screenshot white screen percent is {white_percent}")
            except:
                log.info(f"white screen detect fail")
            break

    on_scenario_fail = launch_helper.get_hook_file(
        "on_scenario_fail"
    )
    if on_scenario_fail is not None:
        on_scenario_fail(context, scenario)
    # save screen recording
    cur_platform = GlobalContext.platform
    if cur_platform.lower() == "web":
        try:
            GlobalContext.step.clear_all_request_body(context)
            GlobalContext.step.clear_all_request_mock(context)
            GlobalContext.step.remove_web_mock(context)
            GlobalContext.step.clear_all_request_record(context)
        except:
            log.info("failed to remove mock and cache")

    if need_copy_record >= 1 or context.scenario_screen_record \
            or cur_platform.strip().lower() == "web":
        screen_record = gr.get_value("screenRecord")
        screen_record.stop_record()
        link_record(scenario, context.cur_step_index - 1)

    # the processing of the current page after the scene fails
    launch_helper.app_start("scenario_fail_page")
    scenario_screen_record_str = str(context.scenario_screen_record)
    log.info(
        f"scenario_fail, need_copy_record: {str(need_copy_record)},"
        f" context.scenario_screen_record: {scenario_screen_record_str}"
    )


def scenario_success(context, scenario):
    """
    scenario success handler
    """
    # adjustment of the currently displayed page after the scene is successful
    log.info('[scenario_success] start!')
    on_scenario_success = launch_helper.get_hook_file(
        "on_scenario_success"
    )
    gr.set_value("scenario_status", True)
    if on_scenario_success is not None:
        on_scenario_success(context, scenario)
    if context.scenario_screen_record:
        screen_record = gr.get_value("screenRecord")
        screen_record.stop_record()

    cur_platform = GlobalContext.platform
    if cur_platform.lower() == "web":
        try:
            GlobalContext.step.clear_all_request_body(context)
            GlobalContext.step.clear_all_request_mock(context)
            GlobalContext.step.remove_web_mock(context)
            GlobalContext.step.clear_all_request_record(context)
        except:
            log.info("failed to remove mock and cache")
    launch_helper.app_start("scenario_success_page")


class OnBefore:  # pylint: disable=too-few-public-methods
    """
    before run scenario will trigger this
    """

    name = "OnBefore"
    order = 5

    @staticmethod
    def can(context, scenario):
        return True

    @staticmethod
    def run(context, scenario):
        """
        write run info into description,it will be used at reporter
        """
        try:
            log.info('[scenario_OnBefore] start!')
            f_name = scenario.feature.name
            log.info(
                f"running feature:{f_name}, scenario:{scenario.name},"
                f" location: {scenario.feature.location}"
            )
            scenario_init(context, scenario)
            data = launch_helper.get_runtime_data(scenario)
            scenario.description.append(data)

        except Exception:
            traceback.print_exc()

        # hook extend by tester
        before_scenario_extend = launch_helper.get_hook_file(
            "before_scenario_extend"
        )
        if before_scenario_extend is not None:
            before_scenario_extend(context, scenario)


def check_url_in_white_list(context, url):
    """
    check if url in white list
    """
    white_list = [".js", ".css", ".html", ".htm", ".png", ".jpg", ".avi"]
    try:
        if white_list.index(url.lower().strip()) >= 0:
            return True
    except:
        return False
    return False


def format_error(context, scenario, formatter):
    try:
        if scenario.status == "failed" and GlobalContext.get_global_cache("stepErrorInfo") is not None:
            formatter.current_feature_element["stepErrorInfo"] = GlobalContext.get_global_cache(
                "stepErrorInfo")
            if gr.get_value("mock_request_match_list") is not None and len(
                    gr.get_value("mock_request_match_list")) > 0:
                formatter.current_feature_element["stepErrorInfo"]["missedMockRequest"] = []
                for test_url in gr.get_value("mock_request_match_list"):
                    test_url_parse = urlparse(test_url)
                    file_path = test_url_parse.path
                    file_name = os.path.basename(test_url_parse.path)
                    _, file_suffix = os.path.splitext(file_name)
                    if check_url_in_white_list(context, file_suffix):
                        continue
                    formatter.current_feature_element["stepErrorInfo"]["missedMockRequest"].append(test_url)
            request_mock_key_value_list = GlobalContext.get_global_cache("request_mock_key_value")
            request_mock_request_key_value_list = GlobalContext.get_global_cache(
                "request_mock_request_key_value")
            formatter.current_feature_element["stepErrorInfo"]["missedMockStep"] = []
            if request_mock_key_value_list is not None and len(request_mock_key_value_list) > 0:
                for request_mock_key_value in request_mock_key_value_list:
                    if request_mock_key_value is not None and request_mock_key_value.get(
                            "max") is not None and \
                            request_mock_key_value["max"] > 0:
                        formatter.current_feature_element["stepErrorInfo"]["missedMockStep"].append(
                            request_mock_key_value.get("mockStep"))
            if request_mock_request_key_value_list is not None and len(
                    request_mock_request_key_value_list) > 0:
                for request_mock_request_key_value in request_mock_request_key_value_list:
                    if request_mock_request_key_value is not None and request_mock_request_key_value.get(
                            "max") is not None and request_mock_request_key_value["max"] > 0:
                        formatter.current_feature_element["stepErrorInfo"]["missedMockStep"].append(
                            request_mock_request_key_value.get("mockStep"))
    except:
        log.info("failed to format error")


class OnAfter:  # pylint: disable=too-few-public-methods
    """
    scenario after event
    """

    name = "OnAfter"
    order = 100

    @staticmethod
    def can(context, scenario):
        return True

    @staticmethod
    def run(context, scenario):
        """
        exe scenario after
        """
        try:
            if context._runner is not None and context._runner.formatters is not None and len(
                    context._runner.formatters) > 0:
                formatter = context._runner.formatters[0]
                if formatter is not None and formatter.current_feature_element is not None:
                    formatter.current_feature_element["verifyCount"] = GlobalContext.get_global_cache("verifyStepCount")
                    format_error(context, scenario, formatter)
            if scenario.status != "failed":
                scenario_success(context, scenario)

            cur_platform = GlobalContext.platform
            if cur_platform.strip().lower() == "web":
                log.info('[web_scenario_OnAfter] reset page、ele、screenRecord')
                gr.set_value("plugin_page", None)
                gr.set_value("screenRecord", None)
                gr.set_value("plugin_ele", None)
        except Exception:
            traceback.print_exc()

        # if there is a hook custom behavior, call the related function
        after_scenario_extend = launch_helper.get_hook_file(
            "after_scenario_extend"
        )
        if after_scenario_extend is not None:
            after_scenario_extend(context, scenario)
        try:
            GlobalContext.set_global_cache("current_record_path", None)
        except:
            pass


class AfterScenarioFailScreenShoot:
    """
    scenario after event
    """

    name = "AfterScenarioFail"
    order = 0

    @staticmethod
    def can(context, scenario):
        if scenario.status == "failed":
            return True
        return False

    @staticmethod
    def run(context, scenario):
        """
        exe scenario after
        """
        try:
            log.info('[scenario_OnAfter] start!')
            if scenario.status == "failed":
                scenario_fail(context, scenario)
        except Exception as e:
            traceback.print_exc()
            log.info(f"failed to run scenario after, error: {str(e)}")


class OnAfterClean:
    name = "OnAfterClean"
    order = 10000

    @staticmethod
    def can(context, scenario):
        return True

    @staticmethod
    def run(context, scenario):
        """
        exe scenario after
        """
        try:
            GlobalContext.set_global_cache("stepErrorInfo", None)
            GlobalContext.set_global_cache("flybirds_page_info", None)
            GlobalContext.set_global_cache("stepErrorInfo", None)
            gr.set_value("mock_request_match_list", None)
            GlobalContext.set_global_cache("started_record", None)
        except:
            pass


# add scenario event to global processor
var = GlobalContext.join("before_scenario_processor", OnBefore, 1)
var1 = GlobalContext.join("after_scenario_processor", OnAfter, 1)
var3 = GlobalContext.join("after_scenario_processor", OnAfterClean, 1)
var4 = GlobalContext.join("after_scenario_processor", AfterScenarioFailScreenShoot, 1)
