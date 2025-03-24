# -*- coding: utf-8 -*-
"""
equal includ helper
"""
import re
from flybirds.core.exceptions import FlybirdVerifyException, ErrorName


def replace_func(match):
    n = int(match.group(1))
    return ' ' * n


def text_equal(o_text, t_text):
    """
    Determine whether the text is equal
    """
    if o_text == "[@@空@@]" or o_text == "@@空@@":
        o_text = ""

    # 正则替换前后空格
    # 定义正则表达式和替换函数
    pattern = re.compile(r'@@空,\s*(\d+)@@')
    # 使用 sub 函数进行正则替换
    o_text = pattern.sub(replace_func, o_text)

    if "(@#@换行#符号@#@)" in o_text:
        o_text = o_text.replace("(@#@换行#符号@#@)", "\n")
    if t_text is not None and isinstance(t_text, str):
        t_text = t_text.replace(chr(160), " ")
    if o_text != t_text:
        message = "text not equal, expect value:{}, actual value:{}".format(
            o_text, t_text
        )
        raise FlybirdVerifyException(message, error_name=ErrorName.TextNotFoundError)


def text_container(o_text, t_text):
    """
    Determine whether the text is included
    """

    if "(@#@换行#符号@#@)" in o_text:
        o_text = o_text.replace("(@#@换行#符号@#@)", "\n")
    if t_text is not None and isinstance(t_text, str):
        t_text = t_text.replace(chr(160), " ")
    if not (o_text in t_text):
        message = "text not contain, expect value include:{}," \
                  " actual value:{}".format(o_text, t_text)
        raise FlybirdVerifyException(message, error_name=ErrorName.TextNotFoundError)


def text_not_container(o_text, t_text):
    """
    Determine whether the text is included
    """
    if "(@#@换行#符号@#@)" in o_text:
        o_text = o_text.replace("(@#@换行#符号@#@)", "\n")
    if t_text is not None and isinstance(t_text, str):
        t_text = t_text.replace(chr(160), " ")
    if o_text in t_text:
        message = "text contain, expect value not include:{}," \
                  " actual value:{}".format(o_text, t_text)
        raise FlybirdVerifyException(message, error_name=ErrorName.TextFoundError)


def attr_equal(o_attr, t_attr):
    """
    Determine whether the attributes are equal
    """
    if o_attr == "[@@空@@]" or o_attr == "@@空@@":
        o_attr = ""
    if str(o_attr) != str(t_attr):
        message = "attr not equal, expect value:{}, actual value:{}".format(
            o_attr, t_attr
        )
        raise FlybirdVerifyException(message, error_name=ErrorName.AttributeNotEqualError, expect=o_attr, actual=t_attr)


def attr_container(o_attr, t_attr):
    """
    Determine whether the attributes are equal
    """
    if o_attr == "[@@空@@]" or o_attr == "@@空@@":
        o_attr = ""

    if not (str(o_attr) in str(t_attr)):
        message = "attr not contain, expect value include:{}," \
                  " actual value:{}".format(str(o_attr), str(t_attr))
        raise FlybirdVerifyException(message, error_name=ErrorName.AttributeNotFoundError)


def attr_not_container(o_attr, t_attr):
    """
    Determine whether the attributes are equal
    """
    if o_attr == "[@@空@@]" or o_attr == "@@空@@":
        o_attr = ""

    if (str(o_attr) in str(t_attr)):
        message = "attr contain, expect value not include:{}," \
                  " actual value:{}".format(str(o_attr), str(t_attr))
        raise FlybirdVerifyException(message, error_name=ErrorName.AttributeFoundError)
