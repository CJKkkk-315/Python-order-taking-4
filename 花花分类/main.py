from sklearn.metrics import accuracy_score,recall_score,f1_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import pandas as pd

df = pd.read_csv('iris.data',header=None)
X = df.drop([4],axis=1)
y = df[4]
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.5)
DT = DecisionTreeClassifier(max_depth=20)
SV = SVC(C=0.5)
LR = LogisticRegression(solver='liblinear',penalty='l1',multi_class='ovr')
DT.fit(X_train,y_train)
SV.fit(X_train,y_train)
LR.fit(X_train,y_train)
ypred = DT.predict(X_test)
print('DecisionTree accuracy:',accuracy_score(y_test,ypred))
print('DecisionTree recall:',recall_score(y_test,ypred,average='weighted'))
print('DecisionTree f1 score:',f1_score(y_test,ypred,average='weighted'))
ypred = SV.predict(X_test)
print('SV accuracy:',accuracy_score(y_test,ypred))
print('SV recall:',recall_score(y_test,ypred,average='weighted'))
print('SV f1 score:',f1_score(y_test,ypred,average='weighted'))
ypred = LR.predict(X_test)
print('LogisticRegression accuracy:',accuracy_score(y_test,ypred))
print('LogisticRegression recall:',recall_score(y_test,ypred,average='weighted'))
print('LogisticRegression f1 score:',f1_score(y_test,ypred,average='weighted'))