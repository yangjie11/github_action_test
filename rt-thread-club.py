#-*- coding:utf8 -*-
import os
import sys
import time
from selenium import webdriver


def main():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    option.add_argument('no-sandbox')
    option.add_argument('disable-dev-shm-usage')
    driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=option)
    driver.implicitly_wait(10)   #隐形等待

    # login in
    driver.get("https://www.rt-thread.org/account/user/index.html")

    # element = driver.find_element_by_id('username').click()
    driver.find_element_by_css_selector("#username").click()
    element = driver.find_element_by_id('username').clear()
    time.sleep(1)
    element = driver.find_element_by_id('username').send_keys("17634622900")
    element = driver.find_element_by_id('password').click()
    element = driver.find_element_by_id('password').clear()
    time.sleep(1)
    element = driver.find_element_by_id('password').send_keys("kang0830...")
    element = driver.find_element_by_id('login').click()
    #等待页面跳转
    time.sleep(10)
    driver.implicitly_wait(10)   #隐形等待
    # driver.find_element_by_xpath(r'//*[@id="questionlist"]/div[2]/div/div[1]/div[2]/a').click()
    driver.find_element_by_css_selector("btn btn-primary btn-signin").click()
    driver.quit()
    print("Sign in\n")


if __name__ == "__main__":
    main()
