 # language: en
 Feature: Hover Operation

   Scenario: hover
     When go to url[百度]
     And  wait[3]seconds
     And  mouse hover[.soutu-btn]
     And  wait[2]seconds
     And  page rendering complete appears element[text=按图片搜索]