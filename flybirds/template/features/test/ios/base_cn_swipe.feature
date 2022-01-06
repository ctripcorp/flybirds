  # language: zh-CN
 功能: flybirds功能测试-ios swipe

   场景: 验证滑动--元素滑动
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=租车]
     而且 [label=租车]向上滑动[600]
     而且 等待[5]秒
     那么 元素[label=租车]位置[5]秒内未变动
     那么 存在元素[label=租车]
     那么 存在[租车]的元素


   场景: 验证滑动--全屏滑动
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=租车]
     而且 全屏向上滑动[600, readyTime=3, duration=2]
     那么 不存在[label=机票]的元素
     那么 不存在[升级攻略]的文案
     那么 元素[label=机票]消失
     那么 文案[搜索]消失
