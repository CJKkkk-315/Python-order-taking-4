import requests
from bs4 import BeautifulSoup
import csv
import time as ttt
import random

data = []
payload = {}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
  'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'Connection': 'keep-alive',
  'Cookie': 'll="118172"; bid=JRq3LxP8Vn0; __yadk_uid=nIbiOOSAOZnM82HLEZMPzjzemaEe9v8T; douban-fav-remind=1; viewed="2255896"; gr_user_id=0fca241c-afa0-4f67-a4b4-7ab7861f3813; _pk_id.100001.8cb4=c99e6492e055a11e.1666335020.; __gads=ID=6d07164c31bdfa21-22fd05c524d900e7:T=1672501335:RT=1691948216:S=ALNI_MYNjqMivxkobEh_1huk6Z4Dx4Z0pg; __gpi=UID=00000b9b73bc6b76:T=1672501335:RT=1691948216:S=ALNI_MZm_YMKp9ffiHXVUF77B08Jf6xfyQ; push_noty_num=0; __utmz=30149280.1695018550.41.24.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; dbcl2="220718836:JguSCVOlSns"; __utmv=30149280.22071; ck=8zH1; _pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1696830012%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DCriFnaNFY5409kPgADx4I5KlvqJ1jzVZmP-rUrMv6LUts3za9GMjNivsL_NuHsAi%26wd%3D%26eqid%3Df72ee34900166a2c000000056507ee32%22%5D; _pk_ses.100001.8cb4=1; ap_v=0,6.0; __utma=30149280.678084391.1666598591.1696508182.1696830012.44; __utmc=30149280; push_doumail_num=0; __utmt=1; ct=y; __utmb=30149280.113.5.1696830019290',
  'Referer': 'https://www.douban.com/doumail/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60',
  'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}

for page in range(1020,1450,20):
    ttt.sleep(random.randint(1,3))
    try:
        url = f"https://www.douban.com/doumail/?start={page}"
        response = requests.request("GET", url, headers=headers, data=payload)
        soup = BeautifulSoup(response.text)
        for i in soup.find(class_='doumail-list').find(name='ul').find_all(name='li'):
            try:
                name = i.find(class_='sender').find(class_='from').text
                time = i.find(class_='sender').find(class_='time').text
                href = i.find(name='p').find(name='a')['href']
                talk = requests.request("GET", href, headers=headers, data=payload)
                talk_soup = BeautifulSoup(talk.text)
                bd = talk_soup.find(class_='doumail-bd')
                content = ' '.join([j.find(class_='content').find(name='p').text for j in bd.find_all(class_='chat')])
                print(name, time, content)
                data.append([name,time,content])
            except:
                continue
    except:
        print(page)
        break
with open('res.csv', 'w', encoding='utf8', newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(data)
