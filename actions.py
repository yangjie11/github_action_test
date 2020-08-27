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
    os.system("sudo apt -y update && apt -y upgrade")
    os.system("sudo apt -y install unzip")
    os.system("sudo apt -y install curl")
    os.system("sudo python -m pip install --upgrade pip")
    os.system("sudo pip install selenium")
    os.system("sudo chmod a+x chromedriver")
#     chromedriver = "/usr/local/bin/chromedriver"
#     os.environ["webdriver.chrome.driver"] = chromedriver
    os.system("sudo pip install selenium")
    os.system("sudo apt install -y gconf-service libasound2 libatk1.0-0 libcairo2 libcups2 libfontconfig1 libgdk-pixbuf2.0-0 libgtk-3-0 libnspr4 libpango-1.0-0 libxss1 fonts-liberation libappindicator1 libnss3 lsb-release xdg-utils")
    os.system("sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb; apt-get -fy install")
    os.system("sudo python rt-thread-club.py")


if __name__ == "__main__":
    main()
