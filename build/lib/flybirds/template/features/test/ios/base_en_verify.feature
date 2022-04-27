 # language: en
 Feature: flybirds test feature-android verify element

   Scenario: Element Step Test verify text
     When start app[com.ctrip.inner.wireless]
     And  page rendering complete appears element[label=机票]
     Then the text of element[label=机票]is[机票]
     Then the text of element[label=机票]include[机]


   Scenario: Element Step Test verify property
     When start app[com.ctrip.inner.wireless]
     And  page rendering complete appears element[label=机票]
     Then element[label=机票]property[label]is 机票
