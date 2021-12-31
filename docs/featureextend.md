# Problems encountered

During feature authoring, you may encounter the following two scenarios:

The public statements provided cannot meet the needs of their own projects, so they need to be customized. For example, a statement of "jump to Ctrip international ticket list page" is required, but because this statement is closely related to business and is unlikely to be used by other projects, it is not suitable to be put into public statements.

A certain section of logic needs to use multiple public statements to express, but this is not conducive to reuse and reading. It needs to be secondary encapsulated on the basis of public statements. For example, the implementation of login logic includes opening the login page, entering the account and password, clicking confirm and other statements. In order to facilitate reuse and reading, such logic should be written in the code rather than multiple step statements.

For the above two scenarios, you need to use the user-defined statement function. The custom statement function will use python. If you don't know the programming language, you don't have to worry too much, because you will only use the most basic Python syntax, which won't be too difficult.

# How to use
1. Enter the project directory "Pscript/dsl/steps"
2. Create a new. Py file to write custom statements
3. Import the .Py file in feature/steps/steps.py

Following is code example
```python
# -*- coding: utf-8 -*-

from behave import step


@step("Create new milestone[{param1}]and[{param2}]")
def create_milestone_with_title(context, param1, param2):
    param1 = param1.strip()
    param2 = param2.strip()
    print(f'I create milestone with title {param1} and {param2}!')

```