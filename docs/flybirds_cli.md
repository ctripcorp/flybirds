# Flybirds CLI



## **Flybirds  CLI**

**Flybirds  CLI** is a command line application to run simple programs created with **Flybirds**, with completion in your terminal 🚀.

You use **Flybirds  CLI** in your terminal, to run your scripts. Like in:

```bash
flybirds run
```



## Usage

### Install

To use **Flybirds  CLI**, you need to install **flybirds** first.

```bash
pip install flybirds
---> 100%
Successfully installed flybirds
```

That creates a `flybirds` command you can call in your terminal, much like `python`, `git`, or `echo`.

```bash
flybirds --help
Usage: flybirds [OPTIONS] COMMAND [ARGS]...

  Welcome to flybirds. Type "--help" for more information.

```



### **Commands**

------

You can specify one of the following **CLI commands**:

- `create`:  Generate project example.

- `run`: Run the project.




#### **Options**

You can enter the following at the terminal to see what **Flybirds** supports when running your project.
```bash
flybirds run --help
```

- **--path, -P    TEXT(Optional)**

​	Specify the feature set to be executed, which can be a directory or a specific feature file. The default is the ‘**features**’ directory.

​	For example:

```bash
flybirds run --path ./features/test/demo.feature
```
- **--tag, -T    TEXT(Optional)**

​	Run scenes with a specific tag, separated by commas. The beginning of ‘-’ means that the scene containing this tag will not be run.

​	For example:

```bash
flybirds run -T tag1,tag2,-tag3,tag4
```
- **--format, -F    TEXT(Optional)**

  Specify the format for generating test results, the default is json.
  

​		For example:

```bash
#default 
flybirds run --format=json
```

-   **--report, -R   TEXT(Optional)**

​	Specify the directory for generating the report. If not specified, it will be a randomly generated file in the report directory.

​	For example:

```bash
#mac Custom report address
flybirds run --report report/curent/report.json

#windows Custom report address
flybirds run --report report\curent\report.json
```

- **--define, -D   TEXT(Optional)**

​	Pass in user-defined parameters, this parameter has two functions:

Function 1: Override the value of the corresponding configuration item in the  **`config`** file, such as:

```bash 
# switch execution platform by parameter: Android, iOS, Web
flybirds run --define platform=web 

# specify the browser to be launched by the web execution platform with parameters (single)
flybirds run -D browserType=webkit

# Specify the browser to be launched by the web execution platform with parameters (Separate multiple browsers with half-angle comma)
flybirds run -D browserType=webkit,firefox
```

Function 2: Pass in custom parameters for use in custom scripts in the **`pscript`** directory. Use the global parameter **`global_resource`** to get it.

- **--rerun  /--no-rerun (Optional)**

​	Specify whether the failed scene needs to be re-run, the default is ‘True’, it will automatically re-run after failure.

For example:

```bash
#Don't rerun the failure scene
flybirds run --no-rerun 
```

- **--html/--no-html  (Optional)**

​	Specify whether to generate html test result report after case execution。The default is 'True', the result test report will be generated automatically after execution.

For example:

```bash
# Don't generat test reports 
flybirds run --no-html
```

- **--processes, -p    INTEGER(Optional)**

  Specifies the maximum number of processes to be opened for parallel execution. The default is 4 .

  **Note:**  This command is only valid when executed on the **web** platform.

For example:

```bash
flybirds run --path features -p 5
```


