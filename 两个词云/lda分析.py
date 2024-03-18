import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.model_selection import GridSearchCV
import pyLDAvis
import pyLDAvis.sklearn
import matplotlib.pyplot as plt
import warnings

import numpy as np
df = pd.read_excel('外文文献.xls')
# 定义 CountVectorizer，并设置停用词
vectorizer = CountVectorizer(stop_words='english')
# fit 和 transform
data_vectorized = vectorizer.fit_transform(df['Abstract'])
# 定义搜索参数
search_params = {'n_components': list(range(1, 21)), 'learning_decay': [.5, .7, .9]}

# 初始化LDA
lda = LatentDirichletAllocation()

# 使用GridSearchCV寻找最优参数
model = GridSearchCV(lda, param_grid=search_params)

# fit
model.fit(data_vectorized)
# 最优的主题数
best_n_topics = model.best_params_["n_components"]

# 绘制
plt.figure(figsize=(12, 8))
plt.plot(list(range(1, 21)), model.cv_results_['mean_test_score'], label='mean_test_score')
plt.xlabel("Number of Topics")
plt.ylabel("Log Likelyhood Score")
plt.legend(loc='best')
plt.show()
# 最优模型
best_lda_model = model.best_estimator_

# 特征名字
feature_names = vectorizer.get_feature_names_out()

# 主题-词矩阵
topic_word_matrix = pd.DataFrame(best_lda_model.components_, columns=feature_names)
# 文章-主题矩阵
doc_topic_matrix = best_lda_model.transform(data_vectorized)
# 文章-主题矩阵
doc_topic_matrix = best_lda_model.transform(data_vectorized)

