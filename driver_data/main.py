import os
import csv
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

driver_set = {}
driver_speed = {}
for record in records:
    if record[0] not in driver_set:
        driver_set[record[0]] = [0 for _ in range(7)]
    if record[0] not in driver_speed:
        driver_speed[record[0]] = []
    if record[-6]:
        driver_set[record[0]][0] += 1
    if record[-3]:
        driver_set[record[0]][1] += 1
    if record[-9]:
        driver_set[record[0]][2] += 1
    if record[-11]:
        driver_set[record[0]][3] += 1
    if record[-10]:
        driver_set[record[0]][4] += 1
    if record[-4]:
        driver_set[record[0]][5] += int(record[-4])
    if record[-7]:
        driver_set[record[0]][6] += int(record[-7])
    driver_speed[record[0]].append(int(record[4]))
print('Total records:',len(records))
print('Total drivers:',len(driver_set))


head = ['driverID','Overspeed','FatigueDriving','neutralSlide','RapidlySpeedup','RapidlySlowdown','overspeedTime','neutralSlideTime']
with open('behavior_statistics.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for key in driver_set:
        f_csv.writerow([key] + driver_set[key])


