import os
files = [f for f in os.listdir() if f.split('.')[1] == 'slk']
name = 'LW_LT'
files.sort(key=lambda x:int(x.replace(name,'').replace('.slk','')))
c = 'L'
c = ord(c) - ord('A') + 1
srow = 2
erow = 202
res = []
for file in files:
    row = []
    data = [i.replace('\n','').split(';') for i in open(file).readlines() if i.replace('\n','').split(';')[0] == 'C']
    y = data[0][1]
    for i in data:
        if 'Y' not in i[1]:
            i.insert(1,y)
        y = i[1]
        if int(i[2].replace('X','')) == c and erow >= int(i[1].replace('Y','')) >= srow:
            row.append(i[-1].replace('K','').replace('"',''))
    res.append(row[::])

import csv
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)


