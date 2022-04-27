<p align="center">
  <img width="350" src="./docs/logo.png" alt="logo" />
</p>

# Flybirds | [English Version](https://github.com/ctripcorp/flybirds/blob/main/docs/readme_en.md)

[![downloads](https://pepy.tech/badge/flybirds)](https://pepy.tech/project/flybirds)
[![Downloads/month](https://pepy.tech/badge/flybirds/month)](https://pepy.tech/project/flybirds)
[![Downloads/week](https://pepy.tech/badge/flybirds/week)](https://pepy.tech/project/flybirds)
[![pypi version](https://img.shields.io/pypi/v/flybirds.svg)](https://pypi.python.org/pypi/flybirds)
[![pyversions](https://img.shields.io/pypi/pyversions/flybirds.svg)](https://pypi.python.org/pypi/flybirds)

> 基于自然语言的，跨端跨框架 BDD UI自动化测试方案

## 架构

![Arc](https://flybirds.readthedocs.io/zh_CN/latest/_images/flybirds.png)

## Enjoying this?

请给我们支持，点上一颗 Star

## 快速开始 

Flybirds是基于BDD模式的前端UI自动化测试框架,提供了一系列开箱即用的工具和完善的文档。
- 基于Behave，实现BDD中“自然语言测试用例文档”和“自动化测试代码”关联需要用到支持BDD工具。
- 基于Airtest，实现BDD中“测试用例能在自动化测试平台上执行”需要用到移动端UI自动化测试框架。
- 基于Playwright, 实现BDD中“测试用例能在自动化测试平台上执行”需要用到Web端UI自动化测试框架。

## 特性

使用Flybirds你能够完成大部分的手机端自动化操作，以下是一些帮助入门的特性描述：
- 基于BDD模式，类自然语言语法
- 支持Android、iOS、Web 自动化操作、表单提交、UI元素校验、键盘输入、Deeplink跳转等
- 一套用例，支持 Android、iOS、Web 三端
- 默认支持英文、中文两种语言，支持更多语言扩展
- 插件式设计，支持用户自定义自动化扩展
- 提供cli脚手架，快速搭建项目
- 提供html报告

## 环境要求

- python(3.7-3.9)
- nodejs(12+)

## 环境搭建

#### 使用`pip`安装flybirds框架，过程中会自动安装所需的 [依赖包](https://github.com/ctripcorp/flybirds/blob/main/docs/relate_zhCN.md)
```bash
pip3 install flybirds
```
在Mac/Linux系统下，需要手动赋予adb可执行权限，Android项目才能正常工作

- for mac
```bash
cd {your_python_path}/site-packages/airtest/core/android/static/adb/mac
chmod +x adb
```
- for linux
```bash
cd {your_python_path}/site-packages/airtest/core/android/static/adb/linux
chmod +x adb
```

## 创建项目
```bash
flybirds create 
```
Web项目，需安装浏览器
```bash
# 不带参数的运行将安装默认所有浏览器
playwright install
```

```bash
# 通过提供一个参数来安装特定的浏览器
playwright install webkit
```

```bash
# 查看支持安装的浏览器
playwright install --help
```

## 教程
- [环境准备](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id5)
- [运行演示](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id7)
- [项目结构](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id6)
- [自动化操作语法](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#step)
- [运行前检查](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id13)
- [开始运行](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id15)
- [配置参数](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id16)
- [脚手架参数](https://github.com/ctripcorp/flybirds/blob/main/docs/flybirds_cli_zhCN.md)
- [多语言](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id19)
- [持续集成](https://flybirds.readthedocs.io/zh_CN/latest/BDD-UI-Testing-Flybirds.html#id20)
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

