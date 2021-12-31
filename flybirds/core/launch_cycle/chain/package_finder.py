# -*- coding: utf-8 -*-
"""
package search
"""
import os

import pkg_resources
from flybirds.utils.flybirds_log import logger
from flybirds.core.launch_cycle.run_manage import RunManage


class PackageFinder:
    """
    find extend package
    """

    name = "PackageFinder"
    order = 12

    @staticmethod
    def find_package(context):
        if context.__contains__("pkg_query") and context.get(
                "pkg_query") is not None and context.get("pkg_query") != "":
            working_set = pkg_resources.WorkingSet()
            pkg_list = []
            lst = [d for d in working_set]
            for item in lst:
                if context.get("pkg_query") in item.project_name:
                    pkg_list.append(item)
            return pkg_list
        else:
            return None

    @staticmethod
    def can(context):
        return False

    @staticmethod
    def run(context):
        try:
            logger.info("find extend pkg")
            pkg_query = "-flybirds-plugin"
            context["pkg_query"] = pkg_query
            pkg_list = PackageFinder.find_package(context)
            if pkg_list is not None and len(pkg_list) > 0:
                pkg_root_list = []
                for item in pkg_list:
                    logger.info(f"set package env :{str(item.project_name)}")
                    pkg_root_list.append(
                        item.project_name.replace("-", "_"))
                os.environ["extend_pkg_list"] = ",".join(pkg_root_list)
        except Exception as find_error:
            logger.info(f"find pack error :{str(find_error)}")


# add event to processor, launch init should be first one
RunManage.insert("before_run_processor", PackageFinder, 1)
