from selenium import webdriver
from selenium.webdriver.common.by import By

filename = 'D:/DEV_PYTHON_DELETE/workspace/3.10.5/chromedriver.exe'

#driver = webdriver.Chrome(filename)

options = webdriver.ChromeOptions()
options.add_argument('window-size=1024,768')
driver = webdriver.Chrome(filename,options=options)
print(type(driver))

url = 'https://esg.hyundai-steel.com/'
driver.get(url)

#search_textbox = driver.find_element(by=By.NAME, value='query')
#word = '머신러닝'
#search_textbox.send_keys(word)
#search_textbox.submit()

import time
#메인
wait = 1
print(str(wait) + '초 대기')
time.sleep(wait)
imageFile = 'capture1.png'
driver.save_screenshot(imageFile)
print(imageFile + ' 파일로 저장')

#보고서개요
time.sleep(wait)
url = 'https://esg.hyundai-steel.com/2022/front/contents/contentView.do?menuSn=338&cntntsCode=22ov01'
driver.get(url)
imageFile = 'capture2.png'
driver.save_screenshot(imageFile)
print(imageFile + ' 파일로 저장')

#CEO메시지
time.sleep(wait)
url = 'https://esg.hyundai-steel.com/2022/front/contents/contentView.do?menuSn=341&cntntsCode=22ov02'
driver.get(url)
imageFile = 'capture3.png'
driver.save_screenshot(imageFile)
print(imageFile + ' 파일로 저장')



wait = 3
print(str(wait) + '초 후 종료')
driver.implicitly_wait(wait)


driver.quit()
