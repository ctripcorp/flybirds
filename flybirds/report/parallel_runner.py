import json
import logging
import multiprocessing
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import Popen, PIPE
from timeit import default_timer as timer

import flybirds.utils.flybirds_log as log
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


def execute_parallel_feature(feature, behave_cmd, feature_path):
    """
    Runs features in parallel
    :param feature: feature to run
    :param behave_cmd: behave cmd string
    :param feature_path: feature path
    """
    feature_start_time = datetime.now()
    start_timer = timer()
    file_name = report_name()
    cmd = behave_cmd.replace(feature_path, feature, 1).replace('report.json',
                                                               file_name, 1)
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


def parallel_run(context):
    """
    Parallel Behave Runner
    """
    behave_cmd = context.get("cmd_str")
    feature_path = context.get("feature_path")

    if behave_cmd is None or feature_path is None:
        raise Exception("[parallel_runner] parse args has error")
    processes = context.get("processes")
    parsed_tags = context.get("parsed_tags")

    if parsed_tags and len(parsed_tags) > 0:
        # -k, --no-skipped
        cmd = f'behave {feature_path} {" ".join(parsed_tags)} -d -k -f json ' \
              f'--no-summary'
    else:
        cmd = f'behave {feature_path} -d -k -f json --no-summary'
    features = get_features_num(cmd)
    pool = Pool(processes) if len(features) >= processes else Pool(
        len(features))
    results = pool.map(
        partial(execute_parallel_feature, behave_cmd=behave_cmd,
                feature_path=feature_path), features)
    pool.close()
    pool.join()
    log.info(f'parallel run result: {results}')


def dry_run_parsed_cmd(cmd: str) -> str:
    """
    Execute command and return it's stdout as string
    :param cmd: bash command as str
    :return: stdout from command execution
    """
    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()

    return json.loads(out.decode())


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
