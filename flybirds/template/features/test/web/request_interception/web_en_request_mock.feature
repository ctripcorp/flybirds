  # language: en
  Feature: Listening and mocking service requests

    Scenario: Service requests Listening and mock
      Given listening service [movie] bind mockCase[4245512]
      And go to url[列表页]
      Then wait[10]seconds
      And remove service listener [movie]
      And remove all service listeners


