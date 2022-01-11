# Flybirds | [English Version](https://github.com/ctripcorp/flybirds/blob/main/docs/readme_en.md)

> 行为驱动开发（Behavior-driven development，缩写BDD），是一种软件过程的思想或者方法，是一种敏捷软件开发的技术.

Flybirds是基于BDD模式的前端UI自动化测试框架,提供了一系列开箱即用的工具和完善的文档。
- 基于Behave，实现BDD中“自然语言测试用例文档”和“自动化测试代码”关联需要用到支持BDD工具。
- 基于Airtest，实现BDD中“测试用例能在自动化测试平台上执行”需要用到UI自动化测试框架。
 

## 特性

使用Flybirds你能够完成大部分的手机端自动化操作，以下是一些帮助入门的特性描述：
- 基于BDD模式，类自然语言语法
- 支持自动化APP操作、表单提交、UI元素校验、键盘输入、Deeplink跳转等
- 默认支持英文、中文两种语言，支持更多语言扩展
- 插件式设计，支持用户自定义自动化扩展
- 提供cli脚手架，快速搭建项目
- 提供html报告

## 环境要求

- python(3.7-3.9)
- nodejs(12+)

## 快速开始

### 1. 环境搭建

#### 使用`pip`安装flybirds框架，过程中会自动安装所需的 [依赖包](https://github.com/ctripcorp/flybirds/blob/main/docs/relate_zhCN.md)
```bash
pip3 install flybirds
```
在Mac/Linux系统下，需要手动赋予adb可执行权限

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
#### 使用脚手架创建项目
```bash
flybirds create 
```

创建过程中会提示输入以下信息
- 项目名称
- 测试平台：Android / iOS
- 测试设备名称（ 可跳过，后续可在config中配置`deviceId`节点 ）
- webDriverAgent的**BundleID**（ 可跳过，ios设备连接使用，后续可在config中配置`webDriverAgent`节点 ）
- APP测试包名称（可跳过，默认为ctrip演示包，后续可在config中配置`packageName`节点）

为了帮助使用，项目创建时，会在test目录下生成演示features，后续可自行删除

### 2. 测试执行

1. 请确保配置的测试设备能够正常连接
    - Android: 执行命令 `adb devices` , 检查设备列表中是否包含测试设备
    - iOS：以`tidevice`库举例，执行命令 `tidevice list`，检查设备列表中是否包含测试设备  

    [Android设备连接 Q&A](https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/)
   - 请先安装手机对应品牌的官方驱动，确保能使用电脑对手机进行USB调试
   - 确保已经打开了手机中的"开发者选项"，并且打开"开发者选项"内的"允许USB调试"
   - 部分手机需要打开"允许模拟位置"、"允许通过USB安装应用"
   - 关闭电脑上已经安装的手机助手软件，能避免绝大多数问题，请务必在任务管理器中手工结束手机助手进程
   
   [iOS设备连接 Q&A](https://airtest.doc.io.netease.com/IDEdocs/device_connection/4_ios_connection/)
   - 请先准备一台macOS ，使用xcode部署 iOS-Tagent 成功后，能够在mac或windows机器上连接到iOS手机。请点击[链接](https://github.com/AirtestProject/IOS-Tagent)下载项目代码到本地进行部署。
   - mac 环境通过 Homebrew 安装iproxy `brew install libimobiledevice`
   - windows 环境安装[itunes](https://support.apple.com/downloads/itunes)


2. 下载安装测试包
    - Android：框架会通过`config`中配置的`packagePath`自动下载测试包并安装（请确保手机已经打开”允许安装未知来源“ ）。也可手动下载安装：[下载地址](https://download2.ctrip.com/html5/Ctrip_V8.43.0_SIT4-100053_Product_9725895.apk)
    - iOS:
       1. 请手动下载演示APP进行安装：[下载地址](https://download2.ctrip.com/html5/Ctrip_V8.43.0_SIT4-092310_Product_9725506.ipa)
       2. 开启wdaproxy： ```shell tidevice --udid 
       $udid wdaproxy -B $web_driver_angnt_bundle_id -p $port```


3. 运行测试，默认运行features目录下所有feature

```bash
cd {PATH_TO_PROJECT_FOLDER}
flybirds run  # 运行所有feature
flybirds run -P features/test/android  # 运行所有android feature
flybirds run -P features/test/ios # 运行所有ios feature
```

- 演示feature中包含了主要的自动化语法，为了让演示正常运行，建议不要修改配置项`packageName`和`packagePath`。如无需演示，可自行修改

- 更多执行参数说明 ：[项目脚手架](#fc)
- 更多演示项目说明 ： [项目结构](#dp) 
- 更多Feature编写说明 ：[Feature编写](#fw)



    


### 3. <span id="dp">项目结构</span>

- [项目结构&配置参数](https://github.com/ctripcorp/flybirds/blob/main/docs/demoproject_zhCN.md)


### 4. <span id="fw">Feature编写</span>

- [Behave语法](https://github.com/ctripcorp/flybirds/blob/main/docs/behaves_zhCN.md)
- [公共语句说明](https://github.com/ctripcorp/flybirds/blob/main/docs/casedsl_zhCN.md)
- [页面元素](https://github.com/ctripcorp/flybirds/blob/main/docs/pageelement_zhCN.md)
- [业务Feature语句扩展](https://github.com/ctripcorp/flybirds/blob/main/docs/featureextend_zhCN.md)

### 5. <span id="fc">项目脚手架</span>

- [脚手架参数说明](https://github.com/ctripcorp/flybirds/blob/main/docs/flybirds_cli_zhCN.md)


### 6. 更多项目介绍
- [携程机票BDD-UI-Testing框架Flybirds](https://flybirds.readthedocs.io/zh_CN/latest/)

## 贡献

1. Fork 仓库
2. 创建分支 (`git checkout -b my-new-feature`)
3. 提交修改 (`git commit -am 'Add some feature'`)
4. 推送 (`git push origin my-new-feature`)
5. 创建 PR


## 欢迎 fork 和反馈

如有建议或意见，欢迎在 github [issues](https://github.com/ctripcorp/flybirds/issues) 区提问


## 协议

本仓库遵循 [MIT 协议](http://www.opensource.org/licenses/MIT)


## 致谢

感谢以下仓库让Flybirds变得更好：
- [airtest](https://github.com/AirtestProject)
- [behave](https://github.com/behave)
- [multiple-cucumber-html-reporter](https://github.com/wswebcreation/multiple-cucumber-html-reporter)
