 # language: en
 Feature: flybirds test feature-android find element

  Scenario: test element operation--find in page
    When start app[com.ctrip.inner.wireless]
    And  page rendering complete appears element[label=机票]
    Then in[ScrollView]from down find[label=租车]element


   Scenario: test element operation--find in full screen
    When start app[com.ctrip.inner.wireless]
    And  page rendering complete appears element[label=机票]
    Then from down find[label=租车]element