  # language: en
  Feature: Compare picture

    Scenario: compare two pictures and input threshold
      When go to url[百度]
      Then compare target element [#lg,threshold=0.8] with compared picture [compareData/todo.png]

    Scenario: compare two pictures and input threshold
      When go to url[百度]
      Then compare target element [#lg] with compared picture [compareData/todo.png]

