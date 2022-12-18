# -*- coding: utf-8 -*-
"""
Element verification
"""
import re
import time

import flybirds.core.global_resource as gr
import flybirds.utils.flybirds_log as log
from flybirds.core.global_context import GlobalContext as g_Context
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele \
    as poco_ele
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_findsnap \
    as poco_find_snap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_verify \
    as poco_verify
import flybirds.utils.dsl_helper as dsl_helper
import flybirds.utils.verify_helper as verify
from flybirds.core.exceptions import FlybirdVerifyException
from flybirds.core.plugin.plugins.default.step.common import ocr, img_verify


def wait_text_exist(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    config = None
    use_snap = gr.get_frame_config_value("use_snap", False)
    if "fuzzyMatch" in param_dict.keys():
        if use_snap:
            config = {"textMatches": selector_str}
        else:
            selector_str = "textMatches=" + selector_str
    else:
        if use_snap:
            config = {"text": selector_str}
        else:
            selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)
    if use_snap and config:
        poco_find_snap.find_ele_by_snap(poco_instance, config, optional)
    else:
        poco_ele.wait_exists(poco_instance, selector_str, optional)


def text_not_exist(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    if "fuzzyMatch" in param_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}

    poco_ele.not_exist(poco_instance, selector_str, optional)


def wait_text_disappear(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    if "fuzzyMatch" in param_dict.keys():
        selector_str = "textMatches=" + selector_str
    else:
        selector_str = "text=" + selector_str
    optional = {}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_disappear", 10
        )

    poco_ele.wait_disappear(poco_instance, selector_str, optional)


def wait_ele_exit(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    config = None
    use_snap = gr.get_frame_config_value("use_snap", False)
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    elif use_snap:
        config = {"name": selector_str}
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)
    if use_snap and config:
        print("Use snap to determine the existence of elements")
        poco_find_snap.find_ele_by_snap(poco_instance, config, optional)
    else:
        poco_ele.wait_exists(poco_instance, selector_str, optional)


def ele_not_exit(context, param):
    poco_instance = gr.get_value("pocoInstance")
    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]

    poco_ele.not_exist(poco_instance, selector_str, optional)


def wait_ele_disappear(context, param):
    poco_instance = gr.get_value("pocoInstance")
    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_disappear", 10
        )

    poco_ele.wait_disappear(poco_instance, selector_str, optional)


def ele_text_equal(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")
    pattern = re.compile(r"\s+")
    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    optional = {}
    config = None
    # use snap
    # use_snap = gr.get_frame_config_value("use_snap", False)
    if "path" in param1_dict.keys():
        optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    params_deal_module = None
    deal_method = None
    param2_dict = dsl_helper.params_to_dic(param2, "tText")
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal
    target_str = param2_dict["tText"]
    handled_target_str = re.sub(pattern, "", target_str.replace(u"\u200b", ""))
    handled_selector_str = re.sub(
        pattern, "", selector_str.replace(u"\u200b", "")
    )
    if not (deal_method is None):
        deal_method_fun = getattr(params_deal_module, deal_method)
        handled_target_str = deal_method_fun(handled_target_str)
        pattern = re.compile(r"\s+")
        handled_target_str = re.sub(pattern, "", handled_target_str)
    if False:
        config = {"name": selector_str, "expect_text": target_str}
        poco_find_snap.verify_ele_by_snap(poco_instance, config, optional)
    else:
        poco_verify.ele_text_is(
            poco_instance,
            handled_selector_str,
            handled_target_str,
            optional,
            deal_method,
            params_deal_module,
        )


def ele_text_container(context, param1, param2):
    poco_instance = gr.get_value("pocoInstance")

    param1_dict = dsl_helper.params_to_dic(param1)
    selector_str = param1_dict["selector"]
    optional = {}
    if "path" in param1_dict.keys():
        optional["path"] = param1_dict["path"]
    elif "multiSelector" in param1_dict.keys():
        optional["multiSelector"] = param1_dict["multiSelector"]
    if "timeout" in param1_dict.keys():
        optional["timeout"] = float(param1_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value("wait_ele_timeout", 10)

    deal_method = None
    params_deal_module = None
    param2_dict = dsl_helper.params_to_dic(param2, "tText")
    if "dealMethod" in param2_dict.keys():
        deal_method = param2_dict["dealMethod"]
        params_deal_module = gr.get_value("projectScript").params_deal
    target_str = param2_dict["tText"]
    pattern = re.compile(r"\s+")
    handled_target_str = re.sub(pattern, "", target_str.replace(u"\u200b", ""))
    if not (deal_method is None):
        deal_method_fun = getattr(params_deal_module, deal_method)
        handled_target_str = deal_method_fun(handled_target_str)
        pattern = re.compile(r"\s+")
        handled_target_str = re.sub(pattern, "", handled_target_str)

    poco_verify.ele_text_contains(
        poco_instance,
        selector_str,
        handled_target_str,
        optional,
        deal_method,
        params_deal_module,
    )


def wait_ele_appear(context, param):
    poco_instance = gr.get_value("pocoInstance")

    param_dict = dsl_helper.params_to_dic(param)
    selector_str = param_dict["selector"]
    optional = {}
    if "path" in param_dict.keys():
        optional["path"] = param_dict["path"]
    elif "multiSelector" in param_dict.keys():
        optional["multiSelector"] = param_dict["multiSelector"]
    if "timeout" in param_dict.keys():
        optional["timeout"] = float(param_dict["timeout"])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "page_render_timeout", 30
        )
    optional["context"] = context
    poco_ele.wait_exists(poco_instance, selector_str, optional)


def exist_ele(context, param):
    """
    Compatible with the old version of the statement, it will be discarded in
    the future.
    """
    poco_instance = gr.get_value("pocoInstance")

    params_array = param.split(",")
    selector_str = params_array[0]
    optional = {}
    if len(params_array) >= 2:
        optional["timeout"] = float(params_array[1])
    else:
        optional["timeout"] = gr.get_frame_config_value(
            "wait_ele_timeout", 10
        )
    optional["context"] = context
    poco_ele.wait_exists(poco_instance, selector_str, optional)


def wait_ocr_text_appear(context, param):
    timeout = gr.get_frame_config_value("page_render_timeout", 30)
    start = time.time()
    while True:
        ocr(context)
        txts = [line[1][0] for line in g_Context.ocr_result]
        log.info(f"[wait_ocr_text_appear] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param.replace(" ", "")
        for txt in fixed_txt:
            if trim_param in txt:
                log.info(f"[ocr txt contain] param: {param} found in txt: {txt}")
                return True
            try:
                if re.search(param, txt, flags=0) is not None:
                    log.info(f"[ocr txt contain re] param: {param} found in txt: {txt}")
                    return True
            except:
                pass
            line_param = trim_param.replace("-", "")
            line_txt = txt.replace("-", "")
            if line_param in line_txt:
                log.warn(f"[ocr txt contain line replace] param: {param} found in txt: {txt}")
                return True
        if time.time() - start > 10:
            detect_start = time.time()
            poco_ele.detect_error(context)
            detect_end = time.time()
            detect_cost = detect_end - detect_start
            start = start + detect_cost
        if time.time() - start > timeout:
            for line in g_Context.ocr_result:
                log.info(f"[wait_ocr_text_appear] scan line info is:{line}")
            message = "text not found in {} seconds, expect text:{}" \
                .format(timeout, param)
            raise FlybirdVerifyException(message)


def ocr_txt_exist(context, param):
    if len(g_Context.ocr_result) < 1:
        ocr(context)
    if len(g_Context.ocr_result) >= 1:
        txts = [line[1][0] for line in g_Context.ocr_result]
        log.info(f"[ocr txt exist] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param.replace(" ", "")
        verify.text_container(trim_param, fixed_txt)
        log.info(f"[ocr txt exist] param: {param} found in txt: {fixed_txt}")
    else:
        message = "ocr result is null"
        raise FlybirdVerifyException(message)


def ocr_txt_contain(context, param, islog=True):
    if len(g_Context.ocr_result) < 1:
        ocr(context)
    if len(g_Context.ocr_result) >= 1:
        txts = [line[1][0] for line in g_Context.ocr_result]
        log.info(f"[ocr txt contain] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param.replace(" ", "")
        for txt in fixed_txt:
            if trim_param in txt:
                log.info(f"[ocr txt contain] param: {param} found in txt: {txt}")
                return True
            try:
                if re.search(param, txt, flags=0) is not None:
                    log.info(f"[ocr txt contain re] param: {param} found in txt: {txt}")
                    return True
            except:
                pass
            line_param = trim_param.replace("-", "")
            line_txt = txt.replace("-", "")
            if line_param in line_txt:
                log.warn(f"[ocr txt contain line replace] param: {param} found in txt: {txt}")
                return True
        if islog is True:
            for line in g_Context.ocr_result:
                log.info(f"[image ocr result] scan line info is:{line}")
        message = "ocr result not contain {}".format(param)
        raise FlybirdVerifyException(message)
    else:
        message = "[ocr txt contain] ocr result is null"
        raise FlybirdVerifyException(message)


def ocr_txt_not_exist(context, param):
    if len(g_Context.ocr_result) < 1:
        ocr(context)
    if len(g_Context.ocr_result) >= 1:
        txts = [line[1][0] for line in g_Context.ocr_result]
        log.info(f"[ocr txt not exist] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param.replace(" ", "")
        verify.text_not_container(trim_param, fixed_txt)
        log.info(f"[ocr txt not exist] param: {param} not exist")
    else:
        for line in g_Context.ocr_result:
            log.info(f"[image ocr result] scan line info is:{line}")
        message = "ocr result is null"
        raise FlybirdVerifyException(message)


def paddle_fix_txt(txt, trim=False):
    # replace value in paddle_fix config
    paddle_fix = gr.get_paddle_fix_value()
    if paddle_fix is not None:
        for i in range(len(txt)):
            for key in paddle_fix:
                origin_txt = txt[i]
                if key in origin_txt:
                    txt[i] = origin_txt.replace(key, paddle_fix[key])
                    log.info(f"[paddle_fix_txt] paddle fix success origin_txt: {origin_txt}, fixed txt: {txt[i]}")
    # replace  blank value
    if trim is True:
        for i in range(len(txt)):
            origin_txt = txt[i]
            txt[i] = origin_txt.replace(" ", "")

    return txt


def img_exist(context, param, islog=True):
    start = time.time()
    step_index = context.cur_step_index - 1
    result = img_verify(context, param)
    if len(result) == 0:
        if islog is True:
            src_path = "../../../{}".format(param)
            data = (
                'embeddingsTags, stepIndex={}, <image class ="screenshot"'
                ' width="375" src="{}" />'.format(step_index, src_path)
            )
            context.scenario.description.append(data)
        raise Exception("[image exist verify] image not found !")
    else:
        log.info(f"[image exist verify] cost time:{time.time() - start}")
        log.info(f"[image exist verify] result:{result}")
        return True


def img_not_exist(context, param):
    start = time.time()
    step_index = context.cur_step_index - 1
    result = img_verify(context, param)
    if len(result) == 0:
        log.info(f"[image not exist verify] cost time:{time.time() - start}")
        log.info(f"[image not exist verify] result:{result}")
    else:
        src_path = "../../../{}".format(param)
        data = (
            'embeddingsTags, stepIndex={}, <image class ="screenshot"'
            ' width="375" src="{}" />'.format(step_index, src_path)
        )
        context.scenario.description.append(data)
        # context.cur_step_index += 1
        raise Exception("[image not exist verify] image found !")


def ocr_regional_txt_exist(context, param1, param2):
    if len(g_Context.ocr_regional_result) < 1:
        ocr(context)
    if len(g_Context.ocr_regional_result) >= 1:
        param1_dict = dsl_helper.params_to_dic(param1)
        selector_str = param1_dict["selector"]
        if "id=" in selector_str or "ID=" in selector_str:
            str_list = selector_str.split('=')
        else:
            message = "[ocr regional txt exist] please input regional id with format: id=xx"
            raise FlybirdVerifyException(message)
        regional_id = int(str_list[1])
        regional_dic = list(filter(lambda item: item['id'] == regional_id, g_Context.ocr_regional_result))
        txts = regional_dic[0]["txts"].split(",")
        log.info(f"[ocr regional txt exist] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param2.replace(" ", "")
        verify.text_container(trim_param, fixed_txt)
        log.info(f"[ocr regional txt exist] param: {param2} found in txt: {fixed_txt}")
    else:
        message = "ocr regional result is null!"
        raise FlybirdVerifyException(message)


def ocr_regional_txt_contain(context, param1, param2):
    if len(g_Context.ocr_regional_result) < 1:
        ocr(context)
    if len(g_Context.ocr_regional_result) >= 1:
        param1_dict = dsl_helper.params_to_dic(param1)
        selector_str = param1_dict["selector"]
        if "id=" in selector_str or "ID=" in selector_str:
            str_list = selector_str.split('=')
        else:
            message = "[ocr regional txt contain] please input regional id with format: id=xx"
            raise FlybirdVerifyException(message)
        regional_id = int(str_list[1])
        regional_dic = list(filter(lambda item: item['id'] == regional_id, g_Context.ocr_regional_result))
        txts = regional_dic[0]["txts"].split(",")
        log.info(f"[ocr regional txt contain] ocr txt got: {txts}")
        fixed_txt = paddle_fix_txt(txts, True)
        trim_param = param2.replace(" ", "")
        for txt in fixed_txt:
            if trim_param in txt:
                log.info(f"[ocr regional txt contain] param: {param2} found in txt: {txt}")
                return True
            try:
                if re.search(param2, txt, flags=0) is not None:
                    log.info(f"[ocr regional txt contain re] param: {param2} found in txt: {txt}")
                    return True
            except:
                pass
            line_param = trim_param.replace("-", "")
            line_txt = txt.replace("-", "")
            if line_param in line_txt:
                log.warn(f"[ocr regional txt contain line replace] param: {param2} found in txt: {txt}")
                return True
        message = "ocr result not contain {}".format(param2)
        raise FlybirdVerifyException(message)
    else:
        message = "[ocr txt contain] ocr result is null"
        raise FlybirdVerifyException(message)