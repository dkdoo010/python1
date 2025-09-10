from selenium import webdriver
import os
os.makedirs('data', exist_ok=True)
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

brower = webdriver.Chrome(options=options)
url = 'https://flight.naver.com/'
brower.get(url)

brower.get_screenshot_as_file('data/flight2.png')