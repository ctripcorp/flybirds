  # language: zh-CN
 功能: flybirds功能测试-android find element

  场景: 验证元素操作--在页面中查找
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 在[android.widget.LinearLayout]中向下查找[text=机票]的元素


   场景: 验证元素操作--在全屏查找
     当  启动APP[ctrip.android.view]
     而且 页面渲染完成出现元素[text=机票]
     那么 向下查找[text=租车]的元素