  # language: en
  Feature: Listening and mocking service requests

    Scenario: Service requests Listening and mock
      Given listening service [movie] bind mockCase[4245512]
#      Given listening service [movie,xxx] bind mockCase[4245512,xxxxxxx]
      And go to url[列表页]
      Then wait[10]seconds
      And remove service listener [movie]
#      And remove service listener [movie,xxx]
      And remove all service listeners


