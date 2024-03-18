import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score, f1_score
import numpy as np
import os
from collections import Counter
from lightgbm import LGBMClassifier
from xgboost import XGBClassifier
import warnings
warnings.filterwarnings('ignore', category=UserWarning)
files = os.listdir('data')
df = pd.read_excel('data/' + files[0])
data = df.values
data = data[2:,1:]
for file in files[1:]:
    df = pd.read_excel('data/' + file)
    file_data = df.values
    file_data = file_data[2:,1:]
    data = np.r_[data, file_data]

X = data[:,:-4]
y1 = data[:,-1].astype('int')
X1_train, X1_test, y1_train, y1_test = train_test_split(X, y1, test_size=0.2)
model1 = LGBMClassifier(max_depth=10)
model1.fit(X1_train,y1_train)

X = data[:,:-4]
y2 = data[:,-2].astype('int')
X2_train, X2_test, y2_train, y2_test = train_test_split(X, y2, test_size=0.2)
model2 = LGBMClassifier()
model2.fit(X2_train,y2_train)

X = data[:,:-4]
y3 = data[:,-3].astype('int')
X3_train, X3_test, y3_train, y3_test = train_test_split(X, y3, test_size=0.2)
model3 = LGBMClassifier()
model3.fit(X3_train,y3_train)

X = data[:,:-4]
y4 = data[:,-4].astype('int')
X4_train, X4_test, y4_train, y4_test = train_test_split(X, y4, test_size=0.2)
model4 = LGBMClassifier()
model4.fit(X4_train,y4_train)


y_pred = model1.predict(X1_test)
y_pred_proba = model1.predict_proba(X1_test)[:, 1]
acc = accuracy_score(y1_test,y_pred)
prec = precision_score(y1_test,y_pred)
recall = recall_score(y1_test,y_pred)
auc_score = roc_auc_score(y1_test, y_pred_proba)
f1 = f1_score(y1_test, y_pred)
print(f'lightgbm,1,F1分数:{f1}')
print(f'lightgbm,1,精确率:{acc}')
print(f'lightgbm,1,准确率:{prec}')
print(f'lightgbm,1,召回率:{recall}')
print(f'lightgbm,1,AUC:{auc_score}')



y_pred = model2.predict(X2_test)
y_pred_proba = model2.predict_proba(X2_test)[:, 1]
acc = accuracy_score(y2_test,y_pred)
prec = precision_score(y2_test,y_pred)
recall = recall_score(y2_test,y_pred)
auc_score = roc_auc_score(y2_test, y_pred_proba)
f2 = f1_score(y2_test, y_pred)
print(f'lightgbm,1,F1分数:{f2}')
print(f'lightgbm,2,精确率:{acc}')
print(f'lightgbm,2,准确率:{prec}')
print(f'lightgbm,2,召回率:{recall}')
print(f'lightgbm,2,AUC:{auc_score}')


y_pred = model3.predict(X3_test)
y_pred_proba = model3.predict_proba(X3_test)[:, 1]
acc = accuracy_score(y3_test,y_pred)
prec = precision_score(y3_test,y_pred)
recall = recall_score(y3_test,y_pred)
auc_score = roc_auc_score(y3_test, y_pred_proba)
f3 = f1_score(y3_test, y_pred)
print(f'lightgbm,1,F1分数:{f3}')
print(f'lightgbm,3,精确率:{acc}')
print(f'lightgbm,3,准确率:{prec}')
print(f'lightgbm,3,召回率:{recall}')
print(f'lightgbm,3,AUC:{auc_score}')


y_pred = model4.predict(X4_test)
y_pred_proba = model4.predict_proba(X4_test)[:, 1]
acc = accuracy_score(y4_test,y_pred)
prec = precision_score(y4_test,y_pred)
recall = recall_score(y4_test,y_pred)
auc_score = roc_auc_score(y4_test, y_pred_proba)
f4 = f1_score(y4_test, y_pred)
print(f'lightgbm,1,F1分数:{f4}')
print(f'lightgbm,4,精确率:{acc}')
print(f'lightgbm,4,准确率:{prec}')
print(f'lightgbm,4,召回率:{recall}')
print(f'lightgbm,4,AUC:{auc_score}')

