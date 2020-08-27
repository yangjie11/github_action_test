#-*- coding:utf8 -*-
import os
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    username  = os.environ["USERNAME"]
    password  = os.environ["PASSWORD"]
    
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=option)

    # login in
    driver.get("https://www.rt-thread.org/account/user/index.html?response_type=code&authorized=yes&scope=basic&state=1588816557615&client_id=30792375&redirect_uri=https://club.rt-thread.org/index/user/login.html")

    driver.find_element_by_id("username").click()
    driver.find_element_by_id('username').clear()
    time.sleep(1)
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').clear()
    time.sleep(1)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login').click()
    time.sleep(30)
    driver.switch_to.window(driver.window_handles[-1])
    print("driver.current_url : {0}".format(driver.current_url))
    try:
        driver.find_element_by_link_text(u"立即签到").click()
    except Exception as e:
        print("Error message : {0}".format(e))

    driver.quit()
    print("Sign in\n")


if __name__ == "__main__":
    main()
