import csv

import requests
from bs4 import BeautifulSoup
url1 = 'https://jinrong.swufe.edu.cn/szdw/teachers/jrx.htm'
url2 = 'https://jinrong.swufe.edu.cn/szdw/teachers/bxyjsx.htm'
url3 = 'https://jinrong.swufe.edu.cn/szdw/teachers/zqyqhx.htm'
url4 = 'https://jinrong.swufe.edu.cn/szdw/teachers/jrgcyjrkjx.htm'
url5 = 'https://jinrong.swufe.edu.cn/szdw/xzjf.htm'
ans = []
for url in [url1,url2,url3,url4,url5]:
    res = requests.get(url)
    res.encoding = 'utf8'
    soup = BeautifulSoup(res.text)
    for i in soup.find_all(class_='teas'):
        name = i.find(class_='a1').text
        print(f'正在下载{name}老师信息')
        detail_url = 'https://jinrong.swufe.edu.cn/' + i.find(name='a')['href'][6:]
        if url == url5:
            em = '无邮箱信息'
            ans.append([name, detail_url, em])
            continue
        detail_res = requests.get(detail_url)
        detail_res.encoding = 'utf8'
        detail_soup = BeautifulSoup(detail_res.text)
        content = detail_soup.find(class_='t-content').text
        idx = content.find('@swufe.edu.cn')
        if idx == -1:
            em = '无邮箱信息'
        else:
            em = '@swufe.edu.cn'
            t = -1
            while True:
                if content[idx+t].isalpha() or content[idx+t].isdigit():
                    em = content[idx+t] + em
                    t -= 1
                else:
                    break
        ans.append([name,detail_url,em])

with open('ans.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(ans)