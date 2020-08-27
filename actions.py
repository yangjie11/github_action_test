import os
import logging
import subprocess


def execute_command(cmd_string, cwd=None, shell=True):
    """Execute the system command at the specified address."""

    sub = subprocess.Popen(cmd_string, cwd=cwd, stdin=subprocess.PIPE,
                           stdout=subprocess.PIPE, shell=shell, bufsize=4096)

    stdout_str = ''
    while sub.poll() is None:
        stdout_str += str(sub.stdout.read(), encoding="UTF-8")
        time.sleep(0.1)

    return stdout_str

def init_logger():
    log_format = " %(filename)s %(lineno)d <ignore> %(levelname)s %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        datefmt=date_format
                        )


def main():
    print("python env : ")
    result = execute_command("env", shell=True)
    print(result)
#     os.system("sudo apt -y update && apt -y upgrade")
#     os.system("sudo apt -y install unzip")
#     os.system("sudo apt -y install curl")
#     os.system("sudo python -m pip install --upgrade pip")
#     os.system("sudo pip install selenium")
#     os.system("sudo chmod a+x chromedriver")
#     os.system("sudo pip install selenium")
#     os.system("sudo apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils")
#     os.system("sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
#     os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install")
    os.system("sudo python rt-thread-club.py")


if __name__ == "__main__":
    main()
