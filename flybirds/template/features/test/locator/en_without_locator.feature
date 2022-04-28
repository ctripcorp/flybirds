 # language: en
 Feature: Not using element locator configuration


   Scenario: Use the Numbers
     When go to url[locatorPage]
     And click position[720,400]
     And wait[3]seconds
     Then screenshot


   Scenario: Use the text string
     When go to url[locatorPage]
     And wait[10]seconds
     Then exist text[flybirds test]


   Scenario:  Use the element selector
     When go to url[locatorPage]
     And wait[10]seconds
     Then not exist element[text=测试]

