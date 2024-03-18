import pandas as pd
from datetime import datetime, timedelta
import csv
df = pd.read_excel('小时均值l2016年11月_97点位.xlsx')
c = df.columns
data = df.values
ids = {}
for i in data:
    ids[i[0]] = {}
for i in ids:
    d = {}
    s = '2016-11-01'
    h = 9
    while True:
        while True:
            sh = str(h)
            if len(sh) == 1:
                sh = '0' + sh
            d[s+' '+sh] = [0,0,0]
            if h == 23:
                h = 0
                break
            h += 1

        date = datetime.strptime(s,'%Y-%m-%d')
        new_date = date + timedelta(days=1)
        s = new_date.strftime('%Y-%m-%d')
        if s == '2016-12-01':
            break
    ids[i] = d

res = []

for i in data:
    ids[i[0]][i[1]] = [i[2],i[3],i[4]]
for i in ids:
    for d in ids[i]:
        res.append([i,d,ids[i][d][0],ids[i][d][1],ids[i][d][2]])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
