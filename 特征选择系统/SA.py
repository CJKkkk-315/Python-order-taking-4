import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import random
random_seed = 88
def evaluate_fitness(individual, X, y, model):
    selected_features = X[:, individual == 1]
    if selected_features.shape[1] == 0:
        return 0
    X_train, X_val, y_train, y_val = train_test_split(selected_features, y, test_size=0.2, random_state=random_seed)
    model.fit(X_train, y_train)
    predictions = model.predict(X_val)
    score = cross_val_score(model,selected_features,y,cv=5).mean()
    return score

def simulated_annealing_feature_selection(X, y, show=True):
    num_features = X.shape[1]
    model = DecisionTreeClassifier(random_state=random_seed)

    T_max = 100
    T_min = 1
    cooling_rate = 0.9

    current_solution = np.random.choice([0, 1], size=num_features, p=[0.5, 0.5])
    current_fitness = evaluate_fitness(current_solution, X, y, model)

    best_solution = np.copy(current_solution)
    best_fitness = current_fitness

    best_fitness_history = [best_fitness]
    max_ind_history = []
    T = T_max
    while T > T_min:
        print(T)
        for i in range(30):

            new_solution = np.copy(current_solution)
            flip_index = np.random.randint(num_features)
            new_solution[flip_index] = 1 - new_solution[flip_index]

            new_fitness = evaluate_fitness(new_solution, X, y, model)

            if new_fitness > current_fitness or np.random.rand() < np.exp((new_fitness - current_fitness) / T):
                current_solution = new_solution
                current_fitness = new_fitness

                # 如果新解更好，更新最优解
                if new_fitness > best_fitness:
                    best_solution = new_solution
                    best_fitness = new_fitness

        best_fitness_history.append(best_fitness)
        max_ind_history.append(best_solution)
        T *= cooling_rate
    res_x = []
    res_y = []
    for idx,v in enumerate(max_ind_history):
        for i in range(len(v)):
            if v[i]:
                res_x.append(idx)
                res_y.append(i)
    if show:
        plt.scatter(res_x,res_y)
        plt.title('特征选择随迭代次数变化')
        plt.xlabel('迭代次数')
        plt.ylabel('选择特征')
        plt.show()

        # 绘制最佳适应度随迭代次数变化的图像
        plt.plot(best_fitness_history)
        plt.title('Best Fitness by Iteration')
        plt.xlabel('Iteration')
        plt.ylabel('Best Fitness')
        plt.show()

    # 返回最优解，即选中的特征子集
    selected_features = np.where(best_solution == 1)[0]
    return selected_features, best_solution, best_fitness_history[-1], max_ind_history, best_fitness_history

if __name__ == '__main__':

    df = pd.read_csv('spambase.csv')
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Accuracy without feature selection: ", accuracy_score(y_test, predictions))

    selected_features, best_individual, best_score, max_ind_history = simulated_annealing_feature_selection(X, y)
    print(selected_features, best_individual, best_score, max_ind_history)
    X_selected = X[:, selected_features]
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Accuracy with feature selection: ", accuracy_score(y_test, predictions))