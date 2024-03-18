import pandas as pd
import csv
data = pd.read_excel('2023.5.1-11 shuju.xlsx',sheet_name='Sheet1',header=None)
data = data.values.tolist()[:]
for i in data:
    i[0] = str(i[0]).split()[1]
for i in data[:100]:
    print(i)
now = 0
for i in range(len(data)):
    if data[i][0][-5:] in ['00:59','15:59','30:59','45:59']:
        now = 181
    idx = 181 - now
    if now:
        aw = []
        for j in range(1,13,2):
            aw += [idx,round(data[i][j] - data[i-idx][j],2), round(data[i][j+1] - data[i-idx][j+1],2)]
        data[i] += aw
        now -= 1
    else:
        data[i] += ['','',''] + ['','',''] + ['','',''] + ['','',''] + ['','',''] + ['','','']
for i in range(len(data)):
    data[i] = data[i][:3] + data[i][-18:-15] + data[i][3:5] + data[i][-15:-12] + data[i][5:7] + data[i][-12:-9] + data[i][7:9] + data[i][-9:-6] + data[i][9:11] + data[i][-6:-3] + data[i][11:13] + data[i][-3:]
with open('计算结果.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(data)