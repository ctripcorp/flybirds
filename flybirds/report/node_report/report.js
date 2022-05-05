let args = process.argv.slice(2);
let jsonPath = args[0];
let reportPath = args[1];
let platform = args[2];
console.log(`multiple-cucumber-html-reporter platform: ${platform}`);

const report = require('multiple-cucumber-html-reporter');


const baseConfig = {
    // page title
    pageTitle: 'flybirds test report',
    //behave json path
    jsonDir: jsonPath,
    // gen path
    reportPath: reportPath,
    reportName: 'ui auto platform report',
    pageFooter: '<div class="created-by">flybirds test report</div>',
    openReportInBrowser: false,
    displayDuration: true
};

const webConfig = {
    ...baseConfig,
    customMetadata: true,
    metadata: [
        {name: 'Browser', value: 'not known'},
    ]
};

const appConfig = {
    ...baseConfig,
    hideMetadata: true
};

function getConfig(platform) {
    if (platform === 'web') {
        return webConfig;
    }
    if (platform === 'android' || platform === 'ios') {
        return appConfig;
    }
    return baseConfig;
}

report.generate({
    ...getConfig(platform)
});