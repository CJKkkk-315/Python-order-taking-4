import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
from tkinter import ttk
import pandas as pd
from GA import genetic_algorithm_feature_selection
from SA import simulated_annealing_feature_selection
from PSO import particle_swarm_optimization_feature_selection
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
import csv
import random
X = None
y = None
c_name = None
target_name = None
selected_features, best_individual, best_score, max_ind_history = None, None, None, None
random_seed = 88
# 定义加载数据集功能
def load_dataset():
    global X, y, c_name,target_name
    file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv"), ("Excel Files", "*.xlsx")])
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    c_name = df.columns[:-1]
    target_name = df.columns[-1]
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values

    # 更新数据集信息
    dataset_info.set(f"数据集大小: {df.shape[0]}\n特征数量: {df.shape[1]}")

    # 让其他部分可用a
    feature_selection_method['state'] = 'readonly'
    btn_select_features['state'] = 'normal'
    btn_mutil['state'] = 'normal'

# 定义特征选择功能
def select_features():
    global selected_features, best_individual, best_score, max_ind_history
    if feature_selection_method.get() == '遗传算法':
        selected_features, best_individual, best_score, max_ind_history, _ = genetic_algorithm_feature_selection(X, y)
    elif feature_selection_method.get() == '模拟退火算法':
        selected_features, best_individual, best_score, max_ind_history, _ = simulated_annealing_feature_selection(X, y)
    else:
        selected_features, best_individual, best_score, max_ind_history, _ = particle_swarm_optimization_feature_selection(X, y)




    # 让分类验证按钮可用
    btn_show['state'] = 'normal'
    btn_classify['state'] = 'normal'


def mul_compare():
    global selected_features, best_individual, best_score, max_ind_history
    selected_features, best_individual, best_score, max_ind_history, max_fitness_history = genetic_algorithm_feature_selection(X, y, False)
    plt.plot(max_fitness_history, label='遗传算法', marker='*')

    selected_features, best_individual, best_score, max_ind_history, max_fitness_history = simulated_annealing_feature_selection(X, y, False)
    plt.plot(max_fitness_history, label='模拟退火算法', marker='o')
    selected_features, best_individual, best_score, max_ind_history, max_fitness_history = particle_swarm_optimization_feature_selection(X, y, False)
    plt.plot(max_fitness_history, label='粒子群算法', marker='^')
    plt.legend()
    plt.title('绘制适应度随迭代次数变化')
    plt.xlabel('迭代次数')
    plt.ylabel('适应度')
    plt.show()



    # 让分类验证按钮可用
    btn_show['state'] = 'normal'
    btn_classify['state'] = 'normal'


def show_result():
    # 更新选中的特征子集
    selected_features_list.set('选择的特征:\n' + ' '.join(list(c_name[best_individual == 1])))

    # 更新适应度值
    fitness_value.set(str(best_score))

def export_result():
    c_name_selected = c_name[selected_features]
    X_selected = X[:, selected_features]
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=random_seed)
    model = DecisionTreeClassifier(random_state=random_seed)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    export_df = [list(c_name_selected) + [target_name]]
    for i,j in zip(X_test,predictions):
        export_df.append(list(i)+[j])
    with open('export.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(export_df)
    tkinter.messagebox.showinfo('成功!','导出结果成功！')
# 定义分类验证功能
# def classify():
#     btn_export['state'] = 'normal'
#     X_selected = X[:, selected_features]
#     X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=random_seed)
#     model = DecisionTreeClassifier(random_state=random_seed)
#     model.fit(X_train, y_train)
#     predictions_pre = model.predict(X_test)
#
#     pre_score = accuracy_score(y_test, predictions_pre)
#
#     X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2, random_state=random_seed)
#     model = DecisionTreeClassifier(random_state=random_seed)
#     model.fit(X_train, y_train)
#     predictions = model.predict(X_test)
#
#     # 更新分类准确率
#     classification_accuracy.set(f"特征选择前准确率: {pre_score} \n 特征选择后准确率: {accuracy_score(y_test, predictions)}")

# 定义分类验证功能
def classify():
    btn_export['state'] = 'normal'
    X_selected = X[:, selected_features]
    model = DecisionTreeClassifier(random_state=random_seed)
    score = cross_val_score(model,X_selected,y,cv=5).mean()
    score_pre = cross_val_score(model, X, y, cv=5).mean()

    # 更新分类准确率
    classification_accuracy.set(f"特征选择前准确率: {score_pre} \n 特征选择后准确率: {score}")

root = tk.Tk()
root.title("特征选择系统")

# 设置窗口大小
root.geometry("900x550")

# 创建并添加控件
btn_load_dataset = tk.Button(root, text="加载数据集", command=load_dataset)
btn_load_dataset.pack(pady=10)

dataset_info = tk.StringVar()
lbl_dataset_info = tk.Label(root, textvariable=dataset_info)
lbl_dataset_info.pack(pady=5)

tk.Label(root, text="特征选择算法：").pack(pady=5)
feature_selection_method = ttk.Combobox(root, values=["遗传算法", "粒子群算法", "模拟退火算法"], state="disabled")
feature_selection_method.pack(pady=5)

btn_select_features = tk.Button(root, text="特征选择", command=select_features, state="disabled")
btn_select_features.pack(pady=5)

btn_show = tk.Button(root, text="结果展示", command=show_result, state="disabled")
btn_show.pack(pady=10)


selected_features_list = tk.StringVar()
lbl_selected_features = tk.Label(root, textvariable=syelected_features_list)
lbl_selected_features.pack(pady=5)

fitness_value = tk.StringVar()
lbl_fitness_value = tk.Label(root, textvariable=fitness_value)
lbl_fitness_value.pack(pady=5)



btn_classify = tk.Button(root, text="分类验证", command=classify, state="disabled")
btn_classify.pack(pady=5)

classification_accuracy = tk.StringVar()
lbl_classification_accuracy = tk.Label(root, textvariable=classification_accuracy)
lbl_classification_accuracy.pack(pady=10)

btn_export = tk.Button(root, text="导出数据", command=export_result, state="disabled")
btn_export.pack(pady=10)

btn_mutil = tk.Button(root, text="多算法对比", command=mul_compare, state="disabled")
btn_mutil.pack(pady=5)

# 启动主循环
root.mainloop()

