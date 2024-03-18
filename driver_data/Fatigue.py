import matplotlib.pyplot as plt
import os
from datetime import datetime
records = []
files = os.listdir('driving-records')
for file in files:
    with open('driving-records/' + file,encoding='utf8') as f:
        data = f.read().split('\n')
        for row in data:
            if row:
                records.append(row.split(',')[:19])
for i in range(len(records)):
    while len(records[i]) < 19:
        records[i].append('')
    for j in range(len(records[i])):
        if records[i][j] == '':
            records[i][j] = 0

withtime = {}
for record in records:
    if record[-3]:
        h = datetime.strptime(record[7], '%Y-%m-%d %H:%M:%S').hour
        withtime[h] = withtime.get(h,0) + 1
x = [k for k in withtime.keys()]
y = [v for v in withtime.values()]
plt.bar(x,y)
plt.xlabel('Hour')
plt.ylabel('Fatigue driving times')
plt.title('fatigue with time')
plt.show()

withspeed = {i:0 for i in range(20,180,20)}
for record in records:
    if record[-3]:
        h = (int(record[4])//20 + 1) * 20
        withspeed[h] = withspeed.get(h,0) + 1
xy = [[k,v] for k,v in withspeed.items()]
xy.sort()
x = [v[0] for v in xy]
y = [v[1] for v in xy]
plt.plot(x,y)
plt.xlabel('Speed')
plt.ylabel('Fatigue driving times')
plt.title('fatigue with speed')
plt.show()

withother = {}
for record in records:
    d = datetime.strptime(record[7], '%Y-%m-%d %H:%M:%S').date()
    if d not in withother:
        withother[d] = [0,0,0]
    if record[-3]:
        withother[d][0] += 1
    if record[-6]:
        withother[d][1] += 1
    if record[-9]:
        withother[d][2] += 1
x = [str(k) for k in withother.keys()]
print(x)
plt.plot(x,[i[0] for i in withother.values()],label='fatigue')
plt.plot(x,[i[1] for i in withother.values()],label='overspeed')
plt.plot(x,[i[2] for i in withother.values()],label='neutralslide')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Fatigue driving times')
plt.title('fatigue with other factor')
plt.show()