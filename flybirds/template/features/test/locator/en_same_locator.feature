 # language: en
 Feature: Element locators are the same


   Scenario: text is the same
     When go to url[memberPage]
     And  page rendering complete appears element[元素4]
     And  in[元素4]input[文案2]
     And  wait[5]seconds
     Then screenshot
