# -*- coding: utf-8 -*-
"""
flybirds common error
"""
from enum import Enum
from typing import Dict
from urllib.parse import urlsplit, urlparse, ParseResult

import flybirds.core.global_resource as gr
from flybirds.core.global_context import GlobalContext


class ErrorName(Enum):
    InvalidCharacterError: str = "InvalidCharacterError"
    InvalidSelectorError: str = "InvalidSelectorError"
    InvalidArgumentError: str = "InvalidArgumentError"
    InvalidElementStateError: str = "InvalidElementStateError"
    ElementNotVisibleError: str = "ElementNotVisibleError"
    ElementCannotBeFilledError: str = "ElementCannotBeFilledError"
    MultiElementError: str = "MultiElementError"
    ElementError: str = "ElementError"
    ElementFoundError: str = "ElementFoundError"
    ElementNotFoundError: str = "ElementNotFoundError"
    TextFoundError: str = "TextFoundError"
    TextNotFoundError: str = "TextNotFoundError"
    AttributeNotFoundError: str = "AttributeNotFoundError"
    AttributeFoundError: str = "AttributeFoundError"
    AttributeNotEqualError: str = "AttributeNotEqualError"
    TagFountError: str = "TagFountError"
    MockCountNotMatchError: str = "MockCountNotMatchError"
    RequestParamsError: str = "RequestParamsError"
    RequestNoneError: str = "RequestNoneError"
    CompareNotEqualError: str = "CompareNotEqualError"
    RequestFoundError: str = "RequestFoundError"
    RequestNotFoundError: str = "RequestNotFoundError"
    RequestError: str = "RequestError"
    MockClearError: str = "MockClearError"
    CompareXmlFormatError: str = "CompareXmlFormatError"
    CompareJsonFormatError: str = "CompareJsonFormatError"
    CompareMissExpectRequestError: str = "CompareMissExpectRequestError"
    CompareMissActualRequestError: str = "CompareMissActualRequestError"
    PageNotFoundError: str = "PageNotFoundError"
    UnknownError: str = "UnknownError"
    PageLoadError: str = "PageLoadError"
    ServiceNameParamsNoneError: str = "ServiceNameParamsNoneError"
    UrlNotFoundError: str = "UrlNotFoundError"
    UrlNotMatchError: str = "UrlNotMatchError"
    ParamIsNoneError: str = "ParamIsNoneError"
    PositionNotChangeException: str = "PositionNotChangeException"
    PositionChangeException: str = "PositionChangeException"
    FlybirdInputException: str = "FlybirdInputException"
    LLmCheckPageUIError: str = "LLmCheckPageUIError"


error_map = {
    "element": {
        "Invalid character: the input contains": "InvalidCharacterError",
        "`Unsupported token": "InvalidSelectorError",
        "`Unexpected token": "InvalidSelectorError",
        "Error while parsing selector": "InvalidSelectorError",
        "Malformed selector:": "InvalidSelectorError",
        "Frames are not allowed inside": "InvalidSelectorError",
        " selector cannot be first": "InvalidSelectorError",
        "Only one of the selectors can capture using * modifier": "InvalidSelectorError",
        "Unexpected end of selector while parsing selector": "InvalidSelectorError",
        "Invalid escape char": "InvalidSelectorError",
        "attribute is only supported for roles:": "InvalidSelectorError",
        " must be one of ": "InvalidSelectorError",
        " does not support ": "InvalidSelectorError",
        "attribute must be compared to a number": "InvalidSelectorError",
        "attribute must have a value": "InvalidSelectorError",
        "attribute must be a string or a regular expression": "InvalidSelectorError",
        "Unknown attribute": "InvalidSelectorError",
        "Role must not be empty": "InvalidSelectorError",
        "Please keep customCSSNames in sync with evaluator engines:": "InvalidSelectorError",
        "Unsupported combinator": "InvalidSelectorError",
        "Selector engine should implement ": "InvalidSelectorError",
        "Unknown selector engine ": "InvalidSelectorError",
        "engine expects non-empty selector list": "InvalidSelectorError",
        "engine expects no arguments": "InvalidSelectorError",
        "engine expects a single string": "InvalidSelectorError",
        "engine expects a regexp body and optional regexp flags": "InvalidSelectorError",
        "engine expects a selector list and optional maximum distance in pixels": "InvalidSelectorError",
        "engine expects a one-based index as the last argument": "InvalidSelectorError",
        "Unknown selector kind": "InvalidSelectorError",
        "Unknown engine ": "InvalidSelectorError",
        "Can't query n-th element in a request with the capture.": "InvalidSelectorError",
        "Internal error: there should not be a capture in the selector.": "InvalidSelectorError",
        "Malformed attribute selector:": "InvalidSelectorError",
        "Internal error, unknown internal:control selector": "InvalidSelectorError",
        "Node is not queryable.": "ElementNotVisibleError",
        "cannot be filled": "ElementCannotBeFilledError",
        "Cannot type text into input[type=number]": "ElementCannotBeFilledError",
        "Malformed value": "ElementFailToWriteError",
        "Element is not an <input>, <textarea> or [contenteditable] element": "ElementCannotBeFilledError",
        "strict mode violation: ": "MultiElementError",
        "Not a select element with a multiple attribute": "ElementError",
        "Not an input element": "ElementError",
        "Element is not a checkbox": "ElementError",
        "Element is not connected": "ElementError",
        "Node is not an element": "ElementError",
        "Unknown expect matcher: ": "InvalidSelectorError"
    },
    "page": {

    },
    "mock": {

    }
}


class FlybirdInputException(Exception):
    """
    not find flybirds
    """
    error_name = ErrorName.FlybirdInputException

    def __init__(self, message, select_dic):
        message = f"selectors={str(select_dic)} {message}"
        if error is not None:
            message = f"{message} innerErr:{error}"
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdNotFoundException(Exception):
    """
    not find flybirds
    """
    error_name = ErrorName.ElementNotFoundError

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
    error_name = ErrorName.PositionNotChangeException

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdCallMethodParamsException(Exception):
    """
    params error
    """
    error_name = ErrorName.InvalidArgumentError

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
    error_name = ErrorName.ElementFoundError

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdVerifyException(Exception):
    """
    verify error
    """
    error_name: str
    expect: str
    actual: str

    def __init__(self, message, error_name=ErrorName.UnknownError, expect=None, actual=None):
        super().__init__()
        self.message = message
        self.error_name = error_name
        self.expect = expect
        self.actual = actual

    def __str__(self):
        return str(self.message)


class FlybirdCheckPageUIException(Exception):
    """
    check page UI error
    """
    error_name = ErrorName.LLmCheckPageUIError

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdNetworkTimeOutException(Exception):
    """
    check page UI error
    """
    error_name = ErrorName.LLmCheckPageUIError

    def __init__(self, message):
        super().__init__()
        self.message = message

    def __str__(self):
        return str(self.message)


class FlybirdPositionChanging(Exception):
    """
    position changing
    """
    error_name = ErrorName.PositionChangeException

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
    error_name: str

    def __init__(self, message=None, selector=None, error_name=ErrorName.UnknownError):
        super().__init__()
        self.error_name = error_name
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
    error_name: str

    def __init__(self, message, error_name=ErrorName.UnknownError):
        super().__init__()
        self.error_name = error_name
        self.message = message

    def __str__(self):
        return str(self.message)


class ErrorFlag:
    equ: str = "equ"
    neq: str = "neq"
    contains: str = "contains"
    not_contains: str = "not_contains"
    exist: str = "exist"
    not_exist: str = "not_exist"
    fource: str = "fource"
    text_equ: str = "text_equ"
    text_neq: str = "text_neq"
    text_contains: str = "text_contains"
    text_not_contains: str = "text_not_contains"


class ActionType:
    press: str = "press"
    hover: str = "hover"
    swipe: str = "swipe"
    input: str = "input"
    clear: str = "clear"
    disappear: str = "disappear"
    move: str = "move"
    select: str = "select"
    upload: str = "upload"
    setPageSize: str = "setPageSize"
    switchPage: str = "switchPage"
    setCookie: str = "setCookie"
    setHeader: str = "setHeader"
    setSessionStorage: str = "setSessionStorage"
    setLocalStorage: str = "setLocalStorage"
    getCookie: str = "getCookie"
    getStorage: str = "getStorage"
    getSessionStorage: str = "getSessionStorage"
    returnPrePage: str = "returnPrePage"
    goForward: str = "goForward"
    addRequestFilterKey: str = "addRequestFilterKey"
    addMockKey: str = "addMockKey"
    addCompareData: str = "addCompareData"
    close_dialog: str = "close_dialog"


error_flag_map = {
    f"{ErrorFlag.equ}": {"verify": "等于", "error": "不等于"}
    , f"{ErrorFlag.neq}": {"verify": "不等于", "error": "等于"}
    , f"{ErrorFlag.contains}": {"verify": "包含", "error": "不包含"}
    , f"{ErrorFlag.not_contains}": {"verify": "不包含", "error": "包含"}
    , f"{ErrorFlag.exist}": {"verify": "存在", "error": "不存在"}
    , f"{ErrorFlag.not_exist}": {"verify": "不存在", "error": "存在"}
    , f"{ErrorFlag.fource}": "fource"
    , f"{ErrorFlag.text_equ}": {"verify": "文本等于", "error": "文本不等于"}
    , f"{ErrorFlag.text_neq}": {"verify": "文本不等于", "error": "文本等于"}
    , f"{ErrorFlag.text_contains}": {"verify": "文本包含", "error": "文本不包含"}
    , f"{ErrorFlag.text_not_contains}": {"verify": "文本不包含", "error": "文本包含"}
}


def get_error_msg(exception):
    if hasattr(exception, "message"):
        return exception.message
    else:
        return str(exception)


def get_error_type(exception: Exception, selector, method, error_group="element") -> Dict:
    error_type = None
    for error in error_map.get(error_group):
        if error in get_error_msg(exception):
            error_type = error_map["element"][error]
            break
    if method == "goto":
        error_type = ErrorName.PageLoadError
        error_group = "url"
    if error_group == "element":
        if error_type is None:
            error_type = ErrorName.ElementNotFoundError
    setattr(exception, "error_name", error_type)
    setattr(exception, "flybirds_ele_error", {
        "errorName": error_type,
        "selector": selector,
        "method": method
    })


def ele_error_msg_parse(exception: Exception, config: Dict):
    if exception.error_name == ErrorName.ElementNotFoundError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} not find"}
    elif exception.error_name == ErrorName.ElementNotVisibleError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} not visible"}
    elif exception.error_name == ErrorName.ElementCannotBeFilledError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} cannot be filled"}
    elif exception.error_name == ErrorName.InvalidSelectorError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} is invalid"}
    elif exception.error_name == ErrorName.MultiElementError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} find multi elements"}
    elif exception.error_name == ErrorName.PageLoadError:
        return {"errorName": exception.flybirds_ele_error.get("errorName"),
                "error": f"{exception.flybirds_ele_error.get('selector')} page load error"}

    return common_error_parse(exception, config)


def common_error_parse(exception: Exception, config: Dict):
    error_msg = None
    error_type = None
    try:
        error_type = exception.error_name
        if error_type is None:
            error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)

    except:
        error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    return {"errorName": error_type, "error": error_msg}


def ele_verify_error_parse(exception: Exception, config: Dict):
    error_msg = None
    error_type = None
    try:
        error_type = exception.error_name
        selectors = config.get("selectors")
        verify = config.get("verify")
        error_group = "element"
        if error_type is None:
            error_type = ErrorName.UnknownError
            error_msg = get_error_msg(exception)
        else:
            verify_error = error_flag_map.get(verify.get("type")).get("error")
            for selector in selectors.get("path"):
                error_msg = f"{selector.get('name')} {selector.get('value')}-->"

            error_msg = error_msg.strip("-->")
            error_msg = f"{verify_error} {error_msg}"
    except:
        error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    return {"errorName": error_type, "error": error_msg}


def ele_verify_attr_error_parse(exception: Exception, config: Dict):
    error_msg = None
    error_type = None
    try:
        error_type = exception.error_name
        if error_type is None:
            error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)

    except:
        error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    return {"errorName": error_type, "error": error_msg}


def ele_verify_text_error_parse(exception: Exception, config: Dict):
    error_msg = None
    error_type = None
    try:
        error_type = exception.error_name
        if error_type is None:
            error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)

    except:
        error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    return {"errorName": error_type, "error": error_msg}


def page_url_verify(exception: Exception, config: Dict):
    error_msg = None
    error_type = None
    try:
        error_type = exception.error_name
        if error_type is None:
            error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    except:
        error_type = ErrorName.UnknownError
        error_msg = get_error_msg(exception)
    return {"errorName": error_type, "error": error_msg}


def set_page_info(context):
    page = None
    url = None
    try:
        if hasattr(context, "flybirds_report_config"):
            config = context.flybirds_report_config
            if config is not None:
                if config.get("group") == "url":
                    try:
                        if config is not None and config.get("selectors") and config.get("selectors").get(
                                "path") is not None and len(config.get("selectors").get("path")) > 0 and \
                                config.get("selectors").get("path")[0].get("value") is not None:
                            parsed_url = urlparse(config.get("selectors").get("path")[0].get("value").strip())
                            url = ParseResult("", "", parsed_url.path, parsed_url.params, parsed_url.query,
                                              parsed_url.fragment).geturl()
                            page = parsed_url.path
                    except:
                        page = config.get("selectors").get("path")[0].get("url")
                        url = config.get("selectors").get("path")[0].get("url")
                    GlobalContext.set_global_cache("flybirds_page_info", {"page": page, "url": url})
    except:
        pass


def get_step_group(context):
    try:
        if hasattr(context, "flybirds_report_config"):
            config = context.flybirds_report_config
            return context.flybirds_report_config.get('group')
        return "unknown"
    except:
        return "unknown"


def get_step_selector(context):
    try:
        if hasattr(context, "flybirds_report_config"):
            config = context.flybirds_report_config
            return context.flybirds_report_config.get('selectors').get("path")[0].get("value")
        return "unknown"
    except:
        return None


def ele_error_parse(context, step):
    exception = None
    config = None
    try:
        exception = step.exception
        if hasattr(context, "flybirds_report_config"):
            config = context.flybirds_report_config
            if config is not None:
                if config.get("group") == "url":
                    return ele_error_msg_parse(exception, config)

        if hasattr(exception, "flybirds_ele_error"):
            if hasattr(exception,
                       "error_name") and exception.error_name is not None and exception.flybirds_ele_error.get(
                "selector") is not None:
                return ele_error_msg_parse(exception, config)

            return common_error_parse(exception, config)
        elif not hasattr(exception, "flybirds_ele_error") and hasattr(exception, "error_name"):
            return globals()[config.get("verify_function")](exception, config)
        else:
            return {"errorName": ErrorName.UnknownError, "error": get_error_msg(exception)}
    except:
        return {"errorName": ErrorName.UnknownError, "error": get_error_msg(exception)}


def set_error_info_cache(context, step):
    step_error_info = None
    if GlobalContext.get_global_cache("stepErrorInfo") is not None:
        step_error_info = GlobalContext.get_global_cache("stepErrorInfo")
    else:
        step_error_info = {}

    try:
        step_error_info["stepDef"] = context._runner.step_registry.find_step_definition(step).string
    except:
        step_error_info["stepDef"] = step.name

    try:
        if GlobalContext.get_global_cache("flybirds_page_info") is not None:
            step_error_info["page"] = GlobalContext.get_global_cache("flybirds_page_info").get("page")
            step_error_info["url"] = GlobalContext.get_global_cache("flybirds_page_info").get("url")
    except:
        step_error_info["page"] = None
        step_error_info["url"] = None
    try:
        group = get_step_group(context)
        selector = get_step_selector(context)
        error_info = ele_error_parse(context, step)
        error = step.exc_traceback.tb_frame.f_locals.get("error")
        step_error_info["errorMsg"] = error_info.get("error")
        step_error_info["errorGroup"] = group
        if isinstance(error_info.get("errorName"), str):
            step_error_info["errorType"] = error_info.get("errorName")
        else:
            step_error_info["errorType"] = error_info.get("errorName").value
        step_error_info["selector"] = selector
        step_error_info["traceBack"] = error

    except:
        step_error_info["errorMsg"] = ErrorName.UnknownError.value
        step_error_info["errorGroup"] = "unknown"
        step_error_info["errorType"] = ErrorName.UnknownError.value
        step_error_info["selector"] = None
        step_error_info["traceBack"] = None
    GlobalContext.set_global_cache("stepErrorInfo", step_error_info)
