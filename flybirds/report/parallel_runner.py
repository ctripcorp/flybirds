import base64
import json
import logging
import multiprocessing
from concurrent.futures.thread import ThreadPoolExecutor
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import Popen, PIPE
from timeit import default_timer as timer

import flybirds.utils.flybirds_log as log
from flybirds.core.config_manage import WebConfig
from flybirds.utils.dsl_helper import get_use_define_param
from flybirds.utils.uuid_helper import report_name


def create_logger(filename: str):
    """
    create m_logger to dump execution time and duration of features into a
    log file
    :return:
    """
    m_logger = multiprocessing.get_logger()
    m_logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s;%(levelname)s;%(processName)s;%(message)s')
    handler = logging.FileHandler(filename=filename)
    handler.setFormatter(formatter)

    # to avoid duplicated messages in the output
    if not len(m_logger.handlers):
        m_logger.addHandler(handler)
    return m_logger


logger = create_logger('multiprocessing_features.log')


def parallel_run(context):
    """
    Parallel Behave Runner
    """
    behave_cmd = context.get("cmd_str")
    feature_path = context.get("feature_path")

    if behave_cmd is None or feature_path is None:
        raise Exception("[parallel_runner] parse args has error")

    parsed_tags = context.get("parsed_tags")

    if parsed_tags and len(parsed_tags) > 0:
        # -k, --no-skipped
        cmd = f'behave {feature_path} {" ".join(parsed_tags)} -d -k -f json ' \
              f'--no-summary'
    else:
        cmd = f'behave {feature_path} -d -k -f json --no-summary'
    features = get_features_num(cmd)

    log.info('start thread...')
    with ThreadPoolExecutor(max_workers=3) as t_pool:
        browser_types = get_browser_types(context)
        for b_type in browser_types:
            t_pool.submit(multiplication, b_type, context, features)
    log.info('all thread done...')


def multiplication(browser_type, context, features):
    log.info('multiplication start')
    log.info(f'multiplication browser_type:{browser_type}')

    behave_cmd = context.get("cmd_str")
    feature_path = context.get("feature_path")
    processes = context.get("processes")

    cur_browser_type = str(base64.b64encode(browser_type.encode('utf-8')),
                           'utf-8')
    behave_cmd = behave_cmd + f'  -D cur_browser={cur_browser_type}'
    log.info(f'cmd str: {behave_cmd}')

    pool = Pool(processes) if len(features) >= processes else Pool(
        len(features))
    results = pool.map(
        partial(execute_parallel_feature, behave_cmd=behave_cmd,
                feature_path=feature_path, browser_type=browser_type),
        features)
    pool.close()
    pool.join()
    log.info(f'parallel run result: {results}')


def execute_parallel_feature(feature, behave_cmd, feature_path, browser_type):
    """
    Runs features in parallel
    :param feature: feature to run
    :param behave_cmd: behave cmd string
    :param feature_path: feature path
    :param browser_type: browser_type
    """
    feature_start_time = datetime.now()
    start_timer = timer()
    file_name = report_name(feature, browser_type)
    cmd = behave_cmd.replace(feature_path, feature, 1).replace('report.json',
                                                               file_name, 1)
    log.info(f'cmd str: {cmd}')

    p = Popen(cmd, stdout=PIPE, shell=True)
    code = p.wait()
    p.communicate()

    status = 'Passed' if code == 0 else 'Failed'
    logging.info('{0:50}: {1}!!'.format(feature, status))
    feature_end_time = datetime.now()
    end_timer = timer()
    logger.info(f'{feature.split("/")[-1].split(".")[0]};'
                f'{feature_start_time};'
                f'{feature_end_time};'
                f'{end_timer - start_timer};'
                f'{status}')
    return status


def dry_run_parsed_cmd(cmd: str) -> str:
    """
    Execute command and return it's stdout as string
    :param cmd: bash command as str
    :return: stdout from command execution
    """
    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()

    return json.loads(out.decode('utf-8-sig'))


def get_features_num(cmd: str):
    parsed_output = dry_run_parsed_cmd(cmd)
    if not parsed_output:
        log.warn(
            f'No json output from executed behave dry run command. Nothing to '
            f'be executed.Command: {cmd}\nNothing to execute')
        return
    features = list({feature['location'].split(':')[0]
                     for feature in parsed_output
                     })
    log.info(f'features num need to be executed in parallel: {len(features)}')
    return features


def get_browser_types(context):
    user_data = get_use_define_param(context, 'browserType')
    browser_type = WebConfig(user_data, None).browser_type

    # check browser_type
    browser_types = browser_type
    if isinstance(browser_type, str):
        browser_types = browser_type.split(',')
    browser_types = list(set(browser_types))
    temp = []
    [temp.append(i.strip().lower()) for i in browser_types if
     i.strip().lower() in ['chromium', 'firefox', 'webkit']]
    # add default value
    if len(temp) == 0:
        log.warn(
            'flybirds did not find a browser that would launch. Now chromium '
            'will be launched by default.')
        temp.append('chromium')
    context['browser_types'] = temp
    return temp
