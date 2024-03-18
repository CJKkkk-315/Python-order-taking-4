import numpy as np
import pandas as pd
import random
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import random
# 遗传算法参数
POPULATION_SIZE = 15
NUM_GENERATIONS = 50
MUTATION_RATE = 0.1
ELITISM = 5
CROSSOVER_RATE = 0.8
random_seed = 88
# 创建一个随机种群
def create_population(num_features):
    population = []
    for _ in range(POPULATION_SIZE):
        individual = np.random.choice([0, 1], size=num_features)
        population.append(individual)
    return np.array(population)

# 评估适应度
def evaluate_fitness(individual, X, y, model):
    selected_features = X[:, individual == 1]
    if selected_features.shape[1] == 0:
        return 0
    # X_train, X_val, y_train, y_val = train_test_split(selected_features, y, test_size=0.2, random_state=random_seed)
    # model.fit(X_train, y_train)
    # predictions = model.predict(X_val)
    score = cross_val_score(model,selected_features, y, cv=5).mean()
    # score = accuracy_score(y_val, predictions)
    return score

# 选择操作
def selection(population, fitness):
    sorted_idx = np.argsort(fitness)[::-1]
    population = population[sorted_idx]
    return population[:ELITISM]

# 交叉操作
def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        crossover_point = random.randint(1, len(parent1) - 1)
        offspring1 = np.hstack((parent1[:crossover_point], parent2[crossover_point:]))
        offspring2 = np.hstack((parent2[:crossover_point], parent1[crossover_point:]))
        return offspring1, offspring2
    else:
        return parent1.copy(), parent2.copy()

# 变异操作
def mutation(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

# 遗传算法主函数
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

def genetic_algorithm_feature_selection(X, y, show=True):
    num_features = X.shape[1]
    population = create_population(num_features)
    model = DecisionTreeClassifier(random_state=random_seed)

    max_fitness_history = []
    max_ind_history = []
    res_x = []
    res_y = []
    for gen in range(NUM_GENERATIONS):
        fitness = np.array([evaluate_fitness(ind, X, y, model) for ind in population])

        max_fitness_history.append(np.max(fitness))
        max_ind_history.append(population[np.argmax(fitness)])
        new_population = []

        elite = selection(population, fitness)
        new_population.extend(elite)

        while len(new_population) < POPULATION_SIZE:
            parent1, parent2 = random.sample(list(elite), 2)
            offspring1, offspring2 = crossover(parent1, parent2)
            offspring1 = mutation(offspring1)
            offspring2 = mutation(offspring2)
            new_population.append(offspring1)
            new_population.append(offspring2)

        population = np.array(new_population)
        print(np.max(fitness))
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
        # 新增：绘制适应度随迭代次数变化的图像

        plt.plot(max_fitness_history)
        plt.title('绘制适应度随迭代次数变化')
        plt.xlabel('迭代次数')
        plt.ylabel('适应度')
        plt.show()

    best_individual = population[np.argmax(fitness)]
    selected_features = np.where(best_individual == 1)[0]
    return selected_features, best_individual, max_fitness_history[-1], max_ind_history, max_fitness_history

if __name__ == '__main__':

    df = pd.read_csv('sonar.csv')
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Accuracy without feature selection: ", accuracy_score(y_test, predictions))

    selected_features, best_individual, max_fitness, max_ind_history = genetic_algorithm_feature_selection(X, y)
    print(selected_features, best_individual, max_fitness, max_ind_history)
    X_selected = X[:, selected_features]
    X_train, X_test, y_train, y_test = train_test_split(X_selected, y, test_size=0.2)
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print("Accuracy with feature selection: ", accuracy_score(y_test, predictions))
