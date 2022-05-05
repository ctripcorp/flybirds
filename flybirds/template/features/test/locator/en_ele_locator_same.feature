 # language: en
 Feature: Element locators are the same


   Scenario: element text is the same
     When go to url[locatorPage]
     And  page rendering complete appears element[元素5]
     Then exist[元素5]element
