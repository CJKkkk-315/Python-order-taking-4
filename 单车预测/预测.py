import csv
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd
import matplotlib.pyplot as plt
import warnings
# warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


data = pd.read_csv('res_data.csv',encoding='gbk',header=None)
le = LabelEncoder()
data[1] = le.fit_transform(data[1])

X = data.drop([4],axis=1).values
y = data[4].values.reshape((-1,1))
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

mlp = MLPRegressor(solver='lbfgs', hidden_layer_sizes=(10,), activation='relu', max_iter=5000, tol=1e-5)

# 拟合训练数据
mlp.fit(X_train, y_train)

# 预测测试数据


for i in range(30):
    idx = [X_test[:,3] == i]
    X_sub_test = X_test[tuple(idx)]
    y_sub_test = y_test[tuple(idx)]
    y_pred = mlp.predict(X_sub_test)


    # 计算均方误差
    mse = mean_squared_error(y_sub_test, y_pred)
    print(f'区域{i}准确度:',sum(y_sub_test)/sum(y_pred))
    print(f'区域{i}均方误差:', mse)

    # 检查模型是否收敛
    if mlp.n_iter_ < mlp.max_iter:
        print(f'模型在 {mlp.n_iter_} 次迭代后收敛。')
    else:
        print(f'模型未在 {mlp.max_iter} 次迭代内收敛。')


    plt.plot([i for i in range(len(y_sub_test))][:100],y_sub_test[:100],marker='*',label='预测值')
    plt.plot([i for i in range(len(y_sub_test))][:100],y_pred[:100],marker='o',label='真实值')
    plt.legend()
    plt.title(f'区域{i}预测结果')
    # plt.show()


a = [11,'晴天',17.1,0]
a[1] = le.fit_transform([a[1]])[0]
print(mlp.predict([a]))