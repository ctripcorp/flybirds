  # language: zh-CN
  功能: 页面操作


    场景: 设置浏览器尺寸
    假如 跳转页面到[百度]
    那么 设置浏览器高度[1280]和宽度[760]


    场景: 返回上一页
    假如 跳转页面到[百度]
    而且 点击[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
    而且 等待[2]秒
    那么 切换目标页面标题[百度一下，你就知道]链接[https://www.baidu.com]


    场景: 返回上一页
    假如 跳转页面到[百度]
    而且 点击[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
    而且 等待[2]秒
    那么 切换目标页面标题[百度一下，你就知道]链接[ ]


    场景: 返回上一页
    假如 跳转页面到[百度]
    而且 点击[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
    而且 等待[2]秒
    那么 切换目标页面标题[ ]链接[https://www.baidu.com]


    场景: 返回上一页
    假如 跳转页面到[列表页]
    而且 页面渲染完成出现元素[text=霸王别姬 - Farewell My Concubine]
    而且 点击[text=霸王别姬 - Farewell My Concubine]
    而且 等待[3]秒
    而且 返回上一页
    而且 等待[2]秒
    那么 结束录屏


    场景: 判断当前页面
    假如 跳转页面到[列表页]
    而且 页面渲染完成出现元素[text=霸王别姬 - Farewell My Concubine]
    而且 点击[text=霸王别姬 - Farewell My Concubine]
    而且 等待[3]秒
    那么 当前页面是[列表详情页]
#    而且 当前页面是[https://spa6.scrape.center/detail/ZWYzNCN0ZXVxMGJ0dWEjKC01N3cxcTVvNS0takA5OHh5Z2ltbHlmeHMqLSFpLTAtbWIx]



