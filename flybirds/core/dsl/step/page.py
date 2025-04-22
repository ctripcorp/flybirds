# -*- coding: utf-8 -*-
"""
This module defines the steps related to the page.
"""

from behave import step

from flybirds.core.exceptions import ErrorFlag, ActionType
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap, VerifyStep, FlybirdsReportTagInfo
from flybirds.utils.dsl_helper import get_params


@step("execute js[{param}]")
@ele_wrap
def execute_js_page(context, param=None):
    g_Context.step.excute_js_page(context, param)


@step("go to url[{param}]")
@FlybirdsReportTagInfo(group="url", selectors={
    "path": [{"type": "url", "value": "param", "name": "url"}]}, verify_function="page_url_verify")
@ele_wrap
def jump_to_page(context, param=None):
    g_Context.step.jump_to_page(context, param)


@step("set web page with width[{width}] and height[{height}]")
@FlybirdsReportTagInfo(group="page", selectors={
    "path": [{"type": "size", "value": "width", "name": "宽"}, {"type": "size", "value": "height", "name": "高"}]},
                       verify_function="common_error_parse", action=ActionType.setPageSize)
@ele_wrap
def set_web_page_size(context, width, height):
    g_Context.step.set_web_page_size(context, width, height)


@step("switch to target page title[{title}] url[{url}]")
@FlybirdsReportTagInfo(group="page", selectors={
    "path": [{"type": "title", "value": "title", "name": "标题"}, {"type": "url", "value": "url", "name": "url"}]},
                       verify_function="common_error_parse", action=ActionType.switchPage)
@ele_wrap
def switch_target_page(context, title, url):
    g_Context.step.switch_target_page(context, title, url)


@step("switch to latest page")
@ele_wrap
def switch_target_page(context):
    g_Context.step.switch_to_latest_page(context)


@step("set cookie name[{name}] value[{value}] url[{url}]")
@FlybirdsReportTagInfo(group="cookie", selectors={
    "path": [{"type": "key", "value": "name", "name": "key"}, {"type": "value", "value": "value", "name": "value"}]},
                       verify_function="common_error_parse", action=ActionType.setCookie)
@ele_wrap
def add_cookie(context, name, value, url):
    g_Context.step.add_cookies(context, name, value, url)


@step("set header [{name}] value[{value}]")
@FlybirdsReportTagInfo(group="header", selectors={
    "path": [{"type": "key", "value": "name", "name": "key"}, {"type": "value", "value": "value", "name": "value"}]},
                       verify_function="common_error_parse", action=ActionType.setHeader)
@ele_wrap
def add_header(context, name, value):
    g_Context.step.add_header(context, name, value)


@step("set sessionStorage name[{name}] value[{value}]")
@FlybirdsReportTagInfo(group="sessionStorage", selectors={
    "path": [{"type": "key", "value": "name", "name": "key"}, {"type": "value", "value": "value", "name": "value"}]},
                       verify_function="common_error_parse", action=ActionType.setSessionStorage)
@ele_wrap
def add_session_storage(context, name, value):
    g_Context.step.add_session_storage(context, name, value)


@step("set localStorage name[{name}] value[{value}]")
@FlybirdsReportTagInfo(group="localStorage", selectors={
    "path": [{"type": "key", "value": "name", "name": "key"}, {"type": "value", "value": "value", "name": "value"}]},
                       verify_function="common_error_parse", action=ActionType.setLocalStorage)
@ele_wrap
def add_local_storage(context, name, value):
    g_Context.step.add_local_storage(context, name, value)


@step("get cookie")
@FlybirdsReportTagInfo(group="cookie", selectors={"path": []}, verify_function="common_error_parse",
                       action=ActionType.getCookie)
@ele_wrap
def get_cookie(context):
    g_Context.step.get_cookie(context)


@step("get local storage")
@FlybirdsReportTagInfo(group="storage", selectors={
    "path": []}, verify_function="common_error_parse", action=ActionType.getStorage)
@ele_wrap
def get_local_storage(context):
    g_Context.step.get_local_storage(context)


@step("get session storage")
@FlybirdsReportTagInfo(group="sessionStorage", selectors={
    "path": []}, verify_function="common_error_parse", action=ActionType.getSessionStorage)
@ele_wrap
def get_session_storage(context):
    g_Context.step.get_session_storage(context)


@step("return to previous page")
@FlybirdsReportTagInfo(group="page", selectors={
    "path": []}, verify_function="common_error_parse", action=ActionType.returnPrePage)
def return_pre_page(context):
    g_Context.step.return_pre_page(context)


@step("browser forward")
@FlybirdsReportTagInfo(group="page", selectors={
    "path": []}, verify_function="common_error_parse", action=ActionType.goForward)
def page_go_forward(context):
    g_Context.step.page_go_forward(context)


@step("go to home page")
def to_app_home(context):
    g_Context.step.to_app_home(context)


@step("logon account[{selector1}]password[{selector2}]")
@ele_wrap
def app_login(context, selector1=None, selector2=None):
    g_Context.step.app_login(context, selector1, selector2)


@step("logout")
def app_logout(context):
    g_Context.step.app_logout(context)


@step("unblock the current page")
def unblock_page(context):
    g_Context.step.unblock_page(context)


@step("current page is [{param}]")
@FlybirdsReportTagInfo(group="page", selectors={"path": [{}, {"type": "text", "value": "param", "name": "文本"}]},
                       verify={"type": ErrorFlag.equ, "value": "param"}, verify_function="common_error_parse")
@VerifyStep()
@ele_wrap
def cur_page_is(context, param=None):
    g_Context.step.cur_page_is(context, param)


@step("current page is not last page")
@VerifyStep()
def has_page_changed(context):
    g_Context.step.has_page_changed(context)
