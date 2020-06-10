import json
import os
import re
import logging
from gen_sdk_json import gen_sdk_para_json_file
from gen_test_case import gen_chip_test_case
from csp_check import execute_command


def init_logger():
    log_format = "[%(filename)s %(lineno)d %(levelname)s] %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        datefmt=date_format,
                        )


def get_rt_thread_source_code():
    try:
        with open(r"/rt-thread/sdk-index/RT-Thread_Source_Code/index.json", "r") as f:
            sourcr_releases = json.loads(f.read())["releases"]
    except Exception as e:
        logging.error("\nError message : {0}.".format(e))
        exit(1)

    nano_url = None
    released_url = None
    for release in sourcr_releases:
        if release["description"].find("Nano released 3.1.3") != -1:
            nano_url = release["url"]
        if release["description"].find("released v4.0.2") != -1:
            released_url = release["url"]
    if not nano_url:
        logging.error("Can't find nano source url, please check RT-Thread_Source_Code/index.json file.")
        exit(1)
    if not released_url:
        logging.error("Can't find released source url, please check RT-Thread_Source_Code/index.json file.")
        exit(1)

    execute_command("wget -O /rt-thread/nano.zip {0}".format(nano_url))
    execute_command("unzip {0} -d /rt-thread/rt-thread-src".format("/rt-thread/nano.zip"))
    execute_command("rm -rf /rt-thread/nano.zip")
    execute_command("wget -O /rt-thread/released.zip {0}".format(released_url))
    execute_command("unzip {0} -d /rt-thread/rt-thread-src".format("/rt-thread/released.zip"))
    execute_command("rm -rf /rt-thread/released.zip")


def csp_build_test():
    # init logging
    init_logger()
    # get rt-thread_sourcr_code : nano and released
    get_rt_thread_source_code()
    # get update csp url
    try:
        with open('/rt-thread/sdk-index/tools/csp_update_url.json', "r") as f:
            sdk_url = json.loads(f.read())[0]
    except Exception as e:
        logging.error("\nError message : {0}.".format(e))
        exit(1)

    execute_command("wget -O /rt-thread/rt-thread-csp.zip {0}".format(sdk_url))
    execute_command("unzip -o /rt-thread/rt-thread-csp.zip -d /rt-thread/rt-thread-csp")
    execute_command("rm -rf /rt-thread/rt-thread-csp.zip")
    rt_thread_csp_dir = os.listdir("/rt-thread/rt-thread-csp")
    if len(rt_thread_csp_dir) != 1:
        logging.error("Please check the zip : {0}".format(sdk_url))
        exit(1)
    csp_path = os.path.join("/rt-thread/rt-thread-csp", rt_thread_csp_dir[0])
    execute_command("mv {0}/* /rt-thread/rt-thread-csp && rm -rf {0}".format(csp_path))

    gen_sdk_para_json_file("/rt-thread/rt-thread-csp", "/rt-thread/workspace", "/rt-thread/rt-thread-src")

    gen_chip_test_case("csp_chips.json", "mcu_config")

    os.system("python csp_test_case.py")

    execute_command("rm -rf mcu_config")
    execute_command("exit")


if __name__ == "__main__":
    csp_build_test()
