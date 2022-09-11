from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import urllib
import requests
import json
from xml.etree.ElementTree import parse
import xmltodict

#공공API정보 : https://www.data.go.kr/iim/api/selectAPIAcountView.do

API_KEY = 'Akl7ieBMu6umhvzoapVA4n+9CSYKva70qyPxXZbZMXBNB7d+wpQwpiLzzoGtfVp1Jts0pVXtuEzH6tdLBmS7pA=='
API_KEY_ENC = 'Akl7ieBMu6umhvzoapVA4n%2B9CSYKva70qyPxXZbZMXBNB7d%2BwpQwpiLzzoGtfVp1Jts0pVXtuEzH6tdLBmS7pA%3D%3D'
pageNo = '1'
numOfRows = '10'
LAWD_CD= '11440' #각 지역별 코드 행정표준코드관리시스템 (www.code.go.kr)의 법정동코드 10자리중 앞 5자리
#LAWD_CD= '11110' #각 지역별 코드 행정표준코드관리시스템 (www.code.go.kr)의 법정동코드 10자리중 앞 5자리
DEAL_YMD= '202208'
DATA_TYPE= 'JSON'
URL_BASE = 'http://openapi.molit.go.kr/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTradeDev'
URL = URL_BASE+'?'+'pageNo='+pageNo+'&'+'numOfRows='+numOfRows+'&'+'LAWD_CD='+LAWD_CD+'&'+'DEAL_YMD='+DEAL_YMD+'&'+'dataType='+DATA_TYPE+'&'+'serviceKey='+API_KEY_ENC

response = requests.get(URL) 
status = response.status_code 
text = response.text
print('========================================================================================')
print(URL)
print('========================================================================================')
print(text)
print('========================================================================================')

#root = ET.fromstring(response.text)
#print(root)
#for item in root.iter('item'):
#    print(item.attrib.get('거래금액'))
#

request = urllib.request.Request(URL)
response_body = urlopen(request, timeout=60).read() # get bytes data
decode_data = response_body.decode('utf-8')
#print(type(decode_data))
xml_parse = xmltodict.parse(decode_data)     # string인 xml 파싱
xml_dict = json.loads(json.dumps(xml_parse))
item_len=len(xml_dict['response']['body']['items']['item'])
print('item_len::'+str(item_len))
if item_len > 1:
    for i in range(0,item_len):
        print('========================================================================================')
        print(xml_dict['response']['body']['items']['item'][i])
        print('========================================================================================')
        print(xml_dict['response']['body']['items']['item'][i]['거래금액'])
        print(xml_dict['response']['body']['items']['item'][i]['건축년도'])
        print(xml_dict['response']['body']['items']['item'][i]['년'])
        print(xml_dict['response']['body']['items']['item'][i]['법정동'])
        print(xml_dict['response']['body']['items']['item'][i]['아파트'])
        print(xml_dict['response']['body']['items']['item'][i]['월'])
        print(xml_dict['response']['body']['items']['item'][i]['일'])
else:
        print('========================================================================================')
        print(xml_dict['response']['body']['items']['item'])
        print('========================================================================================')
        print(xml_dict['response']['body']['items']['item']['거래금액'])
        print(xml_dict['response']['body']['items']['item']['건축년도'])
        print(xml_dict['response']['body']['items']['item']['년'])
        print(xml_dict['response']['body']['items']['item']['법정동'])
        print(xml_dict['response']['body']['items']['item']['아파트'])
        print(xml_dict['response']['body']['items']['item']['월'])
        print(xml_dict['response']['body']['items']['item']['일'])
 
print('========================================================================================')