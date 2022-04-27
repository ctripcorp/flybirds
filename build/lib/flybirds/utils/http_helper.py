# -*- coding: utf-8 -*-
"""
http help
"""
import requests


def http_get(url, param=None, header=None):
    if url is not None and url != "":
        result = requests.get(url, params=param, headers=header, )
        j_obj = result.json()
        result.close()
        return j_obj
    else:
        return None
