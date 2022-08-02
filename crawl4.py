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
        self.brandName = brandName
        self.url = url
        self.soup = self.get_request_url()
        # csv 파일에 들어갈 컬럼 헤더
        self.mycolumns = ['brandName', 'store', 'sido', 'gungu', 'address', 'phone']
        self.myencoding = 'UTF-8'
        # print('생성자 호출됨')

        # 해당 리스트를 사용하여 csv 파일을 생성
    def save2Csv(self, saveData):
        data = pd.DataFrame(saveData, columns=self.mycolumns)
        data.to_csv(self.brandName + '.csv', encoding=self.myencoding, index=True)
# end class ChickenStore



from itertools import count
#from ChickenUtil import ChickenStore
############################################################################
brandName = 'pelicana'
base_url = 'https://www.pelicana.co.kr/store/stroe_search.html'
############################################################################
def getData():
    savedData = []  # 액셀로 저장될 중첩 리스트 구조
    for page_idx in count():
        url = base_url + '?page=' + str(page_idx + 1)
        # print( url )
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        mytable = soup.find('table', attrs={'class': 'table mt20'})
        mytbody = mytable.find('tbody')
        # print(len(mytbody.findAll('tr')))

        shopExists = False  # 매장 목록이 없다고 가정

        for mytr in mytbody.findAll('tr'):
            shopExists = True
            mylist = list(mytr.strings)
            # print(mylist)
            # print('*' * 30)

            store = mylist[1]
            address = mylist[3]
            # print('{' + address + '}')

            imsiphone = mytr.select_one('td:nth-of-type(3)').string
            if imsiphone is not None:
                phone = imsiphone.strip()
            else:
                phone = ""

            if len(address) >= 2:
                imsi = address.split()
                sido = imsi[0]      # 주소의 시/도
                gungu = imsi[1]     # 주소의 군/구

                mydata = [brandName, store, sido, gungu, address, phone]
                # print(mydata)
                savedData.append(mydata)

        # print('*' * 30)
        if shopExists == False:
            chknStore.save2Csv(savedData)
            break
        # if page_idx >= 2:
        #     chknstore.save2Csv(savedData)
        #     break
############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')
