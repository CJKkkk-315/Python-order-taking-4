import jieba
from sklearn.feature_extraction.text import TfidfTransformer, TfidfVectorizer,CountVectorizer
import numpy as np
import re
from zhconv import convert

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
file_names = [
'2015年esg信息.txt',
'2016年esg信息.txt',
'2017年esg信息.txt',
'2018年esg信息.txt',
'2019年esg信息.txt',
'2020年esg信息.txt',
'2021年esg信息.txt',
'2022年esg信息.txt',
]

documents = []
for file_i in range(len(file_names)):
    file = file_names[file_i]
    print(file)
    try:
        with open(file, encoding='utf8', errors='ignore') as f:
            lines = f.readlines()
            lines = ''.join(lines).replace('\n','').replace(' ','')
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            chinese = re.sub(pattern, '', lines)
            simplified_chinese = convert(chinese, 'zh-hans')
            documents.append(simplified_chinese)
    except:
        with open(file, encoding='gbk', errors='ignore') as f:
            lines = f.readlines()
            lines = ''.join(lines).replace('\n','').replace(' ','')
            pattern = re.compile(r'[^\u4e00-\u9fa5]')
            chinese = re.sub(pattern, '', lines)
            simplified_chinese = convert(chinese, 'zh-hans')
            documents.append(simplified_chinese)

documents = [" ".join(jieba.cut(item)) for item in documents]
vectorizer = TfidfVectorizer(token_pattern=r'(?u)\b\w+\b', stop_words=[f'{i}' for i in range(10)] + ['的', '地', '得'])
X = vectorizer.fit_transform(documents)

tf_idf_mat = X.toarray()
print(tf_idf_mat)
print(X)
dis_mat = simCosine(tf_idf_mat, tf_idf_mat)
print(np.round(dis_mat,3))
for i in range(len(dis_mat)-1):
    print(f'{2015+i}年与{2015+i+1}年相似度为{dis_mat[i][i+1]}')