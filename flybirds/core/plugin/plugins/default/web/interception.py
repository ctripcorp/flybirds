# -*- coding: utf-8 -*-
# @Time : 2022/5/16 17:05
# @Author : hyx
# @File : interception.py
# @desc :web request interception related operations
import os

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.exceptions import FlybirdsException

__open__ = ["Interception"]

from flybirds.utils import file_helper


class Interception:
    """
    web interception impl
    """
    name = "web_interception"

    # -------------------------------------------------------------------------
    # request interception  todo
    # -------------------------------------------------------------------------
    @staticmethod
    def add_some_interception_request_body(service_str):
        # // 缓存服务请求\[([\s\S]*)\]$/ :初始化
        if service_str is None:
            log.error(
                '[addSomeInterceptionRequestBody] param can not be none.')
            return
        service_list = service_str.strip().split(',')
        interception_request = gr.get_value('interceptionRequest')

        for service in service_list:
            interception_request[service.strip()] = {}
        gr.set_value('interceptionRequest', interception_request)

    @staticmethod
    def remove_some_interception_request_body(service_str):
        # // 移除请求缓存\[([\s\S]*)\]$/
        service_list = service_str.strip().split(',')
        interception_request = gr.get_value('interceptionRequest')

        for service in service_list:
            try:
                request_body = interception_request.pop(service.strip())
                log.info(
                    f'remove data cached by request [{service.strip()}]: '
                    f'{request_body}')
            except Exception as e:
                log.error(f'[removeSomeInterceptionRequestBody] has KeyError! '
                          f'error key: {str(e)}')
        gr.set_value('interceptionRequest', interception_request)

    @staticmethod
    def clear_interception_request_body():
        # //移除所有请求缓存
        interception_request = gr.get_value('interceptionRequest')
        interception_request.clear()
        gr.set_value('interceptionRequest', interception_request)

    # -------------------------------------------------------------------------
    # request service listening  todo
    # -------------------------------------------------------------------------
    @staticmethod
    def add_some_interception_mock(service_str, mock_case_id_str):
        # // 监听服务\[([\s\S]*)\]绑定MockCase\[([\s\S]*)\]
        if service_str is None or mock_case_id_str is None:
            log.error('[addSomeInterceptionMock] param can not be none. ')
            return

        service_list = service_str.strip().split(',')
        mock_case_id_list = mock_case_id_str.strip().split(',')
        if len(service_list) != len(mock_case_id_list):
            message = f"serviceCount[{service_str}] not equal " \
                      f"mockCaseCount[{mock_case_id_str}]"
            raise FlybirdsException(message)

        interception_values = gr.get_value('interceptionValues')
        for i, service in enumerate(service_list):
            interception_values[service.strip()] = int(
                mock_case_id_list[i].strip())

        gr.set_value('interceptionValues', interception_values)

    @staticmethod
    def remove_some_interception_mock(service_str):
        # //移除服务监听\[([\s\S]*)\]
        service_list = service_str.strip().split(',')
        interception_values = gr.get_value('interceptionValues')

        for service in service_list:
            try:
                interception_values.pop(service.strip())
                log.info(f'remove mock data from request [{service.strip()}]')
            except Exception as e:
                log.error(f'[removeSomeInterceptionMock] has KeyError! '
                          f'error key: {str(e)}')
        gr.set_value('interceptionValues', interception_values)

    @staticmethod
    def clear_interception_mock():
        # // 移除所有服务监听
        interception_values = gr.get_value('interceptionValues')
        interception_values.clear()
        gr.set_value('interceptionValues', interception_values)

    # -------------------------------------------------------------------------
    # compare service requests  todo
    # -------------------------------------------------------------------------
    @staticmethod
    def request_compare(operation, target_data_path):
        """
        # /^验证服务请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
         operation 待校验的接口名称
         target_data_path 校验报文路径
        """
        request_info = gr.get_server_request_body(operation)
        actual_request_obj = None
        if request_info and request_info.get('postData'):
            actual_request_obj = request_info.get('postData')
        if actual_request_obj is None:
            message = f'未监听到[{operation}]的数据'
            log.error(message)
            raise FlybirdsException(message)

        file_path = os.path.join(os.getcwd(), target_data_path)
        expect_request_obj = None
        if os.path.exists(file_path):
            expect_request_obj = file_helper.get_json_from_file_path(file_path)

        if expect_request_obj is None:
            message = f'未获取到[{target_data_path}]的数据'
            log.error(message)
            raise FlybirdsException(message)
        # todo 处理忽略节点
        handled_expect, handled_actual = handle_config_node(expect_request_obj,
                                                            actual_request_obj,
                                                            operation)
        # todo 获取差异节点

    @staticmethod
    def request_query_string_compare(operation, target_data_path):
        # /^验证服务非json请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
        pass

    @staticmethod
    def request_compare_value(operation, target_json_path, expect_value):
        # /^验证服务\[([\s\S]*)\]的请求参数\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
        pass


def handle_config_node(expect_request_obj, actual_request_obj, operation):
    # todo
    return "handled_expect", "handled_actual"
