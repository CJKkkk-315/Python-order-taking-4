import pandas as pd
import csv
df = pd.read_excel('煤场信号源整理.xlsx')
head = list(df.columns.values)
head[0] = ''
head.append('汽车沟1B路上煤')
head.append('汽车沟2B路上煤')
head.append('煤场#1B路上煤情况')
head.append('煤场#2B路上煤情况')
data = list(df.values.tolist())
for i in range(36,len(data)):
    if data[i][3]:
        if (data[i-36][4] or data[i-36][5]) and data[i-36][6] and (data[i-36][8] or data[i-36][10]):
            data[i].append(1)
        else:
            data[i].append(0)

for i in range(36,len(data)):
    if data[i][3]:
        if (data[i-36][11] or data[i-36][12]) and data[i-36][13] and (data[i-36][8] or data[i-36][10]):
            data[i].append(1)
        else:
            data[i].append(0)

for i in range(36,len(data)):
    if data[i][3]:
        if data[i-18][15] and (data[i-18][8] or data[i-18][10]):
            data[i].append(1)
        else:
            data[i].append(0)

for i in range(36,len(data)):
    if data[i][3]:
        if data[i-12][19] and data[i-12][21]:
            data[i].append(1)
        else:
            data[i].append(0)

with open('res.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    for i in data:
        fcsv.writerow(i)

res_dic = {}
for i in range(len(data)):
    res_dic[str(data[i][1]).split()[0]] = [0,0,0,0]
for i in range(36,len(data)):
    if data[i][3] and sum(data[i][-4:]):
        number = data[i][3]/sum(data[i][-4:])
        print(number)
        if data[i][-1]:
            res_dic[str(data[i][1]).split()[0]][-1] += number
        if data[i][-2]:
            res_dic[str(data[i][1]).split()[0]][-2] += number
        if data[i][-3]:
            res_dic[str(data[i][1]).split()[0]][-3] += number
        if data[i][-4]:
            res_dic[str(data[i][1]).split()[0]][-4] += number

head = ['日期','汽车沟1上煤量','汽车沟2上煤量','煤场1上煤量','煤场2上煤量']
with open('res_all.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerow(head)
    for key in res_dic:
        fcsv.writerow([key,*res_dic[key]])