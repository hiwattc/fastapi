import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import time

class ChickenStore:
    def getWebDriver(self, cmdJavaScript):
        self.driver.execute_script(cmdJavaScript)
        wait = 5
        time.sleep(wait)
        mypage = self.driver.page_source

        return BeautifulSoup(mypage, 'html.parser')

    def getSoup(self):  # BeautifulSoup 객체를 반환해주는 함수
        if self.soup is None:
            return None
        else:
            return BeautifulSoup(self.soup, 'html.parser')

    def get_request_url(self):  # urlopen 함수를 사용하여 url 객체를 반환하는 함수
        request = urllib.request.Request(self.url)
        try:
            response = urllib.request.urlopen(request)
            if response.getcode() == 200:  # http 응답 코드가 정상
                if self.brandName != 'pelicana':
                    return response.read().decode(self.myencoding)
                else:
                    return response
        except Exception as err:
            print(err)
            return None

    def __init__(self, brandName, url):
        self.myencoding = 'UTF-8'
        self.brandName = brandName
        self.url = url

        # csv 파일에 들어갈 컬럼 헤더
        self.mycolumns = ['brandName', 'store', 'sido', 'gungu', 'address', 'phone']

        if self.brandName != 'goobne':
            self.soup = self.get_request_url()
            self.driver = None
        else:
            self.soup = None
            filepath = 'D:/DEV_PYTHON_DELETE/workspace/3.10.5/chromedriver.exe'
            self.driver = webdriver.Chrome(filepath)
            self.driver.get(self.url)
        # print('생성자 호출됨')

        # 해당 리스트를 사용하여 csv 파일을 생성
    def save2Csv(self, saveData):
        data = pd.DataFrame(saveData, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding=self.myencoding, index=True)
# end class ChickenStore


from itertools import count
#from ChickenUtil import ChickenStore
############################################################################
brandName = 'goobne'
base_url = 'http://www.goobne.co.kr/store/search_store.jsp'
############################################################################
def getData():
    savedData = []
    chknStore = ChickenStore(brandName, base_url)

    for page_idx in count():
        print('%s 페이지가 호출 되었습니다.' % str(page_idx + 1))
        bEndPage = False     # True 이면 마지막 페이지 도달

        cmdJavaScript = "javascript:store.getList('%s')" % str(page_idx + 1)
        soup = chknStore.getWebDriver(cmdJavaScript)
        # print(type(soup))

        store_list = soup.find('tbody', attrs={'id': 'store_list'})
        mytrlist = store_list.findAll('tr')

        for onestore in mytrlist:
            mytdlist = onestore.findAll('td')

            if len(mytdlist) > 1:
                store = onestore.select_one('td:nth-of-type(1)').get_text(strip=True)
                phone = onestore.select_one('td:nth-of-type(2)').a.string
                address = onestore.select_one('td:nth-of-type(3)').a.string
                imsi = str(address).split(' ')
                sido = imsi[0]
                gungu = imsi[1]

                savedData.append([brandName, store, sido, gungu, address, phone])
            else:
                bEndPage = True
                break
        print('-' * 30)

        # if page_idx >= 1:
        #     break

        if bEndPage == True:
            break

        chknStore.save2Csv(savedData)
############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')
