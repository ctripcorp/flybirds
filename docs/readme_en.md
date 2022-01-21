<p align="center">
  <img width="350" src="logo.png" alt="logo" />
</p>

# Flybirds | [中文版](https://github.com/ctripcorp/flybirds/blob/main/README.md)

> Make UI automation in natural language.

## Preview

![](feature_en.png)

## Quickly start

Flybirds is a front-end UI automation test framework based on BDD mode, providing a series of out-of-the-box tools and complete documentation.
- Based on Behave, supporting BDD tools are required to associate Natural Language Test Case Documentation with Automated Test Code in BDD.
- Based on Airtest, UI automated test framework is needed to implement "test cases can be executed on automated test platform" in BDD.


### What can I do?

With Flybirds you can do most of the mobile automation, here are some features to help you get started:
- Based on BDD pattern, similar natural language syntax
- Support automatic app operation, form submission, UI element verification, keyboard input, deeplink jump, etc. on the Android side. The IOS side is in progress
- English and Chinese are supported by default. Support more languages ​​extensions
- Plug in design, support user-defined automation framework extension
- Provide cli scaffolding construction to help build projects quickly
- Provide html report


## Requirements

- python(3.7-3.9)
- nodejs(12+)


### 1. Install

#### use `pip` to install flybirds，required pip install [dependency package](https://github.com/ctripcorp/flybirds/blob/main/docs/relate.md) will be automatically installed

```bash
pip install flybirds
```

On MacOS/Linux platform, you need to grant adb execute permission.

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

#### use cli to create project

```bash
flybirds create 
```

You will be prompted to input the following information during project creation
- project name
- test platform：Android / iOS
- test device name（ can be skipped. you can config the node `deviceId` before running ）
- APP package name（ can be skipped，ctrip demo package is default，you can config the node `packageName` before running ）
- webDriverAgent BundleID（ can be skipped. only ios test needed, you can config the node `webDriverAgent` before running ）

To help you use, demo features will be generated in the test directory when the project is created, and can be deleted later


### 2. Run

1. Please ensure that the test device used can be connected normally， then execute the following command
    - Android: run `adb devices` , check if test device is in the list
    - iOS：use tidevice，run `tidevice list`，check if test device is in the list

   [Android device connect Q&A](https://airtest.doc.io.netease.com/IDEdocs/device_connection/2_android_faq/)
   - Please install the official driver of the phone's corresponding brand first to ensure that you can use the computer to perform USB debugging on the phone
   - Make sure that the "Developer Options" in the phone is turned on, and turn on "Allow USB Debugging" in the "Developer Options"
   - Some phones need to turn on "Allow Simulated Location" and "Allow App Installation via USB"
   - Turning off the mobile assistant software installed on the computer can avoid most of the problems. Please be sure to manually end the mobile assistant process in the task manager

   [iOS device connect Q&A](https://airtest.doc.io.netease.com/IDEdocs/device_connection/4_ios_connection/)
   - Please prepare a macOS first. After successfully deploying iOS-Tagent using xcode, you can connect to the iOS phone on the mac or windows machine. Please click [link](https://github.com/AirtestProject/IOS-Tagent)download the project code to local deployment。
   - mac: install iproxy by Homebrew `brew install libimobiledevice`
   - windows: install [itunes](https://support.apple.com/downloads/itunes)

2. Download and install test package
    - Android：project will automatically download and install the test package through `packagepath` in config(Please make sure that the phone is turned on "Allow installation from unknown sources"). It can also be downloaded and installed manually.[Download](https://download2.ctrip.com/html5/Ctrip_V8.43.0_SIT4-100053_Product_9725895.apk)
    - iOS：
      1. download from below address and install manually: [Download](https://download2.ctrip.com/html5/Ctrip_V8.43.0_SIT4-092310_Product_9725506.ipa)
      2. use cmd or shell to start wdaproxy manually ```shell tidevice --udid 
       $udid wdaproxy -B $web_driver_angnt_bundle_id -p $port```

3. Run test，all feature files in the features directory by default

```bash
cd {PATH_TO_PROJECT_FOLDER}
flybirds run  # run all features 
flybirds run -P features/test/android  # run all android features
flybirds run -P features/test/ios # run all ios features
```

- The presentation contains the main automation syntax. In order to make the presentation run normally, it is recommended not to modify the configuration items `packagename` and `packagepath`. If you do not need a presentation, you can modify it yourself
- For more description of the cli ： [flybirds cli](#fc)
- For more description of the project ： [Project atructure](#dp)    
- For more description of the feature writing ： [Feature writing](#fw)





### 3. <span id="dp">Project structure</span>

- [Demo project details](https://github.com/ctripcorp/flybirds/blob/main/docs/demoproject.md)


### 4. <span id="fw">Feature writing</span>

- [Behave syntax](https://github.com/ctripcorp/flybirds/blob/main/docs/behaves.md)
- [Common statement description](https://github.com/ctripcorp/flybirds/blob/main/docs/casedsl.md)
- [Page element](https://github.com/ctripcorp/flybirds/blob/main/docs/pageelement.md)
- [Business feature statement extension](https://github.com/ctripcorp/flybirds/blob/main/docs/featureextend.md)


### 5. <span id="fc">flybirds cli</span>

- [cli details](https://github.com/ctripcorp/flybirds/blob/main/docs/flybirds_cli.md)



## Contributing

1. Fork this repository
2. Create a new branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push (`git push origin my-new-feature`)
5. File a PR


## Welcome to fork and feedback

If you have any suggestion, welcome to GitHub to raise [issues](https://github.com/ctripcorp/flybirds/issues).


## License

This project follows the [MIT](http://www.opensource.org/licenses/MIT) license.


## Thanks

Thanks for all these great works that make this project better.

- [airtest](https://github.com/AirtestProject)
- [behave](https://github.com/behave)
- [multiple-cucumber-html-reporter](https://github.com/wswebcreation/multiple-cucumber-html-reporter)