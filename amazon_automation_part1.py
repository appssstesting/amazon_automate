# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:51:04 2020

@author: Tejas
"""

from selenium import webdriver
import time
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import logindata


# Other imports and desired_cap definition goes here
options = Options()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or "raghav_4NQ9a3"
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or "JQ7M3ZCVjb6MqKeWgjrH"
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"

driver = webdriver.Remote(command_executor=URL, options=options)
# Rest of the test case goes here

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome('/home/enigma/Downloads/chromedriver', chrome_options=options)
action = ActionChains(driver)
time.sleep(1)

name: 'BrowserStack Env Setup'
uses: 'browserstack/github-actions/setup-env@master'
with:
username:  ${{ secrets.BROWSERSTACK_USERNAME }}
access-key: ${{ secrets.BROWSERSTACK_ACCESS_KEY }}
build-name: 'BUILD_INFO'
project-name: 'REPO_NAME'


driver.get('http://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
time.sleep(3)
 
firstLevelMenu = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[2]')
action.move_to_element(firstLevelMenu).perform()
time.sleep(3)
 
secondLevelMenu = driver.find_element_by_xpath('//*[@id="nav-flyout-ya-signin"]/a/span')
secondLevelMenu.click()
time.sleep(3)

signinelement = driver.find_element_by_xpath('//*[@id="ap_email"]')
signinelement.send_keys(logindata.USERNAME)
time.sleep(3)

cont = driver.find_element_by_xpath('//*[@id="continue"]')
cont.click()
time.sleep(3)

passwordelement = driver.find_element_by_xpath('//*[@id="ap_password"]')
passwordelement.send_keys(logindata.PASSWORD)
time.sleep(3)

login = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
login.click()
time.sleep(3)


