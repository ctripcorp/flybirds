 # language: en
 Feature: web find element


   Scenario: Find in full screen
     When go to url[百度]
     And  page rendering complete appears element[text=新闻]
     Then from down find[text=关于百度]element


   Scenario: Find child elements in parent elements
     When go to url[百度]
     Then exist [#hotsearch-content-wrapper] subNode [li.hotsearch-item.odd[data-index="2"]] element
     Then the text of element [.s-bottom-layer-content] subNode [text=帮助中心] is [帮助中心]