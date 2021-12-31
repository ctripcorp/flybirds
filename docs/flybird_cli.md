# Flybird CLI



## **Flybird  CLI**

**Flybird  CLI** is a command line application to run simple programs created with **Flybird**, with completion in your terminal 🚀.

You use **Flybird  CLI** in your terminal, to run your scripts. Like in:

```bash
flybird run
```



## Usage

### Install

To use **Flybird  CLI**, you need to install **flybird** first.

```bash
pip install flybird
---> 100%
Successfully installed flybird
```

That creates a `flybird` command you can call in your terminal, much like `python`, `git`, or `echo`.

```bash
flybird --help
Usage: flybird [OPTIONS] COMMAND [ARGS]...

  Welcome to flybird. Type "--help" for more information.

```



### **Commands**

------

You can specify one of the following **CLI commands**:

- `create`:  Generate project example.

- `run`: Run the project.


  

#### **Options**

You can enter the following at the terminal to see what **Flybird** supports when running your project.
```bash
flybird run --help
```

- **--path, -P    TEXT(Optional)**

​	Specify the feature set to be executed, which can be a directory or a specific feature file. The default is the ‘**features**’ directory.

​	For example:

```bash
flybird run -P ./features/test/demo.feature
```
- **--tag, -T    TEXT(Optional)**

​	Run scenes with a specific tag, separated by commas. The beginning of ‘-’ means that the scene containing this tag will not be run.

​	For example:

```bash
flybird run -T tag1,tag2,-tag3,tag4
```
- **--format, -F    TEXT(Optional)**

  Specify the format for generating test results, the default is json.
  

​		For example:

```bash
#default 
flyird run --format=json
```

-   **--report, -R   TEXT(Optional)**

​	Specify the directory for generating the report. If not specified, it will be a randomly generated file in the report directory.

​	For example:

```bash
#mac Custom report address
flybird run --report report/curent/report.json

#windows Custom report address
flybird run --report report\curent\report.json
```

- **--define, -D   TEXT(Optional)**

​	Pass in user-defined parameters, this parameter has two functions:

Function 1: Overwrite the configuration in the **`config`** file, such as:

```bash 
 # The device and uniqueTag used at runtime are the values specified in the command, and the values configured in the configuration file will not be read
 
flybird run --define deviceId=*** --define uniqueTag=***
```

Function 2: Pass in custom parameters for use in custom scripts in the **`pscript`** directory. Use the global parameter **`global_resource`** to get it.

- **--rerun  /--no-rerun (Optional)**

​	Specify whether the failed scene needs to be re-run, the default is ‘True’, it will automatically re-run after failure.

For example:

```bash
#Don't rerun the failure scene
flybird run --no-rerun 
```





