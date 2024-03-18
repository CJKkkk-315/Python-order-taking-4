import csv
import os
res = []
files = os.listdir('data')
for file in files:
    n = []
    content = open('data/' + file,encoding='utf8').read().split('\n')
    for i in content:
        n.append(len(i))
    res.append([file,sum(n)/len(n)])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)