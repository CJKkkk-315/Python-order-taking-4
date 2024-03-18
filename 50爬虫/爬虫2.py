tag = {'文学':['小说','随笔','日本','文学','散文','诗歌','童话','名著','港台']}
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
res = []
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
for key in tag.keys():
    for subcate in  tag[key]:
        response = requests.get('https://book.douban.com/tag/'+subcate + '?start=20&type=T',headers=headers)
        soup = BeautifulSoup(response.text)
        for i in soup.find(class_='subject-list').find_all(name='li'):
            try:
                name = i.find(name='h2').find(name='a').text.replace('\n','').replace(' ','')
                l = i.find(class_='pub').text.replace('\n','').replace(' ','').split('/')
                writer = l[0]
                price = l[-1]
                time = l[-2]
                p = l[-3]
                score = i.find(class_='rating_nums').text.replace('\n','').replace(' ','')
                hot = i.find(class_='pl').text.replace('\n','').replace(' ','')
                content = i.find(name='p').text.replace('\n','').replace(' ','')
                res.append([name,key,subcate,writer,price,time,p,score,hot,content])
                print([name,key,subcate,writer,price,time,p,score,hot,content])
            except:
                continue
import csv
with open('res2.csv','w',newline='',encoding='utf8') as f:
    fcsv = csv.writer(f)
    for i in res:
        fcsv.writerow(i)

pf = []
for i in res:
    if not i[7]:
        continue
    pf.append(float(i[7]))
plt.figure(figsize=(16, 8))
sns.histplot(data=pf, kde=True, bins=80)
plt.xlabel('图书评分')
ax=plt.gca()
plt.ylabel('频数')
plt.title('图书评分分布图直方图及平滑曲线')
plt.show()