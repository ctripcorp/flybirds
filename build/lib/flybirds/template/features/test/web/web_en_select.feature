 # language: en
 Feature: select


   Scenario: select option
     When go to url[携程]
     And  from [#J_roomCountList] select [6间]
     And  wait[5]seconds
     Then stop record

