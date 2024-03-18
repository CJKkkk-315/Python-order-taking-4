import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
df = pd.read_csv('B-diabetes/diabetes.csv')
X = df.drop(['Outcome'])
y = df['Outcome']
X.fillna(X.mean(),inplace=True)
X_train, X_test, y_train, y_test = train_test_split(X,y1,test_size=0.2)
DT = DecisionTreeClassifier()
RF = RandomForestClassifier()
SV = SVC()
DT.fit(X_train,y_train)
y_pred = DT.predict(X_test)
print(accuracy_score(y_test,y_pred))

RF.fit(X_train,y_train)
y_pred = RF.predict(X_test)
print(accuracy_score(y_test,y_pred))

SV.fit(X_train,y_train)
y_pred = SV.predict(X_test)
print(accuracy_score(y_test,y_pred))


X_train, X_test, y_train, y_test = train_test_split(X,y2,test_size=0.2)
DT = DecisionTreeClassifier()
RF = RandomForestClassifier()
SV = SVC()
DT.fit(X_train,y_train)
y_pred = DT.predict(X_test)
print(accuracy_score(y_test,y_pred))

RF.fit(X_train,y_train)
y_pred = RF.predict(X_test)
print(accuracy_score(y_test,y_pred))

SV.fit(X_train,y_train)
y_pred = SV.predict(X_test)
print(accuracy_score(y_test,y_pred))

test_set = pd.read_csv('test_set_features.csv')
rid = test_set['respondent_id']
test_set.drop(['respondent_id'],axis=1,inplace=True)
LE = LabelEncoder()
for c in test_set.columns:
    if str(test_set[c].dtype) != 'float64':
        test_set[c] = LE.fit_transform(test_set[c])
test_set.fillna(test_set.mean(),inplace=True)

RF.fit(X,y1)
y1_pred = RF.predict(test_set)
RF.fit(X,y2)
y2_pred = RF.predict(test_set)
d = {'respondent_id':rid,'h1n1_vaccine':y1_pred,'seasonal_vaccine':y2_pred}
pd.DataFrame(d).to_csv('res.csv',index=False)