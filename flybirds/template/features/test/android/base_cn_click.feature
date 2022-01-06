  # language: zh-CN
 功能: flybirds功能测试-android click

   场景: 验证点击--点击屏幕位置
     当   启动APP[ctrip.android.view]
     而且 点击屏幕位置[580,1200]
     而且 等待[5]秒
     那么 全屏截图
     那么 关闭App


   场景: 验证点击--点击元素
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     而且 点击[text=机票]
     那么 全屏截图


   场景: 验证点击--点击并输入
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=搜索]
     而且 在[text=搜索]中输入[flybirds]
     而且 等待[10]秒
     那么 全屏截图

