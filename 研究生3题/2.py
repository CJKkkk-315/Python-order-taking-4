import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split, cross_val_predict
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
import warnings
warnings.filterwarnings('ignore')
data = pd.read_excel('data.xls')
data.replace({'default': {'yes': 1, 'no': 0}, 'housing': {'yes': 1, 'no': 0}, 'loan': {'yes': 1, 'no': 0}}, inplace=True)


month_dict = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12}
data['month'] = data['month'].map(month_dict)


data['contact'].replace('unknown', 'cellular', inplace=True)


for col in ['job', 'education']:
    data[col].replace('unknown', data[col].mode()[0], inplace=True)


data = pd.concat([data, pd.get_dummies(data['marital'], prefix='marital')], axis=1)
data.drop(['marital'],axis=1,inplace=True)

job_dict = {
    'management': 1,
    'technician': 2,
    'admin.': 3,
    'blue-collar': 4,
    'services': 5,
    'retired': 6,
    'self-employed': 7,
    'entrepreneur': 8,
    'unemployed': 9,
    'housemaid': 10,
    'student': 11,
}
data['job'] = data['job'].map(job_dict)


education_dict = {'unknown': 0, 'primary': 1, 'secondary': 2, 'tertiary': 3}
contact_dict = {'unknown': 0, 'cellular': 1, 'telephone': 2}
poutcome_dict = {'unknown': 0, 'failure': 1, 'other': 2, 'success': 3}

data['education'] = data['education'].map(education_dict)
data['contact'] = data['contact'].map(contact_dict)
data['poutcome'] = data['poutcome'].map(poutcome_dict)


job_age_ratio = data[data['job'].notna()].groupby('job')['age'].mean()
data['job_age_ratio'] = data['job'].apply(lambda x: job_age_ratio[x] if not pd.isnull(x) else np.nan)

new_data = data.copy()

scaler = MinMaxScaler()
columns_to_scale = ['age', 'balance', 'day', 'month', 'duration', 'campaign', 'pdays', 'previous']
new_data[columns_to_scale] = scaler.fit_transform(new_data[columns_to_scale])

X = new_data.drop('y', axis=1)
y = new_data['y']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

models = {
    'Logistic Regression': LogisticRegression(),
    'Support Vector Machine': SVC(),
    'Decision Tree': DecisionTreeClassifier()
}

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"{name} 模型混淆矩阵:")
    print(confusion_matrix(y_test, y_pred))
    print()

    y_cross_val_pred = cross_val_predict(model, X, y, cv=5)
    print(f"{name} 模型交叉验证预测混淆矩阵:")
    print(confusion_matrix(y, y_cross_val_pred))
    print()

