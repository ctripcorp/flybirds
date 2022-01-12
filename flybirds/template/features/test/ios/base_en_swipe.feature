 # language: en
 Feature: flybirds test feature-android swipe

   Scenario: test swipe--Element swipe
     When start app[com.ctrip.inner.wireless]
     And  page rendering complete appears element[label=租车]
     And  [label=租车]slide to up distance[600]
     And  wait[5]seconds
     Then element[label=租车]position not change in[5]seconds
     Then existing element[label=租车]
     Then exist[租车]element


   Scenario: test swipe--Full screen swipe
     When start app[com.ctrip.inner.wireless]
     And  page rendering complete appears element[label=租车]
     And slide to up distance[600, readyTime=3, duration=2]
     Then not exist element[label=机票]
     Then not exist text[升级攻略]
     Then element[label=机票]disappear
     Then text[搜索]disappear
