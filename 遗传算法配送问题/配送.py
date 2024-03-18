import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
dis = pd.read_excel('距离矩阵.xlsx',header=None).values
origin = 8
school_count = len(dis)
all_school = [i for i in range(len(dis))]
all_school.remove(origin)
school_count -= 1



def black(x):
    s = dis[origin][x[0]]
    for i in range(len(x)-1):
        s += dis[x[i]][x[i+1]]
    s += dis[x[len(x)-1]][origin]
    return s


def generate_ones():
    ones = []
    now = all_school[:]
    while len(now) != 0:
        one = random.choice(now)
        ones.append(one)
        now.remove(one)
    return ones

maxgen = 500
sizepop = 200
nvar = 9
pc = 0.5
pm = 0.2
fit_list = []
pop = [generate_ones() for i in range(sizepop)]
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
    for i in range(len(pop)):
        r = random.random()
        if r < pm:
            x = generate_ones()
            pop[i] = np.array(x)

    pop.pop()
    pop.append(r_pop)
    pop = np.array(pop)
    if not gen%10:
        print('适应度:', max(fit_values), 1/max(fit_values))
    fit_list.append(1/max(fit_values))

res = pop[[black(x) for x in pop].index(min([black(x) for x in pop]))]
res = [8] + list(res) + [8]
print(min([black(x) for x in pop]))
print(res)
print(min(fit_list))
plt.plot([i for i in range(len(fit_list))], fit_list)
plt.show()


plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
name_hash = {int(i.split('—')[0]):i.split('—')[1] for i in """1—北京邮电大学
2—北京大学
3—北京科技大学
4—北京师范大学
5—北京理工大学
6—北京林业大学
7—北京航空航天大学
8—北京中医药大学
9—北京交通大学
10—北京联合大学""".split('\n')}
location = pd.read_excel('各高校坐标.xlsx')
location = location.values[:,1:]
route_x = [location[i][0] for i in res]
route_y = [location[i][1] for i in res]
for x,y,t in zip(route_x, route_y, res):
    plt.text(x,y,name_hash[t+1])
plt.scatter(route_x, route_y, s=10, c='k')
plt.plot(route_x, route_y, 'r-')
plt.show()
