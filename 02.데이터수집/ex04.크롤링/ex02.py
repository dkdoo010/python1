from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium 

import time

brower = webdriver.Chrome()
brower.get('https://naver.com')

btn = brower.find_element(By.CLASS_NAME, 'MyView-module__link_login___HpHMW')
btn.click()
time.sleep(2)

id = brower.find_element(By.ID, 'id')
id.send_keys('hjh6715')
pw = brower.find_element(By.ID, 'pw')
pw.send_keys('')
time.sleep(2)

login = brower.find_element(By.ID, 'log.login')
login.click()
time.sleep(100)