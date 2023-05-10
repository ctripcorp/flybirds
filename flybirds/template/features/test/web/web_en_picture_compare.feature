  # language: en
  Feature: Compare picture

    Scenario: compare two pictures and input threshold
      When go to url[携程官网]
      Then compare target picture [compareData/todo.png,threshold=0.8] with compared picture [compareData/todo2.png]

    Scenario: compare two pictures without threshold
      When go to url[携程官网]
      Then compare target picture [compareData/todo.png] with compared picture [compareData/todo2.png]
