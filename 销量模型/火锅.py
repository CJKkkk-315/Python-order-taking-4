import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression,Ridge,LogisticRegression
from sklearn.neural_network import MLPRegressor
from xgboost import XGBRegressor
from xgboost import XGBRFRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import numpy as np
from collections import defaultdict
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
dfo = pd.read_excel('huoguo2.xlsx')
dfo.drop(['销量'],axis=1,inplace=True)
df = dfo.values
high = df[np.where(df[:,-1] > 9)]
print(high)
mid = df[(df[:,-1] < 9) & (df[:,-1] > 7)]
print(mid)
low = df[(df[:,-1] < 7)]
print(low)
plt.bar(['高销量','中销量','低销量'],[len(high),len(mid),len(low)])
plt.show()
pf = defaultdict(list)
for i in df:
    pf[i[1]].append(i[-1])
xy = sorted([[i,sum(j)/len(j)] for i,j in pf.items()])
plt.bar([str(i[0]) for i in xy],[i[1] for i in xy])
plt.show()

df_corr = dfo.corr()
print(df_corr)
sns.heatmap(df_corr, center=0,cmap='Spectral_r')
plt.show()

for c in dfo.columns:
    if c != '对数销量':
        s = StandardScaler()
        dfo[c] = s.fit_transform(dfo[c].values.reshape(-1, 1))
print(dfo)

X_train, X_test, y_train, y_test = train_test_split(high[:,:-1],high[:,-1],test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('高销量线性回归的R2得分：',r2_score(y_test,y_pred))
print('高销量线性回归的MSE得分：',mean_squared_error(y_test,y_pred))
print(model.coef_)
X_train, X_test, y_train, y_test = train_test_split(mid[:,:-1],mid[:,-1],test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('中销量线性回归的R2得分：',r2_score(y_test,y_pred))
print('中销量线性回归的MSE得分：',mean_squared_error(y_test,y_pred))

X_train, X_test, y_train, y_test = train_test_split(low[:,:-1],low[:,-1],test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('低销量线性回归的R2得分：',r2_score(y_test,y_pred))
print('低销量线性回归的MSE得分：',mean_squared_error(y_test,y_pred))


X = dfo.drop(['对数销量'],axis=1)
y = dfo['对数销量']
X_train, X_test, y_train, y_test = X,X,y,y

model = KNeighborsRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('神经网络的R2得分：',r2_score(y_test,y_pred))
print('神经网络的MSE得分：',mean_squared_error(y_test,y_pred))

model = Ridge()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('岭回归的R2得分：',r2_score(y_test,y_pred))
print('岭回归的MSE得分：',mean_squared_error(y_test,y_pred))

model = XGBRFRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('XGBRF的R2得分：',r2_score(y_test,y_pred))
print('XGBRF的MSE得分：',mean_squared_error(y_test,y_pred))


model = XGBRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('XGB的R2得分：',r2_score(y_test,y_pred))
print('XGB的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('XGB特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.plot([i for i in range(len(y_test))],y_test,label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred))],y_pred,label='预测值',marker='o')
plt.title('XGB')
plt.show()

model = RandomForestRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('随机森林的R2得分：',r2_score(y_test,y_pred))
print('随机森林的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('随机森林特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.plot([i for i in range(len(y_test))],y_test,label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred))],y_pred,label='预测值',marker='o')
plt.title('随机森林')
plt.show()

