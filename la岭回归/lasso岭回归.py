import numpy as np
import pandas as pd
from sklearn.linear_model import LassoCV, RidgeCV, Lasso, Ridge
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# 假设X和y已经处理好了，这里使用随机数据作为示例
df = pd.read_excel('搜狐视频.xls',header=None)
X = df[1].apply(lambda x:int(x.replace('万',''))).values.reshape(-1, 1)
y = df[2].apply(lambda x:int(x.replace('共','').replace('集','').replace('更新至','').replace('全','')))

# Lasso回归与Ridge回归结合交叉验证
lasso_reg = LassoCV(cv=5, fit_intercept=False)
ridge_reg = RidgeCV(cv=5, fit_intercept=True)

lasso_reg.fit(X, y)
ridge_reg.fit(X, y)

# 分别计算R2和RMSE
lasso_r2 = lasso_reg.score(X, y)
ridge_r2 = ridge_reg.score(X, y)

lasso_rmse = np.sqrt(mean_squared_error(y, lasso_reg.predict(X)))
ridge_rmse = np.sqrt(mean_squared_error(y, ridge_reg.predict(X)))

print("Lasso R2:", lasso_r2)
print("Ridge R2:", ridge_r2)
print("Lasso RMSE:", lasso_rmse)
print("Ridge RMSE:", ridge_rmse)

# 画出最终效果图
plt.scatter(X, y, color='blue', label="Actual Data")
plt.plot(X, lasso_reg.predict(X), color='green', label="Lasso Regression")
plt.plot(X, ridge_reg.predict(X), color='red', label="Ridge Regression")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()

# 画出不同参数的RMSE图
alphas = np.logspace(-6, 6, 200)
lasso_rmse_list = []
ridge_rmse_list = []

for alpha in alphas:
    lasso = Lasso(alpha=alpha)
    ridge = Ridge(alpha=alpha)

    lasso_cv_rmse = np.sqrt(-cross_val_score(lasso, X, y, scoring='neg_mean_squared_error', cv=5))
    ridge_cv_rmse = np.sqrt(-cross_val_score(ridge, X, y, scoring='neg_mean_squared_error', cv=5))

    lasso_rmse_list.append(lasso_cv_rmse.mean())
    ridge_rmse_list.append(ridge_cv_rmse.mean())

plt.plot(alphas, lasso_rmse_list, label="Lasso RMSE")
plt.plot(alphas, ridge_rmse_list, label="Ridge RMSE")
plt.xlabel("Alpha")
plt.ylabel("RMSE")
plt.xscale("log")
plt.legend()
plt.show()
