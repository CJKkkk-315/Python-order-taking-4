import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, recall_score, f1_score, precision_score, roc_curve, roc_auc_score,confusion_matrix,ConfusionMatrixDisplay
import pandas as pd
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import warnings
warnings.filterwarnings('ignore')
dfdf = pd.read_csv('heart.csv')
# Define the dataset and dataloader
now = 0
def main():
    def train_and_predict(data, target_col):
        X = data.drop([target_col], axis=1)
        y = data[target_col]
        final_acc = []


        classifiers = [
            RandomForestClassifier(),
            KNeighborsClassifier(),
            DecisionTreeClassifier(),
            MLPClassifier(),
            GaussianNB()
        ]

        for clf in classifiers:
            pipeline = Pipeline(steps=[('classifier', clf)])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=27)
            pipeline.fit(X_train, y_train)
            y_pred = pipeline.predict(X_test)
            y_pro = pipeline.predict_proba(X_test)
            accuracy = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred)
            recall = recall_score(y_test, y_pred)
            f1 = f1_score(y_test, y_pred)
            auc_score = roc_auc_score(y_test,y_pro[:,1])
            final_acc.append(accuracy)
            print(f"{clf.__class__.__name__} 准确率: {accuracy:.3f}")
            print(f"{clf.__class__.__name__} 精确率: {precision:.3f}")
            print(f"{clf.__class__.__name__} 召回率: {recall:.3f}")
            print(f"{clf.__class__.__name__} F1得分: {f1:.3f}")
            print(f"{clf.__class__.__name__} AUC得分: {auc_score:.3f}")
            cm = confusion_matrix(y_true=y_test, y_pred=y_pred)
            disp = ConfusionMatrixDisplay(confusion_matrix=cm)
            disp.plot()
            plt.title(f'{clf.__class__.__name__} confusion matrix')
            plt.show()
            fpr,tpr,_ = roc_curve(y_test,y_pro[:,1])

            plt.plot(fpr,tpr)
            plt.plot([0,1],[0,1],'--')
            plt.title(f'{clf.__class__.__name__} ROC curve')
            plt.show()

        return classifiers, final_acc

    def second_gui(res):
        def refresh(now):
            acc.config(text=f'模型准确率为：\n{res[now][1]}')
            pro.config(text=f'患病概率为：\n{res[now][2]}')
        global now
        root = tk.Toplevel(app)
        root.title("基于深度学习的心脏病诊断系统")
        ttk.Button(root, text="随机森林",command=lambda: refresh(0)).grid(column=0, row=0)
        ttk.Button(root, text="KNN",command=lambda: refresh(1)).grid(column=0, row=3)
        ttk.Button(root, text="决策树",command=lambda: refresh(2)).grid(column=0, row=6)
        ttk.Button(root, text="神经网络",command=lambda: refresh(3)).grid(column=0, row=9)
        ttk.Button(root, text="贝叶斯",command=lambda: refresh(4)).grid(column=0, row=12)

        ttk.Label(root, text="age年龄:").grid(column=1, row=0)
        ttk.Label(root, width=12,text=age.get()).grid(column=2, row=0)

        ttk.Label(root, text="sex性别（0=女，1=男）:").grid(column=1, row=1)
        ttk.Label(root, width=12, text=sex.get()).grid(column=2, row=1)

        ttk.Label(root, text="cp胸痛类型（0=无症状，1=非心绞痛，2=非典型心绞痛，3=典型心绞痛）:").grid(column=1, row=2)
        ttk.Label(root, width=12, text=cp.get()).grid(column=2, row=2)

        ttk.Label(root, text="trestbps静息血压（0~300）:").grid(column=1, row=3)
        ttk.Label(root, width=12, text=trestbps.get()).grid(column=2, row=3)

        ttk.Label(root, text="chol血清总胆固醇（1~1000mg/dL）:").grid(column=1, row=4)
        ttk.Label(root, width=12, text=chol.get()).grid(column=2, row=4)

        ttk.Label(root, text="fbs空腹血糖（0=血糖含量小于120mg/dl，1=血糖含量大于120mg/dl）:").grid(column=1, row=5)
        ttk.Label(root, width=12, text=fbs.get()).grid(column=2, row=5)

        ttk.Label(root, text="restecg静息心电图（0=正常，1=患有某段T波异常，2=左心室肥大）:").grid(column=1, row=6)
        ttk.Label(root, width=12, text=restecg.get()).grid(column=2, row=6)

        ttk.Label(root, text="thalach最大心率（不超220）:").grid(column=1, row=7)
        ttk.Label(root, width=12, text=thalach.get()).grid(column=2, row=7)

        ttk.Label(root, text="exang运动诱发心绞痛（0=否，1=是）:").grid(column=1, row=8)
        ttk.Label(root, width=12, text=exang.get()).grid(column=2, row=8)

        ttk.Label(root, text="oldpeak运动诱发ST段下降（0~8）:").grid(column=1, row=9)
        ttk.Label(root, width=12, text=oldpeak.get()).grid(column=2, row=9)

        ttk.Label(root, text="slope运动高峰ST段斜率（0=上升，1=水平，2=下降）:").grid(column=1, row=10)
        ttk.Label(root, width=12, text=slope.get()).grid(column=2, row=10)

        ttk.Label(root, text="ca主要血管数（0~3）:").grid(column=1, row=11)
        ttk.Label(root, width=12, text=ca.get()).grid(column=2, row=11)

        ttk.Label(root, text="thal缺陷种类（1=正常，2=固定缺陷，3=可逆缺陷）:").grid(column=1, row=12)
        ttk.Label(root, width=12, text=thal.get()).grid(column=2, row=12)



        acc = ttk.Label(root,text=f'模型准确率为：\n{res[now][1]}',font=( '20'))
        acc.grid(column=3, row=0, rowspan=5)
        pro = ttk.Label(root, text=f'患病概率为：\n{res[now][2]}',font=( '20'))
        pro.grid(column=3, row=6, rowspan=5)
    def submit():
        classifiers, final_acc = train_and_predict(dfdf, 'target')
        data = {
            'age': [float(age.get())],
            'sex': [float(sex.get())],
            'cp': [float(cp.get())],
            'trestbps': [float(trestbps.get())],
            'chol': [float(chol.get())],
            'fbs': [float(fbs.get())],
            'restecg': [float(restecg.get())],
            'thalach': [float(thalach.get())],
            'exang': [float(exang.get())],
            'oldpeak': [float(oldpeak.get())],
            'slope': [float(slope.get())],
            'ca': [float(ca.get())],
            'thal': [float(thal.get())],
        }

        df = pd.DataFrame(data)
        test = [i for i in list(df.iloc[0])]
        print(test)
        res = []
        for idx, classifier in enumerate(classifiers):
            res.append([classifier.__class__.__name__, round(final_acc[idx],3), round(classifier.predict_proba([test])[0][1],3)])
        print(res)
        second_gui(res)
    classifiers, final_acc = train_and_predict(dfdf, 'target')
    app = tk.Tk()
    app.title("基于深度学习的心脏病诊断系统")
    app.geometry('1050x200')

    age = tk.StringVar()
    sex = tk.StringVar()
    cp = tk.StringVar()
    trestbps = tk.StringVar()
    chol = tk.StringVar()
    fbs = tk.StringVar()
    restecg = tk.StringVar()
    thalach = tk.StringVar()
    exang = tk.StringVar()
    oldpeak = tk.StringVar()
    slope = tk.StringVar()
    ca = tk.StringVar()
    thal = tk.StringVar()

    ttk.Label(app, text="age年龄").grid(column=0, row=0)
    ttk.Entry(app, width=12, textvariable=age).grid(column=1, row=0)

    ttk.Label(app, text="sex性别（0=女，1=男）").grid(column=0, row=1)
    ttk.Entry(app, width=12, textvariable=sex).grid(column=1, row=1)

    ttk.Label(app, text="cp胸痛类型（0=无症状，1=非心绞痛，2=非典型心绞痛，3=典型心绞痛）").grid(column=0, row=2)
    ttk.Entry(app, width=12, textvariable=cp).grid(column=1, row=2)

    ttk.Label(app, text="trestbps静息血压（0~300）").grid(column=0, row=3)
    ttk.Entry(app, width=12, textvariable=trestbps).grid(column=1, row=3)

    ttk.Label(app, text="chol血清总胆固醇（1~1000mg/dL）").grid(column=0, row=4)
    ttk.Entry(app, width=12, textvariable=chol).grid(column=1, row=4)

    ttk.Label(app, text="fbs空腹血糖（0=血糖含量小于120mg/dl，1=血糖含量大于120mg/dl）").grid(column=0, row=5)
    ttk.Entry(app, width=12, textvariable=fbs).grid(column=1, row=5)

    ttk.Label(app, text="restecg静息心电图（0=正常，1=患有某段T波异常，2=左心室肥大）").grid(column=0, row=6)
    ttk.Entry(app, width=12, textvariable=restecg).grid(column=1, row=6)

    ttk.Label(app, text="thalach最大心率（不超220）").grid(column=5, row=0)
    ttk.Entry(app, width=12, textvariable=thalach).grid(column=6, row=0)

    ttk.Label(app, text="exang运动诱发心绞痛（0=否，1=是）").grid(column=5, row=1)
    ttk.Entry(app, width=12, textvariable=exang).grid(column=6, row=1)

    ttk.Label(app, text="oldpeak运动诱发ST段下降（0~8）").grid(column=5, row=2)
    ttk.Entry(app, width=12, textvariable=oldpeak).grid(column=6, row=2)

    ttk.Label(app, text="slope运动高峰ST段斜率（0=上升，1=水平，2=下降）").grid(column=5, row=3)
    ttk.Entry(app, width=12, textvariable=slope).grid(column=6, row=3)

    ttk.Label(app, text="ca主要血管数（0~3）").grid(column=5, row=4)
    ttk.Entry(app, width=12, textvariable=ca).grid(column=6, row=4)

    ttk.Label(app, text="thal缺陷种类（1=正常，2=固定缺陷，3=可逆缺陷）").grid(column=5, row=5)
    ttk.Entry(app, width=12, textvariable=thal).grid(column=6, row=5)



    submit_button = ttk.Button(app, text="Submit",command=submit).grid(column=6, row=8)

    app.mainloop()
now_acc = []
def register():
    username = entry_new_username.get()
    password = entry_new_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("注册失败", "两次输入的密码不匹配！")
        return

    with open("accounts.txt", "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("注册成功", "注册成功！现在可以登录。")
    now_acc.append([username, password])
    top_register.destroy()


def login():
    username = entry_username.get()
    password = entry_password.get()

    with open("accounts.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")

            if user == username and pwd == password:
                messagebox.showinfo("登录成功", "登录成功！")
                roott.destroy()
                main()
                return
    for i in now_acc:
        if user == i[0] and pwd == i[1]:
            messagebox.showinfo("登录成功", "登录成功！")
            roott.destroy()
            main()
            return
    messagebox.showerror("登录失败", "用户名或密码错误！")
roott = tk.Tk()
roott.geometry("400x300")
roott.title("登录")

# 登录部分
frame_login = tk.Frame(roott)
frame_login.pack(pady=10)

label_username = tk.Label(frame_login, text="用户名：")
label_username.grid(row=0, column=0, padx=5)

entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1, padx=5)

label_password = tk.Label(frame_login, text="密码：")
label_password.grid(row=1, column=0, padx=5)

entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1, padx=5)

button_login = tk.Button(roott, text="登录", command=login)
button_login.pack(pady=10)

# 注册部分
button_register = tk.Button(roott, text="注册新用户", command=lambda: top_register.deiconify())
button_register.pack(pady=10)

top_register = tk.Toplevel(roott)
top_register.withdraw()
top_register.title("注册")

frame_register = tk.Frame(top_register)
frame_register.pack(pady=10)

label_new_username = tk.Label(frame_register, text="用户名：")
label_new_username.grid(row=0, column=0, padx=5)

entry_new_username = tk.Entry(frame_register)
entry_new_username.grid(row=0, column=1, padx=5)

label_new_password = tk.Label(frame_register, text="密码：")
label_new_password.grid(row=1, column=0, padx=5)

entry_new_password = tk.Entry(frame_register, show="*")
entry_new_password.grid(row=1, column=1, padx=5)

label_confirm_password = tk.Label(frame_register, text="确认密码：")
label_confirm_password.grid(row=2, column=0, padx=5)

entry_confirm_password = tk.Entry(frame_register, show="*")
entry_confirm_password.grid(row=2, column=1, padx=5)

button_confirm_register = tk.Button(top_register, text="注册", command=register)
button_confirm_register.pack(pady=10)

roott.mainloop()