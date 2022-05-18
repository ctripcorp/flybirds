# -*- coding: utf-8 -*-
# @Time : 2022/5/16 17:05
# @Author : hyx
# @File : interception.py
# @desc :web request interception related operations
import json
import os
import re

from deepdiff import DeepDiff

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
    def request_compare(operation, target_file_name):
        """
        # /^验证服务请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
         operation 待校验的接口名称
         target_file_name 校验报文文件名称
        """
        request_info = get_server_request_body(operation)
        actual_request_obj = None
        if request_info and request_info.get('postData'):
            actual_request_obj = request_info.get('postData')
        if actual_request_obj is None:
            message = f'[request_compare] not listening to data from ' \
                      f'[{operation}]'
            raise FlybirdsException(message)

        file_path = os.path.join(os.getcwd(), "compareData", target_file_name)
        expect_request_obj = None
        if os.path.exists(file_path):
            expect_request_obj = file_helper.get_json_from_file_path(file_path)

        if expect_request_obj is None:
            message = f'[request_compare] data for file ' \
                      f'[{target_file_name}] was not retrieved!'
            raise FlybirdsException(message)
        exclude_paths, exclude_regex_paths = handle_ignore_node(operation)
        ignore_order = gr.get_web_info_value("ignore_order", False)
        diff = DeepDiff(actual_request_obj, expect_request_obj,
                        ignore_order=ignore_order, verbose_level=2,
                        exclude_paths=exclude_paths,
                        exclude_regex_paths=exclude_regex_paths)
        if not diff:
            log.info(f'compare the service request [{operation}] with '
                     f'[{target_file_name}], the result is the same.')
            return
        format_diff = json.dumps(diff, indent=2)
        log.info(f'Difference when comparing service request [{operation}] '
                 f'with [{target_file_name}]. Difference node:\n'
                 f'{format_diff}')

    @staticmethod
    def request_query_string_compare(operation, target_data_path):
        # /^验证服务非json请求\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
        pass

    @staticmethod
    def request_compare_value(operation, target_json_path, expect_value):
        # /^验证服务\[([\s\S]*)\]的请求参数\[([\s\S]*)\]与\[([\s\S]*)\]一致$/
        pass


def get_server_request_body(service):
    interception_request = gr.get_value('interceptionRequest')
    if interception_request:
        return interception_request.get(service)
    return None


def handle_ignore_node(service):
    service_ignore_nodes = gr.get_service_ignore_nodes(service)
    if service_ignore_nodes is None:
        return
    exclude_paths = []
    exclude_regex_paths = []
    for item in service_ignore_nodes:
        if 'regex' in item:
            regex_item = item.split('regex:')[-1].strip()
            exclude_regex_paths.append(regex_item)
        else:
            nodes = item.split('.')
            new_nodes = []
            for node in nodes:
                rs = re.findall(r"([^\[\]]+)\[(\d+)\]", node.strip())
                if len(rs) == 0:
                    new_nodes.append(node.strip())
                else:
                    [new_nodes.append(i.strip()) for i in list(rs[0])]

            path = 'root'
            for node in new_nodes:
                if node.isdigit():
                    path += f'[{node}]'
                else:
                    path += f"['{node}']"
            exclude_paths.append(path.strip())
    return exclude_paths, exclude_regex_paths
