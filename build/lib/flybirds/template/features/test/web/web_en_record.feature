 # language: en
 Feature: web record

   Scenario: web record
     When go to url[百度]
     And  page rendering complete appears element[text=新闻]
     And  click[#s-top-loginbtn]
     And  wait[10]seconds
     Then stop record


