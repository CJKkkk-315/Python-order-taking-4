import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import numpy as np

pd.options.display.max_columns = None
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('商务大数据上机作业数据.csv')

# 打印描述性统计
print(df.describe())

# 查看每列的缺失值数量
print(df.isnull().sum())

# 使用每列的众数填充其缺失值
for column in df.columns:
    df[column].fillna(df[column].mode()[0], inplace=True)

print(df.isnull().sum())

column = "State"
counts = df[column].value_counts()
plt.figure(figsize=(10,8))
plt.pie(counts, labels = counts.index,)
plt.title(f"{column} 分布饼图")
plt.show()

column = "Total day minutes"
plt.figure(figsize=(10,8))
plt.hist(df[column], bins=20, alpha=0.5, edgecolor='black')
plt.title(f"{column} 频率直方图")
plt.xlabel(column)
plt.ylabel("频率")
plt.show()

column = "Total day calls"
plt.figure(figsize=(10,8))
plt.hist(df[column], bins=20, alpha=0.5, edgecolor='black')
plt.title(f"{column} 频率直方图")
plt.xlabel(column)
plt.ylabel("频率")
plt.show()


LE = LabelEncoder()
df['State'] = LE.fit_transform(df['State'])
df['International plan'] = LE.fit_transform(df['International plan'])
df['Voice mail plan'] = LE.fit_transform(df['Voice mail plan'])

# 把最后一列作为目标变量，其余的作为特征
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# 随机7:3划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 初始化决策树分类器并训练
clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# 在训练集和测试集上分别打印准确率
y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

print("训练集准确率: ", accuracy_score(y_train, y_train_pred))
print("测试集准确率: ", accuracy_score(y_test, y_test_pred))


df['total charge'] = df['Total intl charge'] + df['Total night charge'] + df['Total eve charge'] + df['Total day charge']


target_column = "total charge"
X = df.drop(target_column, axis=1)
y = df[target_column]

# 随机7:3划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 初始化随机森林回归器并训练
regr = RandomForestRegressor(n_estimators=100, random_state=42)
regr.fit(X_train, y_train)


# 获取特征名称和对应的重要性
features = X.columns
importances = regr.feature_importances_

# 将特征和重要性按重要性排序
indices = np.argsort(importances)
features = features[indices]
importances = importances[indices]

# 创建柱状图
plt.figure(figsize=(10, 6))
plt.barh(range(len(importances)), importances, color='b', align='center')
plt.yticks(range(len(importances)), features)

# 添加标题和标签
plt.xlabel('Relative Importance')
plt.title('Feature Importances')

# 显示图形
plt.tight_layout()
plt.show()

from sklearn.cluster import KMeans

selected_features = df[["Total day minutes", "Total eve minutes", "Total night minutes"]]

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(selected_features)


labels = kmeans.labels_

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(selected_features.iloc[:, 0], selected_features.iloc[:, 1], selected_features.iloc[:, 2],
           c=labels, cmap='viridis', s=60)

ax.set_title("KMeans Clustering")
ax.set_xlabel("Day")
ax.set_ylabel("Eve")
ax.set_zlabel("Night")

# 显示图形
plt.show()
