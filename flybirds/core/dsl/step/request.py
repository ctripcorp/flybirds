# -*- coding: utf-8 -*-
# @Time : 2022/5/17 11:29
# @Author : hyx
# @File : request.py
# @desc :
from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap


@step("cache service request [{service}]")
@ele_wrap
def add_request_body(context, service=None):
    # // 缓存服务请求\[([\s\S]*)\]$/ :初始化
    g_Context.step.add_request_body(context, service)


@step("remove service request cache [{service}]")
@ele_wrap
def remove_request_body(context, service=None):
    # // 移除请求缓存\[([\s\S]*)\]$/
    g_Context.step.remove_request_body(context, service)


@step("remove all service request caches")
def clear_all_request_body(context):
    # // 移除所有请求缓存
    g_Context.step.clear_all_request_body(context)


@step("listening service [{service}] bind mockCase[{mock_case_id}]")
@ele_wrap
def add_request_mock(context, service=None, mock_case_id=None):
    # // 监听服务\[([\s\S]*)\]绑定MockCase\[([\s\S]*)\]
    g_Context.step.add_request_mock(context, service, mock_case_id)


@step("remove service listener [{service}]")
@ele_wrap
def remover_request_mock(context, service=None):
    # //移除服务监听\[([\s\S]*)\]
    g_Context.step.remover_request_mock(context, service)


@step("remove all service listeners")
def clear_all_request_mock(context):
    # 移除所有服务监听
    g_Context.step.clear_all_request_mock(context)


@step(
    "compare service request [{operation}] with json file [{target_data_path}]"
)
@ele_wrap
def add_request_mock(context, operation=None, target_data_path=None):
    # /^验证服务请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
    g_Context.step.request_compare_from_path(context, operation,
                                             target_data_path)


@step(
    "compare service non-json request [{operation}] with non-json "
    "file [{target_data_path}]")
@ele_wrap
def remover_request_mock(context, operation=None, target_data_path=None):
    # /^验证服务非json请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
    g_Context.step.request_query_str_compare_from_path(context, operation,
                                                       target_data_path)


@step(
    "service request [{operation}] request parameter [{target_json_path}] "
    "is [{expect_value}]")
@ele_wrap
def clear_all_request_mock(context, operation=None, target_json_path=None,
                           expect_value=None):
    # /^验证服务\[([\s\S]*)\]的请求参数\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
    g_Context.step.request_compare_value(context, operation, target_json_path,
                                         expect_value)
