import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['font.sans-serif'] = ['SimHei']

df = pd.read_csv('movies_train.csv')
df.replace('[]', np.nan, inplace=True)
missing_values = df.isnull().sum()
miss_dict = missing_values.to_dict()
xy = []
for key in miss_dict:
    if miss_dict[key] != 0:
        xy.append([key,miss_dict[key]])
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.bar(x, y, width=0.8, color='b')
plt.xticks(rotation=30)
plt.axhline(df.shape[0],color='red')
plt.title('清理前各列缺失值数量')
plt.xlabel('列名')
plt.ylabel('缺失值数量')
plt.show()

df.drop(['homepage','keywords','tagline'],axis=1,inplace=True)
print(df.columns)
missing_values = df.isnull().sum()
miss_dict = missing_values.to_dict()
xy = []
for key in miss_dict:
    if miss_dict[key] != 0:
        xy.append([key,miss_dict[key]])
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.bar(x, y, width=0.8, color='b')
plt.xticks(rotation=30)
plt.axhline(df.shape[0],color='red')
plt.title('清理后各列缺失值数量')
plt.xlabel('列名')
plt.ylabel('缺失值数量')
plt.show()
print(df.isnull().sum())

for c in df.columns:
    if df[c].isnull().any():
        df[c].fillna(df[c].mode()[0],inplace=True)
print(df.isnull().any())

language = []
for key,value in Counter(df['original_language'].values).items():
    language.append([key,value])
language.sort(key=lambda x:x[1],reverse=True)
language = language[:10]
x = [i[0] for i in language]
y = [i[1] for i in language]
plt.pie(x=y,labels=x)
plt.title('语言分布')
plt.show()

release_date = []
for value in df['release_date']:
    release_date.append(value.split('-')[0])
release_date = Counter(release_date)
res = []
for key,value in release_date.items():
    res.append([key,value])
res.sort(key=lambda x:x[1],reverse=True)
res = res[:20]
x = [i[0] for i in res]
y = [i[1] for i in res]
plt.pie(x=y,labels=x)
plt.title('发布年份分布')
plt.show()

vote = []
for value in df['vote_average']:
    vote.append(int(value))
vote_data = Counter(vote)
res = []
for key,value in vote_data.items():
    res.append([key,value])
res.sort(key=lambda x:x[1],reverse=True)
res = res[:20]
x = [i[0] for i in res]
y = [i[1] for i in res]
plt.bar(x,y)
plt.title('评分分布')
plt.xlabel('评分')
plt.ylabel('个数')
plt.show()