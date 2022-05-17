# -*- coding: utf-8 -*-
"""
flybirds common error
"""
import flybirds.core.global_resource as gr


class FlybirdNotFoundException(Exception):
    """
    not find flybirds
    """

    def __init__(self, message, select_dic, error=None):
        message = f"selectors={str(select_dic)} {message}"
        if error is not None:
            message = f"{message} innerErr:{error}"
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class PositionNotChangeException(Exception):
    """
    position not change
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdCallMethodParamsException(Exception):
    """
    params error
    """

    def __init__(self, method, param_name):
        message = f"call method:{method} has invalid params:{param_name}"
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdEleExistsException(Exception):
    """
    ele not exists
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdVerifyException(Exception):
    """
    verify error
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdPositionChanging(Exception):
    """
    position changing
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)


class ScreenRecordException(Exception):
    """
    screen record error
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdsVerifyEleException(Exception):
    """
    timeout error
    """

    def __init__(self, message=None, selector=None):
        super().__init__()
        if message is not None:
            self.message = message
        elif selector is not None:
            self.message = self.print_message(selector)

    def __str__(self):
        return str(self.message)

    @staticmethod
    def print_message(param):
        default_timeout = gr.get_frame_config_value("wait_ele_timeout", 30)
        message = f'Timeout {default_timeout * 1000}ms exceeded.\n'
        message += '=' * 20 + ' logs ' + '=' * 20
        message += f'\nwaiting for selector "{param}"\n'
        message += '=' * 46
        return message


class FlybirdsException(Exception):
    """
     flybirds exception base class
    """

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)
