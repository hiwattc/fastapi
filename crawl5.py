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
import re

############################################################################
brandName = 'nene'
base_url = 'https://nenechicken.com/17_new/sub_shop01.asp'


############################################################################
def getData():
    savedData = []
    for page_idx in range(1, 45 + 1):
        url = base_url + '?page=%d' % page_idx
        chknStore = ChickenStore(brandName, url)
        soup = chknStore.getSoup()

        tablelist = soup.findAll('table', attrs={'class': 'shopTable'})
        # print(len(tablelist))
        # print(page_idx)
        for onetable in tablelist:
            store = onetable.select_one('.shopName').string
            temp = onetable.select_one('.shopAdd').string

            im_address = onetable.select_one('.shopMap')
            im_address = im_address.a['href']
            # print(im_address)

            if temp == None:    # shopAdd가 없는 항목
                apos = im_address.find("(")
                dpos = im_address.find(")")
                temp = im_address[apos+1:dpos].replace("'", "")
                address = temp
                sido = ''
                gungu = ''
            else:
                regex = '\d\S*'  # 숫자로 시작하고   # \s : white Character # \S : 눈에 보이는 모든 글자
                pattern = re.compile(regex)
                mymatch = pattern.search(im_address)
                # print(mymatch)

                addr_suffix = mymatch.group().replace("');", "")
                address = temp + ' ' + addr_suffix
                # print(address)

                imsi = temp.split(' ')
                sido = imsi[0]
                gungu = imsi[1]
            # end if
            # print(store + '/' + temp)

            phone = onetable.select_one('.tooltiptext').string

            mydata = [brandName, store, sido, gungu, address, phone]
            savedData.append(mydata)

            print('-' * 30)

            if page_idx == 3:
                break

    chknStore.save2Csv(savedData)


############################################################################
print(brandName + ' 매장 크롤링 시작')
getData()
print(brandName + ' 매장 크롤링 끝')

