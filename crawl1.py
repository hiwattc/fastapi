from urllib.request import urlopen
from bs4 import BeautifulSoup

#뉴스기사 검색 URL -> 아래의 경우에는 naver에 산후조리 검색 -> 뉴스 탭으로 이동한 뒤 복사한 URL 
url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&oquery=%EB%A8%B8%EC%8B%A0%EB%9F%AC%EB%8B%9D&tqi=hXheKwprvTossLyGgYossssssZN-349005"

# urlopen 함수를 통해 url주소를 open 하여 읽고, 그 값을 html 이라는 변수에 저장 합니다.
html = urlopen(url).read()

# html 정보가 담겨있는 변수를 bs4 라이브러리에 있는 BeautifulSoup을 이용해
# parsing 하여 soup 에 저장합니다.
soup = BeautifulSoup(html, 'html.parser')

# parsing된 결과인 soup 에서 news_tit class ( 뉴스 제목 클래스를 의미 함) 를 검색하고, 모든 정보를 찾습니다.
html_class = soup.find_all(class_='news_tit')

#print(html_class)

# 뉴스제목을 text로 추출하여 출력합니다.
for tit in html_class:
    title = tit.text.strip()
    print(title)
