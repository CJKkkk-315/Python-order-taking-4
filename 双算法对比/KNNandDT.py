import pandas as pd
import time
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report
import warnings
warnings.filterwarnings('ignore')

df_train = pd.read_csv("adult.data", sep=', ', header=None)
df_test = pd.read_csv("adult.test", sep=', ', skiprows=1, header=None)
print(df_train)

df_train = df_train.replace({"?": None}).dropna()
df_test = df_test.replace({"?": None}).dropna()
print(df_train)


for column in df_train.columns:
    if pd.api.types.is_numeric_dtype(df_train[column]):
        scaler = StandardScaler()
        df_train[column] = scaler.fit_transform(df_train[[column]])
    else:
        le = LabelEncoder()
        df_train[column] = le.fit_transform(df_train[[column]])


for column in df_test.columns:
    if pd.api.types.is_numeric_dtype(df_test[column]):
        scaler = StandardScaler()
        df_test[column] = scaler.fit_transform(df_test[[column]])
    else:
        le = LabelEncoder()
        df_test[column] = le.fit_transform(df_test[[column]])

X_train = df_train.drop(df_train.columns[-1], axis=1)
y_train = df_train[df_train.columns[-1]]
X_test = df_test.drop(df_test.columns[-1], axis=1)
y_test = df_test[df_test.columns[-1]]
start_time = time.time()
knn_classifier = KNeighborsClassifier(n_neighbors=5)
knn_classifier.fit(X_train, y_train)
end_time = time.time()
training_time = end_time - start_time
print("KNN fit time：", training_time, " seconds")
start_time = time.time()
knn_predictions = knn_classifier.predict(X_test)
end_time = time.time()
predict_time = end_time - start_time
print("KNN predict time：", predict_time, " seconds")
knn_accuracy = accuracy_score(y_test, knn_predictions)
knn_f1 = f1_score(y_test, knn_predictions)

tree_classifier = DecisionTreeClassifier()
start_time = time.time()
tree_classifier.fit(X_train, y_train)
end_time = time.time()
training_time = end_time - start_time
print("DecisionTree fit time：", training_time, " seconds")
start_time = time.time()
tree_predictions = tree_classifier.predict(X_test)
end_time = time.time()
predict_time = end_time - start_time
print("DecisionTree predict time：", predict_time, " seconds")
tree_accuracy = accuracy_score(y_test, tree_predictions)
tree_f1 = f1_score(y_test, tree_predictions)
print("KNN Accuracy:", knn_accuracy)
print("DecisionTree Accuracy:", tree_accuracy)

balance_check = y_train.value_counts()
# print(balance_check)

print("KNN F1-score:", knn_f1)
print("DecisionTree F1-score:", tree_f1)



