 # language: en
 Feature: Multi-platform element locator--Scenario Outline


   Scenario Outline: text contains checks
     When go to url[locatorPage]
     And  page rendering complete appears element[元素1]
     Then exist[元素2]element
     Then the text of element[<element>]include[<title>]

     Examples:
       | element | title |
       | 元素1     | 登录    |
       | 元素5     | 帮助    |
