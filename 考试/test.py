from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
digits = load_breast_cancer()
train_test_split(test_size=0.3)
knc.fit(X_train,y_train)
knc.predict(X_test)


from sklearn import metrics
metrics.mean_absolute_error(true,pred)
metrics.mean_squared_error(true,pred)
metrics.r2_score(true,pred)



from sklearn import linear_model
