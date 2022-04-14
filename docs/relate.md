## requirements list

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



## Install browsers

Each version of Playwright needs specific versions of browser binaries to operate.  When you perform UI automation testing on the web platform, you need to use the **[Playwright CLI](https://playwright.dev/python/docs/cli)** to install these browsers.

Playwright can install supported browsers.

```bash
# Running without arguments will install default browsers
playwright install
```

You can also install specific browsers by providing an argument:

```bash
# Install WebKit
playwright install webkit
```



