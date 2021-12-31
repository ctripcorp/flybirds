# Common step
In order to allow the use cases described in natural language to be translated into code to run on the UI automation test platform, the framework provide some common statement templates.

In order to read smoothly, prepositions with no actual meaning (if, when, then, and, but) need to be added before the sentence template.

The "[]" in the statement template needs to add a value, otherwise the statement will be regarded as an illegal statement.

## Common statement template

|  statement template	  | description  |
|  :----      | :----  |
| go to url[]     | jump to the specified url address |
| wait [] seconds     | Wait for a while |
| element [] appear after page rendering    | check whether the specified element has been rendered when entering a new page |
| click[]     | click on the element with the specified attribute |
| click text[]     | Click on the element of the specified text |
| click position[][]     | click to specify the location on the screen |
| input [] into []     | input a string in the specified selector |
| from [] find [] element    | find the element with the specified attribute in the specified direction |
| slide to [] distance []    | swipe the specified distance in the specified direction on the full screen |
| [] slide to [] distance []    | slide the specified distance in the specified direction in the specified area |
| exist text []     | check that the specified string exists in the page|
| not exist text []      | check that the specified string does not exist in the page |
| exist element []     | check the presence of elements with specified attributes on the page |
| not exist element []     | check that there is no element with the specified attribute in the page |
| element [] disappear     | check that the element with the specified attribute in the page disappears within the specified time |
| text [] property [] is []  | check that the specified attribute of the specified text in the page is the specified value |
| element [] property [] is []     | check that the specified attribute of the specified element in the page is the specified value |
| element [] position not change in []seconds     | check that the position of the specified element on the page has not changed within the specified time |
| the text of element [] is []  | check that the text of the specified element in the page is equal to the specified value |
| the text of element [] include []  | check that the text of the specified element in the page contains the specified value |
| go to home page     | go to home page |
| screenshot     | save the current screen image |
| start record      | start recording video |
| start recording timeout []      | start recording screen and set timeout |
| stop record      | stop recording video |
| connect device []    | connect test device |
| install app[]      | install app |
| delete app[]      | delete app |
| start app[]      | start app |
| retart app      | retart app |
| logon account[] password []      | login with account and password |
| logout      | logout |
|   -----  | ----- |


## Statement template：

**connect device[{param}]**
- platform: Android
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
- platform: Android, iOS
- description：find specified string exists in the page
- timeout Search timeout time, priority: default value < “waitEleTimeout” in flybird_config.json< Specified in the statement
```js 
exist text [flight]
exist text [flight, timeout=10]
exist text [.?ght, fuzzyMatch=true]
```
**not exist text[string{, fuzzyMatch=false}]**
- platform: Android, iOS
- description：find specified string not exists in the page
```js 
not exist text [flight]
not exist text [flight, timeout=10]
not exist text [.?ght, fuzzyMatch=true]
```
**text[string{, fuzzyMatch=false, timeout=10}]disappear**
- platform: Android, IOS
- description：specified character string disappears from the page within the specified time
timeout timeout for waiting to disappear, priority: default value < “waitEleDisappear” in flybird_config.json< Specified in the statement
```js 
text [flight] disappear
text [.?ght, fuzzyMatch=true, timeout=20] disappear
```
**exist element [selector{, path=false, multiSelector=false, timeout=10}]**
- platform: Android, iOS
- description：check element of the specified selector on the page
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
```js 
exist element [center_content_layout]
exist element [text=ecnomic]
exist element [textMatches=.?eco]
exist element [textMatches=.?eco and type=android.view.ViewGroup, multiSelector=true, timeout=30]
```
**not exist element[selector{, path=false, multiSelector=false}]**
- platform: Android, iOS
- description：check element of the specified selector not on the page
```js
not exist element [center_content_layout]
not exist element [text=ecnomic]
not exist element [textMatches=.?eco]
not exist element [textMatches=.?eco and type=android.view.ViewGroup, multiSelector=true, timeout=30]
```
**element[selector{, path=false, multiSelector=false, timeout=10}]disappear**
- platform: Android, iOS
- description：specified selector disappears from the page within the specified time
- timeout: timeout for waiting to disappear, priority: default value < “waitEleDisappear” in flybird_config.json < Specified in the statement
```js
element [center_content_layout] disappear
element [text=flight] disappear
```
**the text of element [selector{, path=false, multiSelector=false, timeout=10}] is [string{, dealMethod=name}]**
- platform: Android, iOS
- description：specify the text of the element of the selector as the specified string
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
```js
the text of element [text=trip] is [flight]
the text of element [textMatches=.?economic, timeout=15] is [economic, dealMethod=trim_prefix]
the text of element [textMatches=.?economic and visible=True, multiSelector=true, timeout=15] is [economic, dealMethod=trim_prefix]
```
**the text of element [selector{, path=false, multiSelector=false, timeout=10}] include [string{, dealMethod=name}]**
- platform: Android, iOS
- description：pecify the text of the element of the selector include the specified string
- timeout timeout for waiting to disappear, priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
```js
the text of element [text=trip] include [flight]
the text of element [textMatches=.?economic, timeout=15] include [economic, dealMethod=trim_prefix]
the text of element [textMatches=.?economic and visible=True, multiSelector=true, timeout=15] include [economic, dealMethod=trim_prefix]
```
**element[selector{, path=false, multiSelector=false, timeout=10}] appear after page rendering**
- platform: Android, iOS
- description：when entering a new page, you can determine that the page rendering is complete by specifying the element of the selector to appear on the page
- timeout timeout for waiting to disappear, priority: default value < “pageRenderTimeout” in flybird_config.json < Specified in the statement
```js
element [text=flight] appear after page rendering
element [center_content_layout, timeout=15] appear after page rendering
element [center_content_layout, timeout=40] appear after page rendering
```
**click text[string{, fuzzyMatch=false, timeout=10, verifyEle=null, verifyIsPath=false, verifyIsMultiSelector=false, verifyTimeout=10, verifyAction=null}]**
- platform: Android, iOS
- description：click on the string specified on the page
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < specified in the statement
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
- platform: Android, iOS
- description: click on the element of the specified selector on the page   
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < specified in the statement
- verifyEle: if there is partial rendering after clicking, use the relevant information of the element represented by the selector specified by this attribute to determine
- verifyIsPath：specify whether verifyEle is a selector of type path
- verifyIsMultiSelector：specify whether verifyEle is a multi-attribute type selector
- verifyTimeout: timeout period for judging whether the rendering of the click operation is completed, priority: default value < “clickVerifyTimeout” in flybird_config.json < Specified in the statement
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
- platform: Android, iOS
- description：the value of the specified attribute of the element corresponding to the specified string in the page is the specified value
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
```js
text [economic] property [text] is flight
text [economic, timeout=15] property [text, dealMethod=trim_last] is fli
```
**element[selector{, path=false, multiSelector=false, timeout=10}]property[property name{, dealMethod=name}]is{property value}**
- platform: Android, iOS
- description：the value of the specified attribute of the element of the specified selector on the page is the specified value
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
```js
element [text=flight] property [text] is flight
element [text=flight, timeout=15] property[text, dealMethod=trim_last] is fli
```
**input[selector{, path=false, multiSelector=false, timeout=10}]into[string{, pocoInput=false, afterInputWait=1}]**
- platform: Android, iOS
- description：input the specified copy in the element of the specified selector 
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
- pocoInput: Whether to use the input method of poco, the input method of airtest is used by default， Priority: default < “usePocoInput” in flybird_config.json < Specified in the statement
- afterInputWait: Sleep time after input
， Priority: default < “afterInputWait” in flybird_config.json < Specified in the statement
```js
input [shanghai] into [inputEleId]
input [david, pocoInput=true, afterInputWait=5] into [type=InputView]
```
**[selector{, path=false, multiSelector=false, timeout=10}] slide to {up/down/left/right} distance [value{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- platform: Android, iOS
- description：slide the specified distance in the specified direction in the sliding container of the specified selector
- timeout: find the timeout of "string", priority: default value < “waitEleTimeout” in flybird_config.json < Specified in the statement
- startX: the coordinate value of the X axis of the starting coordinate of the sliding in the container，<=1 represents the percentage，>1 representative pixel
- startY: he coordinate value of the Y axis of the starting coordinate of the sliding in the container，<=1 represents the percentage，>1 representative pixel
- duration: time per swipe， priority: default < “swipeDuration” in flybird_config.json < Specified in the statement
- readyTime: waiting time before sliding starts， priority: default < “swipeReadyTime” in flybird_config.json < Specified in the statement
```js
[containerEleId] slide to left [0.1]
[containerEleId] slide to up [100, duration=5, readyTime=3]
[containerEleId] slide to right [100, startX=0.2, startY=0.4, duration=5, readyTime=3]
```
**slide to {up/down/left/right} distance [value{, startX=0.5, startY=0.5, duration=null, readyTime=null}]**
- platform: Android, iOS
- description：use the full screen as the container to slide the specified distance in the specified direction
- startX: the coordinate value of the X axis of the sliding start coordinate in the full screen，<=1 represents the percentage，>1 representative pixel
- startY: the coordinate value of the Y axis of the sliding start coordinate in the full screen，<=1 represents the percentage，>1 representative pixel
- duration: time per swipe， priority: default < “swipeDuration” in flybird_config.json < Specified in the statement
- readyTime: waiting time before sliding starts， priority: default < “swipeReadyTime” in flybird_config.json < Specified in the statement
```js
slide to up distance [0.05]
slide to down [0.4, readyTime=3, duration=2]
```
**from {up/down/left/right} find [selector{, path=false, multiSelector=false, swipeCount=5, startX=0.5, startY=0.5, distance=0.3, duration=null}]element**
- platform: Android, iOS
- description：swipe to the specified direction on the full screen to find the element of the specified selector
- swipeCount: swipe to find the maximum number of swipes. If the specified element is not found on the page after the sliding operation exceeds this value, it will fail. priority: default < “swipeSearchCount” in flybird_config.json < Specified in the statement
- startX: Slide the X-axis coordinate value of the starting coordinate in the full screen, <=1 means percentage, >1 means pixel
- startY: Slide the Y-axis coordinate value of the starting coordinate in the full screen, <=1 means percentage, >1 means pixel
- duration: time per swipe
， priority: default <“searchSwipeDuration” in flybird_config.json < Specified in the statement
- distance：the distance of each swipe in the swipe search， priority: default < “swipeSearchDistance” in flybird_config.json < Specified in the statement
```js
from right find [text=flight] element
from left find [testId, distance=0.5, duration=2, swipeCount=8] element
```
**element[selector{, path=false, multiSelector=false, timeout=10}]position not change in[time{, verifyCount=5}] seconds**
- platform: Android, iOS
- description： the element of the specified selector has not changed at the specified time and position, the purpose is to determine that the page is not in a sliding state
- timeout: the timeout for find string，priority: default < “waitEleTimeout” in flybird_config.json < specified in the statement
- verifyCount: maximum number of judgments，priority: default <“verifyPosNotChangeCount” in flybird_config.json < Specified in the statement

**start recording timeout[time]**
- platform: Android
- description：start to record the screen, stop recording when the timeout period is not stopped
**start record**
- platform: Android
- description： start recording the screen, using the default timeout period (configured in the configuration file)
**stop record**
- platform: Android
- description：stop the screen recording and associate the video file to the report
**wait[time]seconds**
- platform: Android, iOS
- description：wait for a while
**screenshot***
- platform: Android, iOS
- description：take a screenshot of the current screen and associate it with the report

**go to url[url address]**
- platform: Android
- description：Jump to the specified page through the schema, and the page name is maintained in the form of "page name: page schemaUrl" in config/schema_url.js
```js
go to url [list page]
```
