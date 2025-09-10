from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
brower = webdriver.Chrome(options=options)

brower.maximize_window()

url = 'https://flight.naver.com/'
brower.get(url)

brower.get_screenshot_as_file('data/flight.png')
brower.quit