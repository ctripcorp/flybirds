  # language: zh-CN
 功能:  flybirds功能测试-ios device record

   场景: 验证设备录屏--录屏
     当  启动APP[ctrip.com]
     而且 页面渲染完成出现元素[label=机票]
     而且 开始录屏
     而且 点击[label=机票]
     而且 等待[10]秒
     那么 结束录屏
     那么 关闭App


   场景:验证设备录屏--录屏超时
     当  启动APP[ctrip.com]
     而且 页面渲染完成出现元素[label=机票]
     而且  开始录屏超时[50]
     而且  点击[label=机票]
     而且  等待[10]秒
     那么 结束录屏
     那么 关闭App

