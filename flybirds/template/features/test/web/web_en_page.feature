 # language: en
 Feature: Page Operation


   Scenario: Set web page's size
     When go to url[百度]
     Then set web page with width[1280] and height[760]


   Scenario: Return to previous page
     When go to url[百度]
     And  click[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
     And  wait[2]seconds
     Then switch to target page title[百度一下，你就知道] url[https://www.baidu.com]


   Scenario: Return to previous page
     When go to url[百度]
     And  click[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
     And  wait[2]seconds
     Then switch to target page title[百度一下，你就知道] url[ ]


   Scenario: Return to previous page
     When go to url[百度]
     And  click[//*[@id="hotsearch-content-wrapper"]/li[1]/a/span[2]]
     And  wait[2]seconds
     Then switch to target page title[ ] url[https://www.baidu.com]

   Scenario: Return to previous page
     When go to url[列表页]
     And  page rendering complete appears element[text=霸王别姬 - Farewell My Concubine]
     And  click[text=霸王别姬 - Farewell My Concubine]
     And  wait[3]seconds
     And  return to previous page
     And  wait[2]seconds
     Then stop record


   Scenario: Determine the current page
     When go to url[列表页]
     And  page rendering complete appears element[text=霸王别姬 - Farewell My Concubine]
     And  click[text=霸王别姬 - Farewell My Concubine]
     And  wait[3]seconds
     Then  current page is [列表详情页]
