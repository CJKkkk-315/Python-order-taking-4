import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score

df = pd.read_csv('movie_metadata.csv',encoding='gbk')
df = df.drop(['director_name','actor_2_name','genres','actor_1_name','movie_title','actor_3_name','plot_keywords','movie_imdb_link'], axis=1)
df = df.iloc[700:800,:]
print(df)
df.dropna(inplace=True)

label_encoders = {}
for column in df.columns:
    if not pd.api.types.is_numeric_dtype(df[column]):
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])
        label_encoders[column] = le
print(df)

X = df.drop(columns=['imdb_score'])
y = df['imdb_score']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=88)

regressor = DecisionTreeRegressor(random_state=88)
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Absolute Error: {mae:.4f}")
print(f"R2: {r2:.4f}")

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree
plt.figure(figsize=(18,12))
plot_tree(regressor,fontsize=12,feature_names=df.columns)
plt.show()