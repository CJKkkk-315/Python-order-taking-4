# 导入所需的库
import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# 加载葡萄酒数据集
wine = datasets.load_wine()

# 创建一个包含特征的数据帧
features_df = pd.DataFrame(data=wine.data, columns=wine.feature_names)

# 创建一个包含目标分类的数据帧
target_df = pd.DataFrame(data=wine.target, columns=['target'])

# 查看前5行特征数据
print("特征数据前5行：")
print(features_df.head())

# 查看前5行目标分类数据
print("\n目标分类数据前5行：")
print(target_df.head())

# 拆分数据集为训练集和测试集（80%训练，20%测试）
X_train, X_test, y_train, y_test = train_test_split(features_df, target_df, test_size=0.2)

# 创建决策树分类器
clf = DecisionTreeClassifier()

# 训练决策树模型
clf.fit(X_train, y_train)

# 使用模型进行预测
y_pred = clf.predict(X_test)

# 评价模型性能
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred, target_names=wine.target_names)

print("\n模型准确率：", accuracy)
print("\n分类报告：")
print(report)
