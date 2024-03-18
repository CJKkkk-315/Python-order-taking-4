import requests
import os
from bs4 import BeautifulSoup
urls = [i for i in open('urls.txt').read().split('\n') if i]
files = os.listdir('zip文件')
# print(files)
for url in urls:
    uid = url.split('soft/')[1].split('.')[0]
    res = requests.get(url)
    soup = BeautifulSoup(res.text)
    title = soup.find(name='title').text.replace('-学科网','') + '.zip'
    if title in files:
        os.rename(f'zip文件/{title}',f'zip文件/[{uid}]{title}')
