import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
import tkinter as tk
from tkinter import messagebox
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc
import os
import warnings
warnings.filterwarnings('ignore')



# 数据预处理
def preprocess_data():
    df = pd.read_excel('default of credit card clients.xls', header=1)
    df = df.rename(columns={'default payment next month': 'default'})
    df.drop('ID', axis=1, inplace=True)
    scaler = MinMaxScaler()
    for c in df.columns[:-1]:
        df[c] = scaler.fit_transform(df[c].values.reshape(-1, 1))
    df.to_excel('processed_data.xlsx', index=False)
    return df

# 模型训练
def train_model(df):
    y = df['default']
    X = df.drop('default', axis=1)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)
    return clf, X_test, y_test

# 预测
def predict_model(clf, X_test):
    y_pred = clf.predict(X_test)
    y_pred_pro = clf.predict_proba(X_test)
    return y_pred, y_pred_pro

# 评估
def evaluate_model(y_test, y_pred):
    acc = accuracy_score(y_test, y_pred)
    return acc

# GUI
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title('基于随机森林的信用卡欺诈预测')
        self.master.geometry('350x120')   # 设置窗口大小
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.preprocess_btn = tk.Button(self)
        self.preprocess_btn["text"] = "数据预处理"
        self.preprocess_btn["command"] = self.preprocess
        self.preprocess_btn.grid(row=0, column=0)  # 使用grid布局

        self.train_btn = tk.Button(self)
        self.train_btn["text"] = "模型训练"
        self.train_btn["command"] = self.train
        self.train_btn.grid(row=0, column=3)

        self.predict_btn = tk.Button(self)
        self.predict_btn["text"] = "模型预测"
        self.predict_btn["command"] = self.predict
        self.predict_btn.grid(row=2, column=0)

        self.evaluate_btn = tk.Button(self)
        self.evaluate_btn["text"] = "模型评估"
        self.evaluate_btn["command"] = self.evaluate
        self.evaluate_btn.grid(row=2, column=3)

    def preprocess(self):
        self.df = preprocess_data()
        os.system('start processed_data.xlsx')  # 打开Excel文件
        messagebox.showinfo("Message", "数据预处理完成并已打开预处理后的数据")

    def train(self):
        self.clf, self.X_test, self.y_test = train_model(self.df)
        messagebox.showinfo("Message", "模型训练完成")

    def predict(self):
        self.y_pred, self.y_pred_pro = predict_model(self.clf, self.X_test)
        acc = evaluate_model(self.y_test, self.y_pred)
        messagebox.showinfo("Message", f"模型预测完成，准确率为{acc}")



    def evaluate(self):

        fpr, tpr, _ = roc_curve(self.y_test, self.y_pred_pro[:, 1])
        roc_auc = auc(fpr, tpr)

        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic')
        plt.legend(loc="lower right")
        plt.show()


root = tk.Tk()
app = Application(master=root)
app.mainloop()
