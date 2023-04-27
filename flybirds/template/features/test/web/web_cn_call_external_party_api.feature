  # language: zh-CN
  功能: 调外部接口

    场景:调外部post接口--翻译hello
    假如 跳转页面到[百度]
    那么 等待[3]秒
    而且 调外部接口并传参请求方式[POST]与请求链接[https://fanyi.baidu.com/sug]与请求内容[{"kw":"hello"}]与请求标头[{"Content-Type": "application/json;charset=UTF-8"}]

    场景:调外部get接口--内容
    假如 跳转页面到[百度]
    那么 等待[3]秒
    而且 调外部接口并传参请求方式[get]与请求链接[https://www.baidu.com/s]与请求内容[{"wd": "college","pn": 0}]与请求标头[{"Content-Type": "application/json"}]

    场景:调外部get接口--链接
    假如 跳转页面到[百度]
    那么 等待[3]秒
    而且 调外部接口并传参请求方式[get]与请求链接[https://www.baidu.com/s?wd=college&pn=0]与请求内容[{}]与请求标头[{}]