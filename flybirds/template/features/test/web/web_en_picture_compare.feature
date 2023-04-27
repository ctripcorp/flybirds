  # language: en
  Feature: Validate and compare service requests

    Scenario: json type service request comparison
      When go to url[携程官网]
      Then compare target picture [compareData/todo.png,threshold=0.8] with compared picture [compareData/todo2.png]

    Scenario: json type service request comparison
      When go to url[携程官网]
      Then compare target picture [compareData/todo.png] with compared picture [compareData/todo2.png]
