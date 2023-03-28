 # language: en
 Feature: Input Operation


   Scenario: input
     When go to url[百度]
     And in[#kw]input[flybirds]
     And wait[3]seconds
     Then screenshot


   Scenario: clear and input
     When go to url[百度]
     And in[#kw]input[flybirds]
     And wait[3]seconds
     Then clear [#kw] and input[input test]
     Then screenshot

   Scenario: input
     When go to url[百度]
     And execute js[compareData/testCase.js]
     And wait[3]seconds
     Then screenshot

   Scenario: input
     When go to url[百度]
     And execute js[compareData/testCase.js,casename=RefundApply,tag=Refund]
     And wait[3]seconds
     Then screenshot

   Scenario: input
     When go to url[百度]
     And execute js[compareData/testCase.js,casename=RefundApply,tag=Refund,priority=P1]
     And wait[3]seconds
     Then screenshot