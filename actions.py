import os
import logging


def init_logger():
    log_format = " %(filename)s %(lineno)d <ignore> %(levelname)s %(message)s "
    date_format = '%Y-%m-%d  %H:%M:%S %a '
    logging.basicConfig(level=logging.INFO,
                        format=log_format,
                        datefmt=date_format
                        )


def main():
    os.system("apt -y update && apt -y upgrade")
    os.system("apt -y install unzip")
    os.system("apt -y install curl")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install selenium")
    os.chdir("/rt-thread/actions")
    os.system("chmod a+x chromedriver")
    os.system("mv /rt-thread/actions/chromedriver /usr/local/bin")
    os.system("ls -al /usr/local/bin")
    chromedriver = "/usr/local/bin/chromedriver"
    os.environ["webdriver.chrome.driver"] = chromedriver
    os.system("pip install selenium")
    os.system("apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils")
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install")
    os.system("python rt-thread-club.py")


if __name__ == "__main__":
    main()
