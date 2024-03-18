import csv
data1 = [i for i in csv.reader(open('123.csv'))]
data2 = [i[0] for i in csv.reader(open('456.csv'))]
res = []
for i in data1:
    if i[4] not in data2:
        res.append(i + ['X'])
    else:
        res.append(i + ['√'])

with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(res)