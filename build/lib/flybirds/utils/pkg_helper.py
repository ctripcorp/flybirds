# -*- coding: utf-8 -*-
"""
py ns load
"""
import importlib
import os
import pkgutil
import pkg_resources


def load_pkg_by_ns(pkg_ns):
    """
    py ns load
    """
    base = importlib.import_module(pkg_ns)
    for loader, module_name, is_pkg in \
            pkgutil.walk_packages(base.__path__, f'{base.__name__}.'):
        try:
            __import__(module_name)
        except ImportError as e:
            raise e


def find_package(pkg_query):
    if pkg_query is not None and pkg_query != "":
        working_set = pkg_resources.WorkingSet()
        pkg_list = []
        lst = [d for d in working_set]
        for item in lst:
            if pkg_query in item.project_name:
                pkg_list.append(item)
        if pkg_list is not None and len(pkg_list) > 0:
            pkg_root_list = []
            for item in pkg_list:
                pkg_root_list.append(
                    item.project_name.replace("-", "_"))
            return pkg_root_list
        else:
            return None
    else:
        return None


def find_package_base_path(pkg_query):
    if pkg_query is not None and pkg_query != "":
        working_set = pkg_resources.WorkingSet()
        pkg_list = []
        lst = [d for d in working_set]
        for item in lst:
            if pkg_query in item.project_name:
                pkg_list.append(item)
        if pkg_list is not None and len(pkg_list) > 0:
            pkg_root_list = []
            for item in pkg_list:
                if os.path.isfile(item.module_path):
                    new_item = {
                        "name": item.project_name.replace("-", "_"),
                        "path": os.path.dirname(item.module_path)
                    }
                else:
                    new_item = {
                        "name": item.project_name.replace("-", "_"),
                        "path": item.module_path
                    }

                pkg_root_list.append(new_item)
            return pkg_root_list
        else:
            return None
    else:
        return None
