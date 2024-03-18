# 引入需要的库
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 读取数据
df = pd.read_excel('DataSet.xlsx')
# 去除Index列，没有意义
df.drop(['Index'],axis=1,inplace=True)
# 将0，1转为女男
df['label'] = df['label'].replace(0,'女').replace(1,'男')
print(df)
# 统计男女比例
pj = df['label'].values.tolist()
# 计算出现次数
pj = Counter(pj)
# 转为列表
pj = list(pj.items())
# 饼图展示
plt.pie(labels=[i[0] for i in pj],x=[i[1] for i in pj])
plt.show()

# 选择支持向量机，逻辑回归，和决策树三种模型
SV = SVC()
LR = LogisticRegression()
DT = DecisionTreeClassifier()
# 将label外的列设置为x,label列设置为y
x = df.drop(['label'],axis=1)
y = df['label']
# 以8比2分隔训练集和测试集
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# 依次对三种模型进行训练，预测，精确度计算
SV.fit(xtrain,ytrain)
ypred = SV.predict(xtest)
print('SV:',accuracy_score(ytest,ypred))

LR.fit(xtrain,ytrain)
ypred = LR.predict(xtest)
print('LR:',accuracy_score(ytest,ypred))

DT.fit(xtrain,ytrain)
ypred = DT.predict(xtest)
print('DT:',accuracy_score(ytest,ypred))

