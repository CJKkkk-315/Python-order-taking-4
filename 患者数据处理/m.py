import pandas
df = pandas.read_csv('nta_1.csv')
df = df[['fid','sid1','SID2','twinSex','twinRace','zyg','agrade','bgrade','cgrade','dgrade','egrade','age1sq','w1age1','bagesq1','bw1age1','cagesq1','cw1age1','dagesq1','dw1age1','eagesq1','ew1age1']]
data = df.values.tolist()
# print(data)
res = []
for i in data:
    if 0 in i[6:11] and 3 in i[6:11]:
        a = i[6:11].index(0)
        b = i[6:11].index(3)
        res.append(i[:6]+[chr(ord('a')+a) + ' grade=' + str(i[6+a])]+i[6+a+5:6+a+7]+[chr(ord('a')+b) + ' grade=' + str(i[6+b])]+i[6+b+b+5:6+b+b+7])
for i in res:
    print(*i,sep=',')
    print()
import csv
head = ['fid','sid1','SID2','twinSex','twinRace','zyg','grade','IQ','age','grade','IQ','age']
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in res:
        f_csv.writerow(i)
