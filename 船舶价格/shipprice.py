from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix,accuracy_score,roc_auc_score,classification_report
import pandas as pd
import random
data = pd.read_csv('shipprice(1).csv')
mean = data['capesize'].mean()
data['capesize'] = data['capesize'].apply(lambda x:'H' if x > mean else 'L')

X = data.drop(['capesize'],axis=1)
y = data['capesize']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model3 = LogisticRegression(random_state=10)

model3.fit(X_train,y_train)

model4 = LogisticRegression(random_state=10)

model4.fit(X_train.drop(['bci'],axis=1),y_train)

mean_test_3 = []
mean_test_4 = []
for c in data.columns[:-1]:
    mean_test_3.append(data[c].mean())
    if c != 'bci':
        mean_test_4.append(data[c].mean())
print(f'model 3 probability that ship price is ‘H’ = ',model3.predict_proba([mean_test_3])[0][1])
print(f'model 4 probability that ship price is ‘H’ = ',model4.predict_proba([mean_test_4])[0][1])

ypred = model3.predict(X_test)
ypred_proba = model3.predict_proba(X_test)
print('model 3 confusion_matrix:')
print(confusion_matrix(y_test,ypred))

print('model 3 AUC:')
print(roc_auc_score([0 if i == 'L' else 1 for i in y_test],ypred_proba[:,0]))

print('model 3 classification report:')
print(classification_report(y_test,ypred))

print('model 3 accuracy score:')
print(accuracy_score(y_test,ypred))

print('--------------------------------------------------')

ypred = model4.predict(X_test.drop(['bci'],axis=1))
ypred_proba = model3.predict_proba(X_test)
print('model 4 confusion_matrix:')
print(confusion_matrix(y_test,ypred))

print('model 4 AUC:')
print(roc_auc_score([0 if i == 'L' else 1 for i in y_test],ypred_proba[:,0]))

print('model 4 classification report:')
print(classification_report(y_test,ypred))

print('model 4 accuracy score:')
print(accuracy_score(y_test,ypred))

