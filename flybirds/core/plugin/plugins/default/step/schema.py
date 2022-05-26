# -*- coding: utf-8 -*-
"""
Jump to page
"""
import flybirds.core.global_resource as gr
import flybirds.utils.dsl_helper as dsl_helper
import flybirds.utils.snippet as snippet


def jump_to_page(context, param):
    param_dict = dsl_helper.params_to_dic(param, "pageName")

    page_name = param_dict["pageName"]
    schema_url = gr.get_page_schema_url(page_name)

    schema_goto_module = gr.get_value("projectScript").custom_operation
    deal_method = None
    params_deal_module = None
    if "dealMethod" in param_dict.keys():
        deal_method = param_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal

    snippet.schema_goto(
        page_name,
        schema_url,
        schema_goto_module,
        deal_method,
        params_deal_module,
    )
