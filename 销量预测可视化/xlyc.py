import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_absolute_percentage_error, mean_squared_error
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('数据.xlsx')


c_name = list(df.columns)
c_name = c_name[1:-3]
xl_data = {i: [0 for _ in range(12)] for i in c_name}
sp_encode = {}
sp_decode = {}
idx = 0
for c in c_name:
    sp_encode[c] = idx
    sp_decode[idx] = c
    idx += 1
for c in c_name:
    for index, value in df.iterrows():
        xl_data[c][int(str(value[0]).split('-')[1])-1] += value[c]
for sp in xl_data:
    plt.plot(xl_data[sp], label=sp)
plt.legend()
plt.show()
y_xl = []
n_xl = []
for c in c_name:
    y_pj = []
    n_pj = []
    for index, value in df.iterrows():
        if value['是否周末或节假日']:
            y_pj.append(value[c])
        else:
            n_pj.append(value[c])
    y_xl.append(sum(y_pj)/len(y_pj))
    n_xl.append(sum(n_pj)/len(n_pj))

ww = 0.4
plt.bar([i for i in range(len(y_xl))],y_xl,width=ww,label='节假日')
plt.bar([i+ww for i in range(len(n_xl))],n_xl,width=ww,label='非节假日')
plt.xticks([x+ww/2 for x in range(len(n_xl))], c_name)
plt.legend()
plt.show()

X = []
y = []
for index, value in df.iterrows():
    for c in c_name:
        X.append([sp_encode[c],int(str(value[0]).split('-')[0]),int(str(value[0]).split('-')[1]),int(str(value[0]).split('-')[2].split()[0]),value['平均气温'],value['是否周末或节假日']])
        y.append(value[c])

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = DecisionTreeRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('决策树的MAE得分：',mean_absolute_error(y_test,y_pred))
print('决策树的MAPE得分：',mean_absolute_percentage_error(y_test,y_pred))
print('决策树的MSE得分：',mean_squared_error(y_test,y_pred))
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('决策树')
plt.legend()
plt.show()
res = [[i,j] for i,j in zip(['商品','年','月','日','温度','节假日'],abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('决策树特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')



model = MLPRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('神经网络的MAE得分：',mean_absolute_error(y_test,y_pred))
print('神经网络的MAPE得分：',mean_absolute_percentage_error(y_test,y_pred))
print('神经网络的MSE得分：',mean_squared_error(y_test,y_pred))
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('神经网络')
plt.legend()
plt.show()


model = SVR()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('支持向量机的MAE得分：',mean_absolute_error(y_test,y_pred))
print('支持向量机的MAPE得分：',mean_absolute_percentage_error(y_test,y_pred))
print('支持向量机的MSE得分：',mean_squared_error(y_test,y_pred))
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('支持向量机')
plt.legend()
plt.show()

model = RandomForestRegressor()
model.fit(X_train,y_train)
y_pred = model.predict(X_test)
print('随机森林的MAE得分：',mean_absolute_error(y_test,y_pred))
print('随机森林的MAPE得分：',mean_absolute_percentage_error(y_test,y_pred))
print('随机森林的MSE得分：',mean_squared_error(y_test,y_pred))
plt.plot([i for i in range(len(y_test[:100]))],y_test[:100],label='真实值',marker='*')
plt.plot([i for i in range(len(y_pred[:100]))],y_pred[:100],label='预测值',marker='o')
plt.title('随机森林')
plt.legend()
plt.show()
res = [[i,j] for i,j in zip(['商品','年','月','日','温度','节假日'],abs(model.feature_importances_))]
res.sort(key=lambda x:x[1],reverse=True)
print('随机森林特征重要性：')
for i in range(len(res)):
    print(f'{i+1}) {res[i][0]} {res[i][1]}')


yc = pd.read_excel('预测.xlsx')
for c in c_name:
    ycx = []
    for idx,value in yc.iterrows():
        ycx.append([sp_encode[c],int(str(value[0]).split('-')[0]),int(str(value[0]).split('-')[1]),int(str(value[0]).split('-')[2].split()[0]),value['温度'],value['是否节假日']])
    res = model.predict(ycx)
    yc[c] = [round(i) for i in res]

yc.to_excel('res.xlsx',index=False)