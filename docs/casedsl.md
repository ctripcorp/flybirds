# Common step
In order to allow the use cases described in natural language to be translated into code to run on the UI automation test platform, the framework provide some common statement templates.

In order to read smoothly, prepositions with no actual meaning (if, when, then, and, but) need to be added before the sentence template.

The "[]" in the statement template needs to add a value, otherwise the statement will be regarded as an illegal statement.

## Common statement template

| statement template                                           | description                                                  | suitable for   |
| ------------------------------------------------------------ | ------------------------------------------------------------ | -------------- |
| go to url[]                                                  | jump to the specified url address                            | android 、web  |
| wait [] seconds                                              | Wait for a while                                             | ALL            |
| element [] appear after page rendering                       | check whether the specified element has been rendered when entering a new page | ALL            |
| click[]                                                      | click on the element with the specified attribute            | ALL            |
| click text[]                                                 | Click on the element of the specified text                   | ALL            |
| click position[][]                                           | click to specify the location on the screen                  | ALL            |
| input [] into []                                             | input a string in the specified selector                     | ALL            |
| clear [] and input[]                                         | clear and input a string in the specified selector           | Web            |
| from [] find [] element                                      | find the element with the specified attribute in the specified direction | ALL            |
| slide to [] distance []                                      | swipe the specified distance in the specified direction on the full screen | ALL            |
| [] slide to [] distance []                                   | slide the specified distance in the specified direction in the specified area | ALL            |
| exist text []                                                | check that the specified string exists in the page           | ALL            |
| not exist text []                                            | check that the specified string does not exist in the page   | ALL            |
| exist element []                                             | check the presence of elements with specified attributes on the page | ALL            |
| not exist element []                                         | check that there is no element with the specified attribute in the page | ALL            |
| element [] disappear                                         | check that the element with the specified attribute in the page disappears within the specified time | App            |
| text[]disappear                                              | check that the specified string in the page disappears from the page within a specified time | App            |
| text [] property [] is []                                    | check that the specified attribute of the specified text in the page is the specified value | ALL            |
| element [] property [] is []                                 | check that the specified attribute of the specified element in the page is the specified value | ALL            |
| element [] position not change in []seconds                  | check that the position of the specified element on the page has not changed within the specified time | App            |
| the text of element [] is []                                 | check that the text of the specified element in the page is equal to the specified value | ALL            |
| the text of element [] include []                            | check that the text of the specified element in the page contains the specified value | ALL            |
| go to home page                                              | go to home page                                              | ALL            |
| screenshot                                                   | save the current screen image                                | ALL            |
| start record                                                 | start recording video                                        | App            |
| start recording timeout []                                   | start recording screen and set timeout                       | App            |
| stop record                                                  | stop recording video                                         | ALL            |
| connect device []                                            | connect test device                                          | App            |
| install app[]                                                | install app                                                  | android        |
| delete app[]                                                 | delete app                                                   | android        |
| start app[]                                                  | start app                                                    | App            |
| retart app                                                   | retart app                                                   | App            |
| close app                                                    | close app                                                    | App            |
| logon account[] password []                                  | login with account and password                              | ALL            |
| logout                                                       | logout                                                       | ALL            |
| return to previous page                                      | return to previous page                                      | Android 、 web |
| in[]from [] find [] element                                  | Find the element of the specified selector by sliding in the specified direction within the element that refers to the selector | ALL            |
| from [] select []                                            | Select the specified value in the web select element         | web            |
| exist [] subNode [] element                                  | check that  a parent element exists, and a child element exists under that parent element | web            |
| the text of element [] subNode [] is []                      | check that  a parent element exists, and the text of a child element under that parent element is the specified string | web            |
|                                                              |                                                              |                |
| cache service request [operation[,operation ...]]            | Cache the last request body  for this service locally<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| remove service request cache[operation[,operation ...]]      | Clear cached request body for this operation from local<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| remove all service request caches                            | Remove all operations cached request body                    | web            |
| listening service [operation[,operation ...]] bind mockCase[mockCaseId[,mockCaseId ...]] | Monitor the operation request and intercept it, and mock data with the return message of mockCaseId<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| remove service listener [operation[,operation ...]]          | Remove request listener for this operation<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| remove all service listeners                                 | remove all request listeners                                 | web            |
| compare service request operation] with json file [target_data_path] | Compare the cached  request body of the operation with the file content corresponding to target_data_path<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| compare service non-json request [operation] with non-json file [target_data_path] | Compare the non-json cached request body of the operation with the file content corresponding to target_data_path<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| service request [operation] request parameter [target_json_path] is [expect_value] | Check whether the value of the corresponding parameter of the request body cached by the operation is consistent with the given expected value<br />Note: `operation` is the string between the last  `\` and  `?` in the url | web            |
| -----                                                        | -----                                                        | -----          |



## Statement template：

**connect device[{param}]**
- platform: Android , IOS
- description：connect test device
- example：connect device [10.21.37.123:5555]

**install app[{param}]**
- platform: Android
- description：install app
- example：install app [/Users/xxx/xxx.apk]

**delete app[{param}]**
- platform: Android
- description：delete app
- example：delete app [package name]

**start app[{param}]**
- platform: Android, IOS
- description：start app
- example：start app [package name]

**restart app**
- platform: Android, IOS
- description：restart app

**go to home page**
- description：go to home page
- PS：User-defined implementation, implement the to_home() method in the pscript/app/operation.py file

**logon account[{param1}]password[{param2}]**
- description：Specify user name and password to log in
- PS：User-defined implementation, implement the login(user_name, password) method in the pscript/app/operation.py file

**logout**
- description:logout
- PS：User-defined implementation, implement the logout() method in the pscript/app/operation.py file

**exist text[string{, fuzzyMatch=false, timeout=10}]**
- platform: Android, iOS，Web
- description：find specified string exists in the page
- timeout Search timeout time, priority: default value < “waitEleTimeout” in flybirds_config.json< Specified in the statement
```js 
exist text [flight]
exist text [flight, timeout=10]
exist text [.?ght, fuzzyMatch=true]
```
**not exist text[string{, fuzzyMatch=false}]**
- platform: Android, iOS，Web
- description：find specified string not exists in the page
```js 
not exist text [flight]
not exist text [flight, timeout=10]
not exist text [.?ght, fuzzyMatch=true]
```
**text[string{, fuzzyMatch=false, timeout=10}]disappear**
- platform: Android, IOS，Web
- description：specified character string disappears from the page within the specified time
timeout timeout for waiting to disappear, priority: default value < “waitEleDisappear” in flybirds_config.json< Specified in the statement
```js 
text [flight] disappear
text [.?ght, fuzzyMatch=true, timeout=20] disappear
```
**exist element [selector{, path=false, multiSelector=false, timeout=10}]**
- platform: Android, iOS，Web
- description：check element of the specified selector on the page
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
```js 
exist element [center_content_layout]
exist element [text=ecnomic]
exist element [textMatches=.?eco]
exist element [textMatches=.?eco and type=android.view.ViewGroup, multiSelector=true, timeout=30]
```
**not exist element[selector{, path=false, multiSelector=false}]**
- platform: Android, iOS，Web
- description：check element of the specified selector not on the page
```js
not exist element [center_content_layout]
not exist element [text=ecnomic]
not exist element [textMatches=.?eco]
not exist element [textMatches=.?eco and type=android.view.ViewGroup, multiSelector=true, timeout=30]
```
**element[selector{, path=false, multiSelector=false, timeout=10}]disappear**
- platform: Android, iOS，Web
- description：specified selector disappears from the page within the specified time
- timeout: timeout for waiting to disappear, priority: default value < “waitEleDisappear” in flybirds_config.json < Specified in the statement
```js
element [center_content_layout] disappear
element [text=flight] disappear
```
**the text of element [selector{, path=false, multiSelector=false, timeout=10}] is [string{, dealMethod=name}]**
- platform: Android, iOS，Web
- description：specify the text of the element of the selector as the specified string
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
```js
the text of element [text=trip] is [flight]
the text of element [textMatches=.?economic, timeout=15] is [economic, dealMethod=trim_prefix]
the text of element [textMatches=.?economic and visible=True, multiSelector=true, timeout=15] is [economic, dealMethod=trim_prefix]
```
**the text of element [selector{, path=false, multiSelector=false, timeout=10}] include [string{, dealMethod=name}]**
- platform: Android, iOS，Web
- description：pecify the text of the element of the selector include the specified string
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
```js
the text of element [text=trip] include [flight]
the text of element [textMatches=.?economic, timeout=15] include [economic, dealMethod=trim_prefix]
the text of element [textMatches=.?economic and visible=True, multiSelector=true, timeout=15] include [economic, dealMethod=trim_prefix]
```
**element[selector{, path=false, multiSelector=false, timeout=10}] appear after page rendering**
- platform: Android, iOS，Web
- description：when entering a new page, you can determine that the page rendering is complete by specifying the element of the selector to appear on the page
- timeout timeout for waiting to disappear, priority: default value < “pageRenderTimeout” in flybirds_config.json < Specified in the statement
```js
element [text=flight] appear after page rendering
element [center_content_layout, timeout=15] appear after page rendering
element [center_content_layout, timeout=40] appear after page rendering
```
**click text[string{, fuzzyMatch=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- platform: Android, iOS，Web
- description：click on the string specified on the page
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < specified in the statement
- verifyEle: if there is partial rendering after clicking, use the relevant information of the element represented by the selector specified by this attribute to determine
- verifyIsPath：specify whether verifyEle is a selector of type path
- verifyIsMultiSelector：specify whether verifyEle is a multi-attribute type selector
- verifyTimeout The timeout period for judging whether the rendering of the click operation is completed, priority: default value < frame_info.json中的“clickVerifyTimeout” < Specified in the statement
- verifyAction ： When a specific type of change occurs in the element represented by verifyEle, the rendering after clicking is complete，
- position/text/appear/disappear: change of location/change of copy/appear on page/disappear from page
```js
click text [flight]
click text [.?ght, fuzzyMatch=true, timeout=15]
click text [flight, verifyEle=center_content_layout, verifyAction=position]
click text [flight, verifyEle=text=filterand =textView, verifyIsMultiSelector=true, verifyAction=position]
```
**click[selector{, path=false, multiSelector=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- platform: Android, iOS，Web
- description: click on the element of the specified selector on the page   
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < specified in the statement
- verifyEle: if there is partial rendering after clicking, use the relevant information of the element represented by the selector specified by this attribute to determine
- verifyIsPath：specify whether verifyEle is a selector of type path
- verifyIsMultiSelector：specify whether verifyEle is a multi-attribute type selector
- verifyTimeout: timeout period for judging whether the rendering of the click operation is completed, priority: default value < “clickVerifyTimeout” in flybirds_config.json < Specified in the statement
- verifyAction：when a specific type of change occurs in the element represented by verifyEle, the rendering after clicking is complete，
- position/text/appear/disappear: change of location/change of copy/appear on page/disappear from page
```js
click [flight]
click [.?ght, fuzzyMatch=true, timeout=15]
click [flight, verifyEle=center_content_layout, verifyAction=position]
click [flight, verifyEle=text=filterand =textView, verifyIsMultiSelector=true, verifyAction=position]
```
**click position [{x},{y}]**
```js
click position [200,100]
```
**text [string{, fuzzyMatch=false, timeout=10}]property [{, dealMethod=name}]is {}**
- platform: Android, iOS，Web
- description：the value of the specified attribute of the element corresponding to the specified string in the page is the specified value
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
```js
text [economic] property [text] is flight
text [economic, timeout=15] property [text, dealMethod=trim_last] is fli
```
**element[selector{, path=false, multiSelector=false, timeout=10}]property[property name{, dealMethod=name}]is{property value}**
- platform: Android, iOS，Web
- description：the value of the specified attribute of the element of the specified selector on the page is the specified value
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
```js
element [text=flight] property [text] is flight
element [text=flight, timeout=15] property[text, dealMethod=trim_last] is fli
```
**input[selector{, path=false, multiSelector=false, timeout=10}]into[string{, pocoInput=false, afterInputWait=1}]**
- platform: Android, iOS，Web
- description：input the specified copy in the element of the specified selector 
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
- pocoInput: Whether to use the input method of poco, the input method of airtest is used by default， Priority: default < “usePocoInput” in flybirds_config.json < Specified in the statement
- afterInputWait: Sleep time after input
， Priority: default < “afterInputWait” in flybirds_config.json < Specified in the statement
```js
input [shanghai] into [inputEleId]
input [david, pocoInput=true, afterInputWait=5] into [type=InputView]
```
**[selector{, path=false, multiSelector=false, timeout=10}] slide to {up/down/left/right} distance [value{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- platform: Android, iOS，Web
- description：slide the specified distance in the specified direction in the sliding container of the specified selector
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybirds_config.json < Specified in the statement
- startX: the coordinate value of the X axis of the starting coordinate of the sliding in the container，<=1 represents the percentage，>1 representative pixel
- startY: he coordinate value of the Y axis of the starting coordinate of the sliding in the container，<=1 represents the percentage，>1 representative pixel
- duration: time per swipe， priority: default < “swipeDuration” in flybirds_config.json < Specified in the statement
- readyTime: waiting time before sliding starts， priority: default < “swipeReadyTime” in flybirds_config.json < Specified in the statement
```js
[containerEleId] slide to left [0.1]
[containerEleId] slide to up [100, duration=5, readyTime=3]
[containerEleId] slide to right [100, startX=0.2, startY=0.4, duration=5, readyTime=3]
```
**slide to {up/down/left/right} distance [value{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- platform: Android, iOS，Web
- description：use the full screen as the container to slide the specified distance in the specified direction
- startX: the coordinate value of the X axis of the sliding start coordinate in the full screen，<=1 represents the percentage，>1 representative pixel
- startY: the coordinate value of the Y axis of the sliding start coordinate in the full screen，<=1 represents the percentage，>1 representative pixel
- duration: time per swipe， priority: default < “swipeDuration” in flybirds_config.json < Specified in the statement
- readyTime: waiting time before sliding starts， priority: default < “swipeReadyTime” in flybirds_config.json < Specified in the statement
```js
slide to up distance [0.05]
slide to down [0.4, readyTime=3, duration=2]
```
**from {up/down/left/right} find [selector{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]element**
- platform: Android, iOS，Web
- description：swipe to the specified direction on the full screen to find the element of the specified selector
- swipeCount: swipe to find the maximum number of swipes. If the specified element is not found on the page after the sliding operation exceeds this value, it will fail. priority: default < “swipeSearchCount” in flybirds_config.json < Specified in the statement
- startX: Slide the X-axis coordinate value of the starting coordinate in the full screen, <=1 means percentage, >1 means pixel
- startY: Slide the Y-axis coordinate value of the starting coordinate in the full screen, <=1 means percentage, >1 means pixel
- duration: time per swipe
， priority: default <“searchSwipeDuration” in flybirds_config.json < Specified in the statement
- distance：the distance of each swipe in the swipe search， priority: default < “swipeSearchDistance” in flybirds_config.json < Specified in the statement
```js
from right find [text=flight] element
from left find [testId, distance=0.5, duration=2, swipeCount=8] element
```
**element[selector{, path=false, multiSelector=false, timeout=10}]position not change in[time{, verifyCount=5}] seconds**
- platform: Android, iOS
- description： the element of the specified selector has not changed at the specified time and position, the purpose is to determine that the page is not in a sliding state
- timeout: the timeout for find string，priority: default < “waitEleTimeout” in flybirds_config.json < specified in the statement
- verifyCount: maximum number of judgments，priority: default <“verifyPosNotChangeCount” in flybirds_config.json < Specified in the statement

**start recording timeout[time]**
- platform: Android，iOS
- description：start to record the screen, stop recording when the timeout period is not stopped

**start record**
- platform: Android，iOS
- description： start recording the screen, using the default timeout period (configured in the configuration file)

**stop record**
- platform: Android，iOS，Web
- description：stop the screen recording and associate the video file to the report

**wait[time]seconds**
- platform: Android, iOS，Web
- description：wait for a while

**screenshot***
- platform: Android, iOS，Web
- description：take a screenshot of the current screen and associate it with the report

**go to url[url address]**
- platform: Android，Web
- description：Jump to the specified page through the schema, and the page name is maintained in the form of "page name: page schemaUrl" in config/schema_url.js
```js
go to url [list page]
```

**cache service request [operation[,operation ...]]**

- platform：Web
- description： Cache the last request body  for this service locally<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```js
//Example1：
cache service request [getRecommendHotelList]

//Example2：
cache service request [getRecommendHotelList,writecookie]
```

**remove service request cache[operation[,operation ...]]**

- platform：Web
- description：Clear cached request body for this operation from local<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```js
//Example1：
remove service request cache [getRecommendHotelList]

//Example2：
remove service request cache [getRecommendHotelList,writecookie]
```

**remove all service request caches**

- platform：Web
- description：Remove all operations cached request body

**listening service [operation[,operation ...]] bind mockCase[mockCaseId[,mockCaseId ...]]**

- platform：Web
- description：Monitor the operation request and intercept it, and mock data with the return message of mockCaseId<br />Note: `operation` is the string between the last  `\` and  `?` in the url

- **MockCase Configuration**：

  ​	The `mock` data of the service listening `step` statement can be obtained in two ways: **json file configuration** and **function call**.

  -  **json file configuration**：Example 1 below. For the specific setting method and format, please refer to the json file in the **Demo** project **mockCaseData** directory.

    In this method, it should be noted that the `mockCaseId` (json key, such as `4245512` in example 1) corresponding to `response` needs to be unique in the entire `mockCaseData` directory, otherwise the mock data will be used by others with the same `key` data is overwritten.

  - **function call**:  Custom handling with getting `MockData`. This approach requires the implementation of the `get_mock_case_body(mock_case_id)` extension method in the **pscript/custom_handle/operation.py** file of the **Demo** project.

  The `MockCase` binding data prefers the result returned by the custom extension method. When the result of the custom extension method is None, the framework will try to find all json files in the project **mockCaseData** directory and return the mock data corresponding to `mock_case_id` in the json file.

**Mock data configuration example I: json file configuration**

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

**Syntax usage example:**

```js
//Example1：
listening service [movie] bind mockCase[4245512]

//Example2：
listening service [movie,testList] bind mockCase[4245512,123456]
```

**remove service listener [operation[,operation ...]]**

- platform：Web
- description：Remove request listener for this operation<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```js
//Example1：
remove service listener [movie]

//Example2：
remove service listener [movie,testList]
```

**remove all service listeners**

- platform：Web
- description：remove all request listeners

**compare service request operation] with json file [target_data_path]**

- 支持平台：Web
- description：Compare the cached  request body of the operation with the file content corresponding to target_data_path<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```js
compare service request [getRecommendHotelList] with json file [compareData/getRecommendHotelList.json]
```

**compare service non-json request [operation] with non-json file [target_data_path]**

- platform：Web
- description：Compare the non-json cached request body of the operation with the file content corresponding to target_data_path<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```gherkin
compare service non-json request [writecookie] with non-json file [compareData/writecookie.txt]
```

**service request [operation] request parameter [target_json_path] is [expect_value]**

- platform：Web
- description：Check whether the value of the corresponding parameter of the request body cached by the operation is consistent with the given expected value<br />Note: `operation` is the string between the last  `\` and  `?` in the url

```gherkin
# Examples
service request [getRecommendHotelList] request parameter [head.syscode] is [PC]
service request [getRecommendHotelList] request parameter [$.cityId] is [2]
service request [getRecommendHotelList] request parameter [cityId] is [2]
```

- 🍖**Configure ignore nodes：**

​		Service request comparison supports setting **ignore node**, including **specific path** and **regular expression**. For the specific setting method and format, please refer to the json file in the **Demo** project **interfaceIgnoreConfig** directory.

**Example：**

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

**Description**：

- `getRecommendHotelList`, `writecookie` are the request name `operation` of the service request

- `head.cid` is the specific node path in the request body of the service `getRecommendHotelList`. This node will be ignored when comparing messages with files.

- `regex: root\\['head'\\]\\['extension'\\]\\[\\d+\\]\\['value'\\]` is a regular expression. All nodes matching this path in the `getRecommendHotelList` request body will be ignored when comparing.

    	🧨**Note:** When configuring a regular expression, please use `regex:` before the string to declare it.

