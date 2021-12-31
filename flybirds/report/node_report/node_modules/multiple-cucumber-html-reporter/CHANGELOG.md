CHANGELOG
=========

> **NOTE:** All changes can now be found on the [releases](https://github.com/wswebcreation/multiple-cucumber-html-reporter/releases)


<a name="1.11.3"></a>
## [1.11.3](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.11.2...v1.11.3) (2018-10-02)

### Fix
* **fix:** Update template condition to not suppress output for hidden steps w/html embed, related to [59](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/59), tnx to [Yaron Assa](https://github.com/yaronassa)
* **fix:** Replaced json.parse with json.stringify at line 329 of `generate-report.js` for step embeddings, tnx to [Marius](https://github.com/CTMarius)

<a name="1.11.2"></a>
## [1.11.2](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.11.1...v1.11.2) (2018-08-18)

### Fix
* **fix:** fix correct module path

<a name="1.11.1"></a>
## [1.11.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.11.0...v1.11.1) (2018-08-18)

### Fix
* **fix:** this release fixes issue [60](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/60). Now all assets are included in the module so stricter CI's should not have any problems using the assets

<a name="1.11.0"></a>
## [1.11.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.10.2...v1.11.0) (2018-08-17)

### Feature
* **feature:** Add scenario description [53](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/53), tnx to [Stefano Tamagnini](https://github.com/yoghi)
* **feature:** Add status of a feature file to `undefined` if 1 or multiple scenario's in a feature don't have a step implementation [58](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/58), tnx to [David de Kanter](https://github.com/daviddekanter)
* **feature:** Add support to for html-embeddings [59](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/59), tnx to [Yaron Assa](https://github.com/yaronassa)

### Refactor
* **refactor:** Update undefined code examples

<a name="1.10.2"></a>
## [1.10.2](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.10.1...v1.10.2) (2018-07-03)

### Bugfix
* **fix:** Remove error thrown if no json files are found [54](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/54), **tnx to [daviddekanter](https://github.com/daviddekanter)**

<a name="1.10.1"></a>
## [1.10.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.10.0...v1.10.1) (2018-05-04)

### Bugfix
* **fix:** Empty .json files might be skipped instead of making reporter crash [47](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/47), **tnx to [lennt](https://github.com/lenntt)**

<a name="1.10.0"></a>
## [1.10.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.9.0...v1.10.0) (2018-04-26)

### Feature
* **feature:** Add support for multiple screenshots in scenario steps [44](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/44), tnx to [Brian-Dawson-Nerdery](https://github.com/Brian-Dawson-Nerdery)

### Bugfix
* **fix:** Screenshots in the steps are stretched, now they are shown on their `max-width | max-height` showing proper images


<a name="1.9.0"></a>
## [1.9.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.8.0...v1.9.0) (2018-04-15)

### Feature
* **feature:** A custom [`pageTitle`](./README.MD#pageTitle) and a custom [`pageFooter`](./README.MD#pageFooter) can be added, tnx to [muthukumarse](https://github.com/muthukumarse)

<a name="1.8.0"></a>
## [1.8.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.7.0...v1.8.0) (2018-03-21)

### Feature
* **feature:** It now saves the sort state of columns in the Features overview, tnx to [Brian-Dawson-Nerdery](https://github.com/Brian-Dawson-Nerdery)

<a name="1.7.0"></a>
## [1.7.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.6.1...v1.7.0) (2018-03-20)

### Feature
* **feature:** Feature implementation for issue number [32](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/32) *Wrong format duration*.

<a name="1.6.1"></a>
## [1.6.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.6.0...v1.6.1) (2018-03-12)

### Bugfix
* **fix:** Fix for issue number [33](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/33) *Wrong passed/failed tool-tip in features box*

<a name="1.6.0"></a>
## [1.6.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.5.0...v1.6.0) (2018-03-05)

### Features
**Big thanks to [Stefano Tamagnini](https://github.com/yoghi)**

* **feature:** Add support for:
    * embedded attachments with custom mimeType (ogg, video, pdf, ecc... )
    * override the style by adding your own stylesheet
    * add some custom styles by adding your own style sheet
* **feature:** Presenting total number of passed/failed tests in tooltip in addition to percentage, see issue [29](https://github.com/wswebcreation/multiple-cucumber-html-reporter/issues/29)


<a name="1.5.0"></a>
## [1.5.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.4.3...v1.5.0) (2018-02-21)

### Features

* **feature:** Add support for duration display in a readable format **Big thanks to [LennDG](https://github.com/LennDG)**

<a name="1.4.3"></a>
## [1.4.3](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.4.2...v1.4.3) (2018-02-19)

### Bugfix

* **fix:** fix of attaching multiple json and text attachments to the same step **Big thanks to [rjktcby](https://github.com/rjktcby)**

<a name="1.4.2"></a>
## [1.4.2](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.4.1...v1.4.2) (2018-02-01)

### Bugfix

* **fix:** show edge icon for tests run with microsoft edge **Big thanks to [kevinkuszyk](https://github.com/kevinkuszyk)**

<a name="1.4.1"></a>
## [1.4.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.4.0...v1.4.1) (2018-01-01)

### Bugfix

* **fix:** fix: correctly show the skipped features on the report home page **Big thanks to [kevinkuszyk](https://github.com/kevinkuszyk)**

<a name="1.4.0"></a>
## [1.4.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.3.0...v1.4.0) (2017-12-15)

### Features

* **feature:** Ability to define custom metadata **Big thanks to [LennDG](https://github.com/LennDG)**

<a name="1.3.0"></a>
## [1.3.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.2.0...v1.3.0) (2017-11-19)

### Features

* **feature:** add the possibility to add a custom datablock to the features overview

<a name="1.2.0"></a>
## [1.2.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.1.0...v1.2.0) (2017-11-13)

### Features

* **feature:** add `app` as a metadata and update the docs

<a name="1.1.0"></a>
## [1.1.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.0.1...v1.1.0) (2017-09-22)

### Features

* **feature:** add option to disable the log when a report has been generated
* **feature:** defaulted the dropdown to 50 and updated the options to `[50, 100, 150, "All"]`
* **feature:** added *created by* to templates

<a name="1.0.1"></a>
## [1.0.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v1.0.0...v1.0.1) (2017-09-12)

### Bug Fixes

* **fix:** fixed typos, see [PR 9](https://github.com/wswebcreation/multiple-cucumber-html-reporter/pull/9), tnx to [achingbrain](https://github.com/achingbrain)

<a name="1.0.0"></a>
## [1.0.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.2.1...v1.0.0) (2017-09-08)

### Features

* **feature:** added support for CucumberJS 3, the only thing that has changes for reporting is that the `embedding.mime_type` has been changed to `embedding.media.type`.
* **feature:** `metadata` is now also an option, see the readme

<a name="0.2.1"></a>
## [0.2.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.2.0...v0.2.1) (2017-07-26)

### Bug Fixes

* **fix:** Styling for showing scenario title on smaller window size (< `1200 px`)


<a name="0.2.0"></a>
## [0.2.0](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.1.3...v0.2.0) (2017-07-18)

### Features

* **feature:** parse json to show info when `embedding.mime_type` is text and can be parsed as a JSON

### Bug Fixes

* **fix:** remove the embedding image to limit the output size
* **fix:** making the `+ Show Error`, `+ Show Info` and `Screenshot`- link more unique


<a name="0.1.3"></a>
## [0.1.3](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.1.2...v0.1.3) (2017-06-23)

### Bug Fixes

* **fix:** fix templates to work with node 4.4.5 by removing blockbindings

<a name="0.1.2"></a>
## [0.1.2](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.1.1...v0.1.2) (2017-05-26)

### Bug Fixes

* **fix:** sanitize `feature.id` that is used for urls in the features overview


<a name="0.1.1"></a>
## [0.1.1](https://github.com/wswebcreation/multiple-cucumber-html-reporter/compare/v0.1.0...v0.1.1) (2017-05-24)

### Bug Fixes

* **fix:** `embedding.mime_type  'text/plain'` can have encoded and plain text. Fixed this with a base64 check and added tests


<a name="0.1.0"></a>
## 0.1.0 (2017-05-21)

### Features

* **initial:** initial version of `Multiple Cucumer HTML Reporter`
