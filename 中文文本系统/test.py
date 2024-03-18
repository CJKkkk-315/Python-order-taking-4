import jieba
import numpy as np
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 假设您的评论数据集是一个txt文件，每行为一条评论
data_path = '评论文本.txt'

# 加载停用词
def load_stopwords(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f.readlines()]
    return set(stopwords)

stopwords_path = '停用词库.txt'
stopwords = load_stopwords(stopwords_path)

# 读取并预处理评论数据
def preprocess_data(data_path):
    with open(data_path, 'r', encoding='utf-8') as f:
        raw_data = f.readlines()

    processed_data = []
    for line in raw_data:
        seg_list = jieba.cut(line.strip(), cut_all=False)
        filtered_words = [word for word in seg_list if word not in stopwords and len(word) > 1]
        processed_data.append(filtered_words)

    return processed_data

reviews = preprocess_data(data_path)
# 训练Word2Vec模型
model = Word2Vec(reviews, vector_size=100, window=5, min_count=5, workers=4)

# 提取词汇表中的词向量
word_vectors = model.wv.vectors

# 使用K-means聚类
num_clusters = 20
kmeans_clustering = KMeans(n_clusters=num_clusters)
idx = kmeans_clustering.fit_predict(word_vectors)

# 将词汇表中的单词映射到对应的聚类索引
word_centroid_map = {model.wv.index_to_key[i]: idx[i] for i in range(len(model.wv.index_to_key))}

# 输出每个聚类的特征词
ress = {}
for cluster in range(num_clusters):
    words = [word for word, index in word_centroid_map.items() if index == cluster]
    if cluster not in ress:
        ress[cluster] = []
    ress[cluster].extend(words)

plt.plot([j[0] for j in ress.values()],[len(j) for j in ress.values()])
plt.show()
