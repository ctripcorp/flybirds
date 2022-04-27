 # language: en
 Feature: flybirds test feature-android swipe

   Scenario: test swipe--Element swipe
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=租车]
     And  [text=租车]slide to up distance[600]
     And  wait[5]seconds
     Then element[text=租车]position not change in[5]seconds
     Then existing element[text=搜索]
     Then exist text[搜索]


   Scenario: test swipe--Full screen swipe
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=租车]
     And slide to up distance[600, readyTime=3, duration=2]
     Then not exist element[text=机票]
     Then not exist text[升级攻略]
     Then element[text=机票]disappear
     Then text[机票]disappear
