import pandas as pd
s = list(pd.read_excel('use.xlsx').values)
d = {}
tag = 0
for i in s:
    for j in i[0].split('|'):
        jj = j.replace(' ','')[:4]
        if jj not in d:
            d[jj] = tag
            tag += 1
res = [[0 for _ in range(len(d))] for _ in range(len(d))]
for i in s:
    ii = [l.replace(' ','')[:4] for l in i[0].split('|')]
    for j in ii:
        for k in ii:
            if j != k:
                res[d[j]][d[k]] += 1
for i in range(len(res)):
    for j in d:
        if d[j] == i:
            res[i].insert(0,j)
head = ['']
for i in range(len(list(d))):
    if d[list(d)[i]] == i:
        head.append(list(d)[i])
res.insert(0,head)
import csv
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)

