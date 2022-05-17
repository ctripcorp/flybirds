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
