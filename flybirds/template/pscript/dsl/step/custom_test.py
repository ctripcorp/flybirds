# -*- coding: utf-8 -*-
"""
Custom Step statement
"""
from behave import step


@step("Create new milestone[{param1}]and[{param2}]")
def create_milestone_with_title(context, param1, param2):
    param1 = param1.strip()
    param2 = param2.strip()
    print(f'I create milestone with title {param1} and {param2}!')


@step("Close existing milestone[{param1}]and[{param2}]")
def delete_milestone_with_title(context, param1, param2):
    param1 = param1.strip()
    param2 = param2.strip()
    print(f'I delete milestone with title {param1} and{param2}!')
