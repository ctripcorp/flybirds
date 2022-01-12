# -*- coding: utf-8 -*-
"""
flybirds common error
"""


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
