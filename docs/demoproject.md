# Project structure

## Quickly start
- config：configuration file
- features：test case feature file
- pscript：customized extension script
- report：test report

## Config
Must config items：`deviceId`, `packageName`.When connecting to IOS devices, you must configure the `webDriverAgent` 、`platform`.

**flybirds_config.json**

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

  The system to be connected to the test device, currently supports `Android` and `IOS`, if not filled in, the default is: `Android`
  
- `webDriverAgent` 

  The BundleID of the WebDriverAgent in the device. Can be viewed through the `tidevice applist` command. Required when connecting to IOS device.
  
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

**schema_url.json**

page schema access address

- "front page": "ctrip://homepage"   

  above example is the Trip APP homepage


## Pscripts

Store custom scripts in python language (including custom step statements, docking with other platforms such as mocks, custom schema jump logic, login and logout, extension of various hook functions when behave is running, parameter processing methods, etc.)

app/operation.py : Define some app-specific behaviors, such as the splicing of the schema jump protocol, login, logout, and jump to the homepage

- dsl.step：Custom dsl statements, if you create a new .py file to write custom statements, you need to import the .py file in feature/steps/steps.py

- dsl.hook：The extension of each hook function in the execution process, so that users can exert their own influence on the execution process

- other_platform：Stores some code that interacts with other platforms, which can be added or deleted

- params_deal：Store some custom processing methods

