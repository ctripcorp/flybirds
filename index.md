Flybirds
--

![clip](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/tripflybirds.gif)

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

![architecture](https://flybirds.readthedocs.io/zh_CN/latest/_images/flybirds.png)

* 基于Behave，实现BDD中“自然语言测试用例文档”和“自动化测试代码”关联所需要用到的支持BDD工具。
* 基于Airtest，实现BDD中“测试用例能在自动化测试平台上执行”所需要用到的UI自动化测试框架。
* 基于Playwright, 实现BDD中“测试用例能在自动化测试平台上执行”需要用到Web端UI自动化测试框架。
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

使用**Flybirds**你能够完成大部分的手机端自动化操作，以下是一些帮助入门的特性描述：

* 基于BDD模式，类自然语言语法
* 支持Android、iOS、Web 自动化操作、表单提交、UI元素校验、键盘输入、Deeplink跳转等
* 支持多端脚本复用
* 支持多浏览器渲染引擎：Chromium、WebKit 和 Firefox
* 支持多浏览器并发模式下的兼容性测试
* 默认支持英文、中文两种语言，支持更多语言扩展
* 插件式设计，支持用户自定义自动化扩展
* 提供cli脚手架，快速搭建项目
* 提供html报告

## 环境要求

- python(3.7-3.9)
- nodejs(12+)

## 环境搭建

1. **使用`pip`安装flybirds框架，过程中会自动安装所需的 [依赖包](https://github.com/ctripcorp/flybirds/blob/main/docs/relate_zhCN.md)**

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
2. **使用脚手架创建项目**

```bash
flybirds create 
```

![clicreate](https://flybirds.readthedocs.io/zh_CN/latest/_images/clicreate.png)


## 运行前检查

### Android、iOS
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

### Web
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

## 运行

### 运行参数

在终端输入以下内容来查看**flybirds**运行项目时支持的操作
```bash
flybirds run --help
```
- **run**

  执行features目录下所有的feature文件

  ```bash
  cd {PATH_TO_PROJECT_FOLDER}
  flybirds run  # 运行所有feature
  flybirds run -P features/test/android  # 运行所有android feature
  flybirds run -P features/test/ios # 运行所有ios feature
  ```


- **--path, -P**

  指定需要执行的feature集合，可以是目录，也可以指定到具体feature文件，默认是 ‘**features**’ 目录.

  示例:

  ```bash
  flybirds run -P ./features/test/demo.feature
  ```
- **--tag, -T**

  运行有特定tag的场景，多个用逗号隔开，‘-’开头表示不运行包含此tag的场景
  ```bash
  flybirds run -T tag1,tag2,-tag3,tag4
  ```
- **--format, -F**

  指定生成测试结果的格式，默认是 json. 

  示例:

  ```bash
  #默认
  flybirds run --format=json
  ```

- **--define, -D   TEXT(可选)**

​	传入用户自定义的参数:

作用：覆盖`config`配置文件中的相应配置的值，比如：

```bash 
# 通过参数切换执行平台Android、iOS、Web
flybirds run --define platform=web 
```

- **--rerun  /--no-rerun (可选)**

​	指定失败的场景是否需要重新运行，默认是 ‘True’ ,失败后会自动重跑。

示例：

```bash
#失败场景不重跑
flybirds run --no-rerun 
```

- **--html/--no-html  (可选)**

​	指定case 执行完成后是否生成html测试报告，默认是 ‘True’ ,执行完成后自动生成结果测试报告。

示例：

```bash
#不生成测试报告
flybirds run --no-html
```

- **--processes, -p    INTEGER(可选)**

  指定并发执行时开启进程的最大数量。默认是4 。

  **注意：** 此命令只在 **web** 平台执行时有效。

示例：

```bash
flybirds run --path features -p 5
```

### 运行演示

为了帮助使用，项目创建时，会生成中英文的Android、iOS、Web 演示feature，方便用户参考。

```
features/test/
features/test/android
features/test/android/cn/everything.feature
features/test/android/en/everything.feature
features/test/ios
features/test/ios/cn/everything.feature
features/test/ios/en/everything.feature
```

以“Android”为例
1. 执行命令 `adb devices` , 检查设备列表中是否包含测试设备
2. 开始运行
```
cd {PATH_TO_PROJECT_FOLDER}
flybirds run -P features/test/android
```
框架会通过`flybirds_config`中配置的`packagePath`自动下载测试包并安装（请确保手机已经打开”允许安装未知来源“ ）    
运行结果如下

```
11 features passed, 0 failed, 0 skipped, 0 untested
23 scenarios passed, 0 failed, 0 skipped, 0 untested
117 steps passed, 0 failed, 0 skipped, 0 undefined, 0 untested
Took 5m21.300s
=====================================================================================
    Multiple Cucumber HTML report generated in:

    /Users/test/my_first_project/report/7eb9162a-9d42-4fde-a5d7-d8d4bca7a8d8/index.html
=====================================================================================
```

## 项目细节

### 项目结构
- config：配置文件
- features：测试用例feature文件
- pscript：自定义扩展
- report：测试报告


### features目录
基础目录结构如下
* test：存放feature文件，这些文件使用自然语言编写，最好由软件项目中的非技术业务、产品人员参与者编写。
* steps：存放场景中使用的step语句实现，“steps.py”中加载了所有的step语句模版
```
features/
features/test/
features/test/everything.feature
features/steps/
features/steps/steps.py
```
复杂些的目录结构参考如下
```
features/
features/test/
features/test/list.feature
features/test/buy.feature
features/test/detail.feature
features/steps/
features/steps/steps.py
```

### feature文件
> feature文件包含用户动作，行为特征描述及预期结果的文本，行为特征部分使用Gherkin语言编写。

feature文件，也称为功能文件，有两个目的：文档和自动化测试。

以关键字开头（“功能”、“场景”、“场景大纲”、“当”、“而且”、“那么”……）, 文件中的任何位置都允许使用注释行。

**功能(Feature)** 是被测试功能的一些合理的描述性标题，由场景组成。他们可以选择有一个描述、一个背景和一组标签。

**背景(Background)** 由一系列类似于场景的步骤组成。它允许您向功能的场景添加一些上下文。在此功能的每个场景之前执行。

**场景(Senario)** 标题应该是被测试场景的合理描述性标题，由一系列给定条件的步骤组成

**场景大纲(Senario Outline)** 包含功能的详细描述，可以有一组预期条件和结果来配合您的场景步骤

以下是中文feature例子
![featureCN](images/feature_zhCN.png)

以下是英文feature例子
![feature_en](images/feature_en.png)

### 配置参数

#### 必须配置项
进行**移动端**测试时，必须配置项：`deviceId` 、`packageName`。在IOS设备上测试时，必须额外配置`webDriverAgent`。

#### **flybirds_config.json**

- `packageName` 

  app的packageName,示例为ctrip的packageName,此配置必须填写

- `packagePath`

  下载安装app的地址，项目运行时会自动从该地址下载并安装在测试设备中，为空时不下载

- `overwriteInstallation`

  是否每次运行前覆盖安装测试包，默认："True"

- `uniqueTag`

  app的唯一性标识，比如:clientId, 默认："000"

- `defaultUser` 

  运行前需要全局登录时会使用此用户名, 默认：“null”

- `defaultPassword` 

  运行前需要全局登陆时会用此密码, 默认：“null”

- `deviceId` 

  示例为设备的序列号  Android设备使用 “adb devices” 获取, 默认："10.5.170.85:5555"

- `platform` 

    项目case执行的平台，目前支持`android` 、`ios` 和 `web`, 不填时默认为：`android`

- `webDriverAgent` 

  设备里WebDriverAgent的BundleID，可通过`tidevice applist`命令查看。连接IOS设备时必填。

- `headless` 

  浏览器的运行模式，为 true 时表示浏览器将以**无头**方式运行。`platform=web`时必填。默认为：`true`

- `browserType` 

  支持的浏览器类型： `chromium`, `firefox` and `webkit`。`platform=web`时必填。支持同时配置多个值，

  如："browserType": ["firefox","chromium","webkit"]。 默认为："browserType": ["chromium"]。

- `requestInterception` 

    开启请求拦截。`platform=web`时必填。默认为：`true`

- `ignoreOrder` 

​		请求报文比对时忽略报文节点的顺序或重复的列表差异。默认为：`false`。仅在`requestInterception=true`时有效。

- `abortDomainList` 

​		请求拦截时，终止路由的域名列表。如："abortDomainList": ["google.com"]。仅在`requestInterception=true`时有效。

- `beforeRunPage` 

  在开始测试前对app的行为配置，默认时“重启app”保证测试时页面处于大首页，还有startApp(启动app)，stopApp(关闭app)、None(无任何操作), 默认："restartApp"

- `scenarioFailPage`

  在测试用例执行失败后对app的配置行为，默认是“重启app”保证当前内存中不会积压太多历史页面，还有backupPage(返回上一页)，stopApp(停止app)、None(无任何操作), 默认： "restartApp"

- `scenarioSuccessPage` 

  测试用例执行成功后对app的配置行为，默认是“None”无任何操作，还有restartApp(重启app)，backupPage(返回上一页)，stopApp(停止app), 默认："None"

- `beforeRunLogin` 

  开始测试前是否需要登陆, 默认："false"

- `failScreenRecord` 

  失败后是否需要关联用例的执行录屏文件到测试报告中, 默认："true"

- `scenarioScreenRecordTime` 

  failScreenRecord为ture开启失败录屏时，录制屏幕的最大时长, 默认：120

- `failRerun` 

  失败后是否重新运行, 默认：true

- `maxFailRerunCount` 

  失败重新运行所满足的失败个数, 默认：1

- `maxRetryCount` 

  失败重试次数, 默认：2

- `waitEleTimeout` 

  页面中查找元素的超时时间, 默认：15

- `waitEleDisappear` 

  页面中指定元素消失的超时时间, 默认：10

- `clickVerifyTimeout` 

  点击操作的判断渲染完成的超时时间, 默认：15

- `useSwipeDuration` 

  使用全局配置的滑动时间, 默认："false"

- `swipeDuration` 

  当useSwipeDuration为ture时，滑动操作的时间为该值, 默认：6

- `usePocoInput` 

  输入是否使用poco的输入方法，默认使用airtest, 默认：false

- `afterInputWait` 

  输入框输入后的等待时间, 默认：1

- `useSearchSwipeDuration`

  滑动查找中是否使用全局的滑动时间, 默认：false

- `searchSwipeDuration`

  useSearchSwipeDuration为ture时，滑动查找中的所有滑动时间由该值全局设置, 默认：1

- `swipeSearchCount` 

  滑动查找元素的最大滑动次数, 默认：5

- `swipeSearchDistance` 

  滑动查找中每次滑动的距离, 默认：0.3

- `pageRenderTimeout` 

  等待页面渲染完成的时间，语句 “页面渲染完成出现元素[选择器{, path=false, multiSelector=false, timeout=10}]” 中的timeout参数的全局配置时间, 默认：35

- `appStartTime` 

  APP 启动后等待时间, 默认：6

- `swipeReadyTime` 

  滑动开始前的等待时间, 默认：3

- `verifyPosNotChangeCount`

  判断元素位置未发生改变的最大判断次数, 默认：5

- `screenRecordTime` 

  录屏时间, 默认：60

- `useSnap`

  是否使用快照查找文案, 默认：true

- `useAirtestRecord` 

  使用airtest录屏, 默认：true



#### **schema_url.json**

用于对多端页面的`schema`访问地址进行统一配置

**示例：**

- 多端页面的 `schema` 访问地址相同：

  "首页": "ctrip://homepage"
  
  示例为携程APP首页
  
- 多端页面的 `schema` 访问地址不同

  示例为携程android、ios、web端的列表页地址
  
  ```json
  "列表页": {
    "android": "/rn_test/ctrip_list_android/",
    "ios": "/rn_test/ctrip_list_ios/",
    "web": "https://ctrip.test/list"
  }
  ```


#### **ele_locator.json**

用于对多端元素的定位方式进行统一配置

**示例：**

- 多端元素的 定位方式相同：

  "元素1": "text=帮助中心"

  示例为【元素1】的定位方式

- 多端元素的 定位方式不同

  示例为【元素2】在android、ios、web端的定位方式

  ```json
  "元素2": {
    "android": "text=机票",
    "ios": "label=机票",
    "web": "#s-top-loginbtn"
  }
  ```
  
### Hooks
用户可在以下文件中定义hooks
```
pscript/dsl/step/hook.py
```
* **before_step(context, step), after_step(context, step)**

  在每个步骤(step)之前和之后运行

* **before_scenario(context, scenario), after_scenario(context, scenario)**

  在每个场景(senario)之前和之后运行

* **before_feature(context, feature), after_feature(context, feature)**

  在每个功能文件(feature)之前和之后运行

* **before_tag(context, tag), after_tag(context, tag)**

  在用给定名称标记(tag)的部分之前和之后运行

* **before_all(context), after_all(context)**

  在所有执行之前和之后运行

### 标签(Tags)
> 可以使用tag标记不同的场景，方便有选择性的运行。

下面是一个例子
![tag](https://flybirds.readthedocs.io/zh_CN/latest/_images/tag.png)

运行有特定tag的场景，多个用逗号隔开
```
flybirds run -T tag1,tag2
```

‘-’开头表示运行不包含某tag的场景
```
flybirds run -T -tag
```

### 报告(report)
> 报告包含汇总Summary和功能(feature)、场景(senario)的执行结果，对于失败的场景(senario)，报告中会展示当时的屏幕图像和视频, 下面是一个例子。
![report](https://flybirds.readthedocs.io/zh_CN/latest/_images/report.png)


### 自定义DSL step

在编写Feature的过程中，可能会遇到提供的公共语句不能满足自身项目的需求，需要自定义语句。比如：需要对接某个内部工具API，此时需要用到自定义语句功能。

自定义语句功能会用到python，如果你不了解这门编程语言，也不必要太担心，因为只会使用到最基础的python语法，这并不会太难。

**使用方法**
1. 进入项目目录"psscript/dsl/steps"
2. 新建.py文件来编写自定义语句
3. 在feature/steps/steps.py中import该.py文件

示例代码如下
![dsl_extend](https://flybirds.readthedocs.io/zh_CN/latest/_images/dsl_extend.png)

对于团队内部通用的自定义功能，可以考虑创建一个extend package，flybirds支持动态加载，package命名包含“-flybirds-plugin”即可。


## DSL step

### DSL step列表
上面例子中的关键字“当”、“而且”和“那么”部分构成了测试用例的操作步骤，这些操作步骤框架中已经通过python实现。

当然在这个架构中, 各端略有不同，主要是各端的平台差异性导致，以下是各端具体支持的 DSL step 列表, 大部分step能够适用于多端

|DSL step                                                               | 语义                                                         | 适用于         |
|-----------------------------------------------------------------------| ------------------------------------------------------------ | -------------- |
| 跳转到[]                                                                 | 跳转到指定的url地址                                          | android 、web  |
| 等待[]秒                                                                 | 等待一段时间                                                 | ALL            |
| 页面渲染完成出现元素[]                                                          | 进入新的页面时检查指定元素是否渲染完成                       | ALL            |
| 点击[]                                                                  | 点击指定属性的元素                                           | ALL            |
| 点击文案[]                                                                | 点击指定文案的元素                                           | ALL            |
| 点击屏幕位置[][]                                                            | 点击屏幕指定位置                                             | ALL            |
| 在 [] 中输入[]                                                            | 在指定选择器中输入字符串                                     | ALL            |
| 在[]中清空并输入[]                                                           | 在指定选择器中清空并输入字符串                               | Web            |
| 向[] 查找[]的元素                                                           | 向指定方向查找指定属性的元素                                 | ALL            |
| 全屏向[] 滑动[]                                                            | 全屏向指定方向滑动指定距离                                   | ALL            |
| [] 向[] 滑动[]                                                           | 在指定区域内向指定方向滑动指定距离                           | ALL            |
| 存在[]的文案                                                               | 检查页面中存在指定的字符串                                   | ALL            |
| 不存在[]的文案                                                              | 检查页面中不存在指定的字符串                                 | ALL            |
| 存在[]的元素                                                               | 检查页面中存在指定属性的元素                                 | ALL            |
| 不存在[]的元素                                                              | 检查页面中不存在指定属性的元素                               | ALL            |
| 元素[]消失                                                                | 检查页面中指定属性的元素在指定时间内消失                     | App            |
| 文案[]消失                                                                | 检查页面中指定的字符串在规定时间内从页面消失                 | App            |
| 文案[] 的属性[] 为 []                                                       | 检查页面中指定文案的指定属性为指定值                         | ALL            |
| 元素[] 的属性[] 为 []                                                       | 检查页面中指定元素的指定属性为指定值                         | ALL            |
| 元素[] 位置[] 秒内未变动                                                       | 检查页面中指定元素的位置在指定时间内未发生变化               | App            |
| [] 的文案为[]                                                             | 检查页面中指定元素的文案等于指定值                           | ALL            |
| [] 的文案包含[]                                                            | 检查页面中指定元素的文案包含指定值                           | ALL            |
| 回到首页                                                                  | 回到首页                                                     | ALL            |
| 全屏截图                                                                  | 保存当前屏幕图像                                             | ALL            |
| 开始录屏                                                                  | 开始录制视频                                                 | App            |
| 开始录屏超时[]                                                              | 开始录屏并设置超时时间                                       | App            |
| 结束录屏                                                                  | 结束录制视频                                                 | ALL            |
| 连接设备[]                                                                | 连接测试设备                                                 | App            |
| 安装APP[]                                                               | 安装APP                                                      | android        |
| 删除APP[]                                                               | 删除APP                                                      | android        |
| 启动APP[]                                                               | 启动APP                                                      | App            |
| 重启APP                                                                 | 重启APP                                                      | App            |
| 关闭App                                                                 | 关闭App                                                      | App            |
| 登录账号[] 密码[]                                                           | 使用账号密码进行登录                                         | ALL            |
| 退出登录                                                                  | 退出系统登录                                                 | ALL            |
| 返回上一页                                                                 | 返回上一页面                                                 | Android 、 web |
| 在[]中向[]查找[]的元素                                                        | 在指定 选择器 的元素内 向指定方向滑动查找 指定选择器的元素   | ALL            |
| 在[]中选择[]                                                              | 在web页面下拉框元素中选择指定值                              | web            |
| 存在[父选择器]的[子选择器]的元素                                                    | 存在某个父元素，并且该父元素下存在某个子元素                 | web            |
| [父选择器]的[子选择器]的文案为[]                                                   | 存在某个父元素，并且该父元素下某个子元素的文案为指定字符串   | web            |
| 缓存服务请求[operation[,operation ...]]                                     | 缓存该服务的最后一次请求报文到本地。 <br />注意： operation 是 url 最后一个\ 和 ？ 中间的字符串，即请求名 | web            |
| 移除请求缓存[operation[,operation ...]]                                     | 从本地清除该服务的请求缓存报文。<br />注意： operation 是 url 最后一个\ 和 ？ 中间的字符串，即请求名 | web            |
| 移除所有请求缓存                                                              | 移除所有请求的缓存报文                                       | web            |
| 监听服务[operation[,operation ...]]绑定MockCase[mockCaseId[,mockCaseId ...]] | 监听相关operation的请求并拦截，用mockCaseId的返回报文进行替换<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串 | web            |
| 移除服务监听[operation[,operation ...]]                                     | 移除operation 的请求监听<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串 | web            |
| 移除所有服务监听                                                              | 移除所有请求监听                                             | web            |
| 验证服务请求[operation]与[target_data_path]一致                                | 比对相关operation的缓存报文与target_data_path对应的文件内容<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串 | web            |
| 验证服务非json请求[operation]与[target_data_path]一致                           | 比对相关operation的非json类型的缓存报文与target_data_path对应的文件内容<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串 | web            |
| 验证服务[operation]的请求参数[target_json_path]与[expect_value]一致               | 检查相关operation的缓存报文体对应参数的值与给定的期望值是否一致<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串 | web            |
| \-----                                                                | \-----                                                       | \-----         |


### 连接设备[]
**连接设备[{param}]**
- 支持平台：Android 、 IOS
- 语义：连接测试设备
- 例子：连接设备[10.21.37.123:5555]

### 安装APP[]
**安装APP[{param}]**
- 支持平台：Android
- 语义：安装APP
- 例子：安装APP[/Users/xxx/xxx.apk]

### 删除APP[]
**删除APP[{param}]**
- 支持平台：Android
- 语义：删除APP
- 例子：删除APP[package name]

### 启动APP[]
**启动APP[{param}]**
- 支持平台：Android、iOS
- 语义：启动APP
- 例子：启动APP[package name]

### 重启APP[]
**重启app**
- 支持平台：Android、iOS
- 语义：重新启动app

### 回到首页[]
**回到首页**
- 语义：跳转到首页
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 to_home() 方法

### 登录账号[] 密码[]
**登录账号[{param1}]密码[{param2}]**
- 语义：指定用户名、密码登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 login(user_name, password)方法

### 退出登录
**退出登录**
- 语义:退出当前登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 logout() 方法

### 存在 [] 的文案
**存在[字符串{, fuzzyMatch=false, timeout=10}]的文案**
- 支持平台：Android、iOS、Web
- 语义：页面中存在指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js 
存在[机票]的文案
存在[机票, timeout=10]的文案
存在[.?票, fuzzyMatch=true]的文案
```
### 不存在 [] 的文案
**不存在[字符串{, fuzzyMatch=false}]的文案**
- 支持平台：Android、iOS、Web
- 语义：页面中不存在指定的文案
```js 
不存在[机票]的文案
不存在[.?票, fuzzyMatch=true]的文案
```
### 文案 [] 消失
**文案[字符串{, fuzzyMatch=false, timeout=10}]消失**
- 支持平台：Android、iOS、Web
- 语义：指定的字符串在规定时间内从页面消失
timeout 等待消失的超时时间 ，优先级：默认值 < flybirds_config.json中的“waitEleDisappear” < 语句中指定
```js 
文案[机票]消失
文案[.?票, fuzzyMatch=true, timeout=20]消失
```
### 存在 [] 的元素
**存在[选择器{, path=false, multiSelector=false, timeout=10}]的元素**
- 支持平台：Android、iOS、Web
- 语义：页面中存在指定 选择器 的元素
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js 
存在[center_content_layout]的元素
存在[text=经济舱]的元素
存在[textMatches=.?经济舱]的元素
存在[textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true, timeout=30]的元素
存在[机票→第1个兄弟节点, path=true]的元素
```
### 不存在 [] 的元素
**不存在[选择器{, path=false, multiSelector=false}]的元素**
- 支持平台：Android、iOS、Web
- 语义：页面中不存在指定  选择器 的元素
```js
不存在[center_content_layout]的元素
不存在[text=经济舱]的元素
不存在textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true]的元素
不存在[机票→第1个兄弟节点, path=true]的元素
```
### 元素 [] 消失
**元素[选择器{, path=false, multiSelector=false, timeout=10}]消失**
- 支持平台：Android、iOS
- 语义：指定的 选择器 在规定时间内从页面消失
- timeout 等待消失的超时时间 ，优先级：默认值 < flybirds_config.json中的“waitEleDisappear” < 语句中指定
```js
元素[center_content_layout]消失
元素[text=机票]消失
元素[机票→第1个兄弟节点, path=true, timeout=15]消失
```
### [] 的文案为 []
**[选择器{, path=false, multiSelector=false, timeout=10}]的文案为[字符串{, dealMethod=name}]**
- 支持平台：Android、iOS、Web
- 语义：指定 选择器 的元素的文案为指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
[text=机票]的文案为[机票]
[textMatches=.?经济舱, timeout=15]的文案为[经济舱, dealMethod=trim_prefix]
[textMatches=.?经济舱并且visible=True, multiSelector=true, timeout=15]的文案为[经济舱, dealMethod=trim_prefix]
```
### [] 的文案包含 []
**[选择器{, path=false, multiSelector=false, timeout=10}]的文案包含[字符串{, dealMethod=name}]**
- 支持平台：Android、iOS、Web
- 语义：指定 选择器 的元素的文案包含指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
[text=机票]的文案包含[票]
[textMatches=.?经济舱, timeout=15]的文案包含[经济舱]
[textMatches=.?经济舱并且visible=True, multiSelector=true, timeout=15]的文案包含[经济, dealMethod=trim_prefix]
```
### 页面渲染完成出现元素 []
**页面渲染完成出现元素[选择器{, path=false, multiSelector=false, timeout=10}]**
- 支持平台：Android、iOS、Web
- 语义：进入新的页面时通过指定 选择器 的元素出现在页面上来判断页面渲染完成
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“pageRenderTimeout” < 语句中指定
```js
页面渲染完成出现元素[text=机票]
页面渲染完成出现元素[center_content_layout, timeout=15]
页面渲染完成出现元素[center_content_layout, timeout=40]
```
### 点击文案 []
**点击文案[字符串{, fuzzyMatch=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- 支持平台：Android、iOS、Web
- 语义：点击页面上指定的 字符串
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- verifyEle  点击后如果有局部渲染，使用该属性指定的选择器代表的元素的相关信息判断
- verifyIsPath：指定 verifyEle 是否是 path 类型的 选择器
- verifyIsMultiSelector：指定 verifyEle 是否是 多属性 类型的 选择器
- verifyTimeout 判断点击操作的渲染是否完成的超时时间，优先级：默认值 < flybirds_config.json中的“clickVerifyTimeout” < 语句中指定
- verifyAction ： verifyEle代表的元素发生特定类型的变化时表示点击后的渲染完成，
- position/text/appear/disappear: 位置发生变化/文案发生变化/出现在页面上/从页面消失
```js
点击文案[机票]
点击文案[.?票, fuzzyMatch=true, timeout=15]
点击文案[机票, verifyEle=center_content_layout, verifyAction=position]
点击文案[机票, verifyEle=text=筛选并且type=textView, verifyIsMultiSelector=true, verifyAction=position]
```
### 点击 []
**点击[选择器{, path=false, multiSelector=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- 支持平台：Android、iOS、Web
- 语义: 点击页面上指定 选择器 的元素   
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- verifyEle  点击后如果有局部渲染，使用该属性指定的选择器代表的元素的相关信息判断
- verifyIsPath：指定 verifyEle 是否是 path 类型的 选择器
- verifyIsMultiSelector：指定 verifyEle 是否是 多属性 类型的 选择器
- verifyTimeout 判断点击操作的渲染是否完成的超时时间，优先级：默认值 < flybirds_config.json中的“clickVerifyTimeout” < 语句中指定
- verifyAction：verifyEle代表的元素发生特定类型的变化时表示点击后的渲染完成，
- position/text/appear/disappear: 位置发生变化/文案发生变化/出现在页面上/从页面消失
```js
点击[text=机票]
点击[textMatches=.?票, timeout=15]
点击[center_content_layout, verifyEle=center_content_layout, verifyAction=position]
点击[testId, verifyEle=text=筛选并且type=textView, verifyIsMultiSelector=true, verifyAction=position]
```
### 点击屏幕位置 []
**点击屏幕位置[{x},{y}]**
```js
点击屏幕位置[200,100]
```
**文案[字符串{, fuzzyMatch=false, timeout=10}]的属性[属性名{, dealMethod=name}]为{属性值}**
- 支持平台：Android、iOS、Web
- 语义：页面中指定 字符串对应的元素的指定的属性的值为指定的值
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
文案[机票]的属性[text]为机票
文案[机票, timeout=15]的属性[text, dealMethod=trim_last]为机
```
### 元素 [] 的属性 [] 为 []
**元素[选择器{, path=false, multiSelector=false, timeout=10}]的属性[属性名{, dealMethod=name}]为{属性值}**
- 支持平台：Android、iOS、Web
- 语义：页面中指定 选择器 的元素的指定的 属性的值为指定的 值
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
元素[text=机票]的属性[text]为机票
元素[text=机票, timeout=15]的属性[text, dealMethod=trim_last]为机
```
### 在 [] 中输入 []
**在[选择器{, path=false, multiSelector=false, timeout=10}]中输入[文案{, pocoInput=false, afterInputWait=1}]**
- 支持平台：Android、iOS、Web
- 语义：在指定选择器的元素中输入指定的文案 
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- pocoInput: 是否使用 poco 的输入方法，默认使用的是airtest的输入方法， 优先级：默认值 < flybirds_config.json中的“usePocoInput” < 语句中指定
- afterInputWait: 输入完成的休眠时间， 优先级：默认值 < flybirds_config.json中的“afterInputWait” < 语句中指定
```js
在[inputEleId]中输入[上海]
在[type=InputView]中输入[用户名, pocoInput=true, afterInputWait=5]
```
### [] 向{上/下/左/右}滑动 []
**[选择器{, path=false, multiSelector=false, timeout=10}]向{上/下/左/右}滑动[滑动距离{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- 支持平台：Android、iOS、Web
- 语义：在指定 选择器 的滑动容器内向指定 方向 滑动指定 距离
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- startX: 在容器中滑动起始坐标的X轴的坐标值，<=1 代表百分比，>1代表像素点
- startY: 在容器中滑动起始坐标的Y轴的坐标值，<=1 代表百分比，>1代表像素点
- duration: 每次滑动的时间， 优先级：默认值 < flybirds_config.json中的“swipeDuration” < 语句中指定
- readyTime: 滑动开始前的等待时间， 优先级：默认值 < flybirds_config.json中的“swipeReadyTime” < 语句中指定
```js
[containerEleId]向左滑动[0.1]
[containerEleId]向上滑动[100, duration=5, readyTime=3]
[containerEleId]向上滑动[100, startX=0.2, startY=0.4, duration=5, readyTime=3]
```
### 向{上/下/左/右}滑动 []
**全屏向{上/下/左/右}滑动[滑动距离{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- 支持平台：Android、iOS、Web
- 语义：以全屏为容器向指定 方向 滑动指定 距离
- startX: 在全屏中滑动起始坐标的X轴的坐标值，<=1 代表百分比，>1代表像素点
- startY: 在全屏中滑动起始坐标的Y轴的坐标值，<=1 代表百分比，>1代表像素点
- duration: 每次滑动的时间， 优先级：默认值 < flybirds_config.json中的“swipeDuration” < 语句中指定
- readyTime: 滑动开始前的等待时间， 优先级：默认值 < flybirds_config.json中的“swipeReadyTime” < 语句中指定
```js
向上滑动[0.05]
向下滑动[0.4, readyTime=3, duration=2]
```
### 在 [] 中向下查找 [] 的元素
**在[选择器{, path=false, multiSelector=false, timeout=10}]中向{上/下/左/右}查找[选择器{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]的元素**
- 支持平台：Android、iOS、Web
- 语义：在指定 选择器 的元素内 向指定方向滑动查找 指定选择器的元素
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- swipeCount: 滑动查找最大滑动次数，超过这个值的滑动操作后还未在页面中找到指定元素则失败， 优先级：默认值 < flybirds_config.json中的“swipeSearchCount” < 语句中指定
- startX: 在全屏中滑动起始坐标的X轴的坐标值，<=1 代表百分比，>1代表像素点
- startY: 在全屏中滑动起始坐标的Y轴的坐标值，<=1 代表百分比，>1代表像素点
- duration: 每次滑动的时间， 优先级：默认值 < flybirds_config.json中的“searchSwipeDuration” < 语句中指定
- distance：滑动查找中每次滑动的距离， 优先级：默认值 < flybirds_config.json中的“swipeSearchDistance” < 语句中指定
```js
在[containerId]中向下查找[text=机票]的元素
在[containerId]中向下查找[testId, distance=0.5, duration=2, swipeCount=8]
```
### 向{上/下/左/右}查找 [] 的元素
**向{上/下/左/右}查找[选择器{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]的元素**
- 支持平台：Android、iOS、Web
- 语义：在全屏向指定方向滑动查找 指定选择器的元素
- swipeCount: 滑动查找最大滑动次数，超过这个值的滑动操作后还未在页面中找到指定元素则失败， 优先级：默认值 < flybirds_config.json中的“swipeSearchCount” < 语句中指定
- startX: 在全屏中滑动起始坐标的X轴的坐标值，<=1 代表百分比，>1代表像素点
- startY: 在全屏中滑动起始坐标的Y轴的坐标值，<=1 代表百分比，>1代表像素点
- duration: 每次滑动的时间， 优先级：默认值 < flybirds_config.json中的“searchSwipeDuration” < 语句中指定
- distance：滑动查找中每次滑动的距离， 优先级：默认值 < flybirds_config.json中的“swipeSearchDistance” < 语句中指定
```js
向下查找[text=机票]的元素
向下查找[testId, distance=0.5, duration=2, swipeCount=8]
```
### 元素 [] 位置 [] 秒内未变动
**元素[选择器{, path=false, multiSelector=false, timeout=10}]位置[time{, verifyCount=5}]秒内未变动**
- 支持平台：Android、iOS
- 语义： 指定选择器的元素在指定时间位置未发生变化，目的是判断页面未处于滑动状态
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- verifyCount: 最大判断次数，优先级：默认值 < flybirds_config.json中的“verifyPosNotChangeCount” < 语句中指定

### 开始录屏超时 []
**开始录屏超时[time]**
- 支持平台：Android、iOS
- 语义：开始录制屏幕，到超时时间未停止则停止录屏

### 开始录屏
**开始录屏**
- 支持平台：Android、iOS
- 语义： 开始录制屏幕，使用默认的超时时间（在配置文件中配置）

### 结束录屏
**结束录屏**
- 支持平台：Android、iOS、Web
- 语义：结束录制屏幕，并将视频文件关联到报告中

### 等待 [] 秒
**等待[time]秒**
- 支持平台：Android、iOS、Web
- 语义：执行暂停指定时间

### 全屏截图
**全屏截图***
- 支持平台：Android、iOS、Web
- 语义：截取当前屏幕快照并关联到报告中

### 跳转到 []
**跳转到[页面名称]**
- 支持平台：Android、Web
- 语义：通过schema跳转到指定页面，页面名称在config/schema_url.json 中以  "页面名称: 页面schemaUrl"  的形式维护
```js
跳转到[首页]
```
### 缓存服务请求 []
**缓存服务请求[operation[,operation ...]]**
- 支持平台：Web
- 语义：缓存该服务的最后一次请求报文到本地。 <br />注意： operation 是 url 最后一个\ 和 ？ 中间的字符串，即请求名
```js
//示例1：
缓存服务请求[getRecommendHotelList]
//示例2：
缓存服务请求[getRecommendHotelList,writecookie]
```

### 移除请求缓存 []
**移除请求缓存[operation[,operation ...]]**
- 支持平台：Web
- 语义：从本地清除该服务请求的缓存报文。<br />注意： operation 是 url 最后一个\ 和 ？ 中间的字符串，即请求名
```js
//示例1：
移除请求缓存[getRecommendHotelList]
//示例2：
移除请求缓存[getRecommendHotelList,writecookie]
```

### 移除所有请求缓存
**移除所有请求缓存**
- 支持平台：Web
- 语义：移除所有请求的缓存报文

### 监听服务 [] 绑定MockCase []
**监听服务[operation[,operation ...]]绑定MockCase[mockCaseId[,mockCaseId ...]]**
- 支持平台：Web
- 语义：监听相关operation的请求并拦截，用mockCaseId的返回报文进行替换。<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串
- **MockCase配置**：
  ​	服务监听`step`语句的`mock`数据支持通过2种方式来获取：**json文件配置** 和 **函数调用**。
  - **json文件配置**：如以下示例一。具体设置方式及格式可以参考**Demo**项目**mockCaseData** 目录下的json文件。
    此方式需要注意，对应`response` 的`mockCaseId` （json key，如示例一中的`4245512`）在整个`mockCaseData`目录下需要是唯一的，否则该mock数据会被其他具有相同 `key` 的数据覆盖掉。
  - **函数调用**：自定义处理与获取`MockData`。此种方式需要在 **Demo**项目的**pscript/custom_handle/operation.py** 文件中实现 `get_mock_case_body(mock_case_id)` 扩展方法。
  `MockCase` 绑定的报文优先以自定义扩展方法的返回结果为主。当自定义扩展方法返回结果为None时，框架会尝试查找项目**mockCaseData** 目录下的所有json文件，并返回json文件中`mock_case_id` 对应的 mock数据。
**Mock数据配置示例一：json文件配置**
```json
{
  "4245512": {
    "count": 101,
    "results": [
      {
        "id": 10,
        "name": "test-狮子王",
        "alias": "The Lion King",
        "cover": "https://p0.meituan.net/movie/27b76fe6cf3903f3d74963f70786001e1438406.jpg@464w_644h_1e_1c",
        "categories": [
          "动画",
          "歌舞",
          "冒险"
        ],
        "published_at": "1995-07-15",
        "minute": 89,
        "score": 9.0,
        "regions": [
          "美国"
        ]
      }
    ]
  }
}
```
**语法使用示例:**
```js
//示例1：
监听服务[movie]绑定MockCase[4245512]
//示例2：
监听服务[movie,testList]绑定MockCase[4245512,123456]
```

### 移除服务监听 []
**移除服务监听[operation[,operation ...]]**
- 支持平台：Web
- 语义：移除operation 的请求监听<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串
```js
//示例1：
移除服务监听[movie]
//示例2：
移除服务监听[movie,testList]
```

### 移除所有服务监听
**移除所有服务监听**
- 支持平台：Web
- 语义： 移除所有请求监听

### 验证服务请求 [] 与 [] 一致
**验证服务请求[operation]与[target_data_path]一致**
- 支持平台：Web
- 语义：比对相关operation的缓存报文与target_data_path对应的文件内容<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串
```js
验证服务请求[getRecommendHotelList]与[compareData/getRecommendHotelList.json]一致
```

### 验证服务非json请求 [] 与 [] 一致
**验证服务非json请求[operation]与[target_data_path]一致**
- 支持平台：Web
- 语义：比对相关operation的非json类型的缓存报文与target_data_path对应的文件内容<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串
```js
验证服务非json请求[writecookie]与[compareData/writecookie.txt]一致
```

### 验证服务 [] 的请求参数 [] 与 [] 一致
**验证服务[operation]的请求参数[target_json_path]与[expect_value]一致**
- 支持平台：Web
- 语义：检查相关operation的缓存报文体对应参数的值与给定的期望值是否一致<br />注意：operation 是url 最后一个\ 和 ？ 中间的字符串
```js
验证服务[getRecommendHotelList]的请求参数[head.syscode]与[PC]一致
```
- 🍖**配置忽略节点：**
​		服务报文比对支持设置**忽略节点**，包括**具体路径**和**正则表达式**。具体设置方式及格式可以参考**Demo**项目**interfaceIgnoreConfig** 目录下的json文件。
**示例：**
```json
{
  "getRecommendHotelList": [
    "head.cid",
    "regex: root\\['head'\\]\\['extension'\\]\\[\\d+\\]\\['value'\\]"
  ],
  "writecookie": [
    "token"
  ]
}
```
**说明**：
- `getRecommendHotelList`、`writecookie` 为 服务请求的请求名`operation` 
- `head.cid` 为服务`getRecommendHotelList` 请求体的具体节点路径。与文件进行报文比对时，该节点会被忽略。
- `regex: root\\['head'\\]\\['extension'\\]\\[\\d+\\]\\['value'\\]`  是一个正则表达式。 `getRecommendHotelList` 请求体中所有匹配该路径的节点在比对时都将被忽略。
     🧨  **注意：** 配置正则表达式时，请在字符串前用`regex:`进行标注申明。

## Android端例子

### 点击
```Gherkin
# language: zh-CN
功能: flybirds功能测试-android click

   场景: 验证点击--点击屏幕位置
     当   启动APP[ctrip.android.view]
     而且 点击屏幕位置[580,1200]
     而且 等待[5]秒
     那么 全屏截图
     那么 关闭App


   场景: 验证点击--点击元素
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     而且 点击[text=机票]
     那么 全屏截图


   场景: 验证点击--点击并输入
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=搜索]
     而且 在[text=搜索]中输入[flybirds]
     而且 等待[10]秒
     那么 全屏截图
```

### 查找元素
```Gherkin
# language: zh-CN
功能: flybirds功能测试-android find element

  场景: 验证元素操作--在页面中查找
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 在[android.widget.LinearLayout]中向下查找[text=机票]的元素


   场景: 验证元素操作--在全屏查找
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 向下查找[text=租车]的元素
```

### 录屏
```Gherkin
# language: zh-CN
功能:  flybirds功能测试-android device record

   场景: 验证设备录屏--录屏
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     而且 开始录屏
     而且 点击[text=机票]
     而且 等待[10]秒
     那么 结束录屏
     那么 关闭App


   场景:验证设备录屏--录屏超时
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     而且  开始录屏超时[50]
     而且  点击文案[机票]
     而且  等待[10]秒
     那么 结束录屏
     那么 关闭App
```

### 滑动
```Gherkin
# language: zh-CN
功能: flybirds功能测试-android swipe

   场景: 验证滑动--元素滑动
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=租车]
     而且 [text=租车]向上滑动[600]
     而且 等待[5]秒
     那么 元素[text=租车]位置[5]秒内未变动
     那么 存在元素[text=搜索]
     那么 存在[搜索]的文案


   场景: 验证滑动--全屏滑动
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=租车]
     而且 全屏向上滑动[600, readyTime=3, duration=2]
     那么 不存在[text=机票]的元素
     那么 不存在[升级攻略]的文案
     那么 元素[text=机票]消失
     那么 文案[机票]消失
```

### 验证元素
```Gherkin
# language: zh-CN
功能: flybirds功能测试-android verify element

   场景: 验证元素--元素文案
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 [text=机票]的文案为[机票]
     那么 [text=机票]的文案包含[机]


   场景: 验证元素--元素属性
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 元素[text=机票]的属性[text]为机票

```

## iOS端例子

### 点击
```Gherkin
# language: zh-CN
功能:  flybirds功能测试-ios click

   场景: 验证点击--点击屏幕位置
     当   启动APP[com.ctrip.inner.wireless]
     而且 点击屏幕位置[580,1200]
     而且 等待[5]秒
     那么 全屏截图
     那么 关闭App


   场景: 验证点击--点击元素
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     而且 点击[label=机票]
     那么 全屏截图


   场景: 验证点击--点击并输入
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=搜索]
     而且 在[label=搜索]中输入[flybirds]
     而且 等待[10]秒
     那么 全屏截图
```

### 查找元素
```Gherkin
# language: zh-CN
功能: flybirds功能测试-ios find element

   场景: 验证元素操作--在页面中查找
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 在[ScrollView]中向下查找[label=租车]的元素


   场景: 验证元素操作--在全屏查找
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 向下查找[label=租车]的元素
```

### 滑动
```Gherkin
# language: zh-CN
功能: flybirds功能测试-ios swipe

   场景: 验证滑动--元素滑动
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=租车]
     而且 [label=租车]向上滑动[600]
     而且 等待[5]秒
     那么 元素[label=租车]位置[5]秒内未变动
     那么 存在元素[label=租车]
     那么 存在[租车]的元素


   场景: 验证滑动--全屏滑动
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=租车]
     而且 全屏向上滑动[600, readyTime=3, duration=2]
     那么 不存在[label=机票]的元素
     那么 不存在[升级攻略]的文案
     那么 元素[label=机票]消失
     那么 文案[搜索]消失
```

### 验证
```Gherkin
  # language: zh-CN
 功能: flybirds功能测试-ios verify element

   场景: 验证元素--元素文案
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 [label=机票]的文案为[机票]
     那么 [label=机票]的文案包含[机]


   场景: 验证元素--元素属性
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 元素[label=机票]的属性[label]为机票

```

## Web端例子

### 点击
```Gherkin
# language: zh-CN
功能: web点击

    场景: 点击元素
    假如 跳转页面到[百度]
    而且 点击[#s-top-loginbtn]
    而且 等待[3]秒
    那么 全屏截图


    场景: 点击文案
    假如 跳转页面到[百度]
    而且 点击文案[新闻]
    而且 等待[3]秒
    那么 全屏截图


    场景: 点击屏幕位置
    假如 跳转页面到[百度]
    而且 点击屏幕位置[720,400]
    而且 等待[3]秒
    那么 全屏截图
```

### 查找元素
```Gherkin
# language: zh-CN
功能: web查找元素

    场景: 在全屏查找
    假如 跳转页面到[百度]
    而且 页面渲染完成出现元素[text=新闻]
    那么 向下查找[text=关于百度]的元素


    场景: 在父元素中查找子元素
    假如 跳转页面到[百度]
    那么 存在[#hotsearch-content-wrapper]的[li.hotsearch-item.odd[data-index="2"]]的元素
    那么 [.s-bottom-layer-content]的[text=帮助中心]文案为[帮助中心]
```

### 输入
```Gherkin
# language: zh-CN
功能: 输入操作

    场景: 输入
    假如 跳转页面到[百度]
    而且 在[#kw]中输入[flybirds]
    而且 等待[3]秒
    那么 全屏截图


    场景: 清空并输入
    假如 跳转页面到[百度]
    而且 在[#kw]中输入[flybirds]
    而且 等待[3]秒
    那么 在[#kw]中清空并输入[input test]
    那么 全屏截图

```

### 页面操作
```Gherkin
# language: zh-CN
功能: 页面操作

    场景: 返回上一页
    假如 跳转页面到[列表页]
    而且 页面渲染完成出现元素[text=霸王别姬 - Farewell My Concubine]
    而且 点击[text=霸王别姬 - Farewell My Concubine]
    而且 等待[3]秒
    而且 返回上一页
    而且 等待[2]秒
    那么 结束录屏


    场景: 判断当前页面
    假如 跳转页面到[列表页]
    而且 页面渲染完成出现元素[text=霸王别姬 - Farewell My Concubine]
    而且 点击[text=霸王别姬 - Farewell My Concubine]
    而且 等待[3]秒
    那么 当前页面是[列表详情页]
```

### 录屏
```Gherkin
# language: zh-CN
功能:  web录屏

    场景:录屏
    假如 跳转页面到[百度]
    而且 页面渲染完成出现元素[text=新闻]
    而且 点击[#s-top-loginbtn]
    而且 等待[10]秒
    那么 结束录屏

```

### 下拉框选择
```Gherkin
# language: zh-CN
功能: 下拉框

    场景: 下拉框选择
    假如 跳转页面到[携程]
    而且 在[#J_roomCountList]中选择[6间]
    而且 等待[5]秒
    那么 结束录屏
```

### 滑动
```Gherkin
# language: zh-CN
功能: web滑动

    场景: 滑动
    假如 跳转页面到[列表页]
    而且 等待[2]秒
    而且 [text=霸王别姬 - Farewell My Concubine]向下滑动[600]
    而且 等待[5]秒
    那么 存在元素[text=肖申克的救赎 - The Shawshank Redemption]
    那么 存在[肖申克的救赎 - The Shawshank Redemption]的文案


    场景:全屏滑动
    假如 跳转页面到[列表页]
    而且 等待[2]秒
    而且 全屏向下滑动[600]
    而且 等待[5]秒
    那么 不存在[text=测试]的元素
    那么 不存在[测试]的文案
```

### 验证
```Gherkin
# language: zh-CN
功能: web元素属性验证

    场景: 验证元素文案
    假如 跳转页面到[百度]
    那么 [text=新闻]的文案为[新闻]
    那么 [text=新闻]的文案包含[新]


    场景: 验证元素属性
    假如 跳转页面到[百度]
    那么 元素[#kw]的属性[name]为wd
    那么 元素[#su]的属性[value]为百度一下

```

### 缓存服务请求
```Gherkin
# language: zh-CN
功能: 缓存服务请求

    场景:验证缓存服务请求
    假如 缓存服务请求[getRecommendHotelList]
    假如 缓存服务请求[writecookie]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 移除请求缓存[getRecommendHotelList]
    而且 移除所有请求缓存


    场景:验证缓存服务请求--同时传入多个参数
    假如 缓存服务请求[getRecommendHotelList,writecookie]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 移除请求缓存[getRecommendHotelList,writecookie]
```

### 验证服务请求
```Gherkin
# language: zh-CN
功能: 验证比较服务请求

    场景: json类型服务请求比对
    假如 缓存服务请求[getRecommendHotelList]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 验证服务[getRecommendHotelList]的请求参数[head.syscode]与[PC]一致
    而且 验证服务[getRecommendHotelList]的请求参数[$.cityId]与[2]一致
    而且 验证服务[getRecommendHotelList]的请求参数[cityId]与[2]一致
    而且 验证服务请求[getRecommendHotelList]与[compareData/getRecommendHotelList.json]一致


    场景: 非json类型服务请求比对
    假如 缓存服务请求[writecookie]
    而且 跳转到[携程官网]
    那么 等待[5]秒
    而且 验证服务非json请求[writecookie]与[compareData/writecookie.txt]一致

```

### 服务监听Mock
```Gherkin
# language: zh-CN
功能: 监听并mock服务请求

    场景: 服务监听与mock
    假如 监听服务[movie]绑定MockCase[4245512]
    当   跳转页面到[列表页]
    那么 等待[10]秒
    而且 移除服务监听[movie]
    而且 移除所有服务监听

```

## 多端应用例子

### 测试用例
```Gherkin
功能: 乘机人模块

@p1 @android @web
场景:外露乘机人_选择列表页乘机人
   当   跳转页面到[单程填写页]
   那么 页面渲染完成出现元素[已选乘机人姓名]
   那么 [选择乘机人文案]的文案为[选择乘机人]
   那么 [已选乘机人姓名]的文案为[李易峰]
   那么 [已选乘机人证件类型]的文案为[护照]
   那么 [已选乘机人证件号]的文案为[YHE77]
   那么 存在[乘客类型标签儿童]的元素
   那么 返回上一页

```

### 页面对象管理
多端项目中的页面对象管理，是通过json文件进行统一管理，通常存在以下两种情况
1. 各端相同时，参考以下配置
```
// 元素定位配置 ele_locator.json
{
  "选择乘机人文案": “testid=passger_check”,
  "已选乘机人姓名": “testid=passger_name_checked”,
  "已选乘机人证件类型": “testid=passger_ct_checked”,
  "已选乘机人证件号": “testid=passger_cn_checked”
}
```

2. 各端不同时，通过android、ios、web区分
```
// scheme配置 schema_url.json  
{
  "单程填写页": {
    "android": "urlschemel://auth_activity",
    "ios": "urlschemel://ios_auth_activity",
    "web": "https://address"
  }
}

// 元素定位配置 ele_locator.json
{
  "乘客类型标签儿童": {
    "android": "textid=passger_type_child",
    "ios": "lableid=passger_type_child",
    "web": "xpath=//html/body/div"
  }
}

```

## 数据驱动参数化
实际项目中，大部分的自动化测试都是基于数据驱动参数化，因此还需要搭配「 场景大纲+例子」一起使用，这里我们对上面的例子进行改造：

```Gherkin
功能: 乘机人模块

@p1 @android @web
场景大纲:  外露乘机人_选择列表页乘机人
     当   跳转页面到[单程填写页]
     那么 页面渲染完成出现元素[已选乘机人姓名]
     那么 <element>的文案为<title>
     那么 存在[乘客类型标签儿童]的元素
     那么 返回上一页

     例子:
        |   element          |   title      |
        |   选择乘机人文案     |   选择乘机人   |
        |   已选乘机人姓名     |   李易峰      |
        |   已选乘机人证件类型  |   护照       |
        |   已选乘机人证件号    |   YHE77     |

```


## 多浏览器并发
依托PlayWright的跨浏览器能力，Flybirds支持所有的现代渲染引擎，包括 Chromium、WebKit 和 Firefox。
![image](https://flybirds.readthedocs.io/zh_CN/latest/_images/browsers.png)

Flybirds支持多浏览器并发模式，方便高效的进行浏览器兼容性测试
### 配置参数
```
// browserType: 配置浏览器内核
  "web_info": {
    "headless": true,
    "browserType": ["firefox","chromium","webkit"],  
    "defaultTimeout": 30
  },
```

### 执行命令
```bash
# 通过参数指定web执行平台启动的浏览器(多个浏览器时用半角逗号进行分隔)
flybirds run -D browserType=webkit,firefox
```


## 自定义框架扩展

Flybirds的插件式设计模式，保留了良好的扩展，未来我们会开放更多。  

**修改扩展**

如果你希望在项目中修改当前扩展，你可以用本地文件替换plugin下面的（app,device,element,app,step,screen,screen_record），并在 "plugin_info.json" 中做相应配置。

比如你希望修改web中screen.py文件:

    1. 在本地创建一个py文件命名为 screen.py
    2. 在plugin_info.json 的web中添加如下配置:
  ```json
    "screen"： {
    "path": "{local_path}/screen.py",
    "ns": "screen.plugin.myextend"
    }
  ```
  >  {local_path} 为本地路径，"ns"为包名,注意包名的唯一性(以上包名只是例子不做强制限制)

**内部增强包**

对于团队内部通用的自定义功能，可以考虑创建一个extend package，Flybirds支持动态加载，package命名包含“-flybirds-plugin”即可。 携程机票内部，针对DevOps的各类工具，增强包中都进行了对接，安装后就可以使用。


## 其他语种支持

flybirds可以支持40几种语言，在以下文件中增加公共方法的语言配置即可。
```
flybirds/core/dsl/globalization/i18n.py
```

示例代码如下
![lang](https://flybirds.readthedocs.io/zh_CN/latest/_images/lang_extend.png)

## 持续集成
cli提供的命令行执行模式，可以非常方便加入各种持续集成工具.

以Jenkins为例：
```bash
# Inside the jenkins shell command
cd {PATH_TO_PROJECT_FOLDER}
# Run
flybirds run -P ./features/test/everything.feature
cp -R reports $WORKSPACE
```

## 发版计划
我们将按照 SemVer 版本控制规范进行发版。逐步新增功能和代码优化，非常欢迎您加入到我们的共建计划中，在 GitHub 上提出您的宝贵建议，以及在使用时遇到的一切问题，我们也会对此每周进行一次小版本的迭代。您也可以在这里给我们精神支持，点上一颗 Star。

## 参考链接
* GitHub地址：https://github.com/ctripcorp/flybirds
* PyPI地址：https://pypi.org/project/flybirds
* Pages：https://ctripcorp.github.io/flybirds/
* PlayWright: https://github.com/microsoft/playwright-python
* Airtest: https://github.com/AirtestProject/Airtest
* Behave: https://github.com/behave/behave
* 欢迎在 GitHub [issues](https://github.com/ctripcorp/flybirds/issues) 和[Discussions](https://github.com/ctripcorp/flybirds/discussions)区提问
* 支持邮箱：flybirds_support@trip.com

