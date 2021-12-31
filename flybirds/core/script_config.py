# -*- coding: utf-8 -*-
"""
manage user py code
"""
import sys
import os


class ScriptImportManage:
    """
    use user py module code
    """

    def __init__(self):
        sys.path.insert(1, os.path.join(os.getcwd(), "pscript"))
        params_deal_path = os.path.join(
            os.getcwd(), "pscript", "params_deal.py"
        )
        if os.path.exists(params_deal_path):
            params_deal_import_path = "params_deal"
            self.params_deal = __import__(params_deal_import_path)
        app_operation_path = os.path.join(
            os.getcwd(), "pscript", "app", "operation.py"
        )
        if os.path.exists(app_operation_path):
            app_operation_import_path = "app.operation"
            app_module = __import__(app_operation_import_path)
            self.app_operation = getattr(app_module, "operation")
        dsl_hook_path = os.path.join(os.getcwd(), "pscript", "dsl", "hook.py")
        if os.path.exists(dsl_hook_path):
            dsl_hook_import_path = "dsl.hook"
            dsl_module = __import__(dsl_hook_import_path)
            self.dsl_hook = getattr(dsl_module, "hook")
