import json
import logging
import multiprocessing
import os
from datetime import datetime
from functools import partial
from multiprocessing import Pool
from subprocess import Popen, PIPE
from timeit import default_timer as timer

import flybirds.utils.flybirds_log as log
from flybirds.report.fail_feature_create import rerun_launch
from flybirds.utils.uuid_helper import report_name


def create_logger(filename: str):
    """
    create m_logger to dump execution time and duration of features into a logfile
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


def execute_parallel_feature(feature, behave_cmd, feature_path, context):
    """
    Runs features in parallel
    :param feature: feature to run
    :param behave_cmd: behave parameters with respective values
    :param feature_path: behave parameters with respective values
    :param context: behave parameters with respective values
    :type feature: str
    """
    feature_start_time = datetime.now()
    start_timer = timer()
    file_name = report_name()
    cmd = behave_cmd.replace(feature_path, feature).replace('report.json',
                                                            file_name)
    log.info(
        f'[execute_parallel_feature] process:({os.getpid()}),cmd str: {cmd}')

    p = Popen(cmd, stdout=PIPE, shell=True)
    code = p.wait()
    p.communicate()

    # report_dir_path = context.get("report_dir_path")
    # file_path = os.path.join(report_dir_path, file_name)
    # log.info(f'[execute_parallel_feature] file_path:{file_path}')
    #
    # report_json = file_helper.get_json_from_file_path(file_path,
    #                                                   'execute_parallel_feature'
    #                                                   )
    # log.info(f'[execute_parallel_feature] report_json:{report_json}')

    # raise Exception('yanzheng')
    status = 'Passed' if code == 0 else 'Failed'
    logging.info('{0:50}: {1}!!'.format(feature, status))
    feature_end_time = datetime.now()
    end_timer = timer()
    logger.info(f'{feature.split("/")[-1].split(".")[0]};'
                f'{feature_start_time};'
                f'{feature_end_time};'
                f'{end_timer - start_timer};'
                f'{status}')

    # rerun
    run_args = context.get("run_args")
    need_rerun_args = context.get("need_rerun_args")
    report_dir_path = context.get("report_dir_path")
    rerun_launch(need_rerun_args, report_dir_path, run_args, file_name)

    return status


def parallel_runner(context):
    """
    Parallel Behave Runner
    """
    # args, behave_args = parse_arguments()
    # args = argparse.Namespace(processes=4, suite='features', tags=None)
    # behave_args = ['-f=json.pretty', '-o', 'test-results.json']
    behave_cmd = context.get("cmd_str")
    feature_path = context.get("feature_path")

    if behave_cmd is None or feature_path is None:
        raise Exception("parse args has error")
    processes = context.get("processes")
    parsed_tags = context.get("parsed_tags")

    log.info(f'processes: {processes}')
    log.info(f'parsed_tags: {parsed_tags}')
    if parsed_tags and len(parsed_tags) > 0:
        # -k, --no-skipped
        cmd = f'behave {feature_path} {" ".join(parsed_tags)} -d -k -f json --no-summary'
        # behave_args = parsed_tags + behave_args
    else:
        cmd = f'behave {feature_path} -d -k -f json --no-summary'
    log.info(f'log main cmd str: {cmd}')

    """
    main cmd str: behave features -d -k -f json --no-summary
    main cmd str: behave features/test/features1.features --tags @example --tags ~@skip -d -k -f json --no-summary

    behave features --tags=tag1,tag2,-tag3,tag4 -d -k -f json --no-summary
    """
    parsed_output = dry_run_parsed_cmd(cmd)
    if not parsed_output:
        log.warn(
            f'No json output from executed behave dry run command. Command: {cmd}\nNothing to execute')
        return
    features = list({feature['location'].split(':')[0]
                     for feature in parsed_output
                     })
    log.info(f'features to execute in parallel: {features}')

    pool = Pool(processes) if len(features) >= processes else Pool(
        len(features))
    results = pool.map(
        partial(execute_parallel_feature, behave_cmd=behave_cmd,
                feature_path=feature_path, context=context), features)
    log.info(f'parallel result: {results}')
    # set exit status to 1 in case at least one feature failed
    # any_feature_failed = 'Failed' in results
    # if any_feature_failed:
    #     sys.exit(1)
    # else:
    #     sys.exit(0)


def dry_run_parsed_cmd(cmd: str) -> str:
    """
    Execute command and return it's stdout as string
    :param cmd: bash command as str
    :return: stdout from command execution
    """
    p = Popen(cmd, stdout=PIPE, shell=True)
    out, err = p.communicate()

    return json.loads(out.decode())
