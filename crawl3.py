from selenium import webdriver
from selenium.webdriver.common.by import By

filename = 'D:/DEV_PYTHON_DELETE/workspace/3.10.5/chromedriver.exe'
driver = webdriver.Chrome(filename)
print(type(driver))

#url = 'http://www.google.com'
url = 'https://www.naver.com'
driver.get(url)

# search_textbox = driver.find_element_by_name('q')
# search_textbox = driver.find_element(by=By.NAME, value='q')
search_textbox = driver.find_element(by=By.NAME, value='query')

word = '머신러닝'
search_textbox.send_keys(word)

search_textbox.submit()

import time

# 3초 후 스크린샷 찍고 저장
wait = 3
print(str(wait) + '초 대기')
time.sleep(wait)

imageFile = 'capture.png'
driver.save_screenshot(imageFile)
print(imageFile + ' 파일로 저장')

wait = 3
print(str(wait) + '초 후 종료')
driver.implicitly_wait(wait)

driver.quit()
