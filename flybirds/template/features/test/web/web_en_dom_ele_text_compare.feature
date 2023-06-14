  # language: en
  Feature: Compare dom element

    Scenario: compare text of two dom element text by text value
      When go to url[百度]
      Then wait[5]seconds
      And compare target element[#lg] with compared text path of [compareData/todu.txt]
