from sklearn.decomposition import PCA
import pandas as pd
import warnings
from sklearn.preprocessing import StandardScaler
import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
warnings.filterwarnings('ignore')

data = pd.read_excel('数据(1).xlsx')

X = data[['安徽省人均消费支出（元）','安徽省能源消费量（万吨）','安徽省人口数（万人）']]
X.dropna(inplace=True)
y = data['安徽省碳排放量（mt）']
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
c_name = X.columns
pca = PCA()
pca.fit(X_scaled)

explained_variances = pca.explained_variance_ratio_

cumulative_variances = np.cumsum(explained_variances)

loadings = pca.components_[-1]
loadings_abs = abs(loadings)
loadings_order = loadings_abs.argsort()[::-1]

for i in range(len(loadings_order)):
    print(c_name[i],'对于碳排放量的影响大小为:',abs(loadings[loadings_order[i]]))

X = data['安徽省碳排放量（mt）']
X.dropna(inplace=True)
y = data['安徽省生产总值']

X = X.values.reshape(-1, 1)
y = y.values.reshape(-1, 1)

model = LogisticRegression()
model.fit(X, y)
test = np.linspace(min(X),max(X),1000)
y_pred = model.predict(test)

plt.scatter(X, y)
plt.plot(test, y_pred, color='red')
plt.xlabel('碳排放量')
plt.ylabel('生产总值')

plt.show()

