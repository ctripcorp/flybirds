# -*- coding: utf-8 -*-
"""
Poco element click
"""
import flybirds.core.global_resource as gr
import flybirds.core.plugin.plugins.default.ui_driver.poco.findsnap as findsnap
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage as pm
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_position as pi
from flybirds.core.plugin.plugins.default.ui_driver.poco import poco_text
from flybirds.core.exceptions import PositionNotChangeException


def air_bdd_click(
        poco,
        select_dsl_str,
        optional,
        verify_dsl_str=None,
        verify_optional=None,
        verify_action=None,
):
    """
    click on the element,
    optional parameters to determine whether the clicked page is rendered
    :param poco:
    :param select_dsl_str:
    :param optional: Optional parameters
    :param verify_dsl_str:
    :param verify_optional:
    :param verify_action:
    :return:
    """

    poco_ele.wait_exists(poco, select_dsl_str, optional)
    poco_object = pm.create_poco_object_by_dsl(
        poco, select_dsl_str, optional
    )

    o_position = None
    o_text = None
    if (not (verify_action is None)) and verify_action == "position":
        verify_poco_object = pm.create_poco_object_by_dsl(
            poco, verify_dsl_str, verify_optional
        )
        o_position = verify_poco_object.get_position()
    elif (not (verify_action is None)) and verify_action == "text":
        verify_poco_object = pm.create_poco_object_by_dsl(
            poco, verify_dsl_str, verify_optional
        )
        o_text = verify_poco_object.get_text()

    poco_object.click()
    if gr.get_frame_config_value("use_snap", False):
        # findsnap.refresh_snap()
        findsnap.fix_refresh_status(True)
    if not (verify_dsl_str is None):
        verify_click_end(
            poco,
            verify_dsl_str,
            verify_optional,
            verify_action,
            o_position,
            o_text,
        )


def verify_click_end(poco, verify_dsl_str, verify_optional, verify_action,
                     o_position, o_text
                     ):
    """
    determine whether the rendering of the click effect is completed according
    to the movement of the element,the disappearance of the element or the text
    :param poco:
    :param verify_dsl_str:
    :param verify_optional:
    :param o_position:
    :param verify_action:
    :return:
    """
    if verify_action == "position":
        pos_change = pi.position_change(
            poco, verify_dsl_str, verify_optional, o_position
        )
        if not pos_change:
            raise PositionNotChangeException(
                "during time={} the position of selector={}"
                " not changed".format(
                    verify_optional["timeout"], verify_dsl_str
                )
            )
    elif verify_action == "text":
        pos_change = poco_text.text_change(
            poco, verify_dsl_str, verify_optional, o_text
        )
        if not pos_change:
            raise PositionNotChangeException(
                "during time={} the text of selector={} not changed".format(
                    verify_optional["timeout"], verify_dsl_str
                )
            )
    elif verify_action == "appear":
        poco_ele.wait_exists(poco, verify_dsl_str, verify_optional)
    elif verify_action == "disappear":
        poco_ele.wait_disappear(poco, verify_dsl_str, verify_optional)
