import os
from flybirds.core.launch_cycle.run_manage import RunManage
from flybirds.utils.pkg_helper import load_pkg_by_ns


class HookFinder:
    """
    find extend package
    """

    name = "HookFinder"
    order = 18

    @staticmethod
    def can(context):
        return True

    @staticmethod
    def run(context):
        try:
            if os.environ.get("extend_pkg_list") is not None:
                extend_pkg = os.environ.get("extend_pkg_list")
                extend_pkg_list = extend_pkg.split(",")
                if len(extend_pkg_list) > 0:
                    for pkg in extend_pkg_list:
                        if pkg is not None and pkg != "":
                            load_pkg_by_ns(f"{pkg}.launch.hook")
        except Exception:
            pass


# add event to processor, launch init should be first one
RunManage.insert("before_run_processor", HookFinder, 1)
