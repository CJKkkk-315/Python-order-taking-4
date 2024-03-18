import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_wine, load_breast_cancer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score

# 加载数据集
datasets = {
    'Iris': load_iris(),
    'Wine': load_wine(),
    'Breast Cancer': load_breast_cancer()
}

# 初始化K-近邻分类器
knn = KNeighborsClassifier(n_neighbors=3)

# 进行5-fold交叉验证，并计算准确率
accuracies = {}

for name, dataset in datasets.items():
    X, y = dataset.data, dataset.target
    scores = cross_val_score(knn, X, y, cv=5)
    accuracies[name] = np.mean(scores)
for acc in accuracies.keys():
    print(acc,accuracies[acc])
# 展示准确率
plt.figure(figsize=(8, 6))
plt.bar(accuracies.keys(), accuracies.values())
plt.xlabel('Datasets')
plt.ylabel('Accuracy')
plt.title('K-Nearest Neighbors Classification Accuracy for Different Datasets')
plt.show()
