from geopy.distance import geodesic
import pandas as pd
import csv
# 读取数据
df1 = pd.read_excel('充电桩和需求点.xlsx',sheet_name='XQD')
df2 = pd.read_excel('充电桩和需求点.xlsx',sheet_name='CDZ')
# 转为列表
xqd = list(df1.values.tolist())
cdz = list(df2.values.tolist())
# 提取需要的列
xqd = [i[1:] for i in xqd]
cdz = [[i[4]] + i[2:4] for i in cdz]
res = []
# 遍历所有需求点
for i in xqd:
    aw = []
    # 计算充电桩距离
    for j in cdz:
        aw.append([geodesic((i[1],i[2]), (j[1],j[2])).m,j[0]])
    # 距离排序
    aw.sort(key=lambda x:x[0])
    # 找出最近的充电桩
    res.append([i[0],aw[0][1]])
# 写入csv
with open('res1.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
res = []
# 遍历所有充电桩
for i in cdz:
    aw = 0
    # 计算与所有需求点距离
    for j in xqd:
        # 如果小于500 则数量加1
        if geodesic((i[1],i[2]), (j[1],j[2])).m < 500:
            aw += 1
    # 结果存储到列表
    res.append([i[0],aw])
# 写入csv
with open('res2.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)