import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import _thread
import time
import pandas as pd
import csv
delay = int(input('延迟秒数：'))
bf = int(input('并发数量'))
ress = []
with open('res.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        ress.append(i)
ress_name = [i[0] for i in ress]
print(os.listdir())
dataset = [i for i in os.listdir() if i.split('.')[-1] == 'xlsx'][0]
df = pd.read_excel(dataset,header=None).values.tolist()
key_words = [i[0] for i in df if i and i[0] not in ress_name]
print(key_words)
print(len(key_words))
xwords = [[] for _ in range(bf)]
for i in range(len(key_words)):
    xwords[i%bf].append(key_words[i])
flagaa = 0
start_time = time.perf_counter()
op = webdriver.ChromeOptions()
op.add_argument('--headless')
def function(xid,key_words):
    global flagaa
    global ress
    driver = webdriver.Chrome(executable_path='chromedriver.exe')
    idx = 0
    while idx < len(key_words):
        word = key_words[idx]

        driver.get(f'https://branddb.wipo.int/en/similarname/results?strategy=exact&brandName={word}&fcdesignation=US&fcdesignation=MX&fcdesignation=CA&fcstatus=Registered')
        time.sleep(delay)
        while True:
            try:
                a = driver.find_element(by=By.XPATH,value='/html/body/app-root/div/div/page-results/page-results/div/results-info/div[3]/div').text
                if a == 'No results found!':
                    ress.append([word,'未注册'])
                    print([word,'未注册'])
                else:
                    ress.append([word, '已注册'])
                    print([word, '已注册'])
                break
            except:
                a = driver.find_element(by=By.XPATH,value='/html/body/app-root/div/div/page-similarname/div/w-edit-panel[1]/div[1]/w-section/div[2]/w-slot/div/w-input-radio/fieldset/table/tr[1]/td/label').text
                print(a)
                if 'Exact' in a:
                    flagaa += 1
                    return
                else:
                    pass
        idx += 1

    flagaa += 1
for i in range(bf):
    _thread.start_new_thread(function, (i,xwords[i],))
while 1:
    time.sleep(1)
    if flagaa == bf:
       break
print(ress)
end_time = time.perf_counter()
run_time = (end_time - start_time)
print(run_time)
with open('res.csv','a+',newline='') as f:
    f_csv = csv.writer(f)
    for i in ress:
        print(i)
        f_csv.writerow(i)