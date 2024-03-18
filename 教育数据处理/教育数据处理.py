import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.cluster import KMeans
import seaborn as sns
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('education .data.xlsx')
dfo = pd.read_excel('education .data.xlsx')
print(df)
df.drop(['序号'],axis=1,inplace=True)
aca = Counter(df['academic'].values.tolist())
x = [i for i in aca.keys()]
y = [i for i in aca.values()]
plt.bar(x,y)
plt.title('教育程度分布')
plt.show()

fjob = Counter(df['fjob'].values.tolist())
x = [i for i in fjob.keys()]
y = [i for i in fjob.values()]
plt.pie(labels=x,x=y)
plt.title('家长工作分布')
plt.show()

age = Counter(df['age'].values.tolist())
x = [i for i in age.keys()]
y = [i for i in age.values()]
plt.pie(labels=x,x=y)
plt.title('年龄分布')
plt.show()

LE = LabelEncoder()
df['sex'] = LE.fit_transform(df['sex'])
df['fjob'] = LE.fit_transform(df['fjob'])
df['mjob'] = LE.fit_transform(df['mjob'])
bool_dict = {
    '是':1,
    '否':0
}
df['edusupport'] = df['edusupport'].map(bool_dict)
df['addlesson'] = df['addlesson'].map(bool_dict)
df['absent'] = df['absent'].map(bool_dict)
df['higher'] = df['higher'].map(bool_dict)
edu_dict = {
    '小学':1,
    '初中':2,
    '中专/高中':3,
    '专科':4,
    '本科':5,
    '研究生':6
}
df['academic'] = df['academic'].map(edu_dict)
df['learntime'] = df['learntime'].apply(lambda x:int(x.split('-')[0]) if '-' in x else 8)
df['age'] = df['age'].apply(lambda x:int(x.split('-')[0]))

df_corr = df.corr()
print(df_corr)
sns.heatmap(df_corr, center=0,cmap='Spectral_r')
plt.title('特征相关性')
plt.show()
print(df)

km = KMeans(n_clusters=5)
km.fit(df)
res = {i:[] for i in range(5)}
for idx,label in enumerate(km.labels_):
    res[label].append(idx)
for i in res:
    print(f'类别{i+1}数据共{len(res[i])}条,为：')
    for j in res[i]:
        print(list(dfo.iloc[j]))

y = df['score']
act_fact = df[[df.columns[2],df.columns[3],df.columns[4],df.columns[5],df.columns[6],df.columns[7],df.columns[8],df.columns[9]]]
pas_fact = df[[df.columns[10],df.columns[12],df.columns[13],df.columns[14]]]
print('--------------------------------------------------------------')
print('客观因素对成绩影响：')
X_train, X_test, y_train, y_test = train_test_split(act_fact,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('线性回归的R2得分：',r2_score(y_test,y_pred))
print('线性回归的MSE得分：',mean_squared_error(y_test,y_pred))

model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的R2得分：',r2_score(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))


res = [[i,j] for i,j in zip(act_fact.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.bar([i[0] for i in res],[i[1] for i in res])
plt.title('客观因素特征重要性')
plt.show()

model = SVR()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('支持向量机的R2得分：',r2_score(y_test,y_pred))
print('支持向量机的MSE得分：',mean_squared_error(y_test,y_pred))


print('--------------------------------------------------------------')
print('主观因素对成绩影响：')
X_train, X_test, y_train, y_test = train_test_split(pas_fact,y,test_size=0.2)

model = LinearRegression()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('线性回归的R2得分：',r2_score(y_test,y_pred))
print('线性回归的MSE得分：',mean_squared_error(y_test,y_pred))

model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的R2得分：',r2_score(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))

res = [[i,j] for i,j in zip(pas_fact.columns,abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')
plt.bar([i[0] for i in res],[i[1] for i in res])
plt.title('主观因素特征重要性')
plt.show()


model = SVR()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('支持向量机的R2得分：',r2_score(y_test,y_pred))
print('支持向量机的MSE得分：',mean_squared_error(y_test,y_pred))


x = df['intention'].values
y = df['score'].values

x = x.reshape(-1, 1)
y = y.reshape(-1, 1)

model = LinearRegression()
model.fit(x, y)

y_pred = model.predict(x)

plt.scatter(x, y)
plt.plot(x, y_pred, color='red')
plt.xlabel('intention')
plt.ylabel('score')
plt.title('intention vs. score')
plt.show()
