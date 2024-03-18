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
idx = [[] for _ in range(22)]
data = list(df.values)
for item in data:
    idx[int(item[-1])].append(item)

# 随机过采样
new_data = [[] for _ in range(22)]
for i in range(len(idx)):
    while len(new_data[i]) != max_n:
        new_data[i].append(random.sample(idx[i],1)[0])

random_over_sample_data = []
for item in new_data:
    random_over_sample_data.extend(item)
random.shuffle(random_over_sample_data)

# 随机欠采样
new_data = [[] for _ in range(22)]
for i in range(len(idx)):
    while len(new_data[i]) != min_n:
        new_data[i].append(random.sample(idx[i],1)[0])

random_under_sample_data = []
for item in new_data:
    random_under_sample_data.extend(item)
random.shuffle(random_under_sample_data)

# SMOTE算法
class Smote():

    def __init__(self, N=50, k=5):
        self.N = N
        self.k = k
        self.newindex = 0
    def fit(self, samples):
        self.samples = samples
        self.T, self.numattrs = self.samples.shape
        if (self.N < 100):
            np.random.shuffle(self.samples)
            self.T = int(self.N * self.T / 100)
            self.samples = self.samples[0:self.T, :]
            self.N = 100
        if (self.T <= self.k):
            self.k = self.T - 1
        N = int(self.N / 100)
        self.synthetic = np.zeros((self.T * N, self.numattrs))
        neighbors = NearestNeighbors(n_neighbors=self.k + 1,).fit(self.samples)
        for i in range(len(self.samples)):
            nnarray = neighbors.kneighbors(self.samples[i].reshape((1, -1)),
                                           return_distance=False)[0][1:]
            self.__populate(N, i, nnarray)
        return self.synthetic
    def __populate(self, N, i, nnarray):
        for j in range(N):
            nn = random.randint(0, self.k - 1)
            diff = self.samples[nnarray[nn]] - self.samples[i]
            gap = random.uniform(0, 1)
            self.synthetic[self.newindex] = self.samples[i] + gap * diff
            self.newindex += 1


for i in range(len(idx)):

    print(len(idx[i]))
    need_n = max_n - len(idx[i])
    need_p = need_n / len(idx[i])
    smote = Smote(N=int(need_p))
    idx[i] = smote.fit(np.array(idx[i]))
    print(len(idx[i]))
