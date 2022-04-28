  # language: zh-CN
  功能: 不使用元素定位配置


    场景: 使用数字
    假如 跳转页面到[locatorPage]
    而且 点击屏幕位置[720,400]
    而且 等待[3]秒
    那么 全屏截图


    场景: 使用文案
    当 跳转到[locatorPage]
    而且 等待[10]秒
    那么 存在[flybirds test]的文案


    场景: 使用元素选择器
    当 跳转到[locatorPage]
    而且 等待[10]秒
    那么 不存在[text=测试]的元素

