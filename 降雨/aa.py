import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
d = {}
data = []
qid = set()
df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet1').values.tolist()
for i in df:
    if i[5] != '/':
        data.append([i[1],i[5], i[0]])
        qid.add(i[0])
df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet2').values.tolist()
for i in df:
    if i[5] != '/':
        data.append([i[1], i[5], i[0]])
        qid.add(i[0])
df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet3').values.tolist()
for i in df:
    if i[5] != '/':
        data.append([i[1], i[5], i[0]])
        qid.add(i[0])
qidd = ''
d0 = {}
d1 = {}
d2 = {}
d3 = {}
d4 = {}
for i in range(2013,2023):
    d0[str(int(i))] = 0
    d1[str(int(i))] = 0
    d2[str(int(i))] = 0
    d3[str(int(i))] = 0
    d4[str(int(i))] = 0
res = []
for i in range(0,len(data),24):
    res.append([str(int(data[i][0])),sum([j[1] for j in data[i:i+24]])])
for i in res:
    try:
        if i[1] == 0:
            d0[str(int(i[0]))] += 1
        elif i[1] < 9.9:
            d1[str(int(i[0]))] += 1
        elif i[1] < 24.9:
            d2[str(int(i[0]))] += 1
        elif i[1] < 49.9:
            d3[str(int(i[0]))] += 1
        else:
            d4[str(int(i[0]))] += 1
    except:
        print(i)
xy = sorted(d0.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title(qidd + '无雨次数统计图')
plt.show()

xy = sorted(d1.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title(qidd + '小雨次数统计图')
plt.show()

xy = sorted(d2.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title(qidd + '中雨次数统计图')
plt.show()

xy = sorted(d3.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title(qidd + '大雨次数统计图')
plt.show()

xy = sorted(d4.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title(qidd + '暴雨次数统计图')
plt.show()