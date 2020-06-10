# -*- coding: UTF-8 -*-
import os
import json
import time
import pytest
import shutil
import random
import logging
from csp_check import execute_command


def init_logger():
    log_format = "[%(filename)s %(lineno)d %(levelname)s] %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.WARN,
                        format=log_format,
                        datefmt=date_format,
                        )


if __name__ == "__main__":
    init_logger()
    logging.info("=================> Project build start.")
    begin_time = time.time()
    pytest.main(["csp_test_case.py", '--html=report.html', '--self-contained-html', '-s'])
    execute_command("rm -rf /rt-thread/eclipse/workspace")
    logging.info("=================> Project build end, time consuming : {0}.".format(time.time() - begin_time))


def get_build_result(cmd_pre, project_name):

    project_path = os.path.join("/rt-thread/workspace", project_name)
    if not os.path.exists(project_path):
        logging.error("Error : {0} not exit.".format(project_path))
        return False

    cmd = cmd_pre + " -cleanBuild '{0}' 1>build.log 2>/dev/null".format(project_name)
    execute_command(cmd)
    build_result = judge_build_result()

    project_path = os.path.join("/rt-thread/workspace", project_name)
    execute_command("rm -rf {0}".format(project_path))

    return build_result


def csp_test(project_name):
    cmd_pre = r"/rt-thread/eclipse/eclipse -nosplash --launcher.suppressErrors "\
              r"-application org.eclipse.cdt.managedbuilder.core.headlessbuild " \
              r"-data '/rt-thread/eclipse/workspace'"
    return get_build_result(cmd_pre, project_name)


def judge_build_result():
    try:
        with open("build.log", 'r') as f:
            log_info = f.readlines()
    except Exception as e:
        logging.error("Error message : {0}".format(e))
        return False

    build_result = False
    for line in log_info:
        if (line.find('error') != -1) or (line.find("Error") != -1):
            logging.error(line)
        if (line.find("region `ROM' overflowed") != -1) or (line.find("region `RAM' overflowed") != -1):
            logging.error(line)
        if line.find("Finished building target: rtthread.elf") != -1:
            build_result = True
            break
    execute_command("rm -rf build.log")
    return build_result
