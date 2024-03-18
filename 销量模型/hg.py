import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression,Ridge,LogisticRegression
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score,mean_squared_error
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('cangyin.xlsx')
print(df.columns)
df = df[['评分','人均','评论数','口味','环境','服务','门店价','折扣比例','对数销量']]
df = df.rename(columns={'对数销量':'销量'})
print(len(df))
df = df.dropna(how='any')
print(len(df))
print(df)
df['人均'] = df['人均'].map(lambda x:int(x))
df['环境']= df['环境'].map(lambda x:float(x))
df['口味']= df['口味'].map(lambda x:float(x))
df['服务']= df['服务'].map(lambda x:float(x))
df['评论数']= df['评论数'].map(lambda x:float(x))
plt_list = [[i,j] for i,j in zip(df['评分'],df['销量'])]
plt_list.sort(key=lambda x:x[0])
plt.bar([i[0] for i in plt_list],[i[1] for i in plt_list])
plt.xlabel('评分')
plt.ylabel('销量')
plt.show()

plt_list = [[i,j] for i,j in zip(df['折扣比例'],df['销量'])]
plt_list.sort(key=lambda x:x[0])
plt.bar([i[0] for i in plt_list],[i[1] for i in plt_list])
plt.xlabel('折扣比例')
plt.ylabel('销量')
plt.show()

print(df.describe())
df_corr = df.corr('spearman')
print(df_corr)
sns.heatmap(df_corr, vmax=0.6, vmin=-0.6, center=0,cmap='PiYG')
plt.show()
print(df)
col_name = '评分  人均  评论数  口味  环境  服务  门店价  折扣比例'.split()
X = df.drop(['销量'],axis=1)
y = df['销量']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
model = MLPRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('神经网络的R2得分：',r2_score(y_test,y_pred))
print('神经网络的MSE得分：',mean_squared_error(y_test,y_pred))
model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的R2得分：',r2_score(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(col_name,model.feature_importances_)]
res.sort(key=lambda x:x[1],reverse=True)
print('决策树特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('线性回归的R2得分：',r2_score(y_test,y_pred))
print('线性回归的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(col_name,abs(model.coef_))]
res.sort(key=lambda x:x[1],reverse=True)
print('线性回归特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
model = Ridge()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('岭回归的R2得分：',r2_score(y_test,y_pred))
print('岭回归的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(col_name,abs(model.coef_))]
res.sort(key=lambda x:x[1],reverse=True)
print('岭回归特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.bar('评分  人均  评论数  口味  环境  服务  门店价  折扣比例'.split(),model.coef_)
plt.show()

x = sm.add_constant(X)
model = sm.OLS(y,X)
model = model.fit()
print(model.summary())