import tkinter as tk
import pandas as pd
import tkinter.messagebox
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from tkinter import ttk
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
df_scaled = None
model = None
def data_preprocessing():
    global df_scaled
    data = pd.read_csv('winequality-red.csv',delimiter=';')
    print(data['quality'].unique())
    top = tk.Toplevel()
    top.title('原始数据')
    top.geometry('900x350')  # 这里可以设置弹出框大小

    message_label = ttk.Label(top, text=str(data))
    message_label.pack(padx=10, pady=10)

    button = ttk.Button(top, text="OK", command=top.destroy)
    button.pack(padx=10, pady=10)

    scaler = StandardScaler()
    df_scaled = pd.DataFrame(scaler.fit_transform(data.drop(['quality'],axis=1)), columns=data.columns[:-1])
    df_scaled['quality'] = data['quality']
    top = tk.Toplevel()
    top.title('预处理后数据')
    top.geometry('1100x350')  # 这里可以设置弹出框大小

    message_label = ttk.Label(top, text=str(df_scaled))
    message_label.pack(padx=10, pady=10)

    button = ttk.Button(top, text="OK", command=top.destroy)
    button.pack(padx=10, pady=10)
def model_training():
    global df_scaled,model
    df = df_scaled
    X = df.drop(['quality'],axis=1)
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=70)
    model = DecisionTreeRegressor()
    model.fit(X_train, y_train)
    tkinter.messagebox.showinfo('训练结果','训练完成！')
def model_testing():
    # call your model testing function here
    global df_scaled, model
    df = df_scaled
    X = df.drop(['quality'], axis=1)
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=70)

    y_pred = model.predict(X_test)
    X_test['quality'] = y_test
    X_test['predict'] = y_pred
    X_test.to_csv('res.csv',index=False)
    tkinter.messagebox.showinfo('测试结果', '预测结果已保存为res.csv！')

def model_evaluation():
    # call your model evaluation function here
    global df_scaled, model
    df = df_scaled
    X = df.drop(['quality'], axis=1)
    y = df['quality']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=70)

    y_pred = model.predict(X_test)
    tkinter.messagebox.showinfo('测试结果', f'MSE指标:{mean_squared_error(y_test, y_pred)}！')
    plt.plot([i for i in range(len(y_test[:300]))], y_test[:300], label='真实值', marker='*')
    plt.plot([i for i in range(len(y_pred[:300]))], y_pred[:300], label='预测值', marker='o')
    plt.title('预测值与真实值比较')
    plt.legend()
    plt.show()
# 创建一个新的tkinter窗口
window = tk.Tk()
window.title("决策树根据葡萄酒特征进行质量预测")
window.geometry('400x250')  # 设置窗口尺寸，例如 400x400

# 创建数据预处理按钮并添加到窗口中
data_preprocessing_button = tk.Button(window, text="数据预处理", command=data_preprocessing)
data_preprocessing_button.pack(padx=10, pady=10)  # 设置水平和垂直间距

# 创建模型训练按钮并添加到窗口中
model_training_button = tk.Button(window, text="模型训练", command=model_training)
model_training_button.pack(padx=10, pady=10)  # 设置水平和垂直间距

# 创建模型测试按钮并添加到窗口中
model_testing_button = tk.Button(window, text="模型测试", command=model_testing)
model_testing_button.pack(padx=10, pady=10)  # 设置水平和垂直间距

# 创建模型评估按钮并添加到窗口中
model_evaluation_button = tk.Button(window, text="模型评估", command=model_evaluation)
model_evaluation_button.pack(padx=10, pady=10)  # 设置水平和垂直间距

# 运行tkinter事件循环
window.mainloop()
