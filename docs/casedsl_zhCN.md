# 公共语句
为了让自然语言描述的用例能翻译成代码在UI自动化测试平台运行，框架提供了公共语句模板。

为了阅读通顺，语句模板前需要加上无实际含义的介词（假如，当，那么，并且，但是）。

语句模板中"[]"内需输入值，否则语句将视为不合法语句。

## 以下是常用语句模板：

|  语句模板	  | 语义  |
|  :----      | :----  |
| 跳转到[]     | 跳转到指定的url地址 |
| 等待[]秒     | 等待一段时间 |
| 页面渲染完成出现元素[]    | 进入新的页面时检查指定元素是否渲染完成 |
| 点击[]     | 点击指定属性的元素 |
| 点击文案[]     | 点击指定文案的元素 |
| 点击屏幕位置[][]     | 点击屏幕指定位置 |
| 在 [] 中输入[]     | 在指定选择器中输入字符串 |
| 向[] 查找[]的元素    | 向指定方向查找指定属性的元素 |
| 全屏向[] 滑动[]    | 全屏向指定方向滑动指定距离 |
| [] 向[] 滑动[]    | 在指定区域内向指定方向滑动指定距离 |
| 存在[]的文案      | 检查页面中存在指定的字符串|
| 不存在[]的文案      | 检查页面中不存在指定的字符串 |
| 存在[]的元素     | 检查页面中存在指定属性的元素 |
| 不存在[]的元素     | 检查页面中不存在指定属性的元素 |
| 元素[]消失     | 检查页面中指定属性的元素在指定时间内消失 |
| 文案[] 的属性[] 为 []     | 检查页面中指定文案的指定属性为指定值 |
| 元素[] 的属性[] 为 []     | 检查页面中指定元素的指定属性为指定值 |
| 元素[] 位置[] 秒内未变动     | 检查页面中指定元素的位置在指定时间内未发生变化 |
| 元素[] 的文案为[]  | 检查页面中指定元素的文案等于指定值 |
| 元素[] 的文案包含[]  | 检查页面中指定元素的文案包含指定值 |
| 回到首页     | 回到首页 |
| 全屏截图     | 保存当前屏幕图像 |
| 开始录屏      | 开始录制视频 |
| 开始录屏超时[]      | 开始录屏并设置超时时间 |
| 结束录屏      | 结束录制视频 |
| 连接设备[]    | 连接测试设备 |
| 安装APP[]      | 安装APP |
| 删除APP[]      | 删除APP |
| 启动APP[]      | 启动APP |
| 重启APP      | 重启APP |
| 登录账号[] 密码[]      | 使用账号密码进行登录 |
| 退出登录      | 退出系统登录 |
|   -----  | ----- |


## 语句模版：

**连接设备[{param}]**
- 支持平台：Android
- 语义：连接测试设备
- 例子：连接设备[10.21.37.123:5555]

**安装APP[{param}]**
- 支持平台：Android
- 语义：安装APP
- 例子：安装APP[/Users/xxx/xxx.apk]

**删除APP[{param}]**
- 支持平台：Android
- 语义：删除APP
- 例子：删除APP[package name]

**启动APP[{param}]**
- 支持平台：Android、iOS
- 语义：启动APP
- 例子：启动APP[package name]

**重启app**
- 支持平台：Android、iOS
- 语义：重新启动app

**回到首页**
- 语义：跳转到首页
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 to_home() 方法

**登录账号[{param1}]密码[{param2}]**
- 语义：指定用户名、密码登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 login(user_name, password)方法

**退出登录**
- 语义:退出当前登录
- 注：用户自定义实现, 在 pscript/app/operation.py 文件中实现 logout() 方法

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
存在[center_content_layout]的元素
存在[text=经济舱]的元素
存在[textMatches=.?经济舱]的元素
存在[textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true, timeout=30]的元素
存在[机票→第1个兄弟节点, path=true]的元素
```
**不存在[选择器{, path=false, multiSelector=false}]的元素**
- 支持平台：Android、iOS
- 语义：页面中不存在指定  选择器 的元素
```js
不存在[center_content_layout]的元素
不存在[text=经济舱]的元素
不存在textMatches=.?经济舱并且type=android.view.ViewGroup, multiSelector=true]的元素
不存在[机票→第1个兄弟节点, path=true]的元素
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
**页面渲染完成出现元素[选择器{, path=false, multiSelector=false, timeout=10}]**
- 支持平台：Android、iOS
- 语义：进入新的页面时通过指定 选择器 的元素出现在页面上来判断页面渲染完成
- timeout 查找的超时时间，优先级：默认值 < flybirds_config.json中的“pageRenderTimeout” < 语句中指定
```js
页面渲染完成出现元素[text=机票]

页面渲染完成出现元素[center_content_layout, timeout=15]

页面渲染完成出现元素[center_content_layout, timeout=40]
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
**点击屏幕位置[{x},{y}]**
```js
点击屏幕位置[200,100]
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
**元素[选择器{, path=false, multiSelector=false, timeout=10}]位置[time{, verifyCount=5}]秒内未变动**
- 支持平台：Android、iOS
- 语义： 指定选择器的元素在指定时间位置未发生变化，目的是判断页面未处于滑动状态
- timeout 查找“字符串”的超时时间，优先级：默认值 < flybirds_config.json中的“waitEleTimeout” < 语句中指定
- verifyCount: 最大判断次数，优先级：默认值 < flybirds_config.json中的“verifyPosNotChangeCount” < 语句中指定
**开始录屏超时[time]**
- 支持平台：Android
- 语义：开始录制屏幕，到超时时间未停止则停止录屏
**开始录屏**
- 支持平台：Android
- 语义： 开始录制屏幕，使用默认的超时时间（在配置文件中配置）
**结束录屏**
- 支持平台：Android
- 语义：结束录制屏幕，并将视频文件关联到报告中
**等待[time]秒**
- 支持平台：Android、iOS
- 语义：执行暂停指定时间
**全屏截图***
- 支持平台：Android、iOS
- 语义：截取当前屏幕快照并关联到报告中

**跳转到[页面名称]**
- 支持平台：Android
- 语义：通过schema跳转到指定页面，页面名称在config/schema_url.json 中以  "页面名称: 页面schemaUrl"  的形式维护
```js
跳转到[首页]
```
