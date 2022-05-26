  # language: zh-CN
  功能: 验证比较服务请求


    场景: json类型服务请求比对
    假如 缓存服务请求[getRecommendHotelList]
    而且 跳转页面到[携程官网]
    那么 等待[5]秒
    而且 验证服务[getRecommendHotelList]的请求参数[head.syscode]与[PC]一致
    而且 验证服务[getRecommendHotelList]的请求参数[$.cityId]与[2]一致
    而且 验证服务[getRecommendHotelList]的请求参数[cityId]与[2]一致
    而且 验证服务请求[getRecommendHotelList]与[compareData/getRecommendHotelList.json]一致


    场景: 非json类型服务请求比对
    假如 缓存服务请求[writecookie]
    而且 跳转到[携程官网]
    那么 等待[5]秒
    而且 验证服务非json请求[writecookie]与[compareData/writecookie.txt]一致
