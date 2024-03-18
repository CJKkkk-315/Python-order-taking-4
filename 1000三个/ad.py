import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split, cross_val_score, KFold
from sklearn import svm
from sklearn.metrics import accuracy_score, confusion_matrix
from tkinter import *
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
from tkinter import ttk
import tkinter.messagebox
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
data_path = 'adult.data'
data = pd.read_csv(data_path, header=None)


def preprocess_data():
    global data
    global X, y, X_train, X_test, y_train, y_test
    top = tk.Toplevel()
    top.title('原始数据')
    top.geometry('1100x350')

    message_label = ttk.Label(top, text=str(data))
    message_label.pack(padx=10, pady=10)

    button = ttk.Button(top, text="OK", command=top.destroy)

    button.pack(padx=10, pady=10)
    label_encoder = preprocessing.LabelEncoder()
    for column in data.columns[:-1]:
        if data[column].dtype == type(object):
            data[column] = label_encoder.fit_transform(data[column])
    top = tk.Toplevel()
    top.title('预处理后数据')
    top.geometry('900x350')

    message_label = ttk.Label(top, text=str(data))
    message_label.pack(padx=10, pady=10)

    button = ttk.Button(top, text="OK", command=top.destroy)
    button.pack(padx=10, pady=10)
    X = data.iloc[:, :-1]
    y = data.iloc[:, -1]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)


def train_model():
    global clf
    clf = svm.SVC()
    clf.fit(X_train, y_train)
    tkinter.messagebox.showinfo('模型训练', '模型训练完成！')

def predict_model():
    global y_pred
    y_pred = clf.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(10, 7))
    plt.matshow(cm, cmap=plt.cm.Blues, fignum=1)
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('Actual')

    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(x=j, y=i, s=cm[i, j], va='center', ha='center', color='red')

    plt.show()


def evaluate_model():
    cv = KFold(n_splits=5, random_state=1, shuffle=True)
    scores = cross_val_score(clf, X, y, scoring='accuracy', cv=cv, n_jobs=-1)
    plt.figure(figsize=(10, 7))
    plt.plot(range(1, 6), scores)
    plt.title('Accuracy over 5-folds')
    plt.xlabel('Fold')
    plt.ylabel('Accuracy')
    plt.ylim(np.min(scores) - 0.01, np.max(scores) + 0.01)
    plt.show()
    print('Average Accuracy:', np.mean(scores))


root = Tk()
root.geometry('400x150')
root.title('基于支持向量机的收入预测软件')
button1 = Button(root, text="数据预处理", command=preprocess_data)
button1.pack()

button2 = Button(root, text="模型训练", command=train_model)
button2.pack()

button3 = Button(root, text="模型预测", command=predict_model)
button3.pack()

button4 = Button(root, text="模型评估", command=evaluate_model)
button4.pack()

root.mainloop()
