# -*- coding: utf-8 -*-
"""
Poco element apis
"""
import time
import os

import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap \
    as find_snap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage as pm
import flybirds.utils.flybirds_log as log
from flybirds.core.exceptions import FlybirdEleExistsException
from flybirds.core.exceptions import FlybirdVerifyException
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan
from flybirds.core.plugin.plugins.default.step.common import img_verify
from flybirds.core.plugin.plugins.default.step.click import click_image


def wait_exists(poco, selector_str, optional):
    """
    determine whether the element exists within the specified time
    """
    timeout = optional["timeout"]
    context = None
    if 'context' in optional:
        context = optional["context"]
    current_wait_second = 1
    find_success = False
    while timeout > 0:
        create_success = False
        try:
            poco_target = pm.create_poco_object_by_dsl(
                poco, selector_str, optional
            )
            create_success = True
            search_time = current_wait_second
            if search_time > 3:
                search_time = 3
            ele_exists = poco_target.exists()
            log.info(
                "wait_exists: {}, ele_exists: {}, timeout: {}".format(
                    selector_str, ele_exists, timeout
                )
            )

            if ele_exists:
                find_success = True
                break

            poco_target.wait_for_appearance(timeout=search_time)
            find_success = True
            log.info(
                "wait_for_appearance: find_success: {}, timeout: {}".format(
                    find_success, timeout
                )
            )
            break
        except Exception:
            if not create_success:
                time.sleep(1)
        if current_wait_second == 3:
            # modal error detection
            try:
                result = detect_error(context)
                log.info(f"detect_error result:{result}")
                if result is False:
                    break
            except Exception:
                log.info("detect_error exception")
            time.sleep(1)
        if current_wait_second > 4:
            break
        timeout -= current_wait_second
        current_wait_second += 1
    if not find_success:
        message = "during {}s time, not find {} in page".format(
            optional["timeout"], selector_str
        )
        raise FlybirdVerifyException(message)


def not_exist(poco, selector_str, optional):
    """
    determine whether the element does not exist
    """
    ele_exists = False
    try:
        poco_object = pm.create_poco_object_by_dsl(
            poco, selector_str, optional
        )
        ele_exists = poco_object.exists()
    except Exception:
        pass
    if ele_exists:
        message = "{} exists in page".format(selector_str)
        raise FlybirdEleExistsException(message)


def wait_disappear(poco, selector_str, optional):
    """
    determine whether the element disappears within the specified time
    """
    timeout = optional["timeout"]
    current_wait_second = 1
    disappear_success = False
    while timeout > 0:
        create_success = False
        try:
            poco_target = pm.create_poco_object_by_dsl(
                poco, selector_str, optional
            )
            create_success = True
            search_time = current_wait_second
            if search_time > 3:
                search_time = 3
            poco_target.wait_for_disappearance(timeout=search_time)
            disappear_success = True
            break
        except Exception:
            if not create_success:
                time.sleep(1)
        if current_wait_second > 4:
            break
        timeout -= current_wait_second
        current_wait_second += 1
    if not disappear_success:
        message = "during {}s time, {} not disappear in page".format(
            optional["timeout"], selector_str
        )
        raise FlybirdVerifyException(message)


def detect_error(context):
    language = g_Context.get_current_language()
    modal_list = lan.parse_glb_str("modal_list", language)
    break_list = lan.parse_glb_str("break_list", language)
    poco = g_Context.ui_driver_instance

    img_path = "tpl/app"
    if context is not None and os.path.exists(img_path):
        images = sorted([tpl for tpl in os.listdir(img_path) if str(tpl).endswith('png')])
        for img in images:
            path = os.path.join(img_path, img)
            result = img_verify(context, path)
            log.info(f"in detect error method, img detect result is {result}")
            if len(result) > 0:
                click_image(context, path)
                log.info("detect_error: x_button_exists: true")
                return True

    for error_str in modal_list:
        log.info(f"in detect error method, error_str detect: {error_str}")
        error_target = pm.create_poco_object_by_dsl(
            poco, error_str, None
        )
        is_existed = error_target.exists()
        if is_existed:
            error_target.click()
            if gr.get_frame_config_value("use_snap", False):
                find_snap.fix_refresh_status(True)
            log.info("detect_error: {}, layer_errors_exists: true"
                     .format(error_str))
            return True

    for break_str in break_list:
        log.info(f"in detect error method, break_str detect: {break_str}")
        break_target = pm.create_poco_object_by_dsl(
            poco, break_str, None
        )
        is_existed = break_target.exists()
        if is_existed:
            break_target.click()
            if gr.get_frame_config_value("use_snap", False):
                find_snap.fix_refresh_status(True)
            log.info("detect_error: {}, layer_errors_exists: true"
                     .format(break_str))
            return False
