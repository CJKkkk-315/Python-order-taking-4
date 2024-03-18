import requests
from bs4 import BeautifulSoup
import csv
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
head = ['古诗名','内容','解析']
rows = []
url = "https://so.gushiwen.cn/gushi/tangshi.aspx"
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
payload = {}
response = requests.get(url, headers=headers, data=payload)
soup = BeautifulSoup(response.text,'lxml')
d = {}
#爬取唐诗300首诗名，作者及链接
for i in soup.find_all(class_='typecont'):
    for j in i.find_all(name='span'):
        try:
            v1 = j.text
            v2 = j.find(name='a')['href']
            url = v2
            #进入每个链接，获取其中的诗歌内容及解析
            response = requests.get('https://so.gushiwen.cn' + url, headers=headers, data=payload)
            soup1 = BeautifulSoup(response.text, 'lxml')
            v3 = soup1.find(class_='contyishang').find(name='p').text
            v4 = soup1.find(class_='contson').text
            rows.append([v1,v4,v3])
            au = v1.split('(')[1].split(')')[0]
            d[au] = d.get(au, 0) + 1
        except:
            pass
data = sorted(d.items(),key=lambda x:x[1])
data = data[::-1][:20]
plt.bar([i[0] for i in data],[i[1] for i in data])
plt.xlabel('作者')
plt.ylabel('作品数量')
plt.show()
#写入csv
with open('res4.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in rows:
        try:
            f_csv.writerow(i)
        except:
            pass