import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC
from pyswarms.discrete.binary import BinaryPSO
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
random_seed = 88
class Particle:
    def __init__(self, dimension):
        self.position = np.random.randint(2, size=dimension)
        self.velocity = np.random.rand(dimension)
        self.pbest_position = self.position.copy()
        self.pbest_value = 0

class PSO:
    def __init__(self, dimension, n_particles, classifier, X, y):
        self.dimension = dimension
        self.n_particles = n_particles
        self.particles = [Particle(dimension) for _ in range(n_particles)]
        self.gbest_value = 0
        self.gbest_position = np.random.randint(2, size=dimension)
        self.classifier = classifier
        self.X = X
        self.y = y
        self.history_fitness = []
        self.history_position = []

    def _sigmoid(self, x):
        return 1 / (1 + np.exp(-x))
    def compute_position(self, position):
        change_position = (
                                 np.random.random_sample(size=len(position))
                                 < self._sigmoid(position)
                         ) * 1
        return change_position
    def fitness(self, particle):
        # feature subset
        change_positon = self.compute_position(particle.position)
        subset = self.X[:, change_positon == 1]
        #
        # X_train, X_val, y_train, y_val = train_test_split(subset, self.y, test_size=0.2)
        #
        # model.fit(X_train, y_train)
        # predictions = model.predict(X_val)
        # score = accuracy_score(y_val, predictions)
        score = cross_val_score(self.classifier,subset, self.y,cv=5).mean()
        return score

    def update(self, particle):
        particle.velocity = 1 * particle.velocity + 2 * (particle.pbest_position - particle.position) + 2 * (self.gbest_position - particle.position)
        particle.position = particle.position + particle.velocity

        pbest_value = self.fitness(particle)
        if pbest_value > particle.pbest_value:
            particle.pbest_value = pbest_value
            particle.pbest_position = particle.position.copy()

        if pbest_value > self.gbest_value:
            self.gbest_value = pbest_value
            self.gbest_position = particle.position.copy()

    def run(self, iterations):
        for _ in range(iterations):
            print(1)
            for particle in self.particles:
                self.update(particle)
            print(self.gbest_value)
            self.history_fitness.append(self.gbest_value)
            self.history_position.append(self.gbest_position)
        return self.gbest_position

    def plot(self):
        plt.plot()
        plt.title('Fitness over iterations')
        plt.xlabel('Iterations')
        plt.ylabel('Fitness')
        plt.show()

def particle_swarm_optimization_feature_selection(X, y, show=True):

    clf = DecisionTreeClassifier()

    pso = PSO(X.shape[1], 50, clf, X, y)
    best_features = pso.compute_position(pso.run(50))

    selected_features = np.where(best_features == 1)[0]
    res_x = []
    res_y = []
    for idx, v in enumerate(pso.history_position):
        vv = pso.compute_position(v)
        for i in range(len(vv)):
            if vv[i]:
                res_x.append(idx)
                res_y.append(i)
    if show:
        plt.scatter(res_x, res_y)
        plt.title('特征选择随迭代次数变化')
        plt.xlabel('迭代次数')
        plt.ylabel('选择特征')
        plt.show()

        plt.plot(pso.history_fitness)
        plt.title('绘制适应度随迭代次数变化')
        plt.xlabel('迭代次数')
        plt.ylabel('适应度')
        plt.show()
    history_position = []
    for i in pso.history_position:
        history_position.append(pso.compute_position(i))
    return selected_features, best_features, pso.gbest_value, history_position, pso.history_fitness

if __name__ == '__main__':

    df = pd.read_csv('sonar.csv')
    X = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values
    print(particle_swarm_optimization_feature_selection(X,y))
