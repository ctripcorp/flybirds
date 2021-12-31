# -*- coding: utf-8 -*-
"""
file download
"""
import urllib


def downlaod(url, path):
    """
    file download
    """
    urllib.request.urlretrieve(url, path)
