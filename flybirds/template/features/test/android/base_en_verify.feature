 # language: en
 Feature: flybirds test feature-android verify element

   Scenario: Element Step Test verify text
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=机票]
     Then the text of element[text=机票]is[机票]
     Then the text of element[text=机票]include[机]


   Scenario: Element Step Test verify property
     When start app[ctrip.android.view]
     And  page rendering complete appears element[text=机票]
     Then element[text=机票]property[text]is 机票
