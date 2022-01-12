 # language: en
 Feature: flybirds test feature-ios click

   Scenario: test click--click position
     When start app[com.ctrip.inner.wireless]
     And  click position[580,1200]
     And  wait[5]seconds
     Then screenshot
     Then close app


   Scenario: test click--click text
     When start app[com.ctrip.inner.wireless]
     And page rendering complete appears element[label=机票]
     And click[label=机票]
     Then screenshot


   Scenario: test click--Click and Input
     When start app[com.ctrip.inner.wireless]
     And page rendering complete appears element[label=搜索]
     And in[label=搜索]input[flybirds]
     And wait[10]seconds
     Then screenshot

