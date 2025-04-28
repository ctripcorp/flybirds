# -*- coding: utf-8 -*-
# @Time : 2022/5/16 17:05
# @Author : hyx
# @File : interception.py
# @desc :web request interception related operations
import json
import os
import re
import cv2
import requests
from PIL import Image
import io
from flybirds.utils import dsl_helper, uuid_helper
from urllib.parse import parse_qs

from flybirds.core.plugin.plugins.default.screen import BaseScreen
from deepdiff import DeepDiff
from jsonpath_ng import parse as parse_path

import xml.etree.ElementTree as et
import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.exceptions import FlybirdsException, ErrorName

__open__ = ["Interception"]

from flybirds.utils import file_helper
from flybirds.utils.file_helper import read_json_data, read_json_data_by_key
import xmltodict


class Interception:
    """
    web interception impl
    """
    name = "web_interception"

    # -------------------------------------------------------------------------
    # request interception
    # -------------------------------------------------------------------------
    @staticmethod
    def add_some_interception_request_body(service_str):
        if service_str is None or service_str.strip() == '':
            log.error(
                '[addSomeInterceptionRequestBody] param can not be none.')
            raise FlybirdsException("request name cannot be none or empty", ErrorName.ServiceNameParamsNoneError)
        service_list = service_str.strip().split(',')
        interception_request = gr.get_value('interceptionRequest')

        for service in service_list:
            interception_request[service.strip()] = {}
        gr.set_value('interceptionRequest', interception_request)

    @staticmethod
    def remove_some_interception_request_body(service_str):
        service_list = service_str.strip().split(',')
        interception_request = gr.get_value('interceptionRequest')

        try:
            for service in service_list:
                request_body = interception_request.pop(service.strip())
                log.info(
                    f'remove data cached by request [{service.strip()}]: '
                    f'{request_body}')
        except Exception as e:
            message = f'[removeSomeInterceptionRequestBody]  ' \
                      f'has KeyError! error key: {str(e)}'
            raise FlybirdsException(message, error_name=ErrorName.MockClearError)
        gr.set_value('interceptionRequest', interception_request)

    @staticmethod
    def clear_interception_request_body():
        interception_request = gr.get_value('interceptionRequest')
        interception_request.clear()
        gr.set_value('interceptionRequest', interception_request)

    @staticmethod
    def clear_all_request_record():
        operate_record = gr.get_value('operate_record')
        operate_record.clear()
        gr.set_value('operate_record', operate_record)

    # -------------------------------------------------------------------------
    # request service listening
    # -------------------------------------------------------------------------
    @staticmethod
    def add_some_interception_mock(service_str, mock_case_id_str):
        if service_str is None or mock_case_id_str is None:
            log.error('[addSomeInterceptionMock] param can not be none. ')
            return

        service_list = service_str.strip().split(',')
        mock_case_id_list = mock_case_id_str.strip().split(',')
        if len(service_list) != len(mock_case_id_list):
            message = f"serviceCount[{service_str}] not equal " \
                      f"mockCaseCount[{mock_case_id_str}]"
            raise FlybirdsException(message, ErrorName.MockCountNotMatchError)

        interception_values = gr.get_value('interceptionValues')
        for i, service in enumerate(service_list):
            interception_values[service.strip()] = mock_case_id_list[i].strip()

        gr.set_value('interceptionValues', interception_values)

    @staticmethod
    def open_web_mock(service_str, mock_case_id_str, request_mock_key_value: list):
        if service_str is None or mock_case_id_str is None:
            log.error('[addSomeInterceptionMock] param can not be none. ')
            raise FlybirdsException("cannot ad null service name as mock key",
                                    error_name=ErrorName.ServiceNameParamsNoneError)

        service_list = service_str.strip().split(',')
        mock_case_id_list = mock_case_id_str.strip().split(',')
        if len(service_list) != len(mock_case_id_list):
            message = f"serviceCount[{service_str}] not equal " \
                      f"mockCaseCount[{mock_case_id_str}]"
            raise FlybirdsException(message, error_name=ErrorName.MockCountNotMatchError)

        interception_values = request_mock_key_value
        for i, service in enumerate(service_list):
            if service is not None and len(service.strip()) > 0:
                if ":" in service:
                    split_service = service.split(":")
                    if split_service[0].strip() == "reg":
                        interception_values.append({
                            "max": 1,
                            "key": split_service[1].strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "reg",
                            "mockStep": gr.get_value("stepName", None)
                        })
                    elif split_service[0].strip() == "equ":
                        interception_values.append({
                            "max": 1,
                            "key": split_service[1].strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "equ",
                            "mockStep": gr.get_value("stepName", None)
                        })
                    else:
                        interception_values.append({
                            "max": 1,
                            "key": service.strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "contains",
                            "mockStep": gr.get_value("stepName", None)
                        })
                else:
                    interception_values.append({
                        "max": 1,
                        "key": service.strip(),
                        "value": mock_case_id_list[i].strip(),
                        "method": "contains",
                        "mockStep": gr.get_value("stepName", None)
                    })

    @staticmethod
    def remove_some_interception_mock(service_str):
        service_list = service_str.strip().split(',')
        interception_values = gr.get_value('interceptionValues')

        try:
            for service in service_list:
                case_id = interception_values.pop(service.strip())
                log.info(f'remove mock data [{case_id}] from request '
                         f'[{service.strip()}]')
        except Exception as e:
            message = f'[removeSomeInterceptionMock]  ' \
                      f'has KeyError! error key: {str(e)}'
            raise FlybirdsException(message, error_name=ErrorName.MockClearError)
        gr.set_value('interceptionValues', interception_values)

    @staticmethod
    def clear_interception_mock():
        interception_values = gr.get_value('interceptionValues')
        interception_values.clear()
        gr.set_value('interceptionValues', interception_values)

    # -------------------------------------------------------------------------
    # compare service requests
    # -------------------------------------------------------------------------
    @staticmethod
    def request_compare(operation, target_data_path, contains_key):
        # Call the get_server_request_body() function to get the server request information,
        # and return a dictionary object
        request_info = get_server_request_body(operation)
        actual_request_obj = None

        # If the returned request information is not None and has a postData attribute,
        # assign the postData to the actual_request_obj variable
        if request_info is not None and request_info.get('postData'):
            actual_request_obj = request_info.get('postData')

        # Output the information of actual_request_obj in the log
        log.info(f'[request_compare] actualObj:{actual_request_obj}')

        # If actual_request_obj is None, an exception is thrown
        if actual_request_obj is None:
            message = f'[request_compare] not get listener data for [{operation}]'
            raise FlybirdsException(message, error_name=ErrorName.RequestNoneError)

        # Deserialize actual_request_obj into a Python object
        if actual_request_obj.startswith('<?xml') or actual_request_obj.startswith('<'):

            try:
                # If the format is XML, parse the XML.
                actual_request_obj = xmltodict.parse(actual_request_obj)
            except ValueError:
                message = f'[xml convert] format is wrong, data:' + actual_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareXmlFormatError)

        else:
            try:
                # If the format is json, parse the json.
                actual_request_obj = json.loads(actual_request_obj)
            except ValueError:
                message = f'[json convert] format is wrong, data:' + actual_request_obj
                raise FlybirdsException(message, ErrorName.CompareJsonFormatError)

        log.info(f'[request_compare] actualObj dict:{actual_request_obj}')
        expect_request_obj = get_operate_actual_request_body(target_data_path)
        # Output the information of expect_request_obj in the log
        log.info(f'[request_compare] expectObj dict:{expect_request_obj}')

        # If expect_request_obj is None, an exception is thrown
        if expect_request_obj is None:
            message = f'[request_compare] cannot get data form path [{target_data_path}]]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)

        # If the expect_request_obj is xml file, and contains a root node, remove the root node
        if 'root' in expect_request_obj:
            expect_request_obj = expect_request_obj['root']

            # Call the convert_values() function to convert numbers and boolean values
            expect_request_obj = delete_values(expect_request_obj)
            expect_request_obj = convert_values(expect_request_obj)
            log.info(f'[request_compare] expectObj dict after deal:{expect_request_obj}')

        # Call the handle_diff() function to compare the differences between the actual request object
        # and the expected request object, and output the log
        # match_json = get_matched_json(expect_request_obj, actual_request_obj)
        # log.info(f'[request_compare] actualObj dict after match expectObj: {match_json}')
        handle_diff(actual_request_obj, expect_request_obj, operation, target_data_path, contains_key)

    @staticmethod
    def page_not_requested(operation):
        operation_list = operation.strip().split(',')
        for operation in operation_list:
            request_info = get_server_request_opetate(operation.strip())
            if request_info:
                message = f'[pageNotRequested] the request [{operation}] has been requested'
                raise FlybirdsException(message, error_name=ErrorName.RequestFoundError)
            else:
                message = f'[pageNotRequested] the request [{operation}] has not been requested'
                log.info(message)

    @staticmethod
    def page_requests_some_interfaces(operation):
        operation_list = operation.strip().split(',')
        for operation in operation_list:
            request_info = get_server_request_opetate(operation.strip())
            if request_info:
                message = f'[page requests] the request [{operation}] has been requested'
                log.info(message)
            else:
                message = f'[page requests] the request [{operation}] has not been requested'
                raise FlybirdsException(message, error_name=ErrorName.RequestNotFoundError)

    @staticmethod
    def page_wait_interface_request_finished(operation):
        pattern = re.compile('.*\/%s(\?.*)?$' % operation)
        log.info(f'pattern: {pattern}')
        ele = gr.get_value("plugin_ele")
        try:
            page_render_timeout = gr.get_frame_config_value("page_render_timeout", 30)
            # with ele.page.expect_response(pattern, timeout=float(page_render_timeout* 1000)) as response_info:
            #     pass
            with ele.page.expect_request_finished(lambda request: pattern.match(request.url)) as request_info:
                pass
            request = request_info.value
            # response_code = response.status
            if request:
                log.info(
                    f'[page wait request finished] request url: {request.url}, request postdata: {request.post_data}, request: {request}')
            else:
                message = f'[page wait request finished] the request [{operation}] has not been requested'
                raise FlybirdsException(message, error_name=ErrorName.RequestNotFoundError)
        except Exception as e:
            message = f'[page wait request finished] the request [{operation}] has error: {e}'
            log.error(message)
            raise FlybirdsException(message, error_name=ErrorName.RequestError)

    @staticmethod
    def request_query_string_compare(operation, target_data_path, contains_key):
        # Define function request_query_string_compare with two parameters, operation and target_data_path

        request_info = get_server_request_body(operation)
        # Call the get_server_request_body function to get server request information, and store it in request_info

        actual_request_obj = None
        # Initialize actual_request_obj to None

        if request_info is not None and request_info.get('postData'):
            # If request_info is not None and request_info contains a 'postData' field

            actual_request_obj = request_info.get('postData')
            # Assign the value of request_info's 'postData' field to actual_request_obj

        if actual_request_obj is None:
            # If actual_request_obj is None
            message = f'[requestQuerystringCompare] not get listener data ' \
                      f'for [{operation}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissActualRequestError)
            # Raise an exception indicating that the listener data could not be retrieved

        # Check data format
        if actual_request_obj.startswith('<?xml') or actual_request_obj.startswith('<'):
            try:
                # If the format is XML, parse the XML.
                actual_request_obj = xmltodict.parse(actual_request_obj)
            except ValueError:
                message = f'[xml convert] format is wrong, data:' + actual_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareXmlFormatError)
        else:
            try:
                # If the format is json, parse the json.
                actual_request_obj = parse_qs(actual_request_obj)
            except ValueError:
                message = f'[json convert] format is wrong, data:' + actual_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareJsonFormatError)

        file_path = os.path.join(os.getcwd(), target_data_path)
        # Get the path of the target data file and store it in file_path

        expect_request_obj = None
        # Initialize expect_request_obj to None

        if os.path.exists(file_path):
            # If the file path exists

            expect_request_obj = file_helper.read_file_from_path(file_path)
            # Read the target data file and store it in expect_request_obj

        if expect_request_obj is None:
            # If expect_request_obj is None

            message = f'[requestQuerystringCompare] cannot get data form ' \
                      f'path [{target_data_path}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)
            # Raise an exception indicating that data could not be retrieved from the specified path

        if expect_request_obj.startswith('<?xml') or expect_request_obj.startswith('<'):
            try:
                # If the format is XML, parse the XML.
                expect_request_obj = xmltodict.parse(expect_request_obj)
            except ValueError:
                message = f'[xml convert] format is wrong, data:' + expect_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareXmlFormatError)

        else:
            try:
                # If the format is json, parse the json.
                expect_request_obj = parse_qs(expect_request_obj)
            except ValueError:
                message = f'[json convert] format is wrong, data:' + expect_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareJsonFormatError)

        handle_diff(actual_request_obj, expect_request_obj, operation,
                    target_data_path, contains_key)
        # Call the handle_diff function to compare the difference between the actual request object
        # and the expected request object, passing in the parameters operation and target_data_path.

    @staticmethod
    def request_compare_value(operation, target_path, expect_value):
        # Call the get_request_target_values() function to get the target values
        target_values = get_request_target_values(operation, target_path)
        # If the target data does not exist, raise an exception.
        if len(target_values) == 0:
            message = f'[requestCompareValue] cannot get the value from ' \
                      f'path [{target_path}] of [{operation}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)

        # If the actual value is not equal to the expected value, raise an exception.
        if expect_value == "[@@空@@]" or expect_value == "@@空@@":
            expect_value = ""
        if str(target_values[0]) != expect_value:
            message = f'value not equal, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], but expect value:' \
                      f'[{expect_value}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)


    @staticmethod
    def request_compare_value_is_none(operation, target_path):
        # Call the get_request_target_values() function to get the target values
        target_values = get_request_target_values(operation, target_path)
        # If the target data does not exist, raise an exception.
        if len(target_values) == 0 or target_values is None:
            return
        else:
            message = f'value not equal, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], but expect value:' \
                      f'[None]'
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)

    @staticmethod
    def request_compare_includes_value(operation, target_path, expect_value):
        # Call the get_request_target_values() function to get the target values
        target_values = get_request_target_values(operation, target_path)

        # If the target data does not exist, raise an exception.
        if len(target_values) == 0:
            message = f'[requestCompareValue] cannot get the value from ' \
                      f'path [{target_path}] of [{operation}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)

        # If the actual value is not equal to the expected value, raise an exception.
        if expect_value == "[@@空@@]" or expect_value == "@@空@@":
            expect_value = ""
        if expect_value in str(target_values[0]):
            message = f'actual value includes expect value, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], expect value:' \
                      f'[{expect_value}]'
            log.info(message)

        else:
            message = f'actual value not includes expect value, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], expect value:' \
                      f'[{expect_value}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)

    @staticmethod
    def request_compare_not_includes_value(operation, target_path, expect_not_contain_value):
        # Call the get_request_target_values() function to get the target values
        target_values = get_request_target_values(operation, target_path)

        # If the target data does not exist, raise an exception.
        if len(target_values) == 0:
            message = f'[requestCompareValue] cannot get the value from ' \
                      f'path [{target_path}] of [{operation}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)

        if expect_not_contain_value not in str(target_values[0]):
            message = f'actual value includes expect value, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], expect value:' \
                      f'[{expect_not_contain_value}]'
            log.info(message)

        else:
            message = f'actual value includes not expect value, service [{operation}] request ' \
                      f'parameter [{target_path}] actual value:' \
                      f'[{target_values[0]}], expect value:' \
                      f'[{expect_not_contain_value}]'
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)

    @staticmethod
    def compare_images(context, target_element, compared_picture_path, threshold=None):

        # default threshold value
        threshold = 0.95

        # Convert parameter string to dictionary
        param_dict = dsl_helper.params_to_dic(target_element, "target_element")

        # Get path from dictionary
        target_element = param_dict["target_element"]

        if "threshold" in param_dict.keys():
            threshold = param_dict["threshold"]

            try:
                threshold = float(threshold)
            except ValueError:
                message = f'[threshold] is not int or float value'
                raise FlybirdsException(message)

        ele = gr.get_value("plugin_ele")
        locator, timeout = ele.wait_for_ele(context, target_element)
        target_image = locator.screenshot()
        target_image_io = Image.open(io.BytesIO(target_image))

        file_path = os.path.join(os.getcwd(), compared_picture_path)
        directory = os.path.dirname(file_path)
        filename = os.path.basename(file_path)

        uuid = uuid_helper.create_uuid()

        old_filename = f"{os.path.splitext(filename)[0]}_{uuid}_old.png"
        target_image_path = os.path.join(directory, old_filename)
        target_image_io.save(target_image_path)

        if threshold is None:
            threshold = 0.95

        file_path1 = target_image_path
        file_path2 = os.path.join(os.getcwd(), compared_picture_path)

        similar = False
        # Read images
        image1 = cv2.imread(file_path1)
        if image1 is None:
            message = f'[target_picture_path] is invalid'
            raise FlybirdsException(message)

        image2 = cv2.imread(file_path2)
        if image2 is None:
            message = f'[target_picture_path] is invalid'
            raise FlybirdsException(message)

        image1_width = image1.shape[1]
        image1_height = image1.shape[0]

        image2_width = image2.shape[1]
        image2_height = image2.shape[0]

        width_diff = abs(image1_width - image2_width)
        height_diff = abs(image1_height - image2_height)

        desired_width = max(image1_width, image2_width)
        desired_height = max(image1_height, image2_height)

        # Resize images to a unified resolution
        resized_image1 = cv2.resize(image1, (desired_width, desired_height))
        resized_image2 = cv2.resize(image2, (desired_width, desired_height))

        # Convert images to grayscale
        gray1 = cv2.cvtColor(resized_image1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(resized_image2, cv2.COLOR_BGR2GRAY)

        # Calculate histograms
        hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
        hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])

        # Calculate histogram similarity
        hist_diff = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)

        # Check if images are similar based on threshold
        if hist_diff >= threshold:
            similar = True
            message = f'Image diff percent [{hist_diff}] request ' \
                      f'is more than threshold [{threshold}]'
            log.info(message)
        else:
            directory = os.path.dirname(file_path1)
            filename = os.path.basename(file_path1)
            diff_filename = f"{os.path.splitext(filename)[0]}_diff.png"
            diff_file_path = os.path.join(directory, diff_filename)
            step_index = context.cur_step_index - 1
            diff_file_path = BaseScreen.screen_link_to_behave_step(context.scenario, step_index, "screen_", True)
            # Calculate difference image
            diff = cv2.absdiff(gray1, gray2)

            # Threshold the difference image
            threshold_value, threshold_diff = cv2.threshold(diff, 50, 255, cv2.THRESH_BINARY)

            # Find contours in the threshold image
            contours, hierarchy = cv2.findContours(threshold_diff, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Mark the difference regions in image2 with rectangles
            for contour in contours:
                x, y, w, h = cv2.boundingRect(contour)
                cv2.rectangle(resized_image1, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imencode('.png', resized_image1)[1].tofile(diff_file_path)

            message = f'Diff percentage of image [{threshold}] ' \
                      f'has been saved in path [{diff_file_path}]'

        return similar, resized_image1

    @staticmethod
    def compare_dom_element_text(context, target_ele, compared_text_path):
        same = False
        diff = ''

        # Convert parameter string to dictionary
        param_dict = dsl_helper.params_to_dic(target_ele, "target_element")

        # Get path from dictionary
        target_element = param_dict["target_element"]

        ele = gr.get_value("plugin_ele")
        locator, timeout = ele.wait_for_ele(context, target_element)
        target_text = locator.inner_text()

        text1 = target_text

        file_path = os.path.join(os.getcwd(), compared_text_path)
        # Get the path of the target data file and store it in file_path

        text2 = None
        # Initialize expect_request_obj to None

        if os.path.exists(file_path):
            # If the file path exists

            text2 = file_helper.read_file_from_path(file_path)
            # Read the target data file and store it in expect_request_obj

        if text2 is None:
            # If expect_request_obj is None

            message = f'[requestQuerystringCompare] cannot get data form ' \
                      f'path [{compared_text_path}]'
            raise FlybirdsException(message, ErrorName.RequestNoneError)
            # Raise an exception indicating that data could not be retrieved from the specified path

        # Compare the text content of the two DOM elements
        if text1 == text2:
            same = True
            message = f'The text of the two UI elements are the same' \
                      f' [{text1}]:' \
                      f' [{compared_text_path}] - [{text2}]:'
            log.info(message)
        else:
            message = f'The text of the two pages are different as' \
                      f' [{text1}]:' \
                      f' [{compared_text_path}] - [{text2}]:'
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)

        return same, diff

    @staticmethod
    def call_external_party_api(method, url, data=None, headers=None):
        # Initialize variables to hold the content and headers
        datacontent = None
        dataheaders = None

        # Try to parse the data and headers as JSON
        try:
            datacontent = json.loads(data)
            dataheaders = json.loads(headers)
        except ValueError:
            message = f'The content of data and headers is not json format: ' \
                      f' [{data}] - [{headers}]'
            raise FlybirdsException(message, error_name=ErrorName.RequestParamsError)

        # Set the content and headers to None if they are empty
        if len(datacontent) == 0:
            datacontent = None

        if len(dataheaders) == 0:
            dataheaders = None

        try:
            response = requests.request(method.upper(), url, params=datacontent, json=data, headers=dataheaders,
                                        verify=False)
            # Check if the response was successful
            response.raise_for_status()
            # Return the response text
            return response.text
        except ValueError:
            message = f'The contents post is invalid: ' \
                      f' [{url}] - [{data}] - [{headers}]:'
            raise FlybirdsException(message, error_name=ErrorName.RequestParamsError)

    @staticmethod
    def open_web_request_mock(service_str, mock_case_id_str, mock_key_list_str, request_mock_key_value: list):
        if service_str is None or mock_case_id_str is None or mock_key_list_str is None:
            log.error('[addSomeInterceptionMock] param can not be none. ')
            return

        service_list = service_str.strip().split(',')
        mock_case_id_list = mock_case_id_str.strip().split(',')
        mock_path_list = mock_key_list_str.strip().split('|||')

        mock_data_path = os.path.join(os.getcwd(), "mockCaseData")
        if gr.get_mock_base_path() is not None and len(gr.get_mock_base_path().strip()) > 0:
            mock_data_path = os.path.join(mock_data_path, gr.get_mock_base_path())
        if len(service_list) != len(mock_case_id_list):
            message = f"serviceCount[{service_str}] not equal " \
                      f"mockCaseCount[{mock_case_id_str}]"
            raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)

        if len(service_list) != len(mock_path_list):
            message = f"serviceCount[{service_str}] not equal " \
                      f"pathCount[{mock_case_id_str}]"
            raise FlybirdsException(message, error_name=ErrorName.MockCountNotMatchError)

        interception_values = request_mock_key_value
        for i, service in enumerate(service_list):
            mock_data = read_json_data_by_key(mock_data_path, mock_case_id_list[i].strip()).get(
                mock_case_id_list[i].strip())
            if mock_data is None:
                log.info(f"open request body match mock case:{mock_case_id_list[i]} failed, mock data is None")
                continue
            if mock_data.get("flybirdsMockResponse") is None:
                log.info(
                    f"open request body match mock case:{mock_case_id_list[i]} failed, mock data response is None")
                continue
            if mock_data.get("flybirdsMockRequest") is None:
                log.info(
                    f"open request body match mock case:{mock_case_id_list[i]} failed, mock data request is None")
                continue
            if service is not None and len(service.strip()) > 0:
                if ":" in service:
                    split_service = service.split(":")
                    if split_service[0].strip() == "reg":
                        interception_values.append({
                            "max": 1,
                            "key": split_service[1].strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "reg",
                            "mockType": "request",
                            "requestPathes": mock_path_list[i].strip().split(','),
                            "requestBody": mock_data.get("flybirdsMockRequest"),
                            "mockStep": gr.get_value("stepName", None)
                        })
                    elif split_service[0].strip() == "equ":
                        interception_values.append({
                            "max": 1,
                            "key": split_service[1].strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "equ",
                            "mockType": "request",
                            "requestPathes": mock_path_list[i].strip().split(','),
                            "requestBody": mock_data.get("flybirdsMockRequest"),
                            "mockStep": gr.get_value("stepName", None)
                        })
                    else:
                        interception_values.append({
                            "max": 1,
                            "key": service.strip(),
                            "value": mock_case_id_list[i].strip(),
                            "method": "contains",
                            "mockType": "request",
                            "requestPathes": mock_path_list[i].strip().split(','),
                            "requestBody": mock_data.get("flybirdsMockRequest"),
                            "mockStep": gr.get_value("stepName", None)
                        })
                else:
                    interception_values.append({
                        "max": 1,
                        "key": service.strip(),
                        "value": mock_case_id_list[i].strip(),
                        "method": "contains",
                        "mockType": "request",
                        "requestPathes": mock_path_list[i].strip().split(','),
                        "requestBody": mock_data.get("flybirdsMockRequest"),
                        "mockStep": gr.get_value("stepName", None)
                    })


def get_request_target_values(operation, target_path):
    # # Call function get_server_request_body to get request_info
    request_info = get_server_request_body(operation)

    # Initialize data variable as None.
    data = None
    # Get postData data.
    if request_info and request_info.get('postData'):
        data = request_info.get('postData')
    # If postData data is not found, raise an exception.
    if data is None:
        message = f'[requestCompareValue] not get listener data for ' \
                  f'[{operation}]'
        raise FlybirdsException(message, error_name=ErrorName.CompareMissActualRequestError)

    # Check the data format.
    if data.startswith('<?xml') or data.startswith('<'):
        try:
            # If the format is XML, parse the XML.
            root = et.fromstring(data)

            # Parse the XML path expression.
            target_elements = root.findall(target_path)
            # Get the target data from XML.
            target_values = [elem.text for elem in target_elements]
            # Print a log message.
            log.info(f'[requestCompareValue] get xmlPathData: {target_values}')
            return target_values
        except ValueError:
            message = f'[xml convert] format is wrong, data:' + data
            raise FlybirdsException(message, error_name=ErrorName.CompareXmlFormatError)

    else:
        try:
            # If the format is not XML, it is assumed to be JSON. Parse the JSON.
            # Parse the data into a dictionary.
            json_data = json.loads(data)
            # Parse the JSON path expression.
            json_path_expr = parse_path(target_path)
            # Get the target data from JSON.
            target_values = [match.value for match in json_path_expr.find(json_data)]
            # Print a log message.
            log.info(f'[requestCompareValue] get jsonPathData: {target_values}')
            return target_values
        except ValueError:
            message = f'[json convert] format is wrong, data:' + data
            raise FlybirdsException(message, error_name=ErrorName.CompareJsonFormatError)


def get_operate_actual_request_body(target_data_path):
    expect_request_obj = None
    # Get the file path
    file_path = os.path.join(os.getcwd(), target_data_path)

    # If the file path exists, read data from the file and assign it to expect_request_obj
    if os.path.exists(file_path):

        expect_request_obj = file_helper.read_file_from_path(file_path)
        if expect_request_obj.startswith('<?xml') or expect_request_obj.startswith('<'):
            try:
                # If the format is XML, parse the XML.
                expect_request_obj = xmltodict.parse(expect_request_obj)
            except ValueError:
                message = f'[xml convert] format is wrong, data:' + expect_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareXmlFormatError)

        else:
            try:
                # If the format is json, parse the json.
                expect_request_obj = file_helper.get_json_from_file_path(file_path)
            except ValueError:
                message = f'[json convert] format is wrong, data:' + expect_request_obj
                raise FlybirdsException(message, error_name=ErrorName.CompareJsonFormatError)

    else:
        message = f'[request_compare] expect_request_obj not get file from [{file_path}]'
        raise FlybirdsException(message, error_name=ErrorName.CompareMissExpectRequestError)
    return expect_request_obj


def get_server_request_body(service):
    interception_request = gr.get_value('interceptionRequest')
    if interception_request:
        return interception_request.get(service)
    return None


def get_server_request_opetate(service):
    operate_record = gr.get_value('operate_record')
    if operate_record:
        return operate_record.get(service)
    return None


def handle_ignore_node(service):
    exclude_paths = []
    exclude_regex_paths = []
    service_ignore_nodes = gr.get_service_ignore_nodes(service)
    if service_ignore_nodes is None:
        return exclude_paths, exclude_regex_paths
    for item in service_ignore_nodes:
        if 'regex' in item:
            regex_item = item.split('regex:')[-1].strip()
            exclude_regex_paths.append(regex_item)
        else:
            path = 'root'
            for level_item in item.split('.'):
                # identifies whether the item is an array
                level_item = level_item.strip()
                item_is_array = re.search(r"([^\[\]]+)\[(\d+)\]",
                                          level_item) is not None

                if item_is_array:
                    property_name = "['" + re.search(r"([^\[\]]+)\[(\d+)\]",
                                                     level_item).group(
                        1) + "']"
                    array_index = ''.join(
                        list(map(
                            lambda x: "[" + x + "]",
                            re.findall(r"\[(\d+)\]", level_item))
                        )
                    )
                    item_str = property_name + array_index
                else:
                    item_str = "['" + level_item + "']"
                path += item_str
            exclude_paths.append(path.strip())
    return exclude_paths, exclude_regex_paths


# Get json data according to refer_json
def get_matched_json(refered_json, matched_json):
    if isinstance(refered_json, dict):
        matched = {}
        for key in refered_json:
            if key in matched_json:
                matched[key] = get_matched_json(refered_json[key], matched_json[key])
        return matched
    elif isinstance(refered_json, list) and refered_json:
        if all(isinstance(subitem, list) for subitem in refered_json):
            matched_items = []
            for item in matched_json:
                if isinstance(item, list) and all(isinstance(subitem, list) for subitem in item):
                    matched_items.append(
                        [get_matched_json(refered_json[i], item[i]) for i in range(min(len(refered_json), len(item)))])
                elif isinstance(item, list):
                    matched_items.append(get_matched_json(refered_json, item))
                else:
                    matched_items.append(item)
            return matched_items
        else:
            matched_items = []
            for ref_item in refered_json:
                for item in matched_json:
                    if isinstance(item, dict):
                        matched_items.append(get_matched_json(ref_item, item))
                    elif isinstance(item, list) and all(isinstance(subitem, list) for subitem in item):
                        matched_items.append([get_matched_json(ref_item, subitem) for subitem in item])
                    elif isinstance(item, list):
                        matched_items.append(get_matched_json(refered_json, item))
                    else:
                        matched_items.append(item)
            return matched_items
    else:
        return matched_json


def handle_diff(actual_request_obj, expect_request_obj, operation,
                target_file_name, contains_key):
    log.info('run in handle_diff')
    exclude_paths, exclude_regex_paths = handle_ignore_node(operation)
    ignore_order = gr.get_web_info_value("ignore_order", False)

    # diffs with jsons
    diff = DeepDiff(actual_request_obj, expect_request_obj,
                    ignore_order=ignore_order, verbose_level=2,
                    exclude_paths=exclude_paths,
                    exclude_regex_paths=exclude_regex_paths)
    if diff:
        format_diff = json.dumps(diff, indent=2)
        message = f'Difference when comparing service request ' \
                  f'[{operation}] with [{target_file_name}]. ' \
                  f'\n Difference node:\n {format_diff} \n'
        raise FlybirdsException(message, error_name=ErrorName.CompareNotEqualError)
    log.info(f'compare the service request [{operation}] with '
             f'[{target_file_name}], the result is the same.')


def get_case_response_body(case_id):
    operation_module = gr.get_value("projectScript").custom_operation
    get_mock_case_body = getattr(operation_module, "get_mock_case_body")
    mock_case_body = get_mock_case_body(case_id)
    if mock_case_body is not None:
        log.info('[get_case_response_body] successfully get mockCaseBody '
                 'from custom operation')
        return mock_case_body
    log.warn('[get_case_response_body] cannot get mockCaseBody from custom '
             'operation. Now try to get from the folder mockCaseData.')
    # read from folder mockCaseData
    mock_data_path = os.path.join(os.getcwd(), "mockCaseData")
    if gr.get_mock_base_path() is not None and len(gr.get_mock_base_path().strip()) > 0:
        mock_data_path = os.path.join(mock_data_path, gr.get_mock_base_path())
    all_mock_data = read_json_data(mock_data_path)
    if all_mock_data.get(case_id):
        log.info('[get_case_response_body] successfully get mockCaseBody '
                 'from folder mockCaseData')
        return all_mock_data.get(case_id)
    log.warn('[get_case_response_body] cannot get mockCaseBody from folder '
             'mockCaseData.')
    return


# 定义函数 convert_values()，将值为数字或布尔类型的字符串转换为对应的数字或布尔值
def convert_values(data):
    for key, value in data.items():
        if key != 'head' and value is not None:
            if isinstance(value, dict):
                convert_values(value)
            elif isinstance(value, str):
                if value.lower() == 'true':
                    data[key] = True
                elif value.lower() == 'false':
                    data[key] = False
                elif value.isdigit():
                    data[key] = int(value)
    return data


# 定义函数 convert_values()，将值为None转为''
def delete_values(data):
    for key, value in data.items():
        if value is None:
            data[key] = ''
        elif isinstance(value, dict):
            delete_values(value)
        elif isinstance(value, str):
            log.info("String dict value", value)
    return data
