import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
df = pd.read_csv('secondary_data.csv',delimiter=';')
X,y = df.drop(['class'],axis=1),df['class']
X = pd.get_dummies(X)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = GaussianNB()
param_grid = {'var_smoothing':[1e-7,1e-8,1e-9,1e-10,1e-11]}
grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print('Best Parameters: ', grid_search.best_params_)
model = DecisionTreeClassifier()
param_grid = {'max_depth': [2, 4, 6, 8, 10],
              'min_samples_split': [2, 4, 6, 8, 10],
              'min_samples_leaf': [1, 2, 3, 4, 5]}

grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, scoring='accuracy')
grid_search.fit(X_train, y_train)
print('Best Parameters: ', grid_search.best_params_)

model = GaussianNB(var_smoothing=1e-07)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5, scoring='accuracy')
print('GaussianNB Accuracy: %0.2f (+/- %0.2f)' % (scores.mean(), scores.std() * 2))
model = DecisionTreeClassifier(max_depth=10, min_samples_split=10, min_samples_leaf=1)
scores = cross_val_score(estimator=model, X=X, y=y, cv=5, scoring='accuracy')
print('Decision Tree Accuracy: %0.2f (+/- %0.2f)' % (scores.mean(), scores.std() * 2))



