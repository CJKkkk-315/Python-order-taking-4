import requests
import csv
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
res = [['标题','介绍','总价','单价']]
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
for k in range(1, 10):
    response = requests.get(f'https://sy.lianjia.com/ershoufang/pg{k}/',headers=headers)
    result = response.text
    soup = BeautifulSoup(result)
    for i in soup.find(class_='sellListContent').find_all(name='li'):
        aw = []
        title = i.find(class_='title').find('a').text
        info = i.find(class_='houseInfo').text
        price = i.find(class_='totalPrice2').text
        uprice = i.find(class_='unitPrice').text
        aw.append(title)
        aw.append(info)
        aw.append(price)
        aw.append(uprice)
        res.append(aw[:])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(res)
for i in res[1:]:
    i[-2] = float(i[-2].replace('万',''))
plt.figure(figsize=(16, 8))
sns.histplot(data=[i[-2] for i in res[1:]], kde=True, bins=80)
plt.xlabel('房屋总价')
ax=plt.gca()
ax.xaxis.set_major_locator(plt.MultipleLocator(10))
plt.xlim(0,200)
plt.ylabel('频数')
plt.title('房屋总价分布图直方图及平滑曲线')
plt.show()