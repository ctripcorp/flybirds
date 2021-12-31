# -*- coding: utf-8 -*-
"""
Convert poco object
"""
import flybirds.core.plugin.plugins.default.ui_driver.poco.parse_selector as msd
import flybirds.core.plugin.plugins.default.ui_driver.poco.poco_selector as pc
import flybirds.utils.snippet as snippet
from flybirds.core.global_context import GlobalContext as g_Context
from flybirds.utils import language_helper as lan


def create_path_poco(poco, path, first_selector="name"):
    """
    convert the path of the ui element described in natural language into
    a poco object.
    """
    multi_list = path.split("->")
    poco_object = None

    # get current language
    language = g_Context.get_current_language()

    for index in range(len(multi_list)):
        cur_selector = multi_list[index].strip()
        if index == 0:
            poco_object = pc.create_poco_object(
                poco,
                msd.create_multi_selector(
                    cur_selector, first_selector
                ),
            )
        else:
            if cur_selector == lan.parse_glb_str("parent", language):
                poco_object = pc.create_parent(poco_object)
            else:
                target_index = 1
                select_dic = {}
                hierarchy_tag = cur_selector
                if cur_selector.startswith(
                        lan.parse_glb_str("rank", language)):
                    target_index = snippet.chose_first_number(cur_selector)
                else:
                    cur_index_selectors = cur_selector.split(" ", 1)
                    target_index = snippet.chose_first_number(
                        cur_index_selectors[0].strip()
                    )
                    select_dic = msd.create_multi_selector(
                        cur_index_selectors[1].strip()
                    )
                    hierarchy_tag = cur_index_selectors[0].strip()
                if lan.parse_glb_str("children", language) in hierarchy_tag:
                    if target_index == 1:
                        poco_object = pc.create_first_child(
                            poco_object, select_dic
                        )
                    else:
                        poco_object = pc.select_child(
                            poco_object, target_index, select_dic
                        )
                if lan.parse_glb_str("sibling", language) in hierarchy_tag:
                    if target_index == 1:
                        poco_object = pc.create_first_sibling(
                            poco_object, select_dic
                        )
                    else:
                        poco_object = pc.select_sibling(
                            poco_object, target_index, select_dic
                        )
                if lan.parse_glb_str("offsprings", language) in hierarchy_tag:
                    if target_index == 1:
                        poco_object = pc.create_first_offspring(
                            poco_object, select_dic
                        )
                    else:
                        poco_object = pc.select_offspring(
                            poco_object, target_index, select_dic
                        )
    return poco_object
