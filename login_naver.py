# 네이버 로그인 하기

# 사용되는 라이브러리
import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 필요한 값 입력
login_url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com' #네이버 로그인 페이지 주소
login_input = { 'id' : '아이디',
                'password' : '패스워드'} # 아이디랑 비밀번호
webdriver_path = "D:/DEV_PYTHON_DELETE/workspace/3.10.5/chromedriver.exe"   # 인식 안되면 경로에서 \을 /로 바꾸기

# 로그인 페이지 크롬으로 열기
driver = webdriver.Chrome(webdriver_path)
driver.get(login_url)
time.sleep(3)

# 아이디랑 비밀번호 입력하는 곳 찾기
id_input = driver.find_element(By.ID,'id')
password_input = driver.find_element(By.ID, 'pw')

# 아이디 입력 send_keys는 네이버 보안으로 사용 불가
id_input.click()
pyperclip.copy(login_input['id'])
id_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 비밀번호 입력 send_keys는 네이버 보안으로 사용 불가
password_input.click()
pyperclip.copy(login_input['password'])
password_input.send_keys(Keys.CONTROL, 'v')
time.sleep(2)

# 로그인 버튼 누름
driver.find_element(By.ID, 'log.login').click()


