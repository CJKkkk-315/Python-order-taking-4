import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 加载数据
df = pd.read_csv('data.csv',encoding='gbk')
city = df.values[:,0]
data = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data = data[:,1:]
# 定义变量名
variables = '食品,衣着,居住,家庭设备及服务,交通和通讯,文教娱乐用品及服务,医疗保健,其他用品及服务'.split(',')

# 绘制数据图
for i, var in enumerate(variables):

    plt.figure(figsize=(10, 6))
    plt.bar(city, data[:, i])
    plt.xlabel('地区')
    plt.ylabel(var)
    plt.title(f'{var}在不同地区的分布')
    plt.show()

# 执行K均值聚类
km = KMeans(n_clusters=4)
km_clusters = km.fit_predict(data)
cluster = {i:[] for i in range(4)}
# 按照聚类结果将不同城市划分
for i,j in zip(city,km_clusters):
    cluster[j].append(i)
print(cluster)
# 计算协方差矩阵
cov_matrix = np.cov(data, rowvar=False)
print("协方差矩阵:")
print(cov_matrix)

# 执行主成分分析
pca = PCA(n_components=4)
principalComponents = pca.fit_transform(data)

# 打印主成分
print("主成分:")
print(pca.components_)

