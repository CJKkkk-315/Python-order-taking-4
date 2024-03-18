import requests
from bs4 import BeautifulSoup
import warnings
import os
import pandas as pd
import _thread
import time
warnings.filterwarnings('ignore')
word = ''
ress = []
dataset = [i for i in os.listdir() if i.split('.')[-1] == 'xlsx'][0]
df = pd.read_excel(dataset,header=None).values.tolist()
key_words = [i for i in df if i]
flagaa = 0
xwords = [[] for _ in range(10)]
for i in range(len(key_words)):
    xwords[i%10].append(key_words[i])
def function(xid,key_words):
    global flagaa
    for xxword in key_words:
        word = xxword[0]
        try:
            url = "https://trademarksoncall.com/mark_search.php"

            payload = f"page=1&query=search&searchMark={word}"
            headers = {
              'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            }

            response = requests.request("POST", url, headers=headers, data=payload, verify=False)
            soup = BeautifulSoup(response.text)
            nt = []
            names = [i.text.lower() for i in soup.find_all(name='h2')]
            tags = [i.find(name='p').text.split('Status ')[1] for i in soup.find_all(class_='content')]
            for i,j in zip(names,tags):
                nt.append([i,j])
            nt = [i for i in nt if i[0].strip() == word.lower()]
            nt = ''.join([i[1] for i in nt])
            re_word = ['REGISTERED', 'ACCE', 'STATEMENT OF USE - TO EXAMINER', 'AFTER', 'FOURTH', 'Live', 'Approved']
            rflag = 1
            for rword in re_word:
                if rword.lower() in nt.lower():
                    ress.append(xxword + [0])
                    print(xxword + [0])
                    rflag = 0
                    break
            if rflag:
                ress.append(xxword + [1])
                print(xxword + [1])
        except:
            ress.append([word, ''])
            print([word, ''])
    flagaa += 1
for i in range(10):
    _thread.start_new_thread(function, (i,xwords[i],))
while 1:
    time.sleep(1)
    if flagaa == 10:
       break
import csv
with open('res2.csv','w',newline='',encoding='utf8') as f:
    f_csv = csv.writer(f)
    for i in ress:
        try:
            f_csv.writerow(i)
        except:
            f_csv.writerow(i[:-1] + [''])