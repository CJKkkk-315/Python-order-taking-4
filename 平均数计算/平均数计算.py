import csv
with open('EastOrientation.csv') as f:
    f_csv = csv.reader(f)
    data = [i[1:-6] for i in f_csv]
col = data[:2]
data = data[2:]
step = 0.5
data = [list(map(float,i)) for i in data]
print(data)
d = {}
now = 0
while now < max([j[0] for j in data]):
    d[round(now,3)] = []
    now += step
print(d)
nn = 0
for i in data:
    d[round((i[0]//step)*step,3)].append(i[1:])
    nn = len(i[1:])
for key in d:
    aw = [0 for _ in range(nn)]
    s = 0
    for i in d[key]:
        t = 0
        for j in i:
            aw[t] += j
            t += 1
        s += 1
    if sum(aw) != 0:
        for i in range(len(aw)):
            aw[i] /= s
    d[key] = aw[:]
for i in range(int(max([j[0] for j in data]))+1):
    try:
        col.append([i*step] + d[i*step])
    except:
        pass
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(col)