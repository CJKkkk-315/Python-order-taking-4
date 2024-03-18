import random
import numpy as np
import matplotlib.pyplot as plt
import math
tsp_data = [list(map(int,line.replace('\n','').split())) for line in open('TSP.txt').readlines()]
filename = 'berlin52.txt'
city_num = []  # 城市编号
city_location = []  # 城市坐标
with open(filename, 'r') as f:
    datas = f.readlines()[6:-1]
for data in datas:
    data = data.split()
    city_num.append(int(data[0]))
    x = float(data[1])
    y = float(data[2])
    city_location.append((x, y))  # 城市坐标
city_count = len(city_num)  # 总的城市数
origin = 1  # 设置起点和终点
remain_cities = city_num[:]
remain_cities.remove(origin)  # 迭代过程中变动的城市
remain_count = city_count - 1  # 迭代过程中变动的城市数
indexs = list(i for i in range(remain_count))
# 计算邻接矩阵
dis = [[0] * city_count for i in range(city_count)]  # 初始化
for i in range(city_count):
    for j in range(city_count):
        if i != j:
            dis[i][j] = math.sqrt(
                (city_location[i][0] - city_location[j][0]) ** 2 + (city_location[i][1] - city_location[j][1]) ** 2)
        else:
            dis[i][j] = 0
tsp_data = [[j for j in i] for i in dis]
maxgen = 2000
sizepop = 500
nvar = 9
# popmax = 10
# popmin = 1
pc = 0.5
pm = 0.2
fit_list = []
def black(x):
    s = tsp_data[0][x[0]]
    for i in range(len(x)-1):
        s += tsp_data[x[i]][x[i+1]]
    s += tsp_data[x[len(x)-1]][0]
    return s

def nearest_city(current_city, remain_cities):
    temp_min = float('inf')
    next_city = None
    for i in range(len(remain_cities)):
        distance = dis[current_city - 1][remain_cities[i] - 1]
        if distance < temp_min:
            temp_min = distance
            next_city = remain_cities[i]
    return next_city


def greedy_initial_route(remain_cities):
    cand_cities = remain_cities[:]
    current_city = origin
    initial_route = []
    while len(cand_cities) > 0:
        next_city = nearest_city(current_city, cand_cities)  # 找寻最近的城市及其距离
        initial_route.append(next_city)  # 将下一个城市添加到路径列表中
        current_city = next_city  # 更新当前城市
        cand_cities.remove(next_city)  # 更新未定序的城市
    return initial_route
pop = [np.array(greedy_initial_route([i+1 for i in range(nvar)]))]

for i in range(sizepop):
    t = [i+1 for i in range(nvar)]
    random.shuffle(t)
    pop.append(np.array(t))

pop = np.array(pop)
fit_values = np.array([1/black(x) for x in pop])


for gen in range(maxgen):
    old_fit_values = max(fit_values)
    fit_values = np.array([1/black(x) for x in pop])
    maxindex = list(fit_values).index(max(fit_values))

    r_pop = pop[maxindex]
    new_pop = np.array(random.choices(pop,weights=fit_values,k=sizepop))
    pop = list(new_pop)
    for i in range(len(pop)):
        popaw = pop[i][:]
        if random.random() > pc:
            a = i
            b = random.randint(0,len(pop)-1)
            for j in range(nvar):
                if random.random() > 0.5:
                    t = list(pop[a]).index(pop[b][j])
                    aw = pop[a][j]
                    popaw[j] = pop[b][j]
                    popaw[t] = aw
            pop.append(np.array(popaw))
            if len(pop) == sizepop:
                break


    for i in range(len(pop)):
        r = random.random()
        a = [i for i in range(nvar)]
        if r < pm:
            x = [i + 1 for i in range(nvar)]
            random.shuffle(x)
            pop[i] = np.array(x)

    pop.pop()
    pop.append(r_pop)
    pop = np.array(pop)
    if max(fit_values) == old_fit_values:
        pm += 0.005
    else:
        pm = 0.005
    if pm > 1:
        break
    print(max(fit_values),pm,len(pop))
    fit_list.append(1/max(fit_values))
print(min([black(x) for x in pop]))
print(pop[[black(x) for x in pop].index(min([black(x) for x in pop]))])
print(min(fit_list))
plt.plot([i for i in range(len(fit_list))],fit_list)
plt.show()


