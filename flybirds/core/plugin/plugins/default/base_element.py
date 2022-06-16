# -*- coding: utf-8 -*-
"""
base element class
"""
from airtest.core.api import (time, text, keyevent)

import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_attr as poco_attr
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_click \
    as poco_click
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_ele as poco_ele
import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_findsnap \
    as find_snap
import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_position \
    as poco_position
import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_selector \
    as poco_selector
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_swipe \
    as poco_swipe
import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_text as poco_text
import \
    flybirds.core.plugin.plugins.default.ui_driver.poco.poco_verify \
    as poco_verify
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_input import (
    air_bdd_input
)
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_manage import (
    create_poco_object_by_dsl
)
from flybirds.core.plugin.plugins.default.ui_driver.poco.poco_screen import (
    air_bdd_screen_size,
)


class BaseElement:
    """Base Element Class"""

    name = "base_element"

    """
    airtest UI  operations
    """

    def str_input(self, input_str, after_input_wait=None):
        """
        Enter a character string, press enter by default after entering
        :param input_str:
        :param after_input_wait:
        :return:
        """
        text(input_str, enter=False)
        if not (after_input_wait is None):
            time.sleep(after_input_wait)

    def key_event(self, key_code):
        """
        Perform key event on the device
        * ``iOS``: Only supports home/volumeUp/volumeDown::
        """
        keyevent(key_code)

    def get_ele_attr(
            self,
            poco,
            selector_str,
            optional,
            attr_name,
            deal_method=None,
            params_deal_module=None,
    ):
        return poco_attr.get_ele_attr(
            poco,
            selector_str,
            optional,
            attr_name,
            deal_method=deal_method,
            params_deal_module=params_deal_module,
        )

    """
       poco ui operations
    """

    def air_bdd_click(
            self,
            poco,
            select_dsl_str,
            optional,
            verify_dsl_str=None,
            verify_optional=None,
            verify_action=None,
    ):
        poco_click.air_bdd_click(
            poco,
            select_dsl_str,
            optional,
            verify_dsl_str=verify_dsl_str,
            verify_optional=verify_optional,
            verify_action=verify_action,
        )

    def verify_click_end(
            self,
            poco,
            verify_dsl_str,
            verify_optional,
            verify_action,
            o_position,
            o_text,
    ):
        poco_click.verify_click_end(
            poco,
            verify_dsl_str,
            verify_optional,
            verify_action,
            o_position,
            o_text,
        )

    def wait_exists(self, poco, selector_str, optional):
        poco_ele.wait_exists(poco, selector_str, optional)

    def not_exist(self, poco, selector_str, optional):
        poco_ele.not_exist(poco, selector_str, optional)

    def wait_disappear(self, poco, selector_str, optional):
        poco_ele.wait_disappear(poco, selector_str, optional)

    def detect_error(self):
        poco_ele.detect_error()

    def find_ele_by_snap(self, poco, config, optional):
        find_snap.find_ele_by_snap(poco, config, optional)

    def verify_ele_by_snap(self, poco, config, optional):
        find_snap.verify_ele_by_snap(poco, config, optional)

    def air_bdd_input(
            self, poco, select_dsl_str, optional, input_str,
            after_input_wait=None
    ):
        air_bdd_input(
            poco,
            select_dsl_str,
            optional,
            input_str,
            after_input_wait=after_input_wait,
        )

    def create_poco_object_by_dsl(self, poco, select_dsl_str, optional):
        return create_poco_object_by_dsl(poco, select_dsl_str, optional)

    def position_change(self, poco, select_str, optional, o_position):
        return poco_position.position_change(poco, select_str, optional,
                                             o_position)

    def position_not_change(
            self, poco, select_str, optional, dur_time, verify_count
    ):
        poco_position.position_not_change(poco, select_str, optional, dur_time,
                                          verify_count)

    def air_bdd_screen_size(self, poco_instance):
        return air_bdd_screen_size(poco_instance)

    def create_poco_object(self, poco, select_dic={}):
        return poco_selector.create_poco_object(poco, select_dic=select_dic)

    def create_parent(self, poco_object):
        return poco_selector.create_parent(poco_object)

    def create_first_child(self, poco_object, select_dic={}):
        return poco_selector.create_first_child(poco_object,
                                                select_dic=select_dic)

    def create_first_offspring(self, poco_object, select_dic={}):
        return poco_selector.create_first_offspring(poco_object,
                                                    select_dic=select_dic)

    def create_first_sibling(self, poco_object, select_dic={}):
        return poco_selector.create_first_sibling(poco_object,
                                                  select_dic=select_dic)

    def select_child(self, poco_object, target_index, select_dic={}):
        return poco_selector.select_child(poco_object, target_index,
                                          select_dic=select_dic)

    def select_offspring(self, poco_object, target_index, select_dic={}):
        return poco_selector.select_offspring(
            poco_object, target_index, select_dic=select_dic
        )

    def select_sibling(self, poco_object, target_index, select_dic={}):
        return poco_selector.select_sibling(poco_object, target_index,
                                            select_dic=select_dic)

    def air_bdd_full_screen_swipe(
            self,
            poco,
            start_point,
            screen_size,
            direction,
            distance,
            duration,
            ready_time=None,
    ):
        poco_swipe.air_bdd_full_screen_swipe(
            poco,
            start_point,
            screen_size,
            direction,
            distance,
            duration,
            ready_time=ready_time,
        )

    def air_bdd_ele_swipe(
            self,
            poco,
            container_dsl_str,
            optional,
            start_point,
            screen_size,
            direction,
            distance,
            duration,
            ready_time=None,
    ):
        poco_swipe.air_bdd_ele_swipe(
            poco,
            container_dsl_str,
            optional,
            start_point,
            screen_size,
            direction,
            distance,
            duration,
            ready_time=ready_time,
        )

    def air_bdd_direction_swipe(
            self, poco, start_point, direction, distance, duration=None
    ):
        poco_swipe.air_bdd_direction_swipe(
            poco, start_point, direction, distance, duration=duration
        )

    def air_bdd_percent_point_swipe(
            self, poco, start_point, end_point, duration=None
    ):
        poco_swipe.air_bdd_percent_point_swipe(
            poco, start_point, end_point, duration=duration
        )

    def full_screen_swipe_search(
            self,
            poco,
            search_dsl_str,
            search_optional,
            swipe_count,
            direction,
            screen_size,
            start_x=None,
            start_y=None,
            distance=None,
            duration=None,
    ):
        poco_swipe.full_screen_swipe_search(
            poco,
            search_dsl_str,
            search_optional,
            swipe_count,
            direction,
            screen_size,
            start_x=start_x,
            start_y=start_y,
            distance=distance,
            duration=duration,
        )

    def air_bdd_swipe_search(
            self,
            poco,
            container_dsl_str,
            container_optional,
            search_dsl_str,
            search_optional,
            swipe_count,
            screen_size,
            direction,
            start_x=None,
            start_y=None,
            distance=None,
            duration=None,
    ):
        poco_swipe.air_bdd_swipe_search(
            poco,
            container_dsl_str,
            container_optional,
            search_dsl_str,
            search_optional,
            swipe_count,
            screen_size,
            direction,
            start_x=start_x,
            start_y=start_y,
            distance=distance,
            duration=duration,
        )

    def get_ele_text_replace_space(
            self,
            poco,
            selector_str,
            optional,
            deal_method_name,
            params_deal_module,
    ):
        return poco_text.get_ele_text_replace_space(
            poco, selector_str, optional, deal_method_name, params_deal_module
        )

    def get_ele_text(
            self,
            poco,
            selector_str,
            optional,
            deal_method_name,
            params_deal_module,
    ):
        return poco_text.get_ele_text(
            poco, selector_str, optional, deal_method_name, params_deal_module
        )

    def text_change(self, poco, select_str, optional, o_text):
        return poco_text.text_change(poco, select_str, optional, o_text)

    def ele_text_is(
            self,
            poco,
            selector_str,
            target_str,
            optional,
            deal_method=None,
            params_deal_module=None,
    ):
        poco_verify.ele_text_is(
            poco,
            selector_str,
            target_str,
            optional,
            deal_method=deal_method,
            params_deal_module=params_deal_module,
        )

    def ele_text_contains(
            self,
            poco,
            selector_str,
            target_str,
            optional,
            deal_method=None,
            params_deal_module=None,
    ):
        poco_verify.ele_text_contains(
            poco,
            selector_str,
            target_str,
            optional,
            deal_method=deal_method,
            params_deal_module=params_deal_module,
        )

    def ele_attr_is(
            self,
            poco,
            selector_str,
            optional,
            target_attr,
            target_attr_value,
            deal_method,
            params_deal_module,
    ):
        poco_verify.ele_attr_is(
            poco,
            selector_str,
            optional,
            target_attr,
            target_attr_value,
            deal_method,
            params_deal_module,
        )
