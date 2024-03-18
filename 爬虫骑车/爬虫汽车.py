import requests
from bs4 import BeautifulSoup
url = 'https://www.cn357.com/notice_6'
res = requests.get(url)

soup = BeautifulSoup(res.text)
for i in soup.find_all(name='tr'):
    print(i)