import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor,BaggingRegressor,AdaBoostRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
random_seed = np.random.randint(1,100)
data = pd.read_csv('replacement_orders_train.csv')
X = data.drop(['2021-Q3'],axis=1)

scaler = MinMaxScaler()
scaler.fit(X)
# X = scaler.transform(X)


y = data['2021-Q3']
# plt_data = [[i,j] for i,j in Counter(y.values.tolist()).items() if 0 < i < 20]
# plt_data.sort()
# plt.plot([i[0] for i in plt_data],[i[1] for i in plt_data])
# plt.show()

xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=random_seed)



model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('LinearRegression RMSE:',RMSE)

model = DecisionTreeRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('DecisionTreeRegressor RMSE:',RMSE)

model = RandomForestRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('RandomForestRegressor RMSE:',RMSE)

model = BaggingRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('BaggingRegressor RMSE:',RMSE)

model = AdaBoostRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('AdaBoostRegressor RMSE:',RMSE)

model = MLPRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('MLPRegressor RMSE:',RMSE)

model = SVR()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('SVR RMSE:',RMSE)





X = scaler.transform(X)


xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2, random_state=random_seed)



model = LinearRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('LinearRegression RMSE:',RMSE)

model = DecisionTreeRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('DecisionTreeRegressor RMSE:',RMSE)

model = RandomForestRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('RandomForestRegressor RMSE:',RMSE)

model = BaggingRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('BaggingRegressor RMSE:',RMSE)

model = AdaBoostRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('AdaBoostRegressor RMSE:',RMSE)

model = MLPRegressor()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('MLPRegressor RMSE:',RMSE)

model = SVR()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
RMSE = np.sqrt(mean_squared_error(ytest,ypred))
print('SVR RMSE:',RMSE)

model = RandomForestRegressor()
