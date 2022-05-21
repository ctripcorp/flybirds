# -*- coding: utf-8 -*-
"""
This module defines the steps related to the web network request.
"""

from behave import step

from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils.dsl_helper import ele_wrap


@step("cache service request [{service}]")
@ele_wrap
def add_request_body(context, service=None):
    """
    cache information of network request(service)

    :param context: step context
    :param service: service request name. (string or None).
    """
    g_Context.step.add_request_body(context, service)


@step("remove service request cache [{service}]")
@ele_wrap
def remove_request_body(context, service=None):
    """
    remove cached information of network request(service)

    :param context: step context
    :param service: service request name. (string or None).
    """
    g_Context.step.remove_request_body(context, service)


@step("remove all service request caches")
def clear_all_request_body(context):
    """
    remove all cached information of network request

    :param context: step context
    """
    g_Context.step.clear_all_request_body(context)


@step("listening service [{service}] bind mockCase[{mock_case_id}]")
@ele_wrap
def add_request_mock(context, service=None, mock_case_id=None):
    """
    Listening to network request(service) and binding mock data to it

    :param context: step context
    :param service: service request name. (string or None).
    :param mock_case_id: unique key for get mock data.
         (String, e.g. a numeric string, or other).
    """
    g_Context.step.add_request_mock(context, service, mock_case_id)


@step("remove service listener [{service}]")
@ele_wrap
def remover_request_mock(context, service=None):
    """
    remove listening and mock data binding to network request(service)

    :param context: step context
    :param service: service request name. (string or None).
    """
    g_Context.step.remover_request_mock(context, service)


@step("remove all service listeners")
def clear_all_request_mock(context):
    """
     remove listening and mock data binding for all services
    """
    g_Context.step.clear_all_request_mock(context)


@step(
    "compare service request [{service}] with json file [{target_data_path}]"
)
@ele_wrap
def request_compare(context, service=None, target_data_path=None):
    """
    compare and verify the request's post body with the data of the target path

    :param context: step context
    :param service: service request name. (string or None).
    :param target_data_path: path of target data to be compared
    """
    g_Context.step.request_compare_from_path(context, service,
                                             target_data_path)


@step(
    "compare service non-json request [{service}] with non-json "
    "file [{target_data_path}]")
@ele_wrap
def request_query_str_compare(context, service=None, target_data_path=None):
    """
    compare and verify the post body of a non-json type request with the
    data in the target path

    :param context: step context
    :param service: service request name. (string or None).
    :param target_data_path: path of target data to be compared
    """
    g_Context.step.request_query_str_compare_from_path(context, service,
                                                       target_data_path)


@step(
    "service request [{service}] request parameter [{target_json_path}] "
    "is [{expect_value}]")
@ele_wrap
def request_compare_value(context, service=None, target_json_path=None,
                          expect_value=None):
    """
    compare and verify the request parameter of the service request with
     the expected value

    :param context: step context
    :param service: service request name. (string or None).
    :param target_json_path: json path of request parameter
    :param expect_value: expected value
    """
    g_Context.step.request_compare_value(context, service, target_json_path,
                                         expect_value)
