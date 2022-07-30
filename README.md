<p align="center">
  <img width="350" src="./docs/logo.png" alt="logo" />
</p>

# Flybirds | [English Version](https://github.com/ctripcorp/flybirds/blob/main/docs/readme_en.md)

[![downloads](https://pepy.tech/badge/flybirds)](https://pepy.tech/project/flybirds)
[![Downloads/month](https://pepy.tech/badge/flybirds/month)](https://pepy.tech/project/flybirds)
[![Downloads/week](https://pepy.tech/badge/flybirds/week)](https://pepy.tech/project/flybirds)
[![pypi version](https://img.shields.io/pypi/v/flybirds.svg)](https://pypi.python.org/pypi/flybirds)
[![pyversions](https://img.shields.io/pypi/pyversions/flybirds.svg)](https://pypi.python.org/pypi/flybirds)

> 跨端跨框架 BDD UI自动化测试方案

## 背景

**Flybirds** 是一套基于BDD模式的前端UI自动化测试框架，提供了一系列开箱即用的工具和完善的文档。

多端研发对于当今时代的前端开发来说是个绕不过去的话题，为了解决这些问题，行业内推出了很多开发方案，但是跨端 UI 自动化测试的解决方案并不多。

Flybirds从2022年初开源至今，通过与社区内活跃用户的交流和反馈，推出了v0.2 版本的跨端跨框架测试方案，一套脚本多端运行，插件化的架构设计，也方便社区开发者自由加入扩展，一起共建成长。

## 我们需要一个怎么样的多端测试方案
近几年，每隔一段时间就会有很多新的开发框架出现，带来了更好的开发体验和性能的同时，也给自动化测试创造了很多难题。

我们到底需要一个怎样的多端测试方案呢？从 Flybirds 的视角来说，我们希望多端测试不会成为研发流程中的障碍，特别是多端生态整体呈现欣欣向荣之时，自动化测试方案应和开发方案共同成长。

不论是 Web 、React Native 端，还是Native端，理想的方案应该进行多端适配，保留良好扩展，兼顾更多框架，由社区共同建设，促进整体生态繁荣，因此就有了Flybirds 向社区提供的跨端跨框架测试方案。


## 插件化架构
插件化架构帮助我们将每一个端的能力拆分开, 插件提供运行时所需的组件、API 和配置，Flybirds 将它们分别注入对应的生命周期。

![Arc](https://flybirds.readthedocs.io/zh_CN/latest/_images/flybirds.png)

* 基于Behave，实现BDD中“自然语言测试用例文档”和“自动化测试代码”关联所需要用到的支持BDD工具。
* 基于Airtest，实现BDD中“测试用例能在自动化测试平台上执行”所需要用到的UI自动化测试框架。
* 基于Playwright, 实现BDD中“测试用例能在自动化测试平台上执行”需要用到Web端UI自动化测试框架。
* 基于PaddleOCR和OpenCV, 实现BDD中“测试用例能在自动化测试平台上执行”需要用到的OCR和图像识别能力。
* 基于Multiple-cucumber-html-reporter，实现可视化的测试报告

## 文件结构

```bash
 																
├─ cli	                        脚手架
├─ core
|   ├─ config_manage.py         配置管理
|   ├─ dsl
|   │    ├─ globalization       国际化处理
|   │    └─ step                Step 列表
|   ├─ global_resource.py       全局配置
|   ├─ launch_cycle             生命周期管理
|   └─ plugin
|        ├─ event               事件管理
|        ├─ plugin_manager.py   插件管理
|        └─ plugins					
|             ├─ android        Andriod 相关处理
|             ├─ ios            iOS 相关处理
|             └─ web            Web 相关处理
├─ report                       报告
├─ template                     模板处理
└─ utils								

```

## 特性

使用Flybirds你能够完成大部分的手机端自动化操作，以下是一些帮助入门的特性描述：
- 基于BDD模式，类自然语言语法
- 支持自动化操作、表单提交、UI元素校验、键盘输入、Deeplink跳转等
- 支持 Android、iOS、React Native、Flutter、Web
- 多端脚本复用
- 支持多浏览器渲染引擎：Chromium、WebKit 和 Firefox
- 支持多浏览器并发模式下的兼容性测试
- 默认支持英文、中文两种语言，支持更多语言扩展
- 插件式设计，支持用户自定义自动化扩展
- 提供cli脚手架，快速搭建项目
- 提供html报告

## Enjoying this?

请给我们支持，点上一颗 Star

## 教程
- [环境准备](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id6)
- [运行前检查](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id8)
- [运行](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id10)
- [项目细节](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id13)
- [DSL step](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id18)
- [Android端例子](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#android)
- [iOS端例子](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#ios)
- [OCR使用例子](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#ocr)
- [Web端例子](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id69)
- [多端应用例子](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id80)
- [数据驱动参数化](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id83)
- [多浏览器并发](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id84)
- [自定义框架扩展](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id87)
- [多语言](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id88)
- [持续集成](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id89)
- [更多细节](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#)


## 贡献

1. Fork 仓库
2. 创建分支 (`git checkout -b my-new-feature`)
3. 提交修改 (`git commit -am 'Add some feature'`)
4. 推送 (`git push origin my-new-feature`)
5. 创建 PR


## 欢迎 fork 和反馈

如有建议或意见，欢迎在 GitHub [issues](https://github.com/ctripcorp/flybirds/issues) 区提问


## 协议

本仓库遵循 [MIT 协议](http://www.opensource.org/licenses/MIT)


## 致谢

感谢以下仓库让Flybirds变得更好：
- [airtest](https://github.com/AirtestProject)
- [behave](https://github.com/behave)
- [playwright](https://github.com/microsoft/playwright-python)
- [multiple-cucumber-html-reporter](https://github.com/wswebcreation/multiple-cucumber-html-reporter)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

