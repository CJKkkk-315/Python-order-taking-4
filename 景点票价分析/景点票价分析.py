import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
plt.rcParams['font.sans-serif'] = ['SimHei']
df = pd.read_excel('景点数据.xlsx')
o_df = pd.read_excel('景点数据.xlsx')
df.drop(['地址','评语','地区','景点名称','序号'],axis=1,inplace=True)
pf = df['评分'].values.tolist()
pf = Counter(pf)
del pf[0]
pf = sorted(pf.items())
plt.scatter([i[0] for i in pf],[i[1] for i in pf])
plt.show()


pj = df['评级'].values.tolist()
pj = Counter(pj)
pj = sorted(pj.items())
plt.pie(labels=[i[0] for i in pj],x=[i[1] for i in pj])
plt.show()

jgd = {'<10':0,'10-30':0,'30-50':0,'50-100':0,'>100':0}
jg = df['价格'].values.tolist()
for i in jg:
    if i < 10:
        jgd['<10'] += 1
    elif i < 30:
        jgd['10-30'] += 1
    elif i < 50:
        jgd['30-50'] += 1
    elif i < 100:
        jgd['50-100'] += 1
    else:
        jgd['>100'] += 1

jgd = list(jgd.items())
plt.bar([i[0] for i in jgd],[i[1] for i in jgd])
plt.show()

xld = {'<10':0,'10-50':0,'50-100':0,'100-200':0,'200-400':0,'400-1000':0,'>1000':0}
xl = df['销量'].values.tolist()
for i in jg:
    if i < 10:
        xld['<10'] += 1
    elif i < 50:
        xld['10-50'] += 1
    elif i < 100:
        xld['50-100'] += 1
    elif i < 200:
        xld['100-200'] += 1
    elif i < 400:
        xld['200-400'] += 1
    elif i < 1000:
        xld['400-1000'] += 1
    else:
        xld['>1000'] += 1

xld = list(xld.items())
plt.plot([i[0] for i in xld],[i[1] for i in xld])
plt.show()

dq = df['省市自治区'].values.tolist()
dq = Counter(dq)
dq = sorted(dq.items())
plt.pie(labels=[i[0] for i in dq],x=[i[1] for i in dq])
plt.show()


LE_pj = LabelEncoder()
LE_dq = LabelEncoder()
RF = RandomForestRegressor()
x = df.drop(['销量'],axis=1)
x['评级'] = LE_pj.fit_transform(x['评级'])
x['省市自治区'] = LE_dq.fit_transform(x['省市自治区'])
y = df['销量']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
RF.fit(xtrain,ytrain)
ypred = RF.predict(xtest)
print(mean_squared_error(ytest,ypred) ** 0.5)
RF.fit(x,y)
ypred = RF.predict(x)
print(ypred)
print(df)
o_df['预测票价'] = ypred
o_df.to_excel('预测结果.xlsx',index=False)