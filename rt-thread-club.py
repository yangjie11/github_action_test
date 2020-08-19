#-*- coding:utf8 -*-
import os
import sys
import time
from selenium import webdriver


def main():
    os.chdir("/rt-thread/actions")
    os.system("chmod a+x chromedriver")
    driver = webdriver.Chrome()
    driver.set_window_position(20,40)
    driver.set_window_size(1100,700)

    # login in
    driver.get("https://www.rt-thread.org/account/user/index.html?response_type=code&authorized=yes&scope=basic&state=1588816557615&client_id=30792375&redirect_uri=https://club.rt-thread.org/index/user/login.html")

    element = driver.find_element_by_id('username').click()
    element = driver.find_element_by_id('username').clear()
    time.sleep(1)
    element = driver.find_element_by_id('username').send_keys("17634622900")
    element = driver.find_element_by_id('password').click()
    element = driver.find_element_by_id('password').clear()
    time.sleep(1)
    element = driver.find_element_by_id('password').send_keys("kang0830...")
    element = driver.find_element_by_id('login').click()
    print(element)
    #等待页面跳转
    time.sleep(10)
    driver.find_element_by_link_text(u"立即签到").click()
    driver.quit()
    print("Sign in\n")


if __name__ == "__main__":
    main()
