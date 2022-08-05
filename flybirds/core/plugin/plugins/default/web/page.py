# -*- coding: utf-8 -*-
# @Time : 2022/3/7 19:18
# @Author : hyx
# @File : page.py
# @desc : web page implement
import json
import time
from urllib.parse import urlparse

import flybirds.core.global_resource as global_resource
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
import flybirds.utils.verify_helper as verify_helper
from flybirds.core.plugin.plugins.default.web.interception import \
    get_case_response_body
from flybirds.utils import dsl_helper
from flybirds.utils.dsl_helper import is_number

__open__ = ["Page"]


class Page:
    """Web Page Class"""

    name = "web_page"
    instantiation_timing = "plugin"

    def __init__(self):
        page, context = self.init_page()
        self.page = page
        self.context = context

    @staticmethod
    def init_page():
        context = gr.get_value("browser_context")
        if context is None or gr.get_web_info_value("browserExit") is None \
                or gr.get_web_info_value("browserExit") is True:
            context = Page.new_browser_context()

        page = context.new_page()
        request_interception = gr.get_web_info_value("request_interception",
                                                     True)
        if request_interception:
            page.route("**/*", handle_route)
            # request listening events
            page.on("request", handle_request)
        page.on("console", handle_page_error)

        ele_wait_time = gr.get_frame_config_value("wait_ele_timeout", 30)
        page_render_timeout = gr.get_frame_config_value("page_render_timeout",
                                                        30)
        page.set_default_timeout(float(ele_wait_time) * 1000)
        page.set_default_navigation_timeout(float(page_render_timeout) * 1000)
        return page, context

    @staticmethod
    def new_browser_context():
        browser = gr.get_value('browser')

        operation_module = gr.get_value("projectScript").custom_operation
        context = None
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

        context = browser.new_context(record_video_dir="videos",
                                      ignore_https_errors=True)
        return context

    def navigate(self, context, param):
        operation_module = gr.get_value("projectScript").custom_operation
        page_url = None
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
        self.page.goto(schema_url_value)

    def return_pre_page(self, context):
        self.page.go_back()

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
            schema_url = global_resource.get_page_schema_url(param)
            target_url = schema_url
        verify_helper.text_equal(target_url, cur_url)


def handle_page_error(msg):
    if hasattr(msg, "type") and msg.type is not None:
        need_log = False
        if msg.type.lower() == "warn":
            need_log = True
        if msg.type.lower() == "error":
            need_log = True
        if need_log:
            if hasattr(msg, "text"):
                log.info(
                    f"=====================page console==================:\n {msg.text}")


def handle_request(request):
    # interception request handle
    parsed_uri = urlparse(request.url)
    operation = parsed_uri.path.split('/')[-1]
    if operation is not None:
        interception_request = gr.get_value('interceptionRequest')
        request_body = interception_request.get(operation)

        if request_body is not None:
            log.info(
                f'[handle_request] start cache service：{operation}')
            current_request_info = {'postData': request.post_data,
                                    'url': request.url,
                                    'updateTimeStamp': int(
                                        round(time.time() * 1000))}
            interception_request[operation] = current_request_info
            gr.set_value("interceptionRequest", interception_request)


def handle_route(route):
    abort_domain_list = gr.get_web_info_value("abort_domain_list", [])
    parsed_uri = urlparse(route.request.url)
    domain = parsed_uri.hostname
    if abort_domain_list and domain in abort_domain_list:
        route.abort()
        return

    resource_type = route.request.resource_type
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
