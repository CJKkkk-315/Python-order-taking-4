import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
data = pd.read_excel('广告收益数据.xlsx')
x = data[['电视','广播','报纸']]
y = data['收益']
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)
model = LinearRegression()
model.fit(xtrain,ytrain)
ypre = model.predict(xtest)
r2 = r2_score(ytest,ypre)
print('R2数值为：',r2)