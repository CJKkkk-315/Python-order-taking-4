import csv
data = [i for i in csv.reader(open('res.csv'))]
res = [[] for i in range(5)]
for i in data:
    flag = 1
    if '天窗漏水' in i[5]:
        res[0].append(i)
        flag = 0
    if '车身漏水' in i[5]:
        res[1].append(i)
        flag = 0
    if '空调问题' in i[5]:
        res[2].append(i)
        flag = 0
    if '车灯进水' in i[5]:
        res[3].append(i)
        flag = 0
    if flag:
        res[4].append(i)

with open('天窗漏水.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(res[0])


with open('车身漏水.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(res[1])


with open('空调问题.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(res[2])


with open('车灯进水.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(res[3])


with open('其他.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(res[4])