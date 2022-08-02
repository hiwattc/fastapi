import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

class ChickenStore:
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
        self.soup = self.get_request_url()
        # csv 파일에 들어갈 컬럼 헤더
        self.mycolumns = ['brandName', 'store', 'sido', 'gungu', 'address', 'phone']

        # print('생성자 호출됨')

        # 해당 리스트를 사용하여 csv 파일을 생성
    def save2Csv(self, saveData):
        data = pd.DataFrame(saveData, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding=self.myencoding, index=True)
# end class ChickenStore



from itertools import count
#from ChickenUtil import ChickenStore

####################################################
brandName = 'cheogajip'
base_url = 'http://www.cheogajip.co.kr/bbs/board.php'


####################################################
def getData():
    savedData = []  # 엑셀로 저장할 리스트

    for page_idx in count():
        url = base_url
        url += '?bo_table=store'
        url += '&page=%s' % str(page_idx + 1)

        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytbody = soup.find('tbody')

        shopExists = False  # 매장 목록이 없다고 가정

        for mytr in mytbody.findAll('tr'):
            shopExists = True
            #             print(page_idx+1)
            #             print(mytr)
            #             print('b' * 30)

            try:
                store = mytr.select_one('td:nth-of-type(2)').string
                address = mytr.select_one('td:nth-of-type(3)').string
                phone = mytr.select_one('td:nth-of-type(4)').string
                imsi = address.split(' ')
                sido = imsi[0]
                gungu = imsi[1]
                # print(store + '  ' + phone )

                savedData.append([brandName, store, sido, gungu, address, phone])

            except AttributeError as err:
                print(err)
                shopExists = False
                break

        #         if page_idx == 0 :
        if shopExists == False:
            chknStore.save2Csv(savedData)
            break


####################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')

