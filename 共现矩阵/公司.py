import csv
data = []
d = {}
tag = 0
with open('data.csv') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append([j for j in i if j])

for i in data:
    for j in i:
        if j not in d:
            d[j] = tag
            tag += 1

res = [[0 for _ in range(len(d))] for _ in range(len(d))]
for i in data:
    for j in i:
        for k in i:
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