 # language: en
 Feature: flybirds test feature-android device record

   Scenario: Test Device Record--record
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=机票]
     And  start record
     And  click[text=机票]
     And  wait[10]seconds
     Then stop record
     Then close app


   Scenario:Test Device Record--Recording Timeout
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=机票]
     And  start recording timeout[50]
     And  click text[机票]
     And  wait[10]seconds
     Then stop record
     Then close app

