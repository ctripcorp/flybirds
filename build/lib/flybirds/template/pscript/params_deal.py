# -*- coding: utf-8 -*-
"""
Parameter process
"""


def replace_comma(u_text):
    """
    Replace the English comma in the text, because the English comma
     has special meaning in the FLYBIRDS framework
    """
    return u_text.replace(',', ' ')
