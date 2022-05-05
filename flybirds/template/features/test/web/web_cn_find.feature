  # language: zh-CN
  功能: web查找元素


    场景: 在全屏查找
    假如 跳转页面到[百度]
    而且 页面渲染完成出现元素[text=新闻]
    那么 向下查找[text=关于百度]的元素


    场景: 在父元素中查找子元素
    假如 跳转页面到[百度]
    那么 存在[#hotsearch-content-wrapper]的[li.hotsearch-item.odd[data-index="2"]]的元素
    那么 [.s-bottom-layer-content]的[text=帮助中心]文案为[帮助中心]