import pandas as pd
from sklearn.datasets import load_iris, load_wine, load_breast_cancer

# 加载数据集
datasets = {
    'Iris': load_iris(),
    'Wine': load_wine(),
    'Breast Cancer': load_breast_cancer()
}

# 将数据集保存为CSV文件
for name, dataset in datasets.items():
    # 将数据和标签合并为一个DataFrame
    data = pd.DataFrame(data=dataset.data, columns=dataset.feature_names)
    data['target'] = dataset.target

    # 保存为CSV文件
    csv_file = f'{name.replace(" ", "_").lower()}_dataset.csv'
    data.to_csv(csv_file, index=False)
    print(f"{name} dataset saved as {csv_file}")
