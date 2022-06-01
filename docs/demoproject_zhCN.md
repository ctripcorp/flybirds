# 项目目录结构

## 快速上手

- config：配置文件
- features：测试用例feature文件
- pscript：自定义的扩展脚本
- report：测试报告

## config目录

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




## pscripts目录

存放python语言自定义的脚本（包括自定义step语句，对接如mock等其他平台，自定义schema跳转逻辑，登陆登出，behave运行时各种钩子函数的扩展，参数处理方法等等）

- **custom_handle/operation.py** ：定义一些app、web特有的行为。比如，app的 schema跳转协议的拼接，登陆，登出，跳转到首页； web的创建自定义BrowserContext，获取MockData等。

  示例一：web端自定义BrowserContext

  ```python
  def create_browser_context(browser):
      """
      custom creates a new browser context.
      :param browser: the browser instance
      """
      # For example, adding parameter when create, locale: language, viewport: screen size
      context = browser.new_context(record_video_dir="videos",
                                    ignore_https_errors=True,
                                    locale="en",
                                    viewport={"width": 800, "height": 800})
      return context
  
  ```

- **dsl.step**：自定义dsl语句，如果新建.py文件来编写自定义语句，需要在feature/steps/steps.py中import 该 .py文件
- **dsl.hook**：执行过程中各个钩子函数的扩展
- **params_deal**：存放自定义的一些处理方法

