import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import NearestNeighbors
from imblearn.over_sampling import SMOTE,RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
import numpy as np
import random
df = pd.read_csv('data/KDDTest+.txt',header=None)
for i in df.columns:
    if str(df[i].dtype) not in ['float64','int64']:
        LE = LabelEncoder()
        df[i] = LE.fit_transform(df[i])
x = []
labels = []
for i in range(22):
    labels.append(i)
    n = list(df[42].values).count(i)
    x.append(n)
    print(i,':',n)
max_n = max(x)
print(max_n)
min_n = min(x)
plt.pie(x=x,labels=labels)
plt.show()
X = df.drop([42],axis=1)
y = df[42]

# 随机过采样
model = RandomOverSampler()
random_over_sample_X, random_over_sample_y = model.fit_resample(X,y)
for i in range(22):
    n = list(random_over_sample_y.values).count(i)
    print(i,':',n)

# 随机欠采样
model = RandomUnderSampler()
random_under_sample_X, random_under_sample_y = model.fit_resample(X,y)
for i in range(22):
    n = list(random_under_sample_y.values).count(i)
    print(i,':',n)

# SMOTE算法
model = SMOTE()
smote_sample_X, smote_sample_y = model.fit_resample(X,y)
for i in range(22):
    labels.append(i)
    n = list(smote_sample_y.values).count(i)
    x.append(n)
    print(i,':',n)
