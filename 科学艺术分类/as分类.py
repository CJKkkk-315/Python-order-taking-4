import os
import pandas as pd
import warnings
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
warnings.filterwarnings('ignore')
data = os.listdir('data')
res_x = []
res_y = []
class_encode = {'Science':2,'Scientific':2, 'SocialScience':1, 'SocialScienc':1, 'Arts':0, 'Art':0}
for i in data:
    df = pd.read_excel('data/' + i)
    d = df.values.tolist()
    for j in d[1:]:
        if str(j[-1]) != 'nan':
            res_x.append(j[1:-1])
            res_y.append(class_encode[j[-1].replace(' ','')])

for i in range(len(res_x)):
    for j in range(len(res_x[i])):
        tag = res_x[i][j]
        if str(tag) == 'nan':
            res_x[i][j] = 0
        elif tag == 'Y1' or tag == 'Y':
            res_x[i][j] = 1
        elif tag == 'Y2':
            res_x[i][j] = 2
        elif tag == 'Y1,2':
            res_x[i][j] = 3

xtrain, xtest, ytrain, ytest = train_test_split(res_x, res_y, test_size=0.5)

model = DecisionTreeClassifier()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
acc = accuracy_score(ytest,ypred)
print('决策树分类精确度',acc)

model = KMeans(n_clusters=3)
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
acc = accuracy_score(ytest,ypred)
print('Kmeans聚类精确度',acc)

model = LogisticRegression()
model.fit(xtrain,ytrain)
ypred = model.predict(xtest)
acc = accuracy_score(ytest,ypred)
print('逻辑回归精确度',acc)