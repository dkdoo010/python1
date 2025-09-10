from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# 검색 키워드 설정
keyword = '파이썬'
search_url = f'https://www.hanbit.co.kr/search/search_list.html?keyword={keyword}'

# 브라우저 옵션 설정
options = Options()
options.add_experimental_option('detach', True)  # 브라우저 창 유지
# options.add_argument('--headless')  # 창 없이 실행하려면 주석 해제

# 브라우저 실행
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(search_url)

# 페이지 로딩 대기
time.sleep(2)

# XPath 요소 찾기 및 클릭 시도
try:
    element = driver.find_element(By.XPATH, '//*[@id="container"]/div[2]/div/div[2]/h2')
    print("텍스트:", element.text)

    # 클릭 가능한 경우 클릭
    if element.is_displayed() and element.is_enabled():
        element.click()
        print("요소를 클릭했습니다.")
    else:
        print("요소는 클릭할 수 없습니다.")
except Exception as e:
    print("요소를 찾거나 클릭하는 중 오류 발생:", e)

