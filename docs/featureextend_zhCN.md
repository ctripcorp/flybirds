# 遇到的问题
在编写Feature的过程中，可能会遇到以下两种场景：

提供的公共语句不能满足自身项目的需求，需要自定义语句。 比如：需要一条"跳转携程国际机票列表页"的语句，但由于这条语句和业务紧密关联并且被其他项目使用到的可能性很小，并不适合放入公共语句中。

某一段逻辑需要使用多条公共语句才能表达，但这样不利于复用和阅读，需要在公共语句基础上做二次封装。 比如: 登陆逻辑的实现包含了打开登陆页面，输入账号密码，点击确认等多条语句。 这样的逻辑为了方便复用和阅读，逻辑应该写在代码里，而不是写多条step语句。

面对以上两种场景，需要用到自定义语句功能。自定义语句功能会用到python，如果你不了解这门编程语言，也不必要太担心，因为只会使用到最基础的python语法，这并不会太难。

# 使用方法
1. 进入项目目录"psscript/dsl/steps"
2. 新建.py文件来编写自定义语句
3. 在feature/steps/steps.py中import该.py文件

示例代码如下
```python
# -*- coding: utf-8 -*-

from behave import step


@step("Create new milestone[{param1}]and[{param2}]")
def create_milestone_with_title(context, param1, param2):
    param1 = param1.strip()
    param2 = param2.strip()
    print(f'I create milestone with title {param1} and {param2}!')

```