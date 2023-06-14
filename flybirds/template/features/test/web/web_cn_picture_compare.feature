  # language: zh-CN
  功能: 对比图片


    场景: 对比图片指定相似度
    假如 跳转页面到[百度]
    那么 对比图片元素[//*[@id="lg"]/map/area,threshold=0.8]和基准图片[compareData/todo.png]


    场景: 对比图片无相似度
    假如 跳转页面到[百度]
    那么 对比图片元素[//*[@id="lg"]/map/area]和基准图片[compareData/todo.png]

