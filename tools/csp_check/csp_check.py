import os
import time
import logging
import subprocess


def init_logger():
    log_format = "[%(filename)s %(lineno)d %(levelname)s] %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.WARN,
                        format=log_format,
                        datefmt=date_format,
                        )


def execute_command(cmd_string, cwd=None, shell=True):
    """Execute the system command at the specified address."""

    sub = subprocess.Popen(cmd_string, cwd=cwd, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, shell=shell, bufsize=4096)

    stdout_str = ''
    while sub.poll() is None:
        stdout_str += str(sub.stdout.read(), encoding="UTF-8")
        time.sleep(0.1)

    return stdout_str


def main():
    init_logger()
    execute_command("apt update && apt -y upgrade && apt -y install unzip")
    os.chdir("/rt-thread/sdk-index/tools/csp_check")
    execute_command("chmod 777 prj_gen")
    execute_command("pip install pyyaml pytest-sugar pytest-parallel")
    os.system("python project_build.py")


if __name__ == '__main__':
    main()
