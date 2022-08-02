from itertools import count
from urllib.request import urlopen
from bs4 import BeautifulSoup

for page_idx in count():
    base_url = "https://www.hyundai-steel.com/kr/recruitinformation/recruit/allList.hds?&searchGubunType4=240"
    url = base_url + '&page=' + str(page_idx + 1)
    html = urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    html_class = soup.find_all(class_='cont')
    print(len(html_class))

    if len(html_class) == 0:
        break
    if page_idx > 100:
        break

    for tit in html_class:
        title = tit.text.strip()
        print(title)
