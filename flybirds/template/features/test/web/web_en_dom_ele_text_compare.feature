  # language: en
  Feature: Compare dom element

    Scenario: compare text of two dom element text by Attrs
      When go to url[百度]
      Then wait[5]seconds
      And compare target element of target url[https://www.baidu.com/] in target element [{"name": "input", "attrs": {"class": "s_ipt"}}] with compared element of compared url[https://www.baidu.com/] in compared element [{"attrs": {"name": "wd"}}]


    Scenario: compare text of two dom element text by text value
      When go to url[百度]
      Then wait[5]seconds
      And compare target element of target url[https://www.baidu.com/] in target element [{"text": "About Baidu"}] with compared element of compared url[https://www.baidu.com/] in compared element [{"text": "About Bai\\w+"},regexp=True]
