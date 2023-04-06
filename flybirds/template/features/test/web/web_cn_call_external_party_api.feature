  # language: zh-CN
  功能: 调外部接口

    场景:调外部接口--发送qmq
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 调外部接口并传参请求方式[POST]与请求链接[http://10.4.154.152:8080/api/sendQmqByAttr]与请求内容[{"consumeSubject":"flight.backendservice.flightchange.sendemail","appID":"100027026","consumeGroup":"100027026","subEnv":"fws","attrs":{"request":"{\"orderId\":13039628477,\"changeOrderId\":88190905,\"emailAddress\":\"zlPZte@trip.com#\",\"emailType\":\"FLTALTER_CONFIRMED_EMAIL\"}"}}]与请求标头[{"Content-Type": "application/json;charset=UTF-8"}]

    场景:调外部接口--镜像接口
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 调外部接口并传参请求方式[POST]与请求链接[http://test.reschedule.flight.fat3.qa.nt.ctripcorp.com/createMirror]与请求内容[{"orderId": "22740918364", "mirrorName": "refundbefore"}]与请求标头[{"Content-Type": "application/json"}]

    场景:调外部接口--内容
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 调外部接口并传参请求方式[get]与请求链接[https://captain.release.ctripcorp.com/v1/releases/latest]与请求内容[{"group_id": "71015015"}]与请求标头[{"Content-Type": "application/json"}]

    场景:调外部接口--链接
    假如 跳转页面到[百度]
    那么 等待[5]秒
    而且 调外部接口并传参请求方式[get]与请求链接[https://captain.release.ctripcorp.com/v1/releases/latest?group_id=71015015]与请求内容[{}]与请求标头[{}]
