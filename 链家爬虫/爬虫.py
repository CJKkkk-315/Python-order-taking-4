import requests
from bs4 import BeautifulSoup
import csv
url = 'https://jn.lianjia.com/ershoufang/licheng/mw1de1ie2dp1p3/'
response = requests.get(url).text
soup = BeautifulSoup(response)
res = []
for i in soup.find(class_='sellListContent').find_all(name='li'):
    row = []
    name = i.find(class_='title').find(name='a').text
    print(name)
    row.append(name)
    price = i.find(class_='totalPrice2').find(name='span').text
    print(price)
    content = i.find(class_='houseInfo').text
    print(content)
    row.extend(content.split('|'))
    uprice = i.find(class_='unitPrice').text
    print(uprice)
    row.append(uprice)
    row.append(float(price))
    res.append(row)
res.sort(key=lambda x:x[-1])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)

    for i in res:
        f_csv.writerow(i)