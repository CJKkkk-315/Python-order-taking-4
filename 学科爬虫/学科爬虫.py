import requests
from bs4 import BeautifulSoup
urls = []
all_urls = open('主链接.txt').read().split('\n')
for uu in all_urls:
    res = requests.get(uu)
    soup = BeautifulSoup(res.text)
    tt = res.text
    tt = tt.split('href=')

    for i in tt:
        if 'www.zxxk.com/soft/' in i.split('.html')[0]:
            urls.append('http://www.' + i.split('.html')[0].split('www.')[1] + '.html')

            # urls.append('http://' + i.split('.html')[0][3:] + '.html')
with open('urls.txt','w') as f:
    for url in urls:
        f.write(url + '\n')
