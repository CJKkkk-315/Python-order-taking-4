import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
X = pd.read_csv('50指数feature_data.csv')
y = pd.read_csv('50指数label.csv')
y = y.values.reshape(y.shape[0],)
print(X.isnull().any())
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)
RF = RandomForestClassifier()
RF.fit(xtrain,ytrain)
ypred = RF.predict(xtest)
rf_acc = accuracy_score(ytest,ypred)
print('RF accuracy_score:',rf_acc)

MLP = MLPClassifier()
MLP.fit(xtrain,ytrain)
ypred = MLP.predict(xtest)
mlp_acc = accuracy_score(ytest,ypred)
print('MLP accuracy_score:',mlp_acc)

LR = LogisticRegression()
LR.fit(xtrain,ytrain)
ypred = LR.predict(xtest)
lr_acc = accuracy_score(ytest,ypred)
print('LR accuracy_score:',lr_acc)

