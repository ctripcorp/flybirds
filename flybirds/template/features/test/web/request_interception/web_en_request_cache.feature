 # language: en
 Feature: cache service requests


   Scenario: Verify cached service requests
     Given cache service request [getRecommendHotelList]
     Given cache service request [writecookie]
     And go to url[携程官网]
     Then wait[5]seconds
     And remove service request cache [getRecommendHotelList]
#     And remove service request cache [writecookie]
     And remove all service request caches


   Scenario: Verify cached service requests--pass in multiple parameters
     Given cache service request [getRecommendHotelList,writecookie]
     And go to url[携程官网]
     Then wait[5]seconds
     And remove service request cache [getRecommendHotelList,writecookie]

