import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
headers = {
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
response = requests.get('http://www.tianqihoubao.com/lishi/',headers=headers)
response.encoding = 'gbk'
soup = BeautifulSoup(response.text)
res = []
d = {}
for i in soup.find(class_='citychk').find_all('dl'):
    p = i.find(name='dt').text
    for j in i.find(name='dd').find_all(name='a'):
        res.append([p,j.text])
        if p not in d:
            d[p] = 0
            d[p] += 1
        else:
            d[p] += 1


data = []
for i,j in d.items():
    data.append([i,j])
data2 = []
for i in data:
    if i[1] != 1:
        data2.append(i)
labels = [i[0] for i in data2]
x = [i[1] for i in data2]
plt.pie(labels=labels,x=x)
plt.title('全国各省份城市数量对比')
plt.show()
import csv
with open('res3.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)

