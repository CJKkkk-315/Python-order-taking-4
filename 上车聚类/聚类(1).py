import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('转换XY后总表.xls')
df.drop([97,96,47,48,49],inplace=True)
total_rows = len(df)
mid_row = total_rows // 2
df1 = df.iloc[:mid_row]
df2 = df.iloc[mid_row:]
# 计算欧氏距离的函数
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def bi_kmeans_clustering(data, k):
    # 当k为0时，表示没有更多的簇需要生成，返回空列表
    if k <= 0:
        return []

    # 当k为1时，表示只需要一个簇，直接返回数据的均值作为质心
    if k == 1:
        return [np.mean(data, axis=0)]

    # 使用K-means算法将数据分成两个簇
    kmeans = KMeans(n_clusters=2)
    kmeans.fit(data)
    cluster_labels = kmeans.labels_

    centroids = []
    # 遍历两个簇的标签
    for label in np.unique(cluster_labels):
        # 提取当前簇的数据
        sub_data = data[cluster_labels == label]

        # 将剩余的k值平分给两个子簇
        sub_k = k // 2

        # 如果当前标签为0，需要考虑k为奇数的情况，将多出的一个簇分配给第一个子簇
        if label == 0:
            sub_k += k % 2

        # 递归调用二分K-means聚类函数，计算子簇的质心
        sub_centroids = bi_kmeans_clustering(sub_data, sub_k)

        # 将计算得到的子簇质心添加到总质心列表中
        centroids.extend(sub_centroids)

    return centroids






def bikmeans(df,k):
    plt.scatter(df['X_纬度'], df['Y_经度'])
    plt.xlabel('X_纬度')
    plt.ylabel('Y_经度')
    plt.title('Data before clustering')
    plt.show()
    data_points = df[['X_纬度', 'Y_经度']].values
    centroids = bi_kmeans_clustering(data_points, k)
    kmeans = KMeans(n_clusters=len(centroids), init=centroids, n_init=1)
    kmeans.fit(data_points)
    df['cluster'] = kmeans.predict(data_points)
    cluster_markers = ['o', 'v', 's', 'D', 'P', 'X'] + ['o', 'v', 's', 'D', 'P', 'X']    # 指定6个不同的类中心点标记
    res = {i:[] for i in range(k)}
    for i in df.values:
        print('编号:',i[1],'距离:',euclidean_distance([i[4],i[5]],centroids[i[-1]]))
        res[i[-1]].append(i[1])
    print('聚类结果：')
    for i in res:
        print(i,res[i])
    plt.figure(figsize=(10, 7))
    for cluster_id, marker in zip(range(k), cluster_markers):
        cluster_data = df[df['cluster'] == cluster_id]
        plt.scatter(cluster_data['X_纬度'], cluster_data['Y_经度'], label=f"Cluster {cluster_id}")

    for i, centroid in enumerate(centroids):
        plt.scatter(centroid[0], centroid[1], marker=cluster_markers[i], s=150, edgecolors='k', label=f"Centroid {i}")
    plt.xlabel('X_纬度')
    plt.ylabel('Y_经度')
    plt.title('Data after clustering')
    plt.legend()
    plt.show()
    return centroids
ca = bikmeans(df1,8)
cb = bikmeans(df2,6)
coordinates = ca + cb


# 初始化一个空的矩阵来存储距离
distance_matrix = np.zeros((len(coordinates), len(coordinates)))

# 计算每对坐标之间的距离并将其存储在矩阵中
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# 将numpy数组转换为pandas DataFrame
df = pd.DataFrame(distance_matrix)
labels = ['A' + str(i+1) for i in range(8)] + ['B' + str(i+1) for i in range(6)]
for i,j in zip(labels,coordinates):
    print(i,'坐标:',j)
df.columns = labels
df.index = labels
# 将DataFrame写入Excel文件
df.to_excel('res.xlsx')
