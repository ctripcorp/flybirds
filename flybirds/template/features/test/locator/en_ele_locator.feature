 # language: en
 Feature: Multi-platform element locator


   Scenario: Multi-platform configuration of element 01
     When go to url[locatorPage]
     And  page rendering complete appears element[元素1]
     And click[元素1]
     And wait[3]seconds
     Then screenshot

   Scenario: Multi-platform configuration of element 02
     When go to url[locatorPage]
     And  page rendering complete appears element[元素1]
     Then in[元素2]from 下 find[元素3]element


   Scenario: Multi-platform configuration of text
     When go to url[locatorPage]
     And  page rendering complete appears element[元素1]
     And  click text[文本元素1]
     And  wait[3]seconds
     Then screenshot





