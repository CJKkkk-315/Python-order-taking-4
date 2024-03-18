import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score, explained_variance_score, mean_absolute_error
import matplotlib as mpl

# 设置全局字体为微软雅黑（请根据实际情况选择合适的字体）
mpl.rcParams['font.family'] = 'Microsoft YaHei'
mpl.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

data = pd.read_excel('美团奶茶团购数据2.xlsx')
data['销量2'] = np.log1p(data['销量2'])
# 定义特征列和目标列
features = ['人均', '评分', '团购价', '原价', '折扣比例', '评论数', '口味', '环境', '服务']
target = '销量2'

# 将数据划分为训练集和测试集
X = data[features]
y = data[target]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建GBDT回归模型并训练
gbdt = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gbdt.fit(X_train, y_train)

# 预测测试集的销量
y_pred = gbdt.predict(X_test)

# 评估模型
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
evar = explained_variance_score(y_test, y_pred)
print("MSE:", mse)
print("拟合优度:", r2)
print('平均绝对误差:',mae)
print('可解释方差:',evar)
# 绘制预测值与真实值的比较图
plt.figure(figsize=(12, 6))
plt.plot(range(len(y_test)), y_test, label='True Values')
plt.plot(range(len(y_pred)), y_pred, label='Predicted Values')
plt.legend()
plt.show()
# 获取特征重要性
feature_importances = gbdt.feature_importances_

# 输出特征重要性
print("Feature Importances:")
for feature, importance in zip(features, feature_importances):
    print(f"{feature}: {importance}")

# 可视化特征重要性
plt.figure(figsize=(12, 6))
plt.bar(features, feature_importances)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Feature Importance in GBDT Model")
plt.show()
