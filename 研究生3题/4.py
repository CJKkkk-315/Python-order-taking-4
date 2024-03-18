import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
import warnings
warnings.filterwarnings('ignore')
data = pd.read_excel('lol.xlsx')
data = data[['armor','attackData','attackMag','attackRange','attackSpeed','lifeData','lifeMag','magic','spellBlock','price']]
data['attack1'] = data['attackData'].map(lambda x:x.split('/')[0])
data['attack2'] = data['attackData'].map(lambda x:x.split('/')[1])
data['attack3'] = data['attackData'].map(lambda x:x.split('/')[2])

data['lifeData1'] = data['lifeData'].map(lambda x:x.split('/')[0])
data['lifeData2'] = data['lifeData'].map(lambda x:x.split('/')[1])
data['lifeData3'] = data['lifeData'].map(lambda x:x.split('/')[2])

data.drop(['lifeData'],axis=1,inplace=True)
data.drop(['attackData'],axis=1,inplace=True)

X = data.drop('price', axis=1)
y = data['price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC(),
    'Decision Tree': DecisionTreeClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{name} 准确率:{accuracy_score(y_test, y_pred)}")
    print(f"{name} 模型混淆矩阵:")
    print(confusion_matrix(y_test, y_pred))
    print()
