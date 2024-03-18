import numpy as np
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

class Particle:
    def __init__(self, dim):
        self.position = np.random.uniform(-1, 1, dim)
        self.pbest_position = self.position.copy()
        self.pbest_value = float('-inf')

class BBPSO:
    def __init__(self, swarm_size, dim, iter_num, X, y):
        self.swarm_size = swarm_size
        self.dim = dim
        self.iter_num = iter_num
        self.X = X
        self.y = y
        self.gbest_position = np.random.uniform(-1, 1, dim)
        self.gbest_value = float('-inf')
        self.swarm = [Particle(dim) for _ in range(swarm_size)]

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def set_pbest(self):
        for particle in self.swarm:
            fitness_candidate = self.fitness(particle.position)
            if(particle.pbest_value < fitness_candidate):
                particle.pbest_position = particle.position.copy()
                particle.pbest_value = fitness_candidate

    def set_gbest(self):
        for particle in self.swarm:
            best_fitness_candidate = self.fitness(particle.pbest_position)
            if(self.gbest_value < best_fitness_candidate):
                self.gbest_position = particle.pbest_position.copy()
                self.gbest_value = best_fitness_candidate

    def fitness(self, position):
        selected_features = self.sigmoid(position) > 0.5
        if not np.any(selected_features):  # If no features selected, return low fitness value
            return float('-inf')
        clf = make_pipeline(StandardScaler(), LogisticRegression())
        score = cross_val_score(clf, self.X[:, selected_features], self.y, cv=3).mean()
        return score

    def move_particles(self):
        for particle in self.swarm:
            mean = (particle.pbest_position + self.gbest_position) / 2
            std_dev = np.abs(particle.pbest_position - self.gbest_position)
            particle.position = np.random.normal(mean, std_dev, self.dim)

    def run(self):
        for i in range(self.iter_num):
            self.set_pbest()
            self.set_gbest()
            self.move_particles()
        print('The best solution is: ', self.sigmoid(self.gbest_position) > 0.5,
              ' in n_iterations: ', self.iter_num, ', with value: ', self.gbest_value)

if __name__ == "__main__":
    X, y = make_classification(n_samples=1000, n_features=10)
    pso = BBPSO(swarm_size=30, dim=X.shape[1], iter_num=100, X=X, y=y)
    pso.run()
