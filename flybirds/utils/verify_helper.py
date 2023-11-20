# -*- coding: utf-8 -*-
"""
equal includ helper
"""
from flybirds.core.exceptions import FlybirdVerifyException


def text_equal(o_text, t_text):
    """
    Determine whether the text is equal
    """
    if o_text == "[@@空@@]" or o_text == "@@空@@":
        o_text = ""
    if o_text != t_text:
        message = "text not equal, expect value:{}, actual value:{}".format(
            o_text, t_text
        )
        raise FlybirdVerifyException(message)


def text_container(o_text, t_text):
    """
    Determine whether the text is included
    """
    if not (o_text in t_text):
        message = "text not contain, expect value include:{}," \
                  " actual value:{}".format(o_text, t_text)
        raise FlybirdVerifyException(message)


def text_not_container(o_text, t_text):
    """
    Determine whether the text is included
    """
    if o_text in t_text:
        message = "text contain, expect value not include:{}," \
                  " actual value:{}".format(o_text, t_text)
        raise FlybirdVerifyException(message)


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
        raise FlybirdVerifyException(message)
