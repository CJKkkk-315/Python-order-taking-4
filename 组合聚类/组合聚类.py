from itertools import combinations
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import calinski_harabasz_score
import pandas as pd
import csv
# 读取数据
data = pd.read_csv('datasample(1).csv.',encoding='gbk')
# 获得变量名
column = data.columns[1:]
# 去掉第一列
data = data.values[:,1:]
c = []
res = []
# combinations函数获取给定列表所有组合情况
for i in range(1,data.shape[1]+1):
    for j in combinations(range(data.shape[1]),i):
        c.append(j)
# 根据每个组合情况抽取对应的变量，并且归一化，聚类评分
for i in c:
    data_now = data[:,i]
    scaler = MinMaxScaler()
    data_now = scaler.fit_transform(data_now)
    model = KMeans(n_clusters=3)
    model.fit(data_now)
    res.append([''.join(list(column[i,])),calinski_harabasz_score(data_now,model.labels_)])
# 写入文件
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
