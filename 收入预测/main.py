from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,recall_score
from sklearn.preprocessing import LabelEncoder
import pandas as pd
train = pd.read_csv('train.csv',header=None)
test = pd.read_csv('test.csv',header=None)
X_train = train.drop(41,axis=1)
y_train = train[41]
X_test = test.drop(41,axis=1)
y_test = test[41]
LE = LabelEncoder()
for c in X_train.columns:
    if str(X_train[c].dtype) != 'int64':
        X_train[c] = LE.fit_transform(X_train[c])

LE = LabelEncoder()
for c in X_test.columns:
    if str(X_test[c].dtype) != 'int64':
        X_test[c] = LE.fit_transform(X_test[c])

DT = DecisionTreeClassifier()
DT.fit(X_train,y_train)
y_pred = DT.predict(X_test)
print('决策树准确率:',accuracy_score(y_test,y_pred))
print('决策树召回率:',recall_score(y_test,y_pred,pos_label=' 50000+.'))

SV = SVC()
SV.fit(X_train,y_train)
y_pred = SV.predict(X_test)
print('支持向量机准确率:',accuracy_score(y_test,y_pred))
print('支持向量机召回率:',recall_score(y_test,y_pred,pos_label=' 50000+.'))

MLP = MLPClassifier()
MLP.fit(X_train,y_train)
y_pred = MLP.predict(X_test)
print('神经网络准确率:',accuracy_score(y_test,y_pred))
print('神经网络召回率:',recall_score(y_test,y_pred,pos_label=' 50000+.'))

RF = RandomForestClassifier()
RF.fit(X_train,y_train)
y_pred = RF.predict(X_test)
print('随机森林准确率:',accuracy_score(y_test,y_pred))
print('随机森林召回率:',recall_score(y_test,y_pred,pos_label=' 50000+.'))

