  # language: zh-CN
 功能: flybirds功能测试-ios verify element

   场景: 验证元素--元素文案
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 [label=机票]的文案为[机票]
     那么 [label=机票]的文案包含[机]


   场景: 验证元素--元素属性
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 元素[label=机票]的属性[label]为机票
