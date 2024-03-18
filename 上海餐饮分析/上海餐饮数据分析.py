# 引入所需要的库
import math
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
# 设置中文字体可视化
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_csv('上海餐饮数据.csv')
# 去除无用特征
df.drop(['城市'],axis=1,inplace=True)
# 对非数值型特征进行编码
LE = LabelEncoder()
df['类别'] = LE.fit_transform(df['类别'])
df['行政区'] = LE.fit_transform(df['行政区'])
print(df)
# 经纬度数据过于贴近，进行归一化处理
gy = MinMaxScaler()
df['Lng'] = gy.fit_transform(df['Lng'].values.reshape(-1,1))
df['Lat'] = gy.fit_transform(df['Lat'].values.reshape(-1,1))
print(df)
# 处理完毕数据，进行特征相关性计算，查看相关性矩阵
df_corr = df.corr()
print(df_corr)
# 可视化矩阵图
sns.heatmap(df_corr, center=0,cmap='Spectral_r')
plt.show()
plt.clf()
# 对点评数进行对数处理，避免极端值影响
df['点评数'] = df['点评数'].apply(lambda x:math.log(x,math.e) if x else 0)
print(df)
# 建立模型，对点评数量进行预测
X = df.drop(['点评数'],axis=1)
y = df['点评数']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestRegressor()
# 拟合模型
model.fit(X_train,y_train)
# 预测
y_pred = model.predict(X_test)
# 计算拟合优度和均值方差
print('随机森林的R2得分：',r2_score(y_test,y_pred))
print('随机森林的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('随机森林特征重要性：')
# 得到特征重要度
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
# 画出均值方差
plt.clf()
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('随机森林')
plt.show()

# 同上
model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的R2得分：',r2_score(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('决策树特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.clf()
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('决策树')
plt.show()

# 建立模型，根据口味，环境，服务对人均消费进行预测
X = df[['服务','环境','口味']]
y = df['人均消费']
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的R2得分：',r2_score(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('决策树特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.clf()
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('决策树')
plt.show()

print('随机森林的R2得分：',r2_score(y_test,y_pred))
print('随机森林的MSE得分：',mean_squared_error(y_test,y_pred))
res = [[i,j] for i,j in zip(X.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('随机森林特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.clf()
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('随机森林')
plt.show()

# 使用KMeans聚类
model = KMeans(n_clusters=5)
model.fit(df)
df['label'] = model.labels_
print(df)