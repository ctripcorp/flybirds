# -*- coding: utf-8 -*-
"""
package search
"""
import os
from flybirds.utils.flybirds_log import logger
from flybirds.core.launch_cycle.run_manage import RunManage
from flybirds.utils.pkg_helper import find_package


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
            pkg_list = find_package(context.get("pkg_query"))
            return pkg_list
        else:
            return None

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        try:
            logger.info("find extend pkg")
            pkg_query = "-flybirds-plugin"
            context["pkg_query"] = pkg_query
            pkg_list = PackageFinder.find_package(context)
            if pkg_list is not None and len(pkg_list) > 0:
                os.environ["extend_pkg_list"] = ",".join(pkg_list)
        except Exception as find_error:
            logger.info(f"find pack error :{str(find_error)}")


# add event to processor, launch init should be first one
RunManage.insert("before_run_processor", PackageFinder, 1)
