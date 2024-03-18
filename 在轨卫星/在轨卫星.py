import pandas as pd
import datetime
import csv
df = pd.read_excel('通信卫星.xlsx',sheet_name='Sheet1')
def d_s(date):
    return date.strftime('%Y-%m-%d')
date = [datetime.datetime.strptime(i,'%Y-%m-%d') for i in df['年代'].astype('str')]
res = {}
for i,j in zip(df['寿命'],date):
    stay = {}
    if str(i) == 'nan':
        day = 1
    elif '天' in i:
        day = float(i[:-1])
    elif '月' in i:
        day = float(i[:-1]) * 30
    elif '年' in i:
        day = float(i[:-1]) * 30 * 12
    for d in range(int(day)):
        yy = d_s(j + datetime.timedelta(days=d)).split('-')[0]
        stay[yy] = stay.get(yy,0) + 1
    for key in stay:
        if stay[key] > 180:
            res[int(key)] = res.get(int(key),0) + 1
        else:
            res[int(key)] = res.get(int(key), 0) + 1 / 12
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for key in res:
        if round(res[key]):
            f_csv.writerow([key,round(res[key])])

