# -*- coding: utf-8 -*-
"""
language help
"""
from behave.i18n import languages

from flybirds.core.dsl.globalization.i18n import globalization
from flybirds.core.dsl.globalization.i18n import step_language


def parse_keyword(text, language):
    """
    parse bh key word
    """
    kw = language
    for kw in languages[language][text]:
        if kw.endswith("<"):
            kw = kw[:-1]
    return kw


def parse_glb_str(text, language):
    """
    parse glb str
    """
    if globalization.__contains__(language):
        sn = globalization[language]
        if sn.__contains__(text):
            return sn[text]
    return None


def parse_glb_step(text, language):
    """
    parse glb step
    """
    if step_language.__contains__(language):
        sn = step_language[language]
        if sn.__contains__(text):
            return sn[text]
    return None


def get_language_list():
    """
    get i18 global step language list
    """
    lg_list = []
    if step_language is not None:
        for name in step_language.keys():
            lg_list.append(name)

    return lg_list


def get_glb_key(kw, language):
    """
    get glb dict key by keyword
    """
    if globalization.__contains__(language):
        l_dict = globalization[language]
        if l_dict is not None:
            for k, v in l_dict.items():
                if v == kw:
                    return k
    return None
