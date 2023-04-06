  # language: en
  Feature: Call external party api

    Scenario: call external party api -- qmq
      When go to url[百度]
      Then wait[1]seconds
      And call external party api of method[POST] and url[http://10.4.154.152:8080/api/sendQmqByAttr] and data[{"consumeSubject":"flight.backendservice.flightchange.sendemail","appID":"100027026","consumeGroup":"100027026","subEnv":"fws","attrs":{"request":"{\"orderId\":13039628477,\"changeOrderId\":88190905,\"emailAddress\":\"zlPZte@trip.com#\",\"emailType\":\"FLTALTER_CONFIRMED_EMAIL\"}"}}] and headers[{"Content-Type": "application/json;charset=UTF-8"}]

    Scenario: call external party api -- create mirror
      When go to url[百度]
      Then wait[1]seconds
      And call external party api of method[POST] and url[http://test.reschedule.flight.fat3.qa.nt.ctripcorp.com/createMirror] and data[{"orderId": "22740918364", "mirrorName": "refundbefore"}] and headers[{"Content-Type": "application/json"}]

    Scenario: call external party api -- get with data
      When go to url[百度]
      Then wait[1]seconds
      And call external party api of method[get] and url[https://captain.release.ctripcorp.com/v1/releases/latest] and data[{"group_id": "71015015"}] and headers[{"Content-Type": "application/json"}]

    Scenario: call external party api -- get with url
      When go to url[百度]
      Then wait[1]seconds
      And call external party api of method[get] and url[https://captain.release.ctripcorp.com/v1/releases/latest?group_id=71015015] and data[{}] and headers[{}]

