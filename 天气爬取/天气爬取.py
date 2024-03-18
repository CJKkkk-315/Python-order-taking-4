import requests
from bs4 import BeautifulSoup
import csv
headers = {

        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }
data = []

for year in [2019,2020,2021]:
    for mouth in range(1,13):
        if len(str(mouth)) == 1:
            mouth = '0' + str(mouth)
        res = requests.get(f'https://lishi.tianqi.com/yinchuan/{year}{mouth}.html',headers=headers)
        soup = BeautifulSoup(res.text)
        for i in soup.find(class_='thrui').find_all(name='li'):
            row = []
            row.append(i.find_all(name='div')[0].text.split()[0])
            row.append(i.find_all(name='div')[1].text)
            row.append(i.find_all(name='div')[2].text)
            row.append(abs(int(i.find_all(name='div')[1].text.replace('℃',''))-int(i.find_all(name='div')[2].text.replace('℃',''))))
            data.append(row)
for mouth in range(1,10):
    if len(str(mouth)) == 1:
        mouth = '0' + str(mouth)
    res = requests.get(f'https://lishi.tianqi.com/yinchuan/2022{mouth}.html',headers=headers)
    soup = BeautifulSoup(res.text)
    for i in soup.find(class_='thrui').find_all(name='li'):
        row = []
        row.append(i.find_all(name='div')[0].text.split()[0])
        row.append(i.find_all(name='div')[1].text)
        row.append(i.find_all(name='div')[2].text)
        row.append(abs(int(i.find_all(name='div')[1].text.replace('℃', '')) - int(i.find_all(name='div')[2].text.replace('℃', ''))))
        data.append(row)
with open('银川.csv','w',encoding='gbk',newline='') as f:
    f_csv = csv.writer(f)
    for i in data:
        f_csv.writerow(i)