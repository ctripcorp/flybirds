# -*- coding: utf-8 -*-

"""
config management all config should load by this module
"""
import json
import os

from flybirds.utils import file_helper
from flybirds.utils import flybirds_log as log
from flybirds.utils.dsl_helper import return_value, str2bool
from flybirds.utils.file_helper import read_json_data


class ConfigManage:
    """
    Manage all configuration information
    """

    def __init__(self, user_data):
        self.run_config = RunConfig(user_data)
        log.info(
            "run_config", str(self.run_config.__dict__)
        )

        self.log_config = LogConfig(user_data, None)
        log.info(
            "Logging configuration information", str(self.log_config.__dict__)
        )
        self.app_info = AppConfig(user_data, None)
        log.info("APP configuration information", str(self.app_info.__dict__))
        self.device_info = DeviceConfig(user_data, None)
        log.info(
            "Device configuration information", str(self.device_info.__dict__)
        )
        if self.device_info is not None \
                and self.device_info.platform.lower() == "web":
            self.web_info = WebConfig(user_data, None)
            log.info(
                "Web configuration information", str(self.web_info.__dict__)
            )

        self.frame_info = FrameConfig(user_data, None)
        log.info(
            "Frame parameter configuration information",
            str(self.frame_info.__dict__),
        )
        self.schema_info = SchemaUrl()
        self.report_info = ReportConfig(user_data, None)
        log.info(
            "Test report configuration information",
            str(self.report_info.__dict__),
        )
        self.flow_behave = FlowBehave(user_data, None)
        log.info(
            "Process control configuration information",
            str(self.flow_behave.__dict__),
        )
        self.ele_locator_info = EleLocator()
        self.ignore_node_info = IgnoreNodeConfig()
        self.paddle_fix_info = PaddleFixConfig()
        log.info(
            "Process paddle fix configuration information",
            str(self.paddle_fix_info.__dict__),
        )


def get_config(config, name):
    """
    load flybirds config
    """
    if config is None:
        path = os.path.join(os.getcwd(), "config", "flybirds_config.json")
        if os.path.exists(path):
            c_f = file_helper.get_json_from_file(path)
            if c_f.__contains__(name):
                return c_f.get(name)
        else:
            raise Exception(f"not find path: {path}")
    elif config.__contains__(name):
        return config.get(name)

    return None


class AppConfig:
    """
    Read configuration information about the test app

    Attributes:
        package_name: the packageName of the app on the android system
        unique_tag: the unique identifier of the app in the business system
    """

    def __init__(self, user_data, config=None):
        app_config = get_config(config, "app_info")
        if app_config is None:
            path = os.path.join(os.getcwd(), "config", "app_info.json")
            if os.path.exists(path):
                app_config = file_helper.get_json_from_file(path)

        if app_config is not None:
            self.package_name = user_data.get(
                "packageName", app_config["packageName"]
            )
            self.unique_tag = user_data.get(
                "uniqueTag", app_config.get("uniqueTag", None)
            )
            self.default_user = user_data.get(
                "defaultUser", app_config.get("defaultUser", None)
            )
            self.default_password = user_data.get(
                "defaultPassword", app_config.get("defaultPassword", None)
            )
            self.user_group = user_data.get(
                "userGroup", app_config.get("userGroup", 1)
            )

            self.package_path = user_data.get(
                "packagePath", app_config.get("packagePath", None)
            )

            self.overwrite_installation = user_data.get(
                "overwriteInstallation",
                app_config.get("overwriteInstallation", None)
            )

            self.ocr_lang = user_data.get(
                "ocrLang",
                app_config.get("ocrLang", "ch")
            )

            self.run_id = user_data.get("runId", None)
            self.build_id = user_data.get("buildId", None)
            self.pkg_version = user_data.get("pkgVersion", None)


class AppEnvConfig:
    """
    Manage all configuration information
    """

    def __init__(self, user_data, config=None):
        self.log_config = LogConfig(user_data, config)
        log.info(
            "Logging configuration information", str(self.log_config.__dict__)
        )
        self.env_config = user_data.get("es", None)


class DeviceConfig:
    """
    Read configuration information about the test device (mobile phone)

    Attributes:
        device_id: the unique identifier of the phone
    """

    def __init__(self, user_data, config):
        device_info = get_config(config, "device_info")
        if device_info is None:
            path = os.path.join(os.getcwd(), "config", "device_config.json")
            if os.path.exists(path):
                device_info = file_helper.get_json_from_file(path)

        if device_info is not None:
            self.device_id = user_data.get("deviceId", device_info["deviceId"])
            platform = "android"
            device_driver = None
            if device_info.__contains__("platform"):
                platform = device_info["platform"]
            if device_info.__contains__("webDriverAgent"):
                device_driver = device_info["webDriverAgent"]

            self.platform = user_data.get("platform", platform).lower()
            self.web_driver_agent = device_driver
            self.screen_size = None


class WebConfig:
    """
    Read configuration information about the web test
    """

    def __init__(self, user_data, config):
        web_info = get_config(config, "web_info")
        # default value
        headless = True
        browser_type = 'chromium'
        request_interception = True
        ignore_order = False
        abort_domain_list = []

        if user_data is None and web_info is None:
            log.warn('[web_info] configuration of web_info is none.')
            self.headless = headless
            self.browser_type = browser_type
            self.request_interception = request_interception
            self.ignore_order = ignore_order
            self.abort_domain_list = abort_domain_list
            return

        if web_info.get("headless") is not None:
            headless = web_info.get("headless")
        if web_info.get("browserType") is not None:
            browser_type = web_info.get("browserType")
        if web_info.get("requestInterception") is not None:
            request_interception = web_info.get("requestInterception")
        if web_info.get("ignoreOrder") is not None:
            ignore_order = web_info.get("ignoreOrder")
        if web_info.get("abortDomainList") is not None:
            abort_domain_list = web_info.get("abortDomainList")
        if web_info.get("browserExitAfterCase") is not None:
            self.browserExit = web_info.get("browserExitAfterCase", True)
        if web_info.get("emulatedDevice") is not None:
            self.emulated_device = web_info.get("emulatedDevice", None)

        if web_info.get("userAgent") is not None:
            self.user_agent = web_info.get("userAgent", None)
        if web_info.get("locale") is not None:
            self.locale = web_info.get("locale", None)

        if web_info.get("timezone") is not None:
            self.timezone = web_info.get("timezone", None)

        if web_info.get("permissions") is not None:
            self.permissions = web_info.get("permissions", None)

        if web_info.get("geolocation") is not None:
            self.geolocation = web_info.get("geolocation", None)

        if web_info.get("width") is not None:
            self.width = web_info.get("width", None)

        if web_info.get("height") is not None:
            self.height = web_info.get("height", None)

        if web_info.get("deviceScaleFactor") is not None:
            self.device_scale_factor = web_info.get("deviceScaleFactor", None)

        if web_info.get("hasTouch") is not None:
            self.has_touch = web_info.get("has_touch", None)

        if web_info.get("defaultBrowserType") is not None:
            self.default_browser_type = web_info.get("defaultBrowserType", None)

        headless = user_data.get("headless", headless)
        if isinstance(headless, str):
            headless = str2bool(headless)
        self.headless = headless
        self.browser_type = user_data.get("browserType", browser_type)
        self.request_interception = user_data.get("requestInterception",
                                                  request_interception)
        self.ignore_order = user_data.get("ignoreOrder", ignore_order)
        self.abort_domain_list = user_data.get("abortDomainList",
                                               abort_domain_list)


class FlowBehave:
    """
    Read some function switches
    """

    def __init__(self, user_data, config):
        flow_config = get_config(config, "flow_behave")
        if flow_config is None:
            path = os.path.join(os.getcwd(), "config", "flow_behave.json")
            if os.path.exists(path):
                flow_config = file_helper.get_json_from_file(path)

        if flow_config is not None:
            self.before_run_page = user_data.get(
                "beforeRunPage",
                return_value(flow_config.get("beforeRunPage", "restartApp"),
                             "restartApp")
            )
            self.scenario_fail_page = user_data.get(
                "scenarioFailPage",
                return_value(flow_config.get("scenarioFailPage", "restartApp"),
                             "restartApp")
            )
            self.scenario_success_page = user_data.get(
                "scenarioSuccessPage",
                return_value(
                    flow_config.get("scenarioSuccessPage", "backupPage"),
                    "backupPage")
            )
            self.before_run_login = user_data.get(
                "beforeRunLogin",
                return_value(flow_config.get("beforeRunLogin", False), False)
            )
            self.fail_screen_record = user_data.get(
                "failScreenRecord",
                return_value(flow_config.get("failScreenRecord", False), False)
            )
            self.scenario_screen_record_time = user_data.get(
                "scenarioScreenRecordTime",
                return_value(flow_config.get("scenarioScreenRecordTime", 120),
                             120)
            )

            self.fail_rerun = return_value(flow_config.get("failRerun", False),
                                           False)
            self.max_fail_rerun_count = return_value(flow_config.get(
                "maxFailRerunCount", 1.0), 1.0)

            # Maximum number of retries
            self.max_retry_count = user_data.get(
                "maxRetryCount",
                return_value(flow_config.get("maxRetryCount", 1), 1)
            )
        if not hasattr(self, "before_run_page"):
            self.before_run_page = user_data.get("beforeRunPage", "restartApp")
        if not hasattr(self, "scenario_fail_page"):
            self.scenario_fail_page = user_data.get(
                "scenarioFailPage", "restartApp"
            )
        if not hasattr(self, "scenario_success_page"):
            self.scenario_success_page = user_data.get(
                "scenarioSuccessPage", "backupPage"
            )
        if not hasattr(self, "before_run_login"):
            self.before_run_login = user_data.get("beforeRunLogin", False)
        if not hasattr(self, "fail_screen_record"):
            self.fail_screen_record = user_data.get("failScreenRecord", False)
        if not hasattr(self, "scenario_screen_record_time"):
            self.scenario_screen_record_time = user_data.get(
                "scenarioScreenRecordTime", 120
            )

        if not hasattr(self, "fail_rerun"):
            self.fail_rerun = False
        if not hasattr(self, "max_fail_rerun_count"):
            self.max_fail_rerun_count = 1.0
        if not hasattr(self, "max_retry_count"):
            self.max_retry_count = 1


class FrameConfig:
    """
    Read some configurations used by the UI framework
    """

    def __init__(self, user_data, config):
        frame_config = get_config(config, "frame_info")
        if frame_config is None:
            path = os.path.join(os.getcwd(), "config", "frame_info.json")
            if os.path.exists(path):
                frame_config = file_helper.get_json_from_file(path)
        if frame_config is not None:
            self.wait_ele_timeout = user_data.get(
                "waitEleTimeout",
                return_value(frame_config.get("waitEleTimeout", 10), 10)
            )
            self.wait_ele_disappear = user_data.get(
                "waitEleDisappear",
                return_value(frame_config.get("waitEleDisappear", 10), 10)
            )
            self.click_verify_timeout = user_data.get(
                "clickVerifyTimeout",
                return_value(frame_config.get("clickVerifyTimeout", 10), 10)
            )
            self.use_swipe_duration = user_data.get(
                "useSwipeDuration",
                return_value(frame_config.get("useSwipeDuration", False),
                             False)
            )
            self.swipe_duration = user_data.get(
                "swipeDuration",
                return_value(frame_config.get("swipeDuration", 1), 1)
            )
            self.use_poco_input = user_data.get(
                "usePocoInput",
                return_value(frame_config.get("usePocoInput", False), False)
            )
            self.after_input_wait = user_data.get(
                "afterInputWait",
                return_value(frame_config.get("afterInputWait", 1), 1)
            )
            self.use_search_swipe_duration = user_data.get(
                "useSearchSwipeDuration",
                return_value(frame_config.get("useSearchSwipeDuration", False),
                             False)
            )
            self.search_swipe_duration = user_data.get(
                "searchSwipeDuration",
                return_value(frame_config.get("searchSwipeDuration", 1), 1)
            )
            self.swipe_search_count = user_data.get(
                "swipeSearchCount",
                return_value(frame_config.get("swipeSearchCount", 5), 5)
            )
            self.swipe_search_distance = user_data.get(
                "swipeSearchDistance",
                return_value(frame_config.get("swipeSearchDistance", 0.3), 0.3)
            )
            self.page_render_timeout = user_data.get(
                "pageRenderTimeout",
                return_value(frame_config.get("pageRenderTimeout", 30), 30)
            )
            self.app_start_time = user_data.get(
                "appStartTime",
                return_value(frame_config.get("appStartTime", 6), 6)
            )
            self.swipe_ready_time = user_data.get(
                "swipeReadyTime",
                return_value(frame_config.get("swipeReadyTime", 3), 3)
            )
            self.verify_pos_not_change_count = user_data.get(
                "verifyPosNotChangeCount",
                return_value(frame_config.get("verifyPosNotChangeCount", 5), 5)
            )
            self.screen_record_time = user_data.get(
                "screenRecordTime",
                return_value(frame_config.get("screenRecordTime", 60), 60)
            )
            # Snapshot method
            self.use_snap = user_data.get(
                "useSnap",
                return_value(frame_config.get("useSnap", False), False)
            )
            # Whether to use airtest record
            self.use_airtest_record = user_data.get(
                "useAirtestRecord",
                return_value(frame_config.get("useAirtestRecord", False),
                             False)
            )
            self.ocr_det_limit_type = user_data.get(
                "ocr_det_limit_type",
                return_value(frame_config.get("ocr_det_limit_type", "max"), "max")
            )
            self.ocr_det_limit_side_len = user_data.get(
                "ocr_det_limit_side_len",
                return_value(frame_config.get("ocr_det_limit_side_len", 960), 960)
            )
        self.set_frame_info_attrs(user_data)
        self.set_other_attrs(user_data)

    def set_frame_info_attrs(self, user_data):
        if not hasattr(self, "wait_ele_timeout"):
            self.wait_ele_timeout = user_data.get("waitEleTimeout", 10)
        if not hasattr(self, "wait_ele_disappear"):
            self.wait_ele_disappear = user_data.get("waitEleDisappear", 10)
        if not hasattr(self, "click_verify_timeout"):
            self.click_verify_timeout = user_data.get("clickVerifyTimeout", 10)
        if not hasattr(self, "use_swipe_duration"):
            self.use_swipe_duration = user_data.get("useSwipeDuration", False)
        if not hasattr(self, "swipe_duration"):
            self.swipe_duration = user_data.get("swipeDuration", 1)
        if not hasattr(self, "use_poco_input"):
            self.use_poco_input = user_data.get("usePocoInput", False)
        if not hasattr(self, "after_input_wait"):
            self.after_input_wait = user_data.get("afterInputWait", 1)
        if not hasattr(self, "use_search_swipe_duration"):
            self.use_search_swipe_duration = user_data.get(
                "useSearchSwipeDuration", False
            )

    def set_other_attrs(self, user_data):
        if not hasattr(self, "search_swipe_duration"):
            self.search_swipe_duration = user_data.get(
                "searchSwipeDuration", 1
            )
        if not hasattr(self, "swipe_search_count"):
            self.swipe_search_count = user_data.get("swipeSearchCount", 5)
        if not hasattr(self, "swipe_search_distance"):
            self.swipe_search_distance = user_data.get(
                "swipeSearchDistance", 0.3
            )
        if not hasattr(self, "page_render_timeout"):
            self.page_render_timeout = user_data.get("pageRenderTimeout", 30)
        if not hasattr(self, "app_start_time"):
            self.app_start_time = user_data.get("appStartTime", 6)
        if not hasattr(self, "swipe_ready_time"):
            self.swipe_ready_time = None
        if not hasattr(self, "verify_pos_not_change_count"):
            self.verify_pos_not_change_count = user_data.get(
                "verifyPosNotChangeCount", 6
            )
        if not hasattr(self, "screen_record_time"):
            self.screen_record_time = user_data.get("screenRecordTime", 60)
        if not hasattr(self, "use_snap"):
            self.use_snap = user_data.get("useSnap", False)
        if not hasattr(self, "use_airtest_record"):
            self.use_airtest_record = user_data.get("useAirtestRecord", False)


class LogConfig:
    """
    Read the related configuration of the log
    """

    def __init__(self, user_data, config):
        log_config = get_config(config, "log")
        if log_config is None:
            path = os.path.join(os.getcwd(), "config", "log_config.json")
            if os.path.exists(path):
                log_config = file_helper.get_json_from_file(path)

        if log_config is not None:
            self.level = user_data.get(
                "logLevel",
                return_value(log_config.get("logLevel", "info"), "info")
            )

        if (not hasattr(self, "level")) or (not isinstance(self.level, str)):
            self.level = user_data.get("logLevel", "info")


class ReportConfig:
    """
    Some configurations of the report
    """

    def __init__(self, user_data, config):
        report_config = get_config(config, "report")
        if report_config is None:
            path = os.path.join(os.getcwd(), "config", "report_config.json")
            if os.path.exists(path):
                report_config = file_helper.get_json_from_file(path)
        if report_config is not None:
            self.screen_shot_dir = user_data.get(
                "screenShotDir", report_config.get("screenShotDir", None)
            )

        if not hasattr(self, "screen_shot_dir"):
            self.screen_shot_dir = user_data.get("screenShotDir", None)


class SchemaUrl:
    """
    All schema urls used
    """

    def __init__(self):
        schema_url_path = os.path.join(
            os.getcwd(), "config", "schema_url.json"
        )
        if os.path.exists(schema_url_path):
            self.all_schema_url = file_helper.get_json_from_file(
                schema_url_path
            )
        else:
            log.warn(
                f"[SchemaUrl] cannot find path: {schema_url_path}")


class PluginConfig:
    """
    plugin config
    """

    def __init__(self, user_data):
        path = os.path.join(os.getcwd(), "config", "plugin_info.json")
        if os.path.exists(path):
            plugin_info = file_helper.get_json_from_file(path)
            self.plugin_info = plugin_info
        else:
            self.plugin_info = {"active": "default", "default": {}}


class RunConfig:
    """
    run base info
    """

    def __init__(self, user_data):
        is_rerun = user_data.get("flybirdsAutoRerun", None)
        if is_rerun is not None and is_rerun.lower() == "yes":
            self.is_rerun = True
        else:
            self.is_rerun = False

        run_at = user_data.get("run_at", "local")
        self.run_at = run_at


class EleLocator:
    """
    element locator config
    """

    def __init__(self):
        ele_locator_path = os.path.join(
            os.getcwd(), "config", "ele_locator.json"
        )
        if not os.path.exists(ele_locator_path):
            log.warn(
                f"[EleLocator] cannot find path: {ele_locator_path} "
                "will set default")
            self.all_ele_locator = json.loads("{}")
        else:
            self.all_ele_locator = file_helper.get_json_from_file(
                ele_locator_path)


class IgnoreNodeConfig:
    """
    all interface ignore node config
    """

    def __init__(self):
        interface_ignore_dir_path = os.path.join(
            os.getcwd(), "interfaceIgnoreConfig"
        )
        all_ignore_data = read_json_data(interface_ignore_dir_path)
        self.all_ignore_nodes = all_ignore_data


class PaddleFixConfig:
    """
    paddle ocr fix config
    """

    def __init__(self):
        paddle_fix_path = os.path.join(
            os.getcwd(), "config", "paddle_fix.json"
        )
        if not os.path.exists(paddle_fix_path):
            self.paddle_fix_node = json.loads("{}")
        else:
            self.paddle_fix_node = file_helper.get_json_from_file(
                paddle_fix_path)
