import pandas as pd

# 读取CSV文件
df = pd.read_csv("soccer.csv")

# 统计不同俱乐部的球员数量
club_counts = df["Club"].value_counts()

# 获取球员最多的五个俱乐部
top_5_clubs = club_counts.head(5).index

# 从球员最多的五个俱乐部抽取球员信息
# 球员数量最多的俱乐部抽取30名，剩下4个俱乐部各抽取5名
club_1 = df[df["Club"] == top_5_clubs[0]].sample(30)
club_2 = df[df["Club"] == top_5_clubs[1]].sample(5)
club_3 = df[df["Club"] == top_5_clubs[2]].sample(5)
club_4 = df[df["Club"] == top_5_clubs[3]].sample(5)
club_5 = df[df["Club"] == top_5_clubs[4]].sample(5)

# 将抽取的球员信息拼接到一个新的dataframe中
new_df = pd.concat([club_1, club_2, club_3, club_4, club_5], ignore_index=True)

# 打印新dataframe的信息
print(new_df.info())

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# 根据球员是否属于同一俱乐部创建共现矩阵
n_players = len(new_df)
cooccurrence_matrix = np.zeros((n_players, n_players))

for i in range(n_players):
    for j in range(n_players):
        if new_df.iloc[i]["Club"] == new_df.iloc[j]["Club"]:
            cooccurrence_matrix[i, j] = 1

# 创建无向图
G = nx.from_numpy_array(cooccurrence_matrix)

# 设置节点颜色
color_map = []
for player in new_df.iterrows():
    if player[1]["Club"] == top_5_clubs[0]:
        color_map.append("red")
    elif player[1]["Club"] == top_5_clubs[1]:
        color_map.append("blue")
    elif player[1]["Club"] == top_5_clubs[2]:
        color_map.append("green")
    elif player[1]["Club"] == top_5_clubs[3]:
        color_map.append("purple")
    else:
        color_map.append("orange")

# 绘制随机分布网络图
plt.figure(figsize=(12, 8))
plt.title("Random Layout")
pos = nx.random_layout(G)
nx.draw(G, pos, node_color=color_map, with_labels=False, node_size=100)
plt.show()

# 绘制Fruchterman-Reingold算法排列节点网络图
plt.figure(figsize=(12, 8))
plt.title("Fruchterman-Reingold Layout")
pos = nx.spring_layout(G)
nx.draw(G, pos, node_color=color_map, with_labels=False, node_size=100)
plt.show()

# 绘制同心圆分布网络图
plt.figure(figsize=(12, 8))
plt.title("Circular Layout")
pos = nx.circular_layout(G)
nx.draw(G, pos, node_color=color_map, with_labels=False, node_size=100)
plt.show()

