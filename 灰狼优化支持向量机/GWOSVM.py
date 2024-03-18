import numpy as np
from sklearn.svm import SVR
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('数据内容.xlsx')
event = df['事故起数'].values
ds = []
for i in range(1,13):
    ds.append(df[f'{i}月死亡人数'].values)
data = []
for i in range(len(event)):
    for j in range(12):
        data.append([event[i],j+1,ds[j][i]])

X1 = np.array([i[0] for i in data])
X2 = np.array([i[1] for i in data])
y = np.array([i[-1] for i in data])
sdx = StandardScaler()
X1 = sdx.fit_transform(X1.reshape(-1, 1)).reshape(1, -1)[0]
X2 = sdx.fit_transform(X2.reshape(-1, 1)).reshape(1, -1)[0]
sdy = StandardScaler()
sdy.fit(y.reshape(-1, 1))
y = sdy.transform(y.reshape(-1, 1)).reshape(1, -1)[0]
X = np.c_[X1, X2]

print(np.c_[X, y])
X_train = X[:6*12]
y_train = y[:6*12]
X_test = X[6*12:8*12]
y_test = y[6*12:8*12]

model = SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
y_pred = sdy.inverse_transform(y_pred.reshape(-1, 1)).reshape(1, -1)[0]
y_test = sdy.inverse_transform(y_test.reshape(-1, 1)).reshape(1, -1)[0]
print('R2',r2_score(y_test, y_pred))
print('MSE',mean_squared_error(y_test, y_pred))
print('MAE',mean_absolute_error(y_test, y_pred))
X2022 = X[8*12:]
y2022 = y[8*12:]

print(X2022)
ypred2022 = model.predict(X2022)
ypred2022 = sdy.inverse_transform(ypred2022.reshape(-1, 1)).reshape(1, -1)[0]
y2022 = sdy.inverse_transform(y2022.reshape(-1, 1)).reshape(1, -1)[0]
plt.plot([str(i) for i in range(1,13)], ypred2022,label='预测值',marker='o')
plt.plot([str(i) for i in range(1,13)], y2022,label='真实值',marker='*')
plt.title('2022年预测值与真实值')
plt.xlabel('月份')
plt.ylabel('死亡人数')
plt.legend()
plt.show()
print(ypred2022)
print(y2022)

