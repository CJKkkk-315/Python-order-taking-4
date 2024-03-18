import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pandas as pd
from scipy.io import arff
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score, StratifiedKFold
from sklearn.metrics import roc_curve, auc
import warnings
warnings.filterwarnings('ignore')
def load_arff_file(file_path):
    with open(file_path, 'r') as f:
        arff_data, meta = arff.loadarff(f)
    return pd.DataFrame(arff_data)

def fill_missing_values(df):
    for col in df.columns:
        most_common = df[col].mode()[0]
        df[col].replace('?', most_common, inplace=True)
        df[col].fillna(most_common, inplace=True)
    return df

def convert_non_numeric_to_numeric(df):
    label_encoders = {}
    for col in df.columns:
        if df[col].dtype == object:
            df[col] = df[col].apply(lambda x: x.decode('utf-8').replace("'","").strip())
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            label_encoders[col] = le
    return df, label_encoders

def train_and_predict(data, target_col):
    X = data.drop(target_col, axis=1).values
    y = data[target_col].values
    print(X)
    print(y)


    classifiers = [
        LogisticRegression(),
        KNeighborsClassifier(),
        DecisionTreeClassifier(),
        RandomForestClassifier(),
        SVC(probability=True),
        GaussianNB()
    ]

    for clf in classifiers:
        # pipeline = Pipeline(steps=[('classifier', clf)])
        # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        # pipeline.fit(X_train, y_train)
        # y_pred = pipeline.predict(X_test)
        # accuracy = accuracy_score(y_test, y_pred)
        # print(f"{clf.__class__.__name__} 准确率: {accuracy:.3f}")
        # 进行5折交叉验证
        cv = StratifiedKFold(n_splits=5)

        tprs = []
        aucs = []
        mean_fpr = np.linspace(0, 1, 100)

        i = 0
        pipeline = Pipeline(steps=[('classifier', clf)])
        for train, test in cv.split(X, y):

            probas_ = pipeline.fit(X[train], y[train]).predict_proba(X[test])
            # Compute ROC curve and area under the curve
            fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
            tprs.append(np.interp(mean_fpr, fpr, tpr))
            tprs[-1][0] = 0.0
            roc_auc = auc(fpr, tpr)
            aucs.append(roc_auc)
            plt.plot(fpr, tpr, lw=1, alpha=0.3,
                     label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))
            i += 1

        plt.plot([0, 1], [0, 1], linestyle='--', lw=2, color='r', label='Luck', alpha=.8)

        mean_tpr = np.mean(tprs, axis=0)
        mean_tpr[-1] = 1.0
        mean_auc = auc(mean_fpr, mean_tpr)
        std_auc = np.std(aucs)
        plt.plot(mean_fpr, mean_tpr, color='b',
                 label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
                 lw=2, alpha=.8)

        plt.xlim([-0.05, 1.05])
        plt.ylim([-0.05, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title(clf.__class__.__name__)
        plt.legend(loc="lower right")
        plt.show()

        # 计算平均准确率
        scores = cross_val_score(clf, X, y, cv=5)
        print(f"{clf.__class__.__name__} 准确率: {np.mean(scores):.3f}")

    final_model = RandomForestClassifier()
    final_model.fit(X,y)
    return final_model
def submit():

    data = {
        'A1_Score': [int(a1_score.get())],
        'A2_Score': [int(a2_score.get())],
        'A3_Score': [int(a3_score.get())],
        'A4_Score': [int(a4_score.get())],
        'A5_Score': [int(a5_score.get())],
        'A6_Score': [int(a6_score.get())],
        'A7_Score': [int(a7_score.get())],
        'A8_Score': [int(a8_score.get())],
        'A9_Score': [int(a9_score.get())],
        'A10_Score': [int(a10_score.get())],
        'age': [int(age.get())],
        'gender': [gender.get()],
        'ethnicity': [ethnicity.get()],
        'jundice': [jundice.get()],
        'austim': [austim.get()],
        'contry_of_res': [contry_of_res.get()],
        'used_app_before': [used_app_before.get()],
        'result': [int(result.get())],
        'relation': [relation.get()],
    }

    df = pd.DataFrame(data)
    test = [str(i) for i in list(df.iloc[0])]
    print(test)
    for i in range(len(test)):
        if df.columns[i] in label_encoders:
            test[i] = label_encoders[df.columns[i]].transform([test[i]])[0]
        else:
            test[i] = float(test[i])
    res = final_model.predict([test])[0]
    if res:
        messagebox.showinfo('预测结果', f'预测结果为患有ADS！')
    else:
        messagebox.showinfo('预测结果', f'预测结果为未患有ADS！')
file_path = 'Autism-Child-Data.arff'
target_col = 'Class/ASD'
df = load_arff_file(file_path)
df.drop(['age_desc'],axis=1,inplace=True)
df = fill_missing_values(df)
df, label_encoders = convert_non_numeric_to_numeric(df)
final_model = train_and_predict(df, target_col)



app = tk.Tk()
app.title("ASD 检测")

a1_score = tk.StringVar()
a2_score = tk.StringVar()
a3_score = tk.StringVar()
a4_score = tk.StringVar()
a5_score = tk.StringVar()
a6_score = tk.StringVar()
a7_score = tk.StringVar()
a8_score = tk.StringVar()
a9_score = tk.StringVar()
a10_score = tk.StringVar()
age = tk.StringVar()
gender = tk.StringVar()
ethnicity = tk.StringVar()
jundice = tk.StringVar()
austim = tk.StringVar()
contry_of_res = tk.StringVar()
used_app_before = tk.StringVar()
result = tk.StringVar()
age_desc = tk.StringVar()
relation = tk.StringVar()

ttk.Label(app, text="A1_Score (0, 1)").grid(column=0, row=0)
ttk.Combobox(app, width=12, textvariable=a1_score, values=['0', '1']).grid(column=1, row=0)

ttk.Label(app, text="A2_Score (0, 1)").grid(column=0, row=1)
ttk.Combobox(app, width=12, textvariable=a2_score, values=['0', '1']).grid(column=1, row=1)

ttk.Label(app, text="A3_Score (0, 1)").grid(column=0, row=2)
ttk.Combobox(app, width=12, textvariable=a3_score, values=['0', '1']).grid(column=1, row=2)
ttk.Label(app, text="A4_Score (0, 1)").grid(column=0, row=3)
ttk.Combobox(app, width=12, textvariable=a4_score, values=['0', '1']).grid(column=1, row=3)
ttk.Label(app, text="A5_Score (0, 1)").grid(column=0, row=4)
ttk.Combobox(app, width=12, textvariable=a5_score, values=['0', '1']).grid(column=1, row=4)
ttk.Label(app, text="A6_Score (0, 1)").grid(column=0, row=5)
ttk.Combobox(app, width=12, textvariable=a6_score, values=['0', '1']).grid(column=1, row=5)
ttk.Label(app, text="A7_Score (0, 1)").grid(column=0, row=6)
ttk.Combobox(app, width=12, textvariable=a7_score, values=['0', '1']).grid(column=1, row=6)
ttk.Label(app, text="A8_Score (0, 1)").grid(column=0, row=7)
ttk.Combobox(app, width=12, textvariable=a8_score, values=['0', '1']).grid(column=1, row=7)
ttk.Label(app, text="A9_Score (0, 1)").grid(column=0, row=8)
ttk.Combobox(app, width=12, textvariable=a9_score, values=['0', '1']).grid(column=1, row=8)

ttk.Label(app, text="A10_Score (0, 1)").grid(column=0, row=9)
ttk.Combobox(app, width=12, textvariable=a10_score, values=['0', '1']).grid(column=1, row=9)

ttk.Label(app, text="age (numeric)").grid(column=2, row=7)
ttk.Entry(app, width=12, textvariable=age).grid(column=3, row=7)

ttk.Label(app, text="gender (m, f)").grid(column=2, row=0)
ttk.Combobox(app, width=12, textvariable=gender, values=['m', 'f']).grid(column=3, row=0)

ttk.Label(app, text="ethnicity").grid(column=2, row=1)
ttk.Combobox(app, width=12, textvariable=ethnicity, values=['Others', 'Middle Eastern', 'White-European', 'Black', 'South Asian', 'Asian', 'Pasifika', 'Hispanic', 'Turkish', 'Latino']).grid(column=3, row=1)

ttk.Label(app, text="jundice (no, yes)").grid(column=2, row=2)
ttk.Combobox(app, width=12, textvariable=jundice, values=['no', 'yes']).grid(column=3, row=2)

ttk.Label(app, text="austim (no, yes)").grid(column=2, row=3)
ttk.Combobox(app, width=12, textvariable=austim, values=['no', 'yes']).grid(column=3, row=3)

ttk.Label(app, text="contry_of_res").grid(column=2, row=4)
ttk.Entry(app, width=12, textvariable=contry_of_res).grid(column=3, row=4)

ttk.Label(app, text="used_app_before (no, yes)").grid(column=2, row=5)
ttk.Combobox(app, width=12, textvariable=used_app_before, values=['no', 'yes']).grid(column=3, row=5)

ttk.Label(app, text="result (numeric)").grid(column=2, row=6)
ttk.Entry(app, width=12, textvariable=result).grid(column=3, row=6)


ttk.Label(app, text="relation").grid(column=2, row=8)
ttk.Combobox(app, width=12, textvariable=relation, values=['Parent', 'Self', 'Relative', 'Health care professional', 'self']).grid(column=3, row=8)

submit_button = ttk.Button(app, text="Submit", command=submit).grid(column=3, row=9)

app.mainloop()
