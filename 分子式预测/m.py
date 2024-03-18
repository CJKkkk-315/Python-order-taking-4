# 引入相关库
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
# 读取训练集和预测集
train = pd.read_excel('分子类型预测 for students.xlsx',sheet_name='training dataset')
test = pd.read_excel('分子类型预测 for students.xlsx',sheet_name='validation dataset')
# 提取formula标识，对构建模型没有帮助
formula = test['formula']
test.drop(['Type','formula'],axis=1,inplace=True)
# 构建编码器
LE = LabelEncoder()
# 将训练集分为X，y
X = train.drop(['Type','formula'],axis=1)
y = train['Type']
# 将非数值型编码为数值型
for c in X.columns:
    if str(X[c].dtype) not in ['float64','int64']:
        X[c] = LE.fit_transform(X[c])
# 使用决策树拟合训练集
DT = DecisionTreeClassifier()
DT.fit(X,y)
# 同样编码预测集
for c in test.columns:
    if str(test[c].dtype) not in ['float64','int64']:
        test[c] = LE.fit_transform(test[c])
# 利用构建好的模型预测
ypred = DT.predict(test)
# 将结果转为dataframe，保存为csv文件
res = {'formula':formula,'predicted type':ypred}
res = pd.DataFrame(res)
res.to_csv('res.csv',index=False)