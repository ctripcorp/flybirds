# -*- coding: utf-8 -*-
"""
Element Snapshots API
"""
import time

import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap as findsnap
import flybirds.utils.verify_helper as verify_helper
from flybirds.core.exceptions import FlybirdVerifyException


def find_ele_by_snap(poco, config, optional):
    """
    determine whether the element exists within the specified time
    """
    timeout = optional["timeout"]
    current_wait_second = 1
    find_success = False

    while timeout > 0:
        create_success = False
        try:
            is_need_refresh = findsnap.get_refresh_status()
            if is_need_refresh:
                findsnap.refresh_snap()
            poco_resoure = findsnap.get_snap()
            if not (poco_resoure is None):
                create_success = True
                search_time = current_wait_second
                if search_time > 3:
                    search_time = 3
                find_result = findsnap.snap_find(poco_resoure, config)
                find_success = not (find_result is None)
                if find_success:
                    break
            else:
                time.sleep(current_wait_second)
        except Exception:
            if not create_success:
                time.sleep(current_wait_second)
        if current_wait_second > 3:
            time.sleep(current_wait_second - 3)

        timeout -= current_wait_second
        current_wait_second += 2
        findsnap.refresh_snap()
    if not find_success:
        message = "during {}s time, not find {} in page".format(
            optional["timeout"], config
        )
        raise FlybirdVerifyException(message)


def verify_ele_by_snap(poco, config, optional):
    """
    use snapshots to judge element text
    """
    timeout = optional["timeout"]
    current_wait_second = 1
    find_success = False
    expect_text = config.get("expect_text")
    expect_str = expect_text.strip().replace(u"\u200b", "")
    target_str = None
    while timeout > 0:
        create_success = False
        try:
            is_need_refresh = findsnap.get_refresh_status()
            if is_need_refresh:
                findsnap.refresh_snap()
            poco_resoure = findsnap.get_snap()
            if not (poco_resoure is None):
                create_success = True
                search_time = current_wait_second
                if search_time > 3:
                    search_time = 3
                find_result = findsnap.snap_find(poco_resoure, config)
                print("find_result", find_result)
                find_success = not (find_result is None)
                if not (find_result is None):
                    target_str = (
                        (find_result[0].get("payload").get("text") or "")
                        .strip()
                        .replace(u"\u200b", "")
                    )
                    find_success = target_str == expect_str
                    if find_success:
                        break
            else:
                print("No snapshot information is obtained")
                time.sleep(current_wait_second)
        except Exception:
            if not create_success:
                time.sleep(current_wait_second)
        if current_wait_second > 3:
            time.sleep(current_wait_second - 3)

        timeout -= current_wait_second
        current_wait_second += 1
        findsnap.refresh_snap()
    if not find_success:
        verify_helper.text_equal(expect_str, target_str)
