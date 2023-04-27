  # language: en
  Feature: Call external party api

    Scenario: call external post party api -- translate hello
      When go to url[百度]
      Then wait[3]seconds
      And call external party api of method[POST] and url[https://fanyi.baidu.com/sug] and data[{"kw":"hello"}] and headers[{"Content-Type": "application/json;charset=UTF-8"}]

    Scenario: call external get party api -- get with data
      When go to url[百度]
      Then wait[3]seconds
      And call external party api of method[get] and url[https://www.baidu.com/s] and data[{"wd": "college","pn": 0}] and headers[{"Content-Type": "application/json"}]

    Scenario: call external get party api -- get with url
      When go to url[百度]
      Then wait[3]seconds
      And call external party api of method[get] and url[https://www.baidu.com/s?wd=college&pn=0] and data[{}] and headers[{}]


