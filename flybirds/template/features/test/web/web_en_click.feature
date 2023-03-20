 # language: en
 Feature: web click

   Scenario: click element
     When go to url[百度]
     And click[#s-top-loginbtn]
     And wait[3]seconds
     Then screenshot

   Scenario: click element
     When go to url[百度,timeout=5]
     And click[#s-top-loginbtn]
     And wait[3]seconds
     Then screenshot


   Scenario: click text
     When go to url[百度]
     And click text[新闻]
     And wait[3]seconds
     Then screenshot


   Scenario: click position
     When go to url[百度]
     And  click position[720,400]
     And  wait[3]seconds
     Then screenshot
