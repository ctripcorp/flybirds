  # language: zh-CN
 功能: flybirds功能测试-android ocr


   场景: 验证扫描文字
     当   启动APP[ctrip.android.view]
     那么 页面扫描完成出现文字[机票]
     那么 扫描存在[酒店]的文案
     那么 扫描存在[旅游]的文案
     那么 扫描不存在[机票机票]的文案


   场景: 验证点击扫描文字
     当   启动APP[ctrip.android.view]
     那么 页面扫描完成出现文字[机票]
     那么 点击扫描文案[机票]
     而且 等待[1]秒
     那么 页面扫描完成出现文字[阿克苏]
     那么 点击扫描文案[阿克苏]
     而且 等待[1]秒
     而且 全屏向上滑动[300]
     那么 页面扫描完成出现文字[阿克苏]
     那么 点击扫描文案[阿克苏]
     那么 全屏截图

   场景: 验证输入
     当   启动APP[ctrip.android.view]
     那么 页面扫描完成出现文字[目的地/酒店/景点/关键字/航班号]
     那么 在扫描文字[目的地/酒店/景点/关键字/航班号]中输入[上海]
     那么 全屏截图


