def parse_tsp_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()[:-1]


    dimension = None
    for line in lines:
        if line.startswith('DIMENSION'):
            dimension = int(line.split(':')[1])

    coords = []
    for line in lines[-dimension:]:
        parts = line.split(' ')
        coords.append((float(parts[1]), float(parts[2])))

    return coords
import random
import math

class Individual:
    def __init__(self, cities):
        self.cities = cities
        self.distance = self.calculate_distance()

    @classmethod
    def create_random(cls, coords):
        cities = list(range(len(coords)))
        random.shuffle(cities)
        return cls(cities)

    def calculate_distance(self):
        total = 0
        for i in range(len(self.cities)):
            total += self.distance_between(self.cities[i-1], self.cities[i])
        return total

    def distance_between(self, city1, city2):
        x_diff = coords[city1][0] - coords[city2][0]
        y_diff = coords[city1][1] - coords[city2][1]
        return math.sqrt(x_diff**2 + y_diff**2)

def run_genetic_algorithm(coords, population_size=200, generations=500, crossover_prob=0.1, mutation_prob=0.1, tournament_size=5):
    def selection(population):
        tournament = random.sample(population, tournament_size)
        return min(tournament, key=lambda individual: individual.distance)

    def crossover(parent1, parent2):
        if random.random() < crossover_prob:
            size = min(len(parent1.cities), len(parent2.cities))
            p1, p2 = [0] * size, [0] * size
            for i in range(size):
                p1[parent1.cities[i]] = i
                p2[parent2.cities[i]] = i
            cxpoint1 = random.randint(0, size)
            cxpoint2 = random.randint(0, size - 1)
            if cxpoint2 >= cxpoint1:
                cxpoint2 += 1
            else:
                cxpoint1, cxpoint2 = cxpoint2, cxpoint1
            for i in range(cxpoint1, cxpoint2):
                temp1 = parent1.cities[i]
                temp2 = parent2.cities[i]
                parent1.cities[i], parent1.cities[p1[temp2]] = temp2, temp1
                parent2.cities[i], parent2.cities[p2[temp1]] = temp1, temp2
                p1[temp1], p1[temp2] = p1[temp2], p1[temp1]
                p2[temp1], p2[temp2] = p2[temp2], p2[temp1]

            return Individual(parent1.cities)
        else:
            return Individual(parent1.cities[:])

    def mutate(individual):
        if random.random() < mutation_prob:
            i = random.randint(0, len(individual.cities) - 1)
            j = random.randint(0, len(individual.cities) - 1)

            individual.cities[i], individual.cities[j] = individual.cities[j], individual.cities[i]

    population = [Individual.create_random(coords) for _ in range(population_size)]

    for _ in range(generations):
        population.sort(key=lambda individual: individual.distance)
        new_population = population[:population_size // 10]
        for _ in range(population_size - len(new_population)):
            parent1 = selection(new_population)
            parent2 = selection(new_population)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)
        population = new_population[:]
    return population[0]


import time
file = 'berlin52.tsp'
print(f'执行锦标赛策略结果：')
start_time = time.time()
coords = parse_tsp_file(file)
best_individual = run_genetic_algorithm(coords)
end_time = time.time()

print(f"最短距离: {best_individual.distance}")
print(f"运行时间: {end_time - start_time}秒")
