# Flybirds  升级指南



从 v0.2.3 开始，`flyrirds` 提供了关于web的一些新特性，并根据这些特性对项目做了调整。这些主要是对现有 API 的添加和改进。



## 使用 CLI

强烈建议对 Flybirds 项目使用官方 CLI。除了开发和部署工具之外，它还升级和安装了新的依赖项，并且修改了项目结构。

现在可以升级 `flybirds-cli` 并运行 `flybirds create` 来创建 Flybirds  项目。



### 依赖

安装插件会将依赖包 `playwright`升级到下一个主版本。另外，名为 `jsonpath_ng`  和  `deepdiff` 的新包会出现在开发依赖项中。它们将在文件比对时发挥作用。



### 项目修改

来看看项目中发生了什么变化。首先要注意的是项目中新增了一些目录。

- **compareData**：用于存放服务请求比对时的文件。
- **interfaceIgnoreConfig** ：用于存放服务请求比对时配置的忽略节点文件。
- **mockCaseData**：被监听的服务请求可绑定的Mock数据会存放在这里。



**值得注意的是**，`pscript` 目录下的 `app` 将被  `custom_handle` 取代。`custom_handle` 加入了一些 `web` 方面的扩展函数。



## 不用 CLI

不用 CLI，就必须手动将 `playwright` 升级到下一个主要版本（如果你想使用最新版本的话），并添加 `jsonpath_ng`   包 和  `deepdiff` 包 。没有什么好的方法，必须手动完成所有的事情，并且还必须手动进行项目结构修改。

