 # language: en
 Feature: flybirds test feature-android click

   Scenario: test click--click position
     When start app[ctrip.android.view]
     And  click position[580,1200]
     And  wait[5]seconds
     Then screenshot
     Then close app


   Scenario: test click--click text
     When start app[ctrip.android.view]
     And page rendering complete appears element[text=机票]
     And click[text=机票]
     Then screenshot


   Scenario: test click--Click and Input
     When start app[ctrip.android.view]
     And page rendering complete appears element[text=搜索]
     And in[text=搜索]input[flybirds]
     And wait[10]seconds
     Then screenshot

