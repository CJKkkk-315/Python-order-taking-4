# 导入必要的库
import pandas as pd
from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from fairlearn.metrics import MetricFrame

# 读取特征和标签
X = pd.read_csv('training_set_features.csv')
y = pd.read_csv('training_set_labels.csv')
# 去除掉无作用的respondent_id列
X.drop(['respondent_id'],axis=1,inplace=True)
y.drop(['respondent_id'],axis=1,inplace=True)
# 单独提取要预测的两个目标
y1 = y['h1n1_vaccine']
y2 = y['seasonal_vaccine']

# 对非数值型特征进行编码
LE = LabelEncoder()
for c in X.columns:
    if str(X[c].dtype) != 'float64':
        X[c] = LE.fit_transform(X[c])
# 利用平均值填充空值
X.fillna(X.mean(),inplace=True)
# 将数据集8比2分隔为训练集和测试机
# X_train, X_test, y_train, y_test = train_test_split(X,y1,test_size=0.2)
# # 使用三种模型进行训练，并输出精确度
# DT = DecisionTreeClassifier()
# RF = RandomForestClassifier()
# SV = SVC()
# DT.fit(X_train,y_train)
# y_pred = DT.predict(X_test)
# print(accuracy_score(y_test,y_pred))
#
# RF.fit(X_train,y_train)
# y_pred = RF.predict(X_test)
# print(accuracy_score(y_test,y_pred))
#
# SV.fit(X_train,y_train)
# y_pred = SV.predict(X_test)
# print(accuracy_score(y_test,y_pred))
#
#
# X_train, X_test, y_train, y_test = train_test_split(X,y2,test_size=0.2)
# DT = DecisionTreeClassifier()
# RF = RandomForestClassifier()
# SV = SVC()
# DT.fit(X_train,y_train)
# y_pred = DT.predict(X_test)
# print(accuracy_score(y_test,y_pred))
#
# RF.fit(X_train,y_train)
# y_pred = RF.predict(X_test)
# print(accuracy_score(y_test,y_pred))
#
# y_pred = SV.predict(X_test)
# print(accuracy_score(y_test,y_pred))
# 读取最终需要预测的数据集
test_set = pd.read_csv('test_set_features.csv')
rid = test_set['respondent_id']
test_set.drop(['respondent_id'],axis=1,inplace=True)
# 对预测集进行同样的编码
LE = LabelEncoder()
for c in test_set.columns:
    if str(test_set[c].dtype) != 'float64':
        test_set[c] = LE.fit_transform(test_set[c])
test_set.fillna(test_set.mean(),inplace=True)
# 最终选用随机森林进行拟合预测
RF = RandomForestClassifier()
RF.fit(X,y1)
y1_pred = RF.predict(test_set)
RF.fit(X,y2)
y2_pred = RF.predict(test_set)
# 预测得到两个标签结果后，转换为dataframe数据集，写入csv文件中
d = {'respondent_id':rid,'h1n1_vaccine':y1_pred,'seasonal_vaccine':y2_pred}
pd.DataFrame(d).to_csv('res.csv',index=False)

RF.fit(X,y1)
sex = X['sex']
y1_pred = RF.predict(X) # 得到预测结果
gm = MetricFrame(metrics=accuracy_score, y_true=y1, y_pred=y1_pred, sensitive_features=sex)
print(gm.overall)  # 获取整个数据集的预测精度
print(gm.by_group) # 获取各个群体的预测精度

from fairlearn.reductions import ExponentiatedGradient,DemographicParity
constraint = DemographicParity()
RF = RandomForestClassifier()
mitigator = ExponentiatedGradient(RF,constraint) # 指数梯度缓解技术
mitigator.fit(X,y1,sensitive_features=sex) # 重新训练模型

y_pred_mitigated = mitigator.predict(X)
sr_mitigated = MetricFrame(metrics=accuracy_score,y_true=y1,y_pred=y_pred_mitigated,sensitive_features=sex)
print(sr_mitigated.overall)
print(sr_mitigated.by_group)
