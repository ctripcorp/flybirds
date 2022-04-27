 # language: en
 Feature: web swipe

   Scenario: element swipe
     When go to url[列表页]
     And  wait[2]seconds
     And  [text=霸王别姬 - Farewell My Concubine]slide to down distance[600]
     And  wait[5]seconds
     Then existing element[text=肖申克的救赎 - The Shawshank Redemption]
     Then exist text[肖申克的救赎 - The Shawshank Redemption]


   Scenario: full screen swipe
     When go to url[列表页]
     And  wait[2]seconds
     And slide to down distance[600]
     And  wait[5]seconds
     Then not exist element[text=测试]
     Then not exist text[测试]