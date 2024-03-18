import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 10个数据样本 (密度, 蔗糖含量)
data = np.array([
    [0.552, 0.249],
    [0.397, 0.392],
    [0.381, 0.995],
    [0.499, 0.987],
    [0.095, 0.059],
    [0.658, 0.157],
    [0.006, 0.074],
    [0.847, 0.138],
    [0.814, 0.531],
    [0.964, 0.821]
])

# 聚类值 k
k = 2

# 使用k-means聚类
kmeans = KMeans(n_clusters=k, init='random', n_init=1)
kmeans.fit(data)

# 输出聚类结果
labels = kmeans.labels_
print(f'Cluster labels: {labels}')

# 将数据点分配到两个集群
clusters = {i: [] for i in range(k)}
for i, label in enumerate(labels):
    clusters[label].append(data[i])

for cluster_label, cluster_data in clusters.items():
    print(f'Cluster {cluster_label}: {np.array(cluster_data)}')

# 绘制聚类结果
colors = ['b', 'r']
markers = ['o', 's']

for i in range(k):
    cluster_data = np.array(clusters[i])
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], c=colors[i], marker=markers[i], label=f'Cluster {i}')

plt.xlabel('Density')
plt.ylabel('Sugar Content')
plt.title('K-means Clustering Results')
plt.legend()
plt.grid()
plt.show()
