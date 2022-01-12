 # language: en
 Feature: flybirds test feature-android find element

  Scenario: test element operation--find in page
    When start app[ctrip.android.view]
    And  page rendering complete appears element[text=机票]
    Then in[android.widget.LinearLayout]from down find[text=租车]element


   Scenario: test element operation--find in full screen
    When start app[ctrip.android.view]
    And  page rendering complete appears element[text=机票]
    Then from down find[text=租车]element