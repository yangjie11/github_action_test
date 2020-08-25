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

    # login in
    driver.get("https://www.rt-thread.org/account/user/index.html")

    driver.find_element_by_css_selector("#username").click()
    driver.find_element_by_id('username').clear()
    time.sleep(1)
    driver.find_element_by_id('username').send_keys("Mr.Liu")
    driver.find_element_by_id('password').click()
    driver.find_element_by_id('password').clear()
    time.sleep(1)
    driver.find_element_by_id('password').send_keys("qwer123456")
    driver.find_element_by_id('login').click()
    time.sleep(10)

    try:
        #driver.find_element_by_xpath('/html[1]/body[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[2]/a[1]').click()
        #driver.find_element_by_class_name("btn-signin")[0].click()
        driver.find_element_by_link_text(u"立即签到").click()
    except Exception as e:
        print("Error message : {0}".format(e))

    driver.quit()
    print("Sign in\n")


if __name__ == "__main__":
    main()
