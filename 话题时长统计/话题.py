from datetime import datetime
import csv
import matplotlib.pyplot as plt
def time_difference_minutes(time_str1, time_str2, time_format='%Y/%m/%d %H:%M'):
    # print(time_str1)
    time1 = datetime.strptime(time_str1, time_format)

    time2 = datetime.strptime(time_str2, time_format)
    time_difference = abs(time2 - time1)
    return time_difference.total_seconds() // 60
data = []
with open('1号楼组群(21444913089@chatroom).csv',encoding='utf8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = data[1:]
start_time = data[0][1]
now = [[start_time],[data[0][2]]]
res = []
for row in data[1:]:
    if time_difference_minutes(start_time,row[1]) > 10:
        now[0].append(start_time)
        res.append(now[::])
        now = [[row[1]],[row[2]]]
    else:
        now[1].append(row[2])
    start_time = row[1]
rres = []
idx = 1
for i in res:
    rres.append([idx,'-'.join(i[0]),len(i[1]),' '.join(i[1])])
with open('res.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(['编号','持续时间','数量','内容'])
    f_csv.writerows(rres)
# minutes_difference = time_difference_minutes(time_str1, time_str2)


x = [datetime.strptime(i[1].split('-')[0], '%Y/%m/%d %H:%M') for i in rres]
y = [i[2] for i in rres]
plt.plot(x,y)
plt.show()

x = [datetime.strptime(i[1].split('-')[0], '%Y/%m/%d %H:%M') for i in rres]
y = [i[2] for i in rres]
plt.plot(x,y)
plt.show()