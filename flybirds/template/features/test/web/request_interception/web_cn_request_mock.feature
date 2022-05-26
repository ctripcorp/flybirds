  # language: zh-CN
  功能: 监听并mock服务请求


    场景: 服务监听与mock
    假如 监听服务[movie]绑定MockCase[4245512]
#    假如 监听服务[movie,xxx]绑定MockCase[4245512,xxxxxxx]
    当   跳转页面到[列表页]
    那么 等待[10]秒
    而且 移除服务监听[movie]
#    而且 移除服务监听[movie,xxx]
    而且 移除所有服务监听


