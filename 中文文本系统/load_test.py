from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import numpy as np

# 给定一组词语
res_words = []
words = open('filtered_words.txt',encoding='utf8').read().split('\n')
for i in words:
    for j in i.split():
        res_words.append(j.strip())
words = res_words[:]
print('均匀' in words)

# 使用预训练的word2vec模型
# 你可以从这里下载预训练的中文词向量: https://github.com/Embedding/Chinese-Word-Vectors
model = Word2Vec.load("训练集1.model")  # 请替换为实际的预训练模型路径

# 获取词语的向量表示
word_vectors = np.array([model.wv[word] for word in words])

# 使用K-means进行聚类
n_clusters = 3  # 假设我们想要将词语分为3类
kmeans = KMeans(n_clusters=n_clusters, random_state=42).fit(word_vectors)

# 输出聚类结果
clusters = [[] for _ in range(n_clusters)]
for idx, label in enumerate(kmeans.labels_):
    clusters[label].append(words[idx])

for i, cluster in enumerate(clusters):
    print(f"聚类 {i}: {', '.join(cluster)}")
