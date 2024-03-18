import os
import jieba
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
from zhconv import convert
import numpy as np
# 读取8个文本文件并存储为文本字符串
text_files = [
'2015年esg信息.txt',
'2016年esg信息.txt',
'2017年esg信息.txt',
'2018年esg信息.txt',
'2019年esg信息.txt',
'2020年esg信息.txt',
'2021年esg信息.txt',
'2022年esg信息.txt',
]
def simCosine(x, y):
    """
    :param x: m x k array
    :param y: n x k array
    :return: m x n array
    """
    xx = np.sum(x ** 2, axis=1) ** 0.5
    x = x / xx[:, np.newaxis]
    yy = np.sum(y ** 2, axis=1) ** 0.5
    y = y / yy[:, np.newaxis]
    dist = np.dot(x, y.transpose()) # cosine similarity
    return dist
texts = []
for file_i in range(len(text_files)):
    file = text_files[file_i]
    print(file)
    try:
        with open(file, encoding='utf8', errors='ignore') as f:
            lines = f.readlines()
            lines = ''.join(lines).replace('\n','').replace(' ','')
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            chinese = re.sub(pattern, '', lines)
            simplified_chinese = convert(chinese, 'zh-hans')
            texts.append(simplified_chinese)
    except:
        with open(file, encoding='gbk', errors='ignore') as f:
            lines = f.readlines()
            lines = ''.join(lines).replace('\n','').replace(' ','')
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            chinese = re.sub(pattern, '', lines)
            simplified_chinese = convert(chinese, 'zh-hans')
            texts.append(simplified_chinese)

# 使用jieba进行分词和预处理
segmented_texts = []
for text in texts:
    seg_list = jieba.lcut(text)
    seg_str = " ".join(seg_list)
    segmented_texts.append(seg_str)

# 将文本转化为TF-IDF向量
tfidf_vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b', stop_words=[f'{i}' for i in range(10)] + ['的', '地', '得'])
tfidf_matrix = tfidf_vectorizer.fit_transform(segmented_texts).toarray()

# 计算文本之间的余弦相似度
similarity_matrix = simCosine(tfidf_matrix, tfidf_matrix)
print(similarity_matrix)
# 打印相似度矩阵
for i in range(len(text_files)):
    for j in range(len(text_files)):
        similarity = similarity_matrix[i][j]
        # print(f"文本{text_files[i]} 与 文本{text_files[j]} 的余弦相似度为: {similarity}")

# 请确保文件存在，并使用适当的文件名替换文本文件列表中的文件名。
