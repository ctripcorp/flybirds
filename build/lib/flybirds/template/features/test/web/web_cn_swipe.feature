  # language: zh-CN
  功能: web滑动

    场景: 滑动
    假如 跳转页面到[列表页]
    而且 等待[2]秒
    而且 [text=霸王别姬 - Farewell My Concubine]向下滑动[600]
    而且 等待[5]秒
    那么 存在元素[text=肖申克的救赎 - The Shawshank Redemption]
    那么 存在[肖申克的救赎 - The Shawshank Redemption]的文案


    场景:全屏滑动
    假如 跳转页面到[列表页]
    而且 等待[2]秒
    而且 全屏向下滑动[600]
    而且 等待[5]秒
    那么 不存在[text=测试]的元素
    那么 不存在[测试]的文案
