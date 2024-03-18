import numpy as np
from sklearn.svm import SVR
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as mdates


# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('数据内容.xlsx')
# 处理数据，处理为（事故数，月份）的形式
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
# 对X , y进行标准化
sdx = StandardScaler()
X1 = sdx.fit_transform(X1.reshape(-1, 1)).reshape(1, -1)[0]
X2 = sdx.fit_transform(X2.reshape(-1, 1)).reshape(1, -1)[0]
sdy = StandardScaler()
sdy.fit(y.reshape(-1, 1))
y = sdy.transform(y.reshape(-1, 1)).reshape(1, -1)[0]
X = np.c_[X1, X2]
# 分割训练集和测试集
X_train = X[:6*12]
y_train = y[:6*12]
X_test = X[6*12:8*12]
y_test = y[6*12:8*12]


def GWO(n_iterations, n_wolves, dim, obj_func, lb, ub):
    # 初始化三个主导狼的位置和适应度分数
    alpha_position = np.zeros(dim)  # Alpha狼的位置
    alpha_score = float("inf")  # Alpha狼的适应度分数

    beta_position = np.zeros(dim)  # Beta狼的位置
    beta_score = float("inf")  # Beta狼的适应度分数

    delta_position = np.zeros(dim)  # Delta狼的位置
    delta_score = float("inf")  # Delta狼的适应度分数

    # 初始化所有狼的位置
    Positions = np.zeros((n_wolves, dim))
    for i in range(n_wolves):
        Positions[i, :] = np.random.uniform(0, 1, dim) * (ub - lb) + lb  # 根据上下界随机初始化位置
    alpha_history = []
    # 开始迭代
    for t in range(n_iterations):

        # 遍历每只狼
        for i in range(n_wolves):
            fitness = obj_func(Positions[i, :])  # 计算当前狼的适应度

            # 更新三个主导狼的位置和适应度分数
            if fitness < alpha_score:
                delta_score = beta_score
                delta_position = beta_position.copy()
                beta_score = alpha_score
                beta_position = alpha_position.copy()
                alpha_score = fitness
                alpha_position = Positions[i, :].copy()

            if fitness > alpha_score and fitness < beta_score:
                delta_score = beta_score
                delta_position = beta_position.copy()
                beta_score = fitness
                beta_position = Positions[i, :].copy()

            if fitness > alpha_score and fitness > beta_score and fitness < delta_score:
                delta_score = fitness
                delta_position = Positions[i, :].copy()

        # 计算系数a，随着迭代进行，a会逐渐减小
        a = 2 - t * (2 / n_iterations)

        # 更新狼群位置
        for i in range(n_wolves):
            for j in range(dim):
                # 对于Alpha狼
                r1 = np.random.random()
                r2 = np.random.random()
                A1 = 2 * a * r1 - a
                C1 = 2 * r2
                D_alpha = abs(C1 * alpha_position[j] - Positions[i, j])
                X1 = alpha_position[j] - A1 * D_alpha

                # 对于Beta狼
                r1 = np.random.random()
                r2 = np.random.random()
                A2 = 2 * a * r1 - a
                C2 = 2 * r2
                D_beta = abs(C2 * beta_position[j] - Positions[i, j])
                X2 = beta_position[j] - A2 * D_beta

                # 对于Delta狼
                r1 = np.random.random()
                r2 = np.random.random()
                A3 = 2 * a * r1 - a
                C3 = 2 * r2
                D_delta = abs(C3 * delta_position[j] - Positions[i, j])
                X3 = delta_position[j] - A3 * D_delta

                # 更新当前狼的位置
                Positions[i, j] = (X1 + X2 + X3) / 3

            # 保证狼的位置在上下界之内
            Positions[i, :] = np.clip(Positions[i, :], lb, ub)
        alpha_history.append(objective(alpha_position))

    plt.plot([i for i in range(len(alpha_history))], alpha_history)
    plt.ylabel('适应度')
    plt.xlabel('迭代次数')
    plt.show()
    # 返回最佳狼（Alpha狼）的位置
    return alpha_position


# 目标函数
def objective(params):
    C, gamma, epsilon = params
    model = SVR(C=C, gamma=gamma, epsilon=epsilon)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    return mean_squared_error(y_test, predictions)


# 无优化的支持向量机
model = SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# y_pred = sdy.inverse_transform(y_pred.reshape(-1, 1)).reshape(1, -1)[0]
# y_test = sdy.inverse_transform(y_test.reshape(-1, 1)).reshape(1, -1)[0]
print('优化前 R2',r2_score(y_test, y_pred))
print('优化前 MSE',mean_squared_error(y_test, y_pred))
print('优化前 MAE',mean_absolute_error(y_test, y_pred))
X2022 = X[8*12:]
y2022 = y[8*12:]
# 进行预测后反标准化
ypred2022 = model.predict(X2022)
ypred2022 = sdy.inverse_transform(ypred2022.reshape(-1, 1)).reshape(1, -1)[0]
y2022 = sdy.inverse_transform(y2022.reshape(-1, 1)).reshape(1, -1)[0]
plt.plot([str(i) for i in range(1,13)], ypred2022,label='预测值',marker='o')
plt.plot([str(i) for i in range(1,13)], y2022,label='真实值',marker='*')
print(ypred2022)
for i, txt in enumerate(ypred2022):
    plt.annotate(round(txt,2), (str(i+1), ypred2022[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('2022年预测值与真实值（优化前）')
plt.xlabel('月份')
plt.ylabel('死亡人数')
plt.legend()
plt.show()
x_all = X
y_all = y
ypred = model.predict(x_all)
ypred = sdy.inverse_transform(ypred.reshape(-1, 1)).reshape(1, -1)[0]
y_all = sdy.inverse_transform(y_all.reshape(-1, 1)).reshape(1, -1)[0]
dates = [datetime(year, month, 1) for year in range(2014, 2023) for month in range(1, 13)]
fig, ax = plt.subplots()
ax.plot(dates, ypred,label='预测值',marker='o')
ax.plot(dates, y_all,label='真实值',marker='*')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1,7])) # 每隔6个月一个主要刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # 日期格式为"年-月"
plt.tight_layout()

plt.title('全部预测值与真实值（优化前）')
plt.xlabel('月份')
plt.ylabel('死亡人数')
plt.legend()
plt.show()

X_train = X
y_train = y

# 设置灰狼优化算法的参数
# 参数界限
lb = [0.1, 0.001, 0.01]
ub = [100, 10, 10]
lb = np.array(lb)
ub = np.array(ub)
# 进行优化
best_params = GWO(n_iterations=50, n_wolves=15, dim=3, obj_func=objective, lb=lb, ub=ub)
print("Best Parameters: C={}, gamma={}, epsilon={}".format(best_params[0], best_params[1], best_params[2]))
# 使用优化后的支持向量机
model = SVR(C=best_params[0], gamma=best_params[1], epsilon=best_params[2])
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
# y_pred = sdy.inverse_transform(y_pred.reshape(-1, 1)).reshape(1, -1)[0]
# y_test = sdy.inverse_transform(y_test.reshape(-1, 1)).reshape(1, -1)[0]
print('优化后 R2',r2_score(y_test, y_pred))
print('优化后 MSE',mean_squared_error(y_test, y_pred))
print('优化后 MAE',mean_absolute_error(y_test, y_pred))
X2022 = X[8*12:]
y2022 = y[8*12:]
ypred2022 = model.predict(X2022)
ypred2022 = sdy.inverse_transform(ypred2022.reshape(-1, 1)).reshape(1, -1)[0]
y2022 = sdy.inverse_transform(y2022.reshape(-1, 1)).reshape(1, -1)[0]
print(ypred2022)
plt.plot([str(i) for i in range(1,13)], ypred2022,label='预测值',marker='o')
plt.plot([str(i) for i in range(1,13)], y2022,label='真实值',marker='*')
for i, txt in enumerate(ypred2022):
    plt.annotate(round(txt,2), (str(i+1), ypred2022[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.title('2022年预测值与真实值（优化后）')
plt.xlabel('月份')
plt.ylabel('死亡人数')
plt.legend()
plt.show()

x_all = X
y_all = y
ypred = model.predict(x_all)
ypred = sdy.inverse_transform(ypred.reshape(-1, 1)).reshape(1, -1)[0]
y_all = sdy.inverse_transform(y_all.reshape(-1, 1)).reshape(1, -1)[0]
dates = [datetime(year, month, 1) for year in range(2014, 2023) for month in range(1, 13)]
fig, ax = plt.subplots()
ax.plot(dates, ypred,label='预测值',marker='o')
ax.plot(dates, y_all,label='真实值',marker='*')
ax.xaxis.set_major_locator(mdates.MonthLocator(bymonth=[1,7])) # 每隔6个月一个主要刻度
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m')) # 日期格式为"年-月"
plt.tight_layout()
plt.title('全部预测值与真实值（优化后）')
plt.xlabel('月份')
plt.ylabel('死亡人数')
plt.legend()
plt.show()
