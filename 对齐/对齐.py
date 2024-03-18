import pandas as pd
import csv
import datetime
import time
df = pd.read_excel('2022年合并的.xlsx')
res = []
all_c = [i for i in list(df.columns) if 'name' not in i]
now_c = all_c[:]
res.append(all_c)
data = df.values.tolist()
data = [[j if str(j) != 'nan' else '' for j in i] for i in data]

for i in data:
    flag = 0
    if '断面名称' in i:
        flag = 1

    if flag:
        # print(i)
        aw = all_c[::]
        print(all_c)
        # time.sleep(1)
        for j in i:
            if j not in aw and j != '':
                aw.append(j)
        all_c = aw[::]
        now_c = i[::]
        res.append(all_c)
        # print(all_c)
    else:
        # print(len(now_c),len(i))
        row = ['' for _ in range(len(all_c))]
        tt = 0
        for k in all_c:
            if k in now_c:
                ttc = i[now_c.index(k)]
                try:
                    ttc = ttc.strftime('%Y/%m/%d')
                except:
                    pass
                row[all_c.index(k)] = ttc
                tt += 1
            else:
                row[all_c.index(k)] = ''
        res.append(row)
with open('res.csv','w',newline='',encoding='utf8') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
# for i in res:
#     print(i)
