 # language: en
 Feature: Page Operation


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
