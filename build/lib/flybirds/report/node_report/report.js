


let args= process.argv.slice(2);
let jsonPath=args[0];
let reportPath=args[1];

const report = require('multiple-cucumber-html-reporter');



report.generate({
        // page title
        pageTitle: 'flybirds test report',
        //behave json path
        jsonDir: jsonPath,
        // gen path
        reportPath: reportPath,
        // page title
        pageTitle: 'ui auto platform report',
        reportName: 'ui auto platform report',
        pageFooter: '<div class="created-by">flybirds test report</div>',
        openReportInBrowser: false,
        displayDuration: true
    });