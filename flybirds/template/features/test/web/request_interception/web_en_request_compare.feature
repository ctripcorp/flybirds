  # language: en
  Feature: Validate and compare service requests


    Scenario: json type service request comparison
      Given cache service request [getRecommendHotelList]
      And go to url[携程官网]
      Then wait[5]seconds
      And  service request [getRecommendHotelList] request parameter [head.syscode] is [PC]
      And  service request [getRecommendHotelList] request parameter [$.cityId] is [2]
      And  service request [getRecommendHotelList] request parameter [cityId] is [2]
      And compare service request [getRecommendHotelList] with json file [compareData/getRecommendHotelList.json]


    Scenario: Non-json type service request comparison
      Given cache service request [writecookie]
      And go to url[携程官网]
      Then wait[5]seconds
      And compare service non-json request [writecookie] with non-json file [compareData/writecookie.txt]
