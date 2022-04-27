# find [![Status](https://travis-ci.org/yuanchuan/find.svg?branch=master)](https://travis-ci.org/yuanchuan/find "See test builds")

Find files or directories by name.

[![NPM](https://nodei.co/npm/find.png?downloads=true&downloadRank=true&stars=true)](https://nodei.co/npm/find/)

## Installation

```bash
$ npm install --save find
```

## Examples

Find all files in current directory.

```javascript
var find = require('find');

find.file(__dirname, function(files) {
  console.log(files.length);
})
```

Filter by regular expression.

```javascript
find.file(/\.js$/, __dirname, function(files) {
  console.log(files.length);
})
```

## Features
  * Recursively search each sub-directories
  * Asynchronously or synchronously
  * Filtering by regular expression or string comparing

## Changelog
#### 0.3.0
  * Added `.use()` method

#### 0.2.0
  * The first `pattern` option is now optional
  * Will follow symbolic links


## API

#### .file([pattern,] root, callback)

```javascript
find.file(__dirname, function(files) {
  //
})
```

#### .dir([pattern,] root, callback)
```javascript
find.dir(__dirname, function(dirs) {
  //
})
```


#### .eachfile([pattern,] root, action)

```javascript
find.eachfile(__dirname, function(file) {
  //
})
```

#### .eachdir([pattern,] root, action)

```javascript
find.eachdir(__dirname, function(dir) {
  //
})
```

#### .fileSync([pattern,] root)
```javascript
var files = find.fileSync(__dirname);
```

#### .dirSync([pattern,] root)
```javascript
var dirs = find.dirSync(__dirname);
```

#### .error([callback])

Handling errors in asynchronous interfaces

```javascript
find
  .file(__dirname, function(file) {
    //
  })
  .error(function(err) {
    if (err) {
      //
    }
  })
```

#### .end([callback])

Detect `end` in `find.eachfile` and `find.eachdir`

```javascript
find
  .eachfile(__dirname, function(file) {
    //
  })
  .end(function() {
    console.log('find end');
  })
```

#### .use(Options)
  * `fs`: The internal fs object to be used.

```javascript
const { fs, vol } = require('memfs');

const json = {
  './README.md': '1',
  './src/index.js': '2'
};

vol.fromJSON(json, '/app');

find
  .use({ fs: fs })
  .file('/app', console.log);
```
