import matplotlib.pyplot as plt
import os
from datetime import datetime
files = os.listdir('driving-records')
name = 'xiezhi1000006'
tt = 1
for file in files:
    records = []
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
    driver_speed = {}
    for record in records:
        if record[0] not in driver_speed:
            driver_speed[record[0]] = []
        driver_speed[record[0]].append([datetime.strptime(record[7], '%Y-%m-%d %H:%M:%S'),int(record[4])])
    day = int(file.split('_')[4])-1
    start = datetime(2017, 1, int(day),8,0,0)
    stop = datetime(2017, 1, int(day),23,30,0)
    key = name
    if key not in driver_speed:
        x = []
        y = []
    else:
        x = [i[0] for i in driver_speed[key][::40]]
        y = [i[1] for i in driver_speed[key][::40]]
    plt.subplot(5,2,tt)
    plt.plot(x,y)
    plt.xlabel('time')
    plt.xlim(start,stop)
    plt.ylabel('speed')
    tt += 1
plt.suptitle(name)
plt.show()
