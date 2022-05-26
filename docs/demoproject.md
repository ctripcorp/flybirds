# Project structure

## Quickly start
- config：configuration file
- features：test case feature file
- pscript：customized extension script
- report：test report

## Config
When testing on **mobile**, you must configure the items: `deviceId`、`packageName`. When testing on IOS devices, you must additionally configure `webDriverAgent`.

#### **flybirds_config.json**

- `packageName` 

  The packageName of the app, the example is the packageName of ctrip, this configuration must be filled in, default: "ctrip.android.view"

- `packagePath`

  the app address for download and install, it will be automatically downloaded from this address and installed on the test device when the project is running，it will not download when it is empty

- `overwriteInstallation`

  Whether to overwrite and install the test package before each run, default: "True"
  
- `uniqueTag` 

  The unique identifier of the app, such as the value of clientId, default: "000"
  
- `defaultUser` 

  This user name will be used when global login is required before running, default: "null"
  
- `defaultPassword`
  
  This password will be used when global login is required before running, default: "null"

- `deviceId` 

  The example is the serial number of the device. Use "adb devices" to get, default: "10.5.170.85:5555"

- `platform` 

   Project case execution platform. currently supports `android`, `ios` and `web`, default is: `android` when not filled
  
- `webDriverAgent` 

  The BundleID of the WebDriverAgent in the device. Can be viewed through the `tidevice applist` command. Required when connecting to IOS device.

- `headless` 

	The running mode of the browser, `true` means the browser will run in **headless** mode. Required for `platform=web`. Default is: `true`.

- `browserType` 

  Supported browser types: `chromium`, `firefox` and `webkit`. Required for `platform=web`. Multiple values are supported to be configured at the same time. For example: `browserType`: ["firefox", "chromium", "webkit"].  Default is: "browserType": ["chromium"].

- `requestInterception` 

  Enable request blocking。Required for `platform=web`。Default is: `true`.

- `ignoreOrder` 

​		List difference ignoring order or duplicates.  Default is：`false`。Valid only when  `requestInterception=true`.

- `abortDomainList` 

​		List of domains that abort routes when requests are blocked. For example："abortDomainList": ["google.com"]. Valid only when  `requestInterception=true`.

- `beforeRunPage` 

  Configure the behavior of the app before starting the test. By default, "restart the app" to ensure that the page is on the main homepage during the test, and startApp (start the app), stopApp (close the app), and None (no operation), default: "restartApp"

- `scenarioFailPage` 

  The configuration behavior of the app after the execution of the test case fails. the default is to "restart the app" to ensure that there will not be too many historical pages in the current memory, as well as backupPage (return to the previous page), stopApp (stop the app), None (nothing) operate), default: "restartApp"

- `scenarioSuccessPage`

  The configuration behavior of the app after the test case is executed successfully, the default is "None" without any operation, there are restartApp (restart app), backupPage (return to the previous page), stopApp (stop app), default: "None"

- `beforeRunLogin` 

  if need to log in before starting the test, default: "false"

- `failScreenRecord`  

  associate the execution screen recording file of the use case to the test report after the failure, default: "true"

- `scenarioScreenRecordTime`

  the maximum duration of the recording screen, default: 120

- `failRerun`

  Whether to rerun after failure, default: "true"

- `maxFailRerunCount`

  Number of failures satisfied by failed reruns, default: 1

- `maxRetryCount`

  Number of failed retries, default: 2

- `waitEleTimeout`

  Timeout for finding elements in the page, default: 15

- `waitEleDisappear`

  The timeout period for the disappearance of the specified element on the page, default: 10

- `clickVerifyTimeout`

  The timeout for the click operation to judge the completion of the rendering, default: 15

- `useSwipeDuration`

  Use the globally configured sliding time, default: "false"

- `swipeDuration`

  When useSwipeDuration is true, the time of the sliding operation is this value, default: "false"

- `usePocoInput`

  whether to use poco's input method, airtest is used by default, default: "false"

- `afterInputWait`

  Waiting time after entering the input box, default: 1

- `useSearchSwipeDuration`

  Whether to use the global sliding time in the sliding search, default: "false"

- `searchSwipeDuration`

  useSearchSwipeDuration is true, all sliding time in the sliding search is set globally by this value, default: 1

- `swipeSearchCount`

  The maximum number of swipes to find an element, default: 5

- `swipeSearchDistance`

  The distance of each swipe in the swipe search, default: 0.3

- `pageRenderTimeout` 

  The time to wait for the page rendering to complete, the global configuration time of the timeout parameter in the sentence "The page rendering is complete and the element [selector{, path=false, multiSelector=false, timeout=10}]" appears, default: 35

- `appStartTime`

  The timeout after APP start, default: 6

- `swipeReadyTime` 

  Waiting time before sliding starts, default: 3

- `verifyPosNotChangeCount` 

  The maximum number of judgments for judging that the position of the element has not changed, default: 5

- `screenRecordTime`
  screen record maxmun time, default: 60

- `useSnap`

   Whether to use snapshots to find text, default: true

- `useAirtestRecord`

   Use airtest record, default: "true"

   

#### **schema_url.json**

For unified configuration of `schema` access addresses for multi-platform pages.

**Examples：**

- The `schema` access address is the same for multi-platform pages：

  "front page": "ctrip://homepage"   

  above example is the Trip APP homepage

- Different `schema` access addresses for multi-platform pages:

  The following example is the list page  of Trip for android, ios and web

  ```json
  "listPage": {
    "android": "/rn_test/ctrip_list_android/",
    "ios": "/rn_test/ctrip_list_ios/",
    "web": "https://ctrip.test/list"
  }
  
  ```



#### **ele_locator.json**

For unified configuration of how to position elements on multiple platforms.

**Examples：**

- Elements on multiple platforms are positioned in the same way：

  "element1": "text=Help Center"

  The above example shows how to position [element 1].

- Different ways of positioning elements for multiple platforms:

  The following example shows how [element 2] is positioned on android, ios and web

  ```json
  "element2":{
    "android": "text=ticket",
    "ios": "label=ticket",
    "web": "#ticket"
  }
  ```




## Pscripts

Store custom scripts in python language (including custom step statements, docking with other platforms such as mocks, custom schema jump logic, login and logout, extension of various hook functions when behave is running, parameter processing methods, etc.)

- **custom_handle/operation.py** : Define some app、web specific behaviors, such as the splicing of the schema jump protocol, login, logout, and jump to the homepage in app, and  creates a new  BrowserContext, get Mock data in web.

  Example : Web-side custom creates BrowserContext

  ```python
  def create_browser_context(browser):
      """
      custom creates a new browser context.
      :param browser: the browser instance
      """
      # For example, adding a 'local' parameter when create.
      context = browser.new_context(record_video_dir="videos",
                                    ignore_https_errors=True,
                                     locale="en")
      return context
  ```

  

- **dsl.step**：Custom dsl statements, if you create a new .py file to write custom statements, you need to import the .py file in feature/steps/steps.py
- **dsl.hook**：The extension of each hook function in the execution process, so that users can exert their own influence on the execution process
- **params_deal**：Store some custom processing methods

