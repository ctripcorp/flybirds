# -*- coding: utf-8 -*-
"""
Poco selector api
"""


def create_poco_object(poco, select_dic={}):
    """
    create page elements corresponding to pocoUi elements
    :param poco:
    :param select_dic: Constructing pocoObject's qualifiers
    :return:
    """
    return poco(**select_dic)


def create_parent(poco_object):
    """
    create the parent element of the pocoUi element
    :param poco_object:
    :return:
    """
    return poco_object.parent()


def create_first_child(poco_object, select_dic={}):
    """
    create the first child element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    if len(select_dic) >= 1:
        return poco_object.child(**select_dic)
    else:
        return poco_object.child()


def create_first_offspring(poco_object, select_dic={}):
    """
    create the first descendant element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    if len(select_dic) >= 1:
        return poco_object.offspring(**select_dic)
    else:
        return poco_object.offspring()


def create_first_sibling(poco_object, select_dic={}):
    """
    create the first sibling element of the pocoUi element
    :param poco_object:
    :param select_dic:
    :return:
    """
    if len(select_dic) >= 1:
        return poco_object.sibling(**select_dic)
    else:
        return poco_object.sibling()


def select_child(poco_object, target_index, select_dic={}):
    """
    select the child element of the pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any child elements or the number of child elements is less than
    target_index,an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return poco_object.child(**select_dic)[target_index]


def select_offspring(poco_object, target_index, select_dic={}):
    """
    select which descendant element of pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any descendant elements or the number of descendant elements is less than
    target_index, an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return poco_object.offspring(**select_dic)[target_index]


def select_sibling(poco_object, target_index, select_dic={}):
    """
    select which sibling element of pocoUi element
    if pocoUi does not exist on the page or the pocoUi element does not have
    any sibling elements or the number of sibling elements is less than
    target_index, an exception is thrown.
    :param poco_object:
    :param target_index:
    :param select_dic:
    :return:
    """
    return poco_object.sibling(**select_dic)[target_index]
