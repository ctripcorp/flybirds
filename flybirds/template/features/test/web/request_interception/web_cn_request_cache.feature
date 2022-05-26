  # language: zh-CN
  功能: 缓存服务请求


    场景:验证缓存服务请求
    假如 缓存服务请求[getRecommendHotelList]
    假如 缓存服务请求[writecookie]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 移除请求缓存[getRecommendHotelList]
#    而且 移除请求缓存[writecookie]
    而且 移除所有请求缓存


    场景:验证缓存服务请求--同时传入多个参数
    假如 缓存服务请求[getRecommendHotelList,writecookie]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 移除请求缓存[getRecommendHotelList,writecookie]

