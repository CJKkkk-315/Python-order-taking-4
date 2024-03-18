import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_csv('去哪儿攻略·.csv',header=None)
df = df[[2,3]].dropna()
print(df)
plt.scatter(df[2], df[3])
plt.ylim(-2,20)
plt.xlim(-1000,10000)

model = LinearRegression()
model.fit(df[2].values.reshape(-1,1),df[3].values.reshape(-1,1))
x = numpy.linspace(-1000,9000)
y = model.predict(x.reshape(-1,1))
plt.plot(x,y,c='red')
plt.show()