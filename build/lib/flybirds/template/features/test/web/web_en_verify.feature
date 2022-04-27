 # language: en
 Feature: web element attribute verify

   Scenario: verify element text
     When go to url[百度]
     Then the text of element[text=新闻]is[新闻]
     Then the text of element[text=新闻]include[新]


   Scenario: verify element attributes
     When go to url[百度]
     Then element[#kw]property[name]is wd
     Then element[#su]property[value]is 百度一下
