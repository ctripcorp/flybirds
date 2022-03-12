Flybirds
--

![architecture](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/architecture.png)

Flybirds ([仓库](https://github.com/ctripcorp/flybirds)) 是一套基于BDD模式的前端UI自动化测试框架，提供了一系列开箱即用的工具和完善的文档。

使用Flybirds你能够完成大部分的手机端自动化操作

* 基于BDD模式，类自然语言语法
* 支持自动化APP操作、表单提交、UI元素校验、键盘输入、Deeplink跳转等
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
![clicreate](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/clicreate.png)

## 快速上手

### 运行演示

为了帮助使用，项目创建时，会生成中英文的Android、iOS演示feature，方便用户参考。

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

接下来，了解下更多项目细节

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
![featureCN](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/feature_zhCN.png)

以下是英文feature例子
![feature_en](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/feature_en.png)


### step操作步骤
上面例子中的关键字“当”、“而且”和“那么”部分构成了测试用例的操作步骤，这些操作步骤框架中已经通过python实现。

#### 设备操作
**连接设备[{param}]**
- 支持平台：Android
- 语义：连接测试设备
```js
连接设备[10.21.37.123:5555]
```

#### APP操作
**安装APP[{param}]**
- 支持平台：Android
- 语义：安装APP
```js
安装APP[/Users/xxx/xxx.apk]
```

**删除APP[{param}]**
- 支持平台：Android
- 语义：删除APP
```js
删除APP[package name]
```

**启动APP[{param}]**
- 支持平台：Android、iOS
- 语义：启动APP
```js
启动APP[package name]
```

#### 元素相关
**存在[字符串{, fuzzyMatch=false, timeout=10}]的文案**
- 支持平台：Android、iOS
- 语义：页面中存在指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js 
存在[机票]的文案

存在[机票, timeout=10]的文案

存在[.?票, fuzzyMatch=true]的文案
```

**不存在[字符串{, fuzzyMatch=false}]的文案**
- 支持平台：Android、iOS
- 语义：页面中不存在指定的文案
```js 
不存在[机票]的文案

不存在[.?票, fuzzyMatch=true]的文案
```

**文案[字符串{, fuzzyMatch=false, timeout=10}]消失**
- 支持平台：Android、iOS
- 语义：指定的字符串在规定时间内从页面消失
timeout 等待消失的超时时间 ，优先级：默认值 < flybirds_config.json中的“waitEleDisappear” < 语句中指定
```js 
文案[机票]消失

文案[.?票, fuzzyMatch=true, timeout=20]消失
```

**存在[选择器{, path=false, multiSelector=false, timeout=10}]的元素**
- 支持平台：Android、iOS
- 语义：页面中存在指定 选择器 的元素
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js 
存在[text=经济舱]的元素

存在[textMatches=.?经济舱]的元素

存在[textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true, timeout=30]的元素

```

**不存在[选择器{, path=false, multiSelector=false}]的元素**
- 支持平台：Android、iOS
- 语义：页面中不存在指定  选择器 的元素
```js
不存在[text=经济舱]的元素

不存在textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true]的元素

```

**元素[选择器{, path=false, multiSelector=false, timeout=10}]消失**
- 支持平台：Android、iOS
- 语义：指定的 选择器 在规定时间内从页面消失
- timeout 等待消失的超时时间 ，优先级：默认值 < flybirds_config.json中的“waitEleDisappear” < 语句中指定
```js
元素[center_content_layout]消失

元素[text=机票]消失

元素[机票→第1个兄弟节点, path=true, timeout=15]消失
```

**[选择器{, path=false, multiSelector=false, timeout=10}]的文案为[字符串{, dealMethod=name}]**
- 支持平台：Android、iOS
- 语义：指定 选择器 的元素的文案为指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
[text=机票]的文案为[机票]

[textMatches=.?经济舱, timeout=15]的文案为[经济舱, dealMethod=trim_prefix]

[textMatches=.?经济舱并且visible=True, multiSelector=true, timeout=15]的文案为[经济舱, dealMethod=trim_prefix]
```

**[选择器{, path=false, multiSelector=false, timeout=10}]的文案包含[字符串{, dealMethod=name}]**
- 支持平台：Android、iOS
- 语义：指定 选择器 的元素的文案包含指定的字符串
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
[text=机票]的文案包含[票]

[textMatches=.?经济舱, timeout=15]的文案包含[经济舱]

[textMatches=.?经济舱并且visible=True, multiSelector=true, timeout=15]的文案包含[经济, dealMethod=trim_prefix]
```

**点击文案[字符串{, fuzzyMatch=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- 支持平台：Android、iOS
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

**点击[选择器{, path=false, multiSelector=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- 支持平台：Android、iOS
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

**文案[字符串{, fuzzyMatch=false, timeout=10}]的属性[属性名{, dealMethod=name}]为{属性值}**
- 支持平台：Android、iOS
- 语义：页面中指定 字符串对应的元素的指定的属性的值为指定的值
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
文案[机票]的属性[text]为机票

文案[机票, timeout=15]的属性[text, dealMethod=trim_last]为机
```

**元素[选择器{, path=false, multiSelector=false, timeout=10}]的属性[属性名{, dealMethod=name}]为{属性值}**
- 支持平台：Android、iOS
- 语义：页面中指定 选择器 的元素的指定的 属性的值为指定的 值
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
```js
元素[text=机票]的属性[text]为机票

元素[text=机票, timeout=15]的属性[text, dealMethod=trim_last]为机
```

**在[选择器{, path=false, multiSelector=false, timeout=10}]中输入[文案{, pocoInput=false, afterInputWait=1}]**
- 支持平台：Android、iOS
- 语义：在指定选择器的元素中输入指定的文案 
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- pocoInput: 是否使用 poco 的输入方法，默认使用的是airtest的输入方法， 优先级：默认值 < flybirds_config.json中的“usePocoInput” < 语句中指定
- afterInputWait: 输入完成的休眠时间， 优先级：默认值 < flybirds_config.json中的“afterInputWait” < 语句中指定
```js
在[inputEleId]中输入[上海]

在[type=InputView]中输入[用户名, pocoInput=true, afterInputWait=5]
```

**[选择器{, path=false, multiSelector=false, timeout=10}]向{上/下/左/右}滑动[滑动距离{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- 支持平台：Android、iOS
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

**在[选择器{, path=false, multiSelector=false, timeout=10}]中向{上/下/左/右}查找[选择器{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]的元素**
- 支持平台：Android、iOS
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

**向{上/下/左/右}查找[选择器{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]的元素**
- 支持平台：Android、iOS
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

#### 页面屏幕相关
**跳转到[页面名称]**
- 支持平台：Android
- 语义：通过schema跳转到指定页面，页面名称在config/schema_url.json 中以  "页面名称: 页面schemaUrl"  的形式维护
- 由于不同APP内部定义的schema规则可能不同，可能需要对项目`pscript/app/operation.py` 文件中的`schema_deal_rule()`方法进行自定义，参考[issue](https://github.com/ctripcorp/flybirds/issues/8)
```js
跳转到[首页]
```

**页面渲染完成出现元素[选择器{, path=false, multiSelector=false, timeout=10}]**
- 支持平台：Android、iOS
- 语义：进入新的页面时通过指定 选择器 的元素出现在页面上来判断页面渲染完成
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“pageRenderTimeout” < 语句中指定
```js
页面渲染完成出现元素[text=机票]

页面渲染完成出现元素[center_content_layout, timeout=15]

页面渲染完成出现元素[center_content_layout, timeout=40]
```

**全屏向{上/下/左/右}滑动[滑动距离{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- 支持平台：Android、iOS
- 语义：以全屏为容器向指定 方向 滑动指定 距离
- startX: 在全屏中滑动起始坐标的X轴的坐标值，<=1 代表百分比，>1代表像素点
- startY: 在全屏中滑动起始坐标的Y轴的坐标值，<=1 代表百分比，>1代表像素点
- duration: 每次滑动的时间， 优先级：默认值 < flybirds_config.json中的“swipeDuration” < 语句中指定
- readyTime: 滑动开始前的等待时间， 优先级：默认值 < flybirds_config.json中的“swipeReadyTime” < 语句中指定
```js
向上滑动[0.05]
向下滑动[0.4, readyTime=3, duration=2]
```

**点击屏幕位置[{x},{y}]**
```js
点击屏幕位置[200,100]
```

#### 录屏&截图
> 对执行失败的用例，框架会自动录屏&截图，保存在测试报告中

**开始录屏超时[time]**
- 支持平台：Android
- 语义：开始录制屏幕，到超时时间未停止则停止录屏
```js
开始录屏超时[300]
```

**开始录屏**
- 支持平台：Android
- 语义： 开始录制屏幕，使用默认的超时时间（在配置文件中配置）
```js
开始录屏
```

**结束录屏**
- 支持平台：Android
- 语义：结束录制屏幕，并将视频文件关联到报告中
```js
结束录屏
```

**全屏截图**
- 支持平台：Android、iOS
- 语义：截取当前屏幕快照并关联到报告中
```js
全屏截图
```

#### 其它
**等待[time]秒**
- 支持平台：Android、iOS
- 语义：执行暂停指定时间
```js
等待[2]秒
```

**登录账号[{param1}]密码[{param2}]**
- 语义：指定用户名、密码登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 login(user_name, password)方法
```js
登录账号[admin]密码[123456]
```

**退出登录**
- 语义:退出当前登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 logout() 方法
```js
退出登录
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
![tag](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/tag.png)

运行有特定tag的场景，多个用逗号隔开
```
flybirds run -T tag1,tag2
```

‘-’开头表示运行不包含某tag的场景
```
flybirds run -T -tag
```

## 运行前检查

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

## 运行参数

在终端输入以下内容来查看**flybirds**运行项目时支持的操作
```bash
flybirds run --help
```
- **run**

  执行features目录下所有的feature文件


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

## 配置参数
**提供了丰富的配置项 ｜ [帮助文档](https://github.com/ctripcorp/flybirds/blob/main/docs/demoproject_zhCN.md)**

必须配置项：deviceId packageName。

连接IOS设备时，需要额外配置webDriverAgent、platform。

![image](https://user-images.githubusercontent.com/19287139/155323963-cfa0c600-65c2-4314-97a7-b2d5aa482e3e.png)

## 报告(report)
> 报告包含汇总Summary和功能(feature)、场景(senario)的执行结果，对于失败的场景(senario)，报告中会展示当时的屏幕图像和视频, 下面是一个例子。
![report](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/report.png)


## 自定义step语句模板

在编写Feature的过程中，可能会遇到提供的公共语句不能满足自身项目的需求，需要自定义语句。比如：需要对接某个内部工具API，此时需要用到自定义语句功能。

自定义语句功能会用到python，如果你不了解这门编程语言，也不必要太担心，因为只会使用到最基础的python语法，这并不会太难。

**使用方法**
1. 进入项目目录"psscript/dsl/steps"
2. 新建.py文件来编写自定义语句
3. 在feature/steps/steps.py中import该.py文件

示例代码如下
![dsl_extend](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/dsl_extend.png)

对于团队内部通用的自定义功能，可以考虑创建一个extend package，flybirds支持动态加载，package命名包含“-flybirds-plugin”即可。


## 自定义框架扩展

理论上BDD-UI-Testing 可以适用在所有端，比如：APP、Web、小程序。

框架的插件式设计模式，保留了良好的扩展，当前版本只开放了APP端支持，未来会逐步开放更多，下面是两个例子供大家参考。  

**增加web端扩展**
1. 在`plugins.default`下添加自己的web包 
2. 添加web对应的实现。比如`page.py,element.py`，如果需要增加其他的插件实现类，只需要在`GlobalContext`类中添加对应的名称。
3. 在`plugin.event`下添加自己的web包。
4. 在`event.web`包下重写或者新增类，比如重写`run`事件可以在`plugin.event.web`下面添加"run.py"，具体实现逻辑可参照已有的`run.py`。
5. 在项目配置文件"flybirdes_config.json"配置 `device_info.platform`值为"web"。

**修改当前APP端扩展**
- 可通过配置"plugin_info.json"对已有的plugins进行修改(只支持修改不支持新增)，比如你希望对plugins下面`ios.app`进行修改：
  1. 可以在本地创建一个自己 app.py
  2. 在plugin_info.json对应平台中添加如下配置:
  ```json
     "app": {
        "path": "{local_path}/app.py",
        "ns": "app.plugin"
      }
  ```
  >  {local_path} 为本地路径，"ns"为包名,注意包名的唯一性


## 其他语种支持

flybirds可以支持40几种语言，在以下文件中增加公共方法的语言配置即可。
```
flybirds/core/dsl/globalization/i18n.py
```

示例代码如下
![lang](https://raw.githubusercontent.com/wiki/ctripcorp/flybirds/images/lang_extend.png)

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

* GitHub地址：https://github.com/ctripcorp/flybirds
* PyPI地址：https://pypi.org/project/flybirds
* 贡献
  1. Fork 仓库
  2. 创建分支 (`git checkout -b my-new-feature`)
  3. 提交修改 (`git commit -am 'Add some feature'`)
  4. 推送 (`git push origin my-new-feature`)
  5. 创建 PR
* 欢迎在 GitHub [issues](https://github.com/ctripcorp/flybirds/issues) 区提问

* 支持邮箱：flybirds_support@trip.com
