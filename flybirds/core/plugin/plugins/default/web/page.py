# -*- coding: utf-8 -*-
# @Time : 2022/3/7 19:18
# @Author : hyx
# @File : page.py
# @desc : web page implement
import json
import time
import os
import re
import uuid
from urllib.parse import urlparse

import flybirds.core.global_resource as gr
from flybirds.core.global_context import GlobalContext
import flybirds.utils.flybirds_log as log
import flybirds.utils.verify_helper as verify_helper
from flybirds.core.plugin.plugins.default.web.interception import \
    get_case_response_body
from flybirds.utils import dsl_helper
from flybirds.utils.dsl_helper import is_number
from flybirds.utils import file_helper
from flybirds.core.exceptions import FlybirdsException
import urllib.parse
import threading
from urllib.parse import urlsplit, urlunsplit
import datetime
from jsonpath_ng import parse as parse_path

__open__ = ["Page"]

mock_lock: threading.Lock = threading.Lock()
mock_req_lock: threading.Lock = threading.Lock()


class Page:
    """Web Page Class"""

    name = "web_page"
    instantiation_timing = "plugin"

    def __init__(self, dic=None):
        page, context = self.init_page(dic)
        self.page = page
        self.context = context

    @staticmethod
    def init_page(dic=None):
        context = gr.get_value("browser_context")
        if context is None or gr.get_web_info_value("browserExit") is None \
                or gr.get_web_info_value("browserExit") is True:
            context = Page.new_browser_context(dic)
            gr.set_value("browser_context", context)

        page = context.new_page()
        request_interception = gr.get_web_info_value("request_interception",
                                                     True)
        if request_interception:
            if not gr.get_value("hook_on_page", None):
                context.route("**/*", handle_route)
            else:
                log.info("use page route=====")
                page.route("**/*", handle_route)
            # request listening events
            context.on("request", handle_request)
        context.on("console", handle_page_error)
        context.on("page", handle_popup)

        ele_wait_time = gr.get_frame_config_value("wait_ele_timeout", 30)
        page_render_timeout = gr.get_frame_config_value("page_render_timeout",
                                                        30)
        page.set_default_timeout(float(ele_wait_time) * 1000)
        page.set_default_navigation_timeout(float(page_render_timeout) * 1000)
        return page, context

    @staticmethod
    def new_browser_context(dic=None):
        browser = gr.get_value('browser')
        operation_module = gr.get_value("projectScript").custom_operation

        if operation_module is not None and \
                hasattr(operation_module, "create_browser_context"):
            create_browser_context = getattr(operation_module,
                                             "create_browser_context")
            if create_browser_context is not None:
                context = create_browser_context(browser)
                if context is not None:
                    log.info(
                        '[new_browser_context] successfully get BrowserContext '
                        'from custom operation')
                    return context

        optional_config = Page.get_web_option_config(dic)
        launch_params = {"proxy": {"server": gr.get_web_info_value("proxy", None)}}
        launch_config = {
            "record_video_dir": "videos",
            "record_video_size": {"width": 1280, "height": 720},
            "ignore_https_errors": True
        }

        if gr.get_value("debug", False):
            launch_config["record_video_dir"] = None

        if gr.get_web_info_value("by_pass", None) is not None:
            launch_params.get("proxy").__setitem__("bypass", gr.get_web_info_value("by_pass", None))
            if optional_config is not None:
                launch_config = {
                    **launch_config,
                    "proxy": launch_params.get("proxy"),
                    **optional_config
                }
            else:
                launch_config = {
                    **launch_config,
                    "proxy": launch_params.get("proxy")
                }
        elif optional_config is not None:
            launch_config = {
                **launch_config,
                **optional_config
            }

        context = browser.new_context(**launch_config)
        # add user custom cookies into browser context
        user_cookie = GlobalContext.get_global_cache("cookies")
        if user_cookie is not None:
            # context.clear_cookies()
            context.add_cookies(cookies=user_cookie)
            log.info(f"this is user cookies: {context.cookies()}")
        else:
            log.info(f"user cookies is None")

        return context

    @staticmethod
    def get_web_option_config(dic=None):
        emulated_device = None
        user_agent = None
        viewport = None
        device_scale_factor = None
        locale = None
        timezone = None
        permissions = None
        geolocation = None
        has_touch = None
        default_browser_type = None
        gl_dict = {}
        if gr.get_web_info_value("emulated_device") is not None:
            playwright = gr.get_value("playwright")
            emulated_device = playwright.devices[
                gr.get_web_info_value("emulated_device")]
        if dic is not None and dic.get("emulated_device") is not None:
            playwright = gr.get_value("playwright")
            emulated_device = playwright.devices[
                dic.get("emulated_device")]
            del dic["emulated_device"]
        if gr.get_web_info_value("user_agent") is not None:
            user_agent = gr.get_web_info_value("user_agent")
        if gr.get_web_info_value("locale") is not None:
            locale = gr.get_web_info_value("locale")
        if gr.get_web_info_value("timezone") is not None:
            timezone = gr.get_web_info_value("timezone")
        if gr.get_web_info_value("permissions") is not None:
            permissions = gr.get_web_info_value("permissions")
        if gr.get_web_info_value("geolocation") is not None:
            geolocation = gr.get_web_info_value("geolocation")
        if gr.get_web_info_value("width") is not None and gr.get_web_info_value(
                "height"):
            viewport = {'width': gr.get_web_info_value("width"),
                        'height': gr.get_web_info_value(
                            "height")}
        if gr.get_web_info_value("device_scale_factor") is not None:
            device_scale_factor = gr.get_web_info_value("device_scale_factor")

        if gr.get_web_info_value("has_touch") is not None:
            has_touch = gr.get_web_info_value("has_touch")

        if gr.get_web_info_value("default_browser_type") is not None:
            default_browser_type = gr.get_web_info_value("default_browser_type")

        if user_agent is not None:
            gl_dict["user_agent"] = user_agent
        if viewport is not None:
            gl_dict["viewport"] = viewport
        if locale is not None:
            gl_dict["locale"] = locale
        if timezone is not None:
            gl_dict["timezone_id"] = timezone
        if geolocation is not None:
            gl_dict["geolocation"] = geolocation
            if permissions is None:
                permissions = ["geolocation"]
            else:
                if permissions.index("geolocation") < 0:
                    permissions.append("geolocation")
        if permissions is not None:
            gl_dict["permissions"] = permissions
        if device_scale_factor is not None:
            gl_dict["device_scale_factor"] = device_scale_factor
        if has_touch is not None:
            gl_dict["hasTouch"] = has_touch
        if default_browser_type is not None:
            gl_dict["default_browser_type"] = default_browser_type

        if emulated_device is not None:
            gl_dict.update(emulated_device)

        if gl_dict is not None and len(gl_dict) > 0:
            if dic is not None and len(dic) > 0:
                gl_dict.update(dic)
            return gl_dict
        else:
            return dic

    def evaluatejs(self, context, param):

        # Convert parameter string to dictionary
        param_dict = dsl_helper.params_to_dic(param, "path")

        # Get path from dictionary
        path = param_dict["path"]

        # Specify path and file extension to look for
        path = os.path.join(os.getcwd(), path)

        # Check if path has .js extension
        if path.find('.js') < 0:
            message = '[path] could not find js'
            raise FlybirdsException(message)

        # Read JavaScript content from file
        jscontent = file_helper.read_file_from_path(path)

        # Check if there are any executable test cases in the list
        if jscontent is None:
            message = '[casecontent] could not find in ' + path
            raise FlybirdsException(message)

        # Split JavaScript content into a list of test cases
        casename = ''
        priority = ''
        tag = ''
        if "casename" in param_dict.keys():
            casename = param_dict["casename"]

        if "priority" in param_dict.keys():
            priority = param_dict["priority"]

        if "tag" in param_dict.keys():
            tag = param_dict["tag"]

        pattern = r'/\*\*(.*?)\}(\s*)\n'
        caselist = split_string_rx(jscontent, pattern)

        # Check if there are any executable test cases in the list
        if len(caselist) == 0:
            message = '[caselist] could not find excuteable case list'
            raise FlybirdsException(message)

        # Format test cases content
        caseformatlist = format_case(caselist)

        # Check if there are any executable test cases in the list
        if len(caseformatlist) == 0:
            message = '[caseformatlist] the content of case list is empty or format is wrong'
            raise FlybirdsException(message)

        caseactuallist = process_caselist(caseformatlist, casename, priority, tag)

        # Check if there are any executable test cases in the list
        if len(caseactuallist) == 0:
            message = '[caseactuallist] could not find excuteable case list'
            raise FlybirdsException(message)

        # Execute each executable test case and log the result
        for item in caseactuallist:
            contentcase = item[2]
            try:
                self.page.evaluate('() => ' + contentcase)
                log.info("evaluate Js Case:", contentcase)
            except Exception:
                message = '[case] excute failed:' + contentcase
                raise FlybirdsException(message)

    def navigate(self, context, param):
        operation_module = gr.get_value("projectScript").custom_operation
        page_url = None
        user_header = GlobalContext.get_global_cache("user_header")
        if user_header:
            self.page.set_extra_http_headers(user_header)
            log.info(f'user_header: {user_header}')
            # self.page.on("request",
            #                    lambda request: log.info('page header request', request.url,
            #                                             request.headers))
        if hasattr(operation_module, "get_page_url"):
            get_page_url = getattr(operation_module,
                                   "get_page_url")
            page_url = get_page_url(param)

        if page_url is not None:
            log.info('[get_page_url] successfully get page_url_value '
                     'from custom operation')
            self.page.goto(page_url)
            return

        param_dict = dsl_helper.params_to_dic(param, "urlKey")
        url_key = param_dict["urlKey"]
        schema_url_value = gr.get_page_schema_url(url_key)

        if "timeout" in param_dict.keys():
            self.page.goto(schema_url_value, timeout=float(param_dict["timeout"]) * 1000)
            return

        self.page.goto(schema_url_value)

    def set_web_page_size(self, context, width, height):
        self.page.set_viewport_size({"width": int(width), "height": int(height)})

    def return_pre_page(self, context):
        self.page.go_back()

    def page_go_forward(self, context):
        self.page.go_forward()

    def sleep(self, context, param):
        if is_number(param):
            self.page.wait_for_timeout(float(param) * 1000)
        else:
            log.warn("default wait for timeout!")
            self.page.wait_for_timeout(3 * 1000)

    def cur_page_equal(self, context, param):
        cur_url = self.page.url.split('?')[0]
        if param.startswith(("http", "https")):
            target_url = param.split('?')[0]
        else:
            schema_url = gr.get_page_schema_url(param)
            target_url = schema_url
        verify_helper.text_equal(target_url, cur_url)

    @staticmethod
    def add_cookies(name, value, url):
        if GlobalContext.get_global_cache("step_cookies") is None:
            GlobalContext.set_global_cache("step_cookies", [])
        GlobalContext.get_global_cache("step_cookies").append({'name': name, 'value': value, "url": url})
        if name is not None and value is not None and url is not None:
            user_cookie = [{'name': name, 'value': value, "url": url}]
            context = gr.get_value("browser_context")
            context.add_cookies(cookies=user_cookie)
            log.info(f"set cookie success: {context.cookies()}")
        else:
            log.info(f"set cookie fail, please check param")

    @staticmethod
    def get_cookie(context):
        context = gr.get_value("browser_context")
        cookies = context.cookies()
        log.info(f"get cookie success: {cookies}")
        return cookies

    @staticmethod
    def get_local_storage(context):
        context = gr.get_value("browser_context")
        local_storage = context.storage_state()
        log.info(f"get local storage success: {local_storage['origins']}")
        return local_storage['origins']

    def get_session_storage(self, context):
        session_storage = self.page.evaluate("() => JSON.stringify(sessionStorage)")
        log.info(f"get session storage success: {session_storage}")
        return session_storage


def handle_page_error(msg):
    if hasattr(msg, "type") and msg.type is not None:
        need_log = False
        if msg.type.lower() == "warn":
            need_log = True
        if msg.type.lower() == "error":
            need_log = True
        if need_log:
            if hasattr(msg, "text"):
                print(f"=====================page console==================:\n {msg.text}")


def handle_request(request):
    if gr.get_value("network_collect") is not None:
        network_key = uuid.uuid4()
        network_key = f"{network_key}_{time.time_ns()}"
        setattr(request, "network_key", network_key)
        gr.get_value("network_collect")[network_key] = {
            "key": network_key,
            "url": request.url,
            "start": str(datetime.datetime.now())
        }

    # interception request handle
    parsed_uri = urlparse(request.url)
    post_data = None
    try:
        post_data = request.post_data
    except Exception as ex:
        log.info("try to get post data from request")
    operation = get_operation(parsed_uri, post_data)
    if operation is not None and len(operation.strip()) > 0:
        interception_request = gr.get_value('interceptionRequest')
        request_body = interception_request.get(operation)
        # 记录页面请求
        operate_record = gr.get_value('operate_record')
        operate_record[operation] = {
            'method': request.method,
            'postData': request.post_data,
            'url': request.url,
            'updateTimeStamp': int(round(time.time() * 1000))
        }
        gr.set_value("operate_record", operate_record)
        if request_body is not None:
            log.info(
                f'[handle_request] start cache service：{operation}')
            current_request_info = {'postData': request.post_data,
                                    'url': request.url,
                                    'updateTimeStamp': int(
                                        round(time.time() * 1000))}
            interception_request[operation] = current_request_info
            gr.set_value("interceptionRequest", interception_request)


def mock_rules(url: str, request_mock_key_value: list):
    if url is None or len(url.strip()) <= 0:
        return None
    scheme, netloc, path, query, fragment = urlsplit(url)
    temp_path = urlunsplit(("", "", path, query, fragment))
    if temp_path is None or len(temp_path.strip()) <= 0:
        return None
    if path is None or len(path.strip()) <= 0:
        return None
    match_mock_key = None
    with mock_lock:
        for mock_rule in request_mock_key_value:
            mock_find = False
            if mock_rule is not None and mock_rule.get("key") and mock_rule.get("value") and mock_rule.get("max"):
                if mock_rule.get("key") is not None and len(mock_rule.get("key").strip()) > 0 and len(
                        mock_rule.get("value").strip()) > 0:
                    if mock_rule.get("max") <= 0:
                        continue
                    method = mock_rule.get("method", None)
                    if method is None or method == "contains":
                        if mock_rule.get("key").strip() in temp_path:
                            mock_find = True
                    elif method == "equ":
                        if mock_rule.get("key").strip().strip("/").strip("\\") == path.strip().strip("/").strip(
                                "\\"):
                            mock_find = True
                    elif method == "reg":
                        match = re.search(mock_rule.get("key").strip(), temp_path)
                        if match:
                            mock_find = True
                    else:
                        if mock_rule.get("key").strip() in temp_path:
                            mock_find = True
                    if mock_find:
                        match_mock_key = mock_rule
                        mock_rule["max"] = mock_rule.get("max") - 1
                        break
    return match_mock_key


def handle_popup(page):
    log.info(f"============open new page============, url: {page.url}")
    if gr.get_value("web_context_hook") is not None:
        web_context_hook = gr.get_value("web_context_hook")
        if hasattr(web_context_hook, "handle_popup"):
            web_context_hook.handle_popup(page)


def mock_rules_req_body(url: str, request_mock_key_value: list, request_body_real):
    if url is None or len(url.strip()) <= 0 or request_mock_key_value is None or len(
            request_mock_key_value) <= 0 or request_body_real is None:
        return None
    scheme, netloc, path, query, fragment = urlsplit(url)
    temp_path = urlunsplit(("", "", path, query, fragment))
    if temp_path is None or len(temp_path.strip()) <= 0:
        return None
    if path is None or len(path.strip()) <= 0:
        return None
    match_mock_key = None
    with mock_req_lock:
        for mock_rule in request_mock_key_value:
            mock_find = False
            if mock_rule is not None and mock_rule.get("key") and mock_rule.get("value") and mock_rule.get("max"):
                if mock_rule.get("key") is not None and len(mock_rule.get("key").strip()) > 0 and len(
                        mock_rule.get("value").strip()) > 0:
                    if mock_rule.get("max") <= 0:
                        continue
                    method = mock_rule.get("method", None)
                    if method is None or method == "contains":
                        if mock_rule.get("key").strip() in temp_path:
                            mock_find = True
                    elif method == "equ":
                        if mock_rule.get("key").strip().strip("/").strip("\\") == path.strip().strip("/").strip(
                                "\\"):
                            mock_find = True
                    elif method == "reg":
                        match = re.search(mock_rule.get("key").strip(), temp_path)
                        if match:
                            mock_find = True
                    else:
                        if mock_rule.get("key").strip() in temp_path:
                            mock_find = True
                    if mock_find:
                        mock_reqeust_find = False
                        if mock_rule.get("mockType", None) == "request" and mock_rule.get("requestPathes",
                                                                                          None) is not None and len(
                            mock_rule.get("requestPathes", None)) > 0 and request_body_real is not None:
                            request_pathes = mock_rule.get("requestPathes",
                                                           None)
                            for request_path in request_pathes:
                                j_path = parse_path(f"$.{request_path}")
                                real = [match.value for match in j_path.find(request_body_real)]
                                except_value = [match.value for match in j_path.find(mock_rule.get("requestBody"))]
                                if json.dumps(real) == json.dumps(except_value):
                                    mock_reqeust_find = True
                                break
                        if mock_reqeust_find:
                            match_mock_key = mock_rule
                            mock_rule["max"] = mock_rule.get("max") - 1
                            break

    return match_mock_key


def handle_route(route):
    abort_domain_list = gr.get_web_info_value("abort_domain_list", [])
    parsed_uri = urlparse(route.request.url)
    domain = parsed_uri.hostname
    if abort_domain_list and domain in abort_domain_list:
        route.abort()
        return
    if GlobalContext.get_global_cache("enableWebContextHook"):
        if hasattr(route, "fetch") and gr.get_value("web_context_hook") is not None:
            web_context_hook = gr.get_value("web_context_hook")
            if hasattr(web_context_hook, "handle_route"):
                result = web_context_hook.handle_route(route)
                if result:
                    return
    resource_type = route.request.resource_type
    # pass options
    if route.request.method.lower() == "options":
        route.continue_()
        return
    # mock response
    request_mock_key_value = GlobalContext.get_global_cache("request_mock_key_value")
    request_mock_request_key_value = GlobalContext.get_global_cache("request_mock_request_key_value")

    # request body match mock
    if request_mock_request_key_value is not None and len(request_mock_request_key_value) > 0:
        try:
            mock_rule_request = None
            if route.request.resource_type == 'xhr' or route.request.resource_type == 'fetch':
                mock_rule_request = mock_rules_req_body(route.request.url, request_mock_request_key_value,
                                                        route.request.post_data_json)
            if mock_rule_request is not None:
                log.info(
                    f"url:{route.request.url}===== match request mock url:{mock_rule_request.get('key')} and mock key :{mock_rule_request.get('requestPathes')} mock case "
                    f":{mock_rule_request.get('value')}===================")
                mock_body_request = get_case_response_body(mock_rule_request.get("value"))
                mock_status = 200
                if mock_body_request:
                    if mock_body_request.get("flybirdsMockResponse") is not None or mock_body_request.get(
                            "status") is not None:
                        mock_body_request = mock_body_request.get("flybirdsMockResponse")
                        mock_status = mock_body_request.get("status", 200)
                    if not isinstance(mock_body_request, str):
                        mock_body_request = json.dumps(mock_body_request)
                    if route.request.headers.get("content-type"):
                        route.fulfill(status=mock_status,
                                      content_type=route.request.headers.get("content-type"),
                                      body=mock_body_request)
                    else:
                        route.fulfill(status=mock_status,
                                      content_type="application/json",
                                      body=mock_body_request)
                    return

        except Exception as mock_error:
            log.info("find requst mock info error", mock_error)

    # request url match mock
    if request_mock_key_value is not None and len(request_mock_key_value) > 0:
        try:
            mock_rule = None
            if route.request.resource_type == 'xhr' or route.request.resource_type == 'fetch':
                mock_rule = mock_rules(route.request.url, request_mock_key_value)
            if mock_rule is not None:
                log.info(
                    f"url:{route.request.url}===== match mock key:{mock_rule.get('key')} mock case "
                    f":{mock_rule.get('value')}===================")
                mock_body = get_case_response_body(mock_rule.get("value"))
                mock_status = 200
                if mock_body:
                    if mock_body.get("flybirdsMockResponse") is not None or mock_body.get("status") is not None:
                        mock_status = mock_body.get("status", 200)
                        mock_body = mock_body.get("flybirdsMockResponse")
                    if not isinstance(mock_body, str):
                        mock_body = json.dumps(mock_body)
                        route.fulfill(status=mock_status,
                                      content_type="application/json;charset=UTF-8",
                                      body=mock_body)
                        return
                    if route.request.headers.get("content-type"):
                        route.fulfill(status=mock_status,
                                      content_type=route.request.headers.get("content-type"),
                                      body=mock_body)
                    else:
                        route.fulfill(status=mock_status,
                                      content_type="application/json",
                                      body=mock_body)
                    return

        except Exception as mock_error:
            log.info("find mock info error", mock_error)

    if GlobalContext.get_global_cache("enableWebContextHook"):
        if gr.get_value("web_context_hook") is not None:
            web_context_hook = gr.get_value("web_context_hook")
            if hasattr(web_context_hook, "handle_abort"):
                result = web_context_hook.handle_abort(route)
                if result:
                    route.abort()
                    return
    if resource_type != 'fetch' and resource_type != 'xhr':
        route.continue_()
        return

    # mock response data
    operation = parsed_uri.path.split('/')[-1]
    mock_case_id = None
    if operation is not None:
        interception_values = gr.get_value('interceptionValues')
        mock_case_id = interception_values.get(operation)
    if mock_case_id:
        mock_body = get_case_response_body(mock_case_id)
        if mock_body:
            if not isinstance(mock_body, str):
                mock_body = json.dumps(mock_body)
            route.fulfill(status=200,
                          content_type="application/json;charset=utf-8",
                          body=mock_body)
    else:
        route.continue_()


def split_string_rx(input_str, pattern):
    matches = re.findall(pattern, input_str, re.DOTALL)
    return matches


def match_string_rx(pattern, input_str):
    ismatch = False
    result = None
    match = re.search(pattern, input_str, re.DOTALL)

    if match:
        result = match.group(1)
        ismatch = True

    return ismatch, result


def match_param_rx(input_str):
    pattern = r'@param \{.*?\} (\w+)=([\w\W]*?)\n'
    matches = re.findall(pattern, input_str)

    return [f"{match[0]}={match[1]}" for match in matches]


def format_case(caselist):
    caseactuallist = []
    # Process each test case and append executable ones to a list
    for case in caselist:
        caseproperty = {}

        if len(case) > 0:
            case = case[0]

        patternname = r'\@constructor=(\w+)'
        ismatchname, casenameproperty = match_string_rx(patternname, case)
        caseproperty.update({'casename': casenameproperty})

        patternpriority = r'@property\s+priority\s*=\s*(\w+)'
        ismatchpriority, casepriorityproperty = match_string_rx(patternpriority, case)
        caseproperty.update({'priority': casepriorityproperty})

        patterntag = r'@property\s+tag\s*=\s*(\w+)'
        ismatchtag, casetagproperty = match_string_rx(patterntag, case)
        caseproperty.update({'tag': casetagproperty})

        paramlistascase = match_param_rx(case)

        parts = case.split('{')
        casecontent = '{' + parts[-1] + '}'
        caseactuallist.append((caseproperty, paramlistascase, casecontent))

        # isadd, outproperty, outValue = process_string(case, casename, priority, tag)
        # if isadd:
        #     caseactuallist.append((isadd, outproperty, outValue))

    return caseactuallist


def process_caselist(caseformatlist, casename, priority, tag):
    actualcaselist = []
    for item in caseformatlist:
        case_found = True
        propertycase = item[0]

        if casename != '':
            if propertycase['casename'] is not None:
                if propertycase['casename'].find(casename) == -1:
                    continue
        if priority != '':
            if propertycase['priority'] is not None:
                if propertycase['priority'].find(priority) == -1:
                    continue
        if tag != '':
            if propertycase['tag'] is not None:
                if propertycase['tag'].find(tag) == -1:
                    continue

        if case_found:
            actualcaselist.append(item)

    return actualcaselist


def get_operation(parsed_uri, request_body=None):
    operation_module = gr.get_value("projectScript").custom_operation
    if operation_module is not None and hasattr(operation_module, "get_operation"):
        get_operation_customer = getattr(operation_module, "get_operation")
        operation = get_operation_customer(parsed_uri, request_body)
        if operation is not None:
            return operation
    return parsed_uri.path.split('/')[-1]
