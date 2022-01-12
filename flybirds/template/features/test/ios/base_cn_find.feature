  # language: zh-CN
 功能: flybirds功能测试-ios find element

   场景: 验证元素操作--在页面中查找
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 在[ScrollView]中向下查找[label=租车]的元素


   场景: 验证元素操作--在全屏查找
     当  启动APP[com.ctrip.inner.wireless]
     而且 页面渲染完成出现元素[label=机票]
     那么 向下查找[label=租车]的元素