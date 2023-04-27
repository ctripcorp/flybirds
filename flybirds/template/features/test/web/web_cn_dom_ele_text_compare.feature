  # language: zh-CN
  功能: 对比DOM元素文本

    场景:对比DOM元素文本--元素属性
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 对比目标元素的链接[https://www.baidu.com/]与属性[{"name": "input", "attrs": {"class": "s_ipt"}}]和比较元素的链接[https://www.baidu.com/]与属性[{"attrs": {"name": "wd"}}]

    场景:对比DOM元素文本--文本内容
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 对比目标元素的链接[https://www.baidu.com/]与文本内容[{"text": "About Baidu"}]和比较元素的链接[https://www.baidu.com/]与文本匹配内容[{"text": "About Bai\\w+"},regexp=True]
