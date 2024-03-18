import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
d = {}
data = []
# df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet1').values.tolist()
# for i in df:
#     if i[5] != 0 and i[5] != '/':
#         data.append([i[1],i[5]])
# df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet2').values.tolist()
# for i in df:
#     if i[5] != 0 and i[5] != '/':
#         data.append([i[1], i[5]])
# df = pd.read_excel('2013-2022年4-10月气象站1小时降水量.xlsx',sheet_name='Sheet3').values.tolist()
# for i in df:
#     if i[5] != 0 and i[5] != '/':ji
#         data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet1').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet2').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet3').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet4').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet5').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet6').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet7').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
df = pd.read_excel('气象站2，2021-2022年4-10月定时降水量.xlsx',sheet_name='Sheet8').values.tolist()
for i in df:
    if i[5] != 0 and i[5] != '/':
        data.append([i[1], i[5]])
for i in range(2021,2023):
    d[str(int(i))] = 0
for i in data:
    try:
        d[str(int(i[0]))] += i[1]
    except:
        print(i)
xy = sorted(d.items())
plt.bar([i[0]for i in xy],[i[1]/12 for i in xy])
plt.show()

all_rain = 0
all_rain_total = 0
small = []
mid = []
big = []
sup = []
for i in data:
    if i[1] > 0:
        all_rain += 1
        all_rain_total += i[1]
        if i[1] < 9.9:
            small.append(i[1])
        elif i[1] < 24.9:
            mid.append(i[1])
        elif i[1] < 49.9:
            big.append(i[1])
        else:
            sup.append(i[1])

x = ['小雨','中雨','大雨','暴雨']
y = [len(small)/all_rain,len(mid)/all_rain,len(big)/all_rain,len(sup)/all_rain,]
width=0.4
plt.bar([x+width/2 for x in range(4)],y, width=width, label='降雨发生率')
y = [sum(small)/all_rain_total,sum(mid)/all_rain_total,sum(big)/all_rain_total,sum(sup)/all_rain_total,]
plt.bar([x-width/2 for x in range(4)],y, width=width, label='降雨贡献率')
plt.xticks([x+width/2 for x in range(4)], ['小雨','中雨','大雨','暴雨'])
plt.legend()
plt.show()


d1 = {}
d2 = {}
d3 = {}
d4 = {}
for i in range(2013,2023):
    d1[str(int(i))] = 0
    d2[str(int(i))] = 0
    d3[str(int(i))] = 0
    d4[str(int(i))] = 0
for i in data:
    try:
        if i[1] < 9.9:
            d1[str(int(i[0]))] += 1
        elif i[1] < 24.9:
            d2[str(int(i[0]))] += 1
        elif i[1] < 49.9:
            d3[str(int(i[0]))] += 1
        else:
            d4[str(int(i[0]))] += 1
    except:
        print(i)
xy = sorted(d1.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title('小雨次数统计图')
plt.show()

xy = sorted(d2.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title('中雨次数统计图')
plt.show()

xy = sorted(d3.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title('大雨次数统计图')
plt.show()

xy = sorted(d4.items())
plt.bar([i[0] for i in xy],[i[1] for i in xy])
plt.title('暴雨次数统计图')
plt.show()