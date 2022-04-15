## 依赖包列表

- pocoui>=1.0.85

- airtest>=1.2.3

- setuptools~=47.1.0

- behave==1.2.6

- jsonpath==0.82

- typer==0.4.0

- tidevice==0.5.9

- pyasn1==0.4.8

- pyOpenSSL==19.1.0

- playwright>=1.19.0

  

## 安装浏览器

每个版本的Playwright都需要特定版本的浏览器二进制文件来运行。当你在web端进行UI 自动测试时, 需要使用 **[Playwright CLI](https://playwright.dev/python/docs/cli)** 来安装这些浏览器。

```bash
# 不带参数的运行将安装默认所有浏览器
playwright install
```

```bash
# 通过提供一个参数来安装特定的浏览器
playwright install webkit
```

```bash
# 查看支持安装的浏览器
playwright install --help
```


