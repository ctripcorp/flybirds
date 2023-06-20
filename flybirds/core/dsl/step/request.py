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
    "compare target element [{target_element}] with compared picture [{compared_picture_path}]"
)
@ele_wrap
def picture_compare(context, target_element, compared_picture_path):
    """
    compare and verify the target picture with compared picture path

    :param context: step context
    :param target_element: target UI element.
    :param compared_picture_path: compared picture path
    """
    g_Context.step.picture_compare_from_path(context, target_element,
                                             compared_picture_path)


@step(
    "compare target element[{target_ele}] with compared text path of [{compared_text_path}]"
)
@ele_wrap
def dom_ele_text_compare(context, target_ele, compared_text_path):
    """
    compare and verify the html's dom element with the text of the target path and compared path

    :param target_ele: target xpath from html root element
    :param compared_text_path: compared  text path
    """
    g_Context.step.dom_ele_compare_from_path(context, target_ele, compared_text_path)


@step(
    "call external party api of method[{method}] and url[{url}] and data[{data}] and headers[{headers}]"
)
@ele_wrap
def call_external_party_api(context, method, url, data, headers=None):
    """
    This function is used to call an external API from within a Python script.

    :param url: a string representing the URL of the external API to call.
    :param data:  a dictionary containing the data to be sent in the request body. This can be in JSON or XML format.
    :param headers: a dictionary containing the headers to be sent with the request. This can include information
                   such as the content type, authorization, and API key.
    :param method: a string representing the HTTP method to be used for the request.
                   This can be 'GET', 'POST', 'PUT', 'DELETE', etc.
    """
    g_Context.step.call_external_party_api(context, method, url, data, headers)


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
    "compare service request [{service}] with xml file [{target_data_xml_path}]"
)
@ele_wrap
def request_compare(context, service=None, target_data_xml_path=None):
    """
    compare and verify the request's post body with the data of the target path

    :param context: step context
    :param service: service request name. (string or None).
    :param target_data_xml_path: path of target data to be compared
    """
    g_Context.step.request_compare_from_path(context, service,
                                             target_data_xml_path)


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


@step("open service [{service}] bind mockCase[{mock_case_id}]")
@ele_wrap
def open_request_mock(context, service, mock_case_id):
    g_Context.step.open_web_mock(context, service, mock_case_id)
