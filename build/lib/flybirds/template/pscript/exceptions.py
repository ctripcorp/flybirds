# -*- coding: utf-8 -*-
"""
This module is used for custom exceptions
"""


class CustomApiException(Exception):

    def __init__(self, api_name, result_code):
        message = 'platform interface{} has failed，resultCode: {}' \
            .format(api_name, result_code)
        super(CustomApiException, self).__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)
