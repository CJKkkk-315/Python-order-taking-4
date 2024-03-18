import csv
data = [i.replace('\n','') for i in open('Neutron_20220831.txt').readlines() if '--' in i]
li = []
for i in data:
    row = i.split(':')
    li.append(int(row[0].strip().split('--')[1]))
maxindex = max(li)
res = [[] for _ in range(maxindex)]
for i in data:
    row = i.split(':')
    index = row[0].strip().split('--')
    value = row[1].strip().split()
    for v,j in zip(value,range(int(index[0]),int(index[1])+1)):
        res[j-1].append(v)
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)