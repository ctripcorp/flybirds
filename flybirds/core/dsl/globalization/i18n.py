# -*- coding: utf-8 -*-
globalization = {
    "en": {
        "rerun failed scenario": u"rerun failed scenario",
        "information association of failed operation":
            "information association of failed operation, run the {} time"
            " :[{}]",
        "start record": "start record",
        "stop record": "stop record",
        "rank": "rank",
        "parent": "parent",
        "children": "children",
        "sibling": "sibling",
        "offsprings": "offsprings",
        "and": "and",
        "up": "up",
        "down": "down",
        "left": "left",
        "right": "right",
        "horizontal": "horizontal",
        "vertical": "vertical",
        "modal_list": ["name=同意并继续",
                       "name=使用App时允许",
                       "name=允许",
                       "name=common update X",
                       "name=我知道了",
                       "text=同意并继续",
                       "text=使用App时允许",
                       "text=允许",
                       "text=common update X",
                       "text=我知道了",
                       "text=Wait",
                       "text=OK",
                       "text=Allow",
                       "text=Deny"],
        "break_list": ["text=System UI isn't responding",
                       "text=Pixel Launcher isn't responding"]
    },
    "zh-CN": {
        "rerun failed scenario": u"\u5931\u8d25\u91cd\u65b0\u8fd0\u884c",
        "information association of failed operation":
            "失败运行的信息关联,运行第{}次:[{}]",
        "start record": u"开始录屏",
        "stop record": u"结束录屏",
        "rank": u"第",
        "parent": u"父节点",
        "children": u"孩子",
        "sibling": u"兄弟",
        "offsprings": u"后代",
        "and": u"并且",
        "up": u"上",
        "down": u"下",
        "left": u"左",
        "right": u"右",
        "horizontal": u"水平",
        "vertical": u"垂直",
        "modal_list": ["name=同意并继续",
                       "name=使用App时允许",
                       "name=允许",
                       "name=common update X",
                       "name=我知道了",
                       "text=同意并继续",
                       "text=使用App时允许",
                       "text=允许",
                       "text=common update X",
                       "text=我知道了",
                       "text=Wait",
                       "text=OK",
                       "text=Allow",
                       "text=Deny"],
        "break_list": ["text=System UI isn't responding",
                       "text=Pixel Launcher isn't responding"]
    },
}

step_language = {
    "en": {
        "install app[{param}]": ["install app[{param}]"],
        "start app[{param}]": ["start app[{param}]"],
        "touch[{selector}]": ["touch[{selector}]"],
        "touch text[{selector}]": ["touch text[{selector}]"],
    },
    "zh-CN": {
        "install app[{selector}]": ["安装APP[{selector}]"],
        "delete app[{selector}]": ["删除APP[{selector}]"],
        "start app[{selector}]": ["启动APP[{selector}]"],
        "restart app": ["重启App"],
        "close app": ["关闭App"],
        "init device[{selector}]": ["设备初始化[{selector}]"],
        "connect device[{selector}]": ["连接设备[{selector}]"],
        "start recording timeout[{param}]": ["开始录屏超时[{param}]"],
        "start record": ["开始录屏"],
        "stop record": ["结束录屏"],
        "execute js[{param}]": ["执行js[{param}]"],
        "go to url[{param}]": ["跳转到[{param}]", "跳转页面到[{param}]"],
        "set header [{name}] value[{value}]": ["设置header名称[{name}]的值为[{value}]"],
        "set sessionStorage name[{name}] value[{value}]": ["设置sessionStorage名称[{name}]的值为[{value}]"],
        "set localStorage name[{name}] value[{value}]": ["设置localStorage名称[{name}]的值为[{value}]"],
        "set cookie name[{name}] value[{value}] url[{url}]": ["设置cookie 名称[{name}] 值[{value}] 网址[{url}]"],
        "get cookie": ["获取cookie"],
        "get local storage": ["获取local storage"],
        "get session storage": ["获取session storage"],
        "return to previous page": ["返回上一页", "浏览器后退"],
        "browser forward": ["浏览器前进"],
        "go to home page": ["回到首页"],
        "logon account[{selector1}]password[{selector2}]": [
            "登录账号[{selector1}]密码[{selector2}]",
            "登陆账号[{selector1}]密码[{selector2}]",
        ],
        "logout": ["退出登陆", "退出登录"],
        "wait[{param}]seconds": ["等待[{param}]秒"],
        "screenshot": ["全屏截图"],
        "ocr [{selector}]": ["全屏扫描[{selector}]"],
        "ocr": ["全屏扫描"],
        "change ocr lang [{param}]": ["切换OCR语言[{param}]"],
        "exist image [{param}]": ["存在图像[{param}]"],
        "not exist image [{param}]": ["不存在图像[{param}]"],
        "information association of failed operation, run the {param1} time"
        " :[{param2}]": ["失败运行的信息关联,运行第{param1}次:[{param2}]"],
        "text[{selector}]property[{param2}]is {param3}": [
            "文案[{selector}]的属性[{param2}]为{param3}"
        ],
        "text[{selector}]property[{param2}]include {param3}": [
            "文案[{selector}]的属性[{param2}]包含{param3}"
        ],
        "text[{selector}]property[{param2}]not include {param3}": [
            "文案[{selector}]的属性[{param2}]不包含{param3}"
        ],
        "element[{selector}]property[{param2}]is {param3}": [
            "元素[{selector}]的属性[{param2}]为{param3}"
        ],
        "element[{selector}]property[{param2}]include {param3}": [
            "元素[{selector}]的属性[{param2}]包含{param3}"
        ],
        "element[{selector}]property[{param2}]not include {param3}": [
            "元素[{selector}]的属性[{param2}]不包含{param3}"
        ],
        "mouse hover[{selector}]": ["鼠标悬浮[{selector}]"],
        "click[{selector}]": ["点击[{selector}]"],
        "click text[{selector}]": ["点击文案[{selector}]"],
        "click ocr text[{selector}]": ["点击扫描文案[{selector}]"],
        "click ocr regional[{selector}] text[{param2}]": ["点击区域[{selector}]中扫描文案[{param2}]"],
        "click ocr regional[{selector}]": ["点击区域[{selector}]"],
        "click image[{selector}]": ["点击图像[{selector}]"],
        "click position[{x},{y}]": ["点击屏幕位置[{x},{y}]"],
        "if [{selector}] exist then click": ["如果[{selector}]存在则点击该元素"],
        "set web page with width[{width}] and height[{height}]": ["设置浏览器宽度[{width}]和高度[{height}]"],
        "in[{selector}]input[{param2}]": ["在[{selector}]中输入[{param2}]"],
        "in ocr[{selector}]input[{param2}]": ["在扫描文字[{selector}]中输入[{param2}]"],
        "clear [{selector}] and input[{param2}]": [
            "在[{selector}]中清空并输入[{param2}]"],
        "clear input[{selector}]": [
            "清空输入框[{selector}]"],
        "element[{selector}]position not change in[{param2}]seconds": [
            "元素[{selector}]位置[{param2}]秒内未变动"
        ],
        "[{selector}]slide to {param2} distance[{param3}]": [
            "[{selector}]向{param2}滑动[{param3}]",
        ],
        "[{selector}]slide to[{left},{top}]": [
            "[{selector}]滑动[{left},{top}]",
        ],
        "slide to {param1} distance[{param2}]": ["全屏向{param1}滑动[{param2}]", "向{param1}滑动[{param2}]"],
        "exist text[{selector}]": ["存在[{selector}]的文案"],
        "ocr exist text[{selector}]": ["扫描存在[{selector}]的文案"],
        "ocr regional[{selector}] exist text[{param2}]": ["扫描区域[{selector}]中存在[{param2}]的文案"],
        "ocr contain text[{selector}]": ["扫描包含[{selector}]的文案"],
        "ocr regional[{selector}] contain text[{param2}]": ["扫描区域[{selector}]中包含[{param2}]的文案"],
        "not exist text[{selector}]": ["不存在[{selector}]的文案"],
        "ocr not exist text[{selector}]": ["扫描不存在[{selector}]的文案"],
        "text[{selector}]disappear": ["文案[{selector}]消失"],
        "exist[{selector}]element": ["存在[{selector}]的元素"],
        "not exist element[{selector}]": ["不存在[{selector}]的元素"],
        "element[{selector}]disappear": ["元素[{selector}]消失"],
        "the text of element[{selector}]is[{param2}]": [
            "[{selector}]的文案为[{param2}]"
        ],
        "the text of element[{selector}]include[{param2}]": [
            "[{selector}]的文案包含[{param2}]"
        ],
        "the text of element[{selector}]not include[{param2}]": [
            "[{selector}]的文案不包含[{param2}]"
        ],
        "page rendering complete appears element[{selector}]": [
            "页面渲染完成出现元素[{selector}]"],
        "page ocr complete find text[{selector}]": [
            "页面扫描完成出现文字[{selector}]"],
        "existing element[{selector}]": ["存在元素[{selector}]"],

        "in[{p_selector}]from {param2} find[{c_selector}]element": [
            "在[{p_selector}]中向{param2}查找[{c_selector}]的元素"
        ],
        "from {param1} find[{selector}]element": [
            "向{param1}查找[{selector}]的元素"],
        "from {param1} find[{selector}]text": [
            "向{param1}扫描[{selector}]的文案"],
        "from {param1} find[{selector}]image": [
            "向{param1}查找[{selector}]的图像"],
        "move element[{selector}]to view": ["移动元素[{selector}]至可视区域"],
        "unblock the current page": ["解除当前页面限制"],
        "current page is [{param}]": ["当前页面是[{param}]"],
        "current page is not last page": ["当前页面已不是上一个指定页面"],
        "switch to target page title[{title}] url[{url}]": ["切换目标页面标题[{title}]链接[{url}]"],
        "switch to latest page": ["切换至最新打开的页面"],
        "from [{selector}] select [{param2}]": ["在[{selector}]中选择[{param2}]"],
        "exist [{p_selector}] subNode [{c_selector}] element": [
            "存在[{p_selector}]的[{c_selector}]的元素"],
        "the text of element [{p_selector}] subNode [{c_selector}] is "
        "[{param3}]": [
            "[{p_selector}]的[{c_selector}]文案为[{param3}]"
        ],
        "cache service request [{service}]": ["缓存服务请求[{service}]"],
        "remove service request cache [{service}]": ["移除请求缓存[{service}]"],
        "remove all service request caches": ["移除所有请求缓存"],
        "listening service [{service}] bind mockCase[{mock_case_id}]": [
            "监听服务[{service}]绑定MockCase[{mock_case_id}]"],
        "remove service listener [{service}]": ["移除服务监听[{service}]"],
        "remove all service listeners": ["移除所有服务监听"],
        "compare service request [{service}] with json file "
        "[{target_data_path}]": [
            "验证服务请求[{service}]与[{target_data_path}]一致",
            "验证服务请求[{service}]与json路径[{target_data_path}]一致"],
        "compare service request [{service}] with json file "
        "[{target_data_path}] with the exceptions removed": [
            "验证服务请求[{service}]与json路径[{target_data_path}]去除除外项后完全一致"],
        "compare service request [{service}] with xml file "
        "[{target_data_xml_path}]": [
            "验证服务请求[{service}]与xml路径[{target_data_xml_path}]一致"],
        "compare service non-json request [{service}] with non-json file "
        "[{target_data_path}]": [
            "验证服务非json请求[{service}]与[{target_data_path}]一致"],
        "service request [{service}] request parameter [{target_json_path}] "
        "is [{expect_value}]": [
            "验证服务[{service}]的请求参数[{target_json_path}]"
            "与[{expect_value}]一致"],
        "service request [{service}] request parameter [{target_json_path}] is none": [
            "验证服务[{service}]的请求参数[{target_json_path}]为空"],
        "service request [{service}] string request parameter [{target_json_path}] "
        "includes [{expect_value}]": [
            "验证服务[{service}]的字符串请求参数[{target_json_path}]"
            "包含[{expect_value}]"],
        "service request [{service}] string request parameter [{target_json_path}] not includes [{expect_value}]": [
            "验证服务[{service}]的字符串请求参数[{target_json_path}]"
            "不包含[{expect_value}]"],
        "page not requested [{service}]": ["页面没有请求[{service}]"],
        "page requests some interfaces [{service}]": ["页面请求了接口[{service}]"],
        "wait interface [{service}] request finished": ["等待接口[{service}]请求结束"],
        "remove all service record": ["移除所有请求记录"],
        "compare target element [{target_element}] with compared picture [{compared_picture_path}]": [
            "对比图片元素[{target_element}]和基准图片路径[{compared_picture_path}]"],
        "compare target element[{target_ele}] with compared text path of [{compared_text_path}]": [
            "对比文本元素[{target_ele}]和基准文本路径[{compared_text_path}]"],
        "call external party api of method[{method}] and url[{url}] and data[{data}] and headers[{headers}]": [
            "调外部接口并传参请求方式[{method}]与请求链接[{url}]与请求内容[{data}]与请求标头[{headers}]"],
        "open service [{service}] bind mockCase[{mock_case_id}]": [
            "开启服务[{service}]绑定MockCase[{mock_case_id}]"],
        "touch[{selector}]": ["点触[{selector}]"],
        "touch text[{selector}]": ["点触文本[{selector}]"],
        "click ele [{selector}] position[{x},{y}]": ["点击元素[{selector}]位置[{x},{y}]"],
        "open mock request service [{service}] match pathList [{path_list}] and bind mockCase[{mock_case_id}]": [
            "开启服务[{service}]匹配请求报文路径[{path_list}]并绑定MockCase[{mock_case_id}]"],
        "exist page text[{selector}]": ["页面存在文案[{selector}]"],
        "the element[{selector}]value is[{param2}]": ["元素[{selector}]的value为[{param2}]"],
        "the element[{selector}]value contains[{param2}]": ["元素[{selector}]的value包含[{param2}]"],
        "the element[{selector}]value not contains[{param2}]": ["元素[{selector}]的value不包含[{param2}]"],
        "witch contain [{param1}] element [{selector}] value is[{param2}]": ["参数含有[{param1}]的元素[{selector}]的文案为[{"
                                                                             "param2}]"],
        "witch contain [{param1}] element [{selector}] value contain [{param2}]": ["参数含有[{param1}]的元素[{"
                                                                                   "selector}]的文案包含[{param2}]"],
        "contain [{param}] by [{selector}] exist": ["存在包含参数[{param}]的元素[{selector}]"],
        "contain [{param}] by [{selector}] not exist": ["不存在包含参数[{param}]的元素[{selector}]"],
        "the [{param}] contained by the element [{selector}] has attribute [{attr_name}] with value [{attr_value}]":
            ["包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值为[{attr_value}]"],
        "the [{param}] contained by the element [{selector}] has attribute [{attr_name}] contain value [{attr_value}]":
            ["包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值包含[{attr_value}]"],
        "the [{param}] contained by the element [{selector}] has attribute [{attr_name}] not contain value [{"
        "attr_value}]":
            ["包含参数[{param}]的元素[{selector}]的属性[{attr_name}]值不包含[{attr_value}]"],
        "the [{param}] contained by the element [{selector}] element value is [{attr_value}]":
            ["包含参数[{param}]的元素[{selector}]的value为[{attr_value}]"],
        "click[{selector}] and accept dialog": ["点击[{selector}]并接受弹窗"],
        "click[{selector}] and cancel dialog": ["点击[{selector}]并取消弹窗"],
        "upload image to element[{selector}]": ["上传图片到元素[{selector}]"]
    },
}
