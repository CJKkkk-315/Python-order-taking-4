import random
import matplotlib.pyplot as plt


class Traffic:
    # 初始化函数
    def __init__(self, n, iterations, density):
        self.road = [0 for _ in range(n)]
        self.iterations = iterations
        # 根据密度计算车辆数量
        cars = int(n*density)
        # 随机抽取对应数量的索引
        p = random.sample([i for i in range(len(self.road))], cars)
        # 将抽取到的索引标记为有车
        for i in p:
            self.road[i] = 1

    # 更新函数
    def update(self):
        # 初始化下一时刻道路状态
        new_road = [0 for _ in range(len(self.road))]
        # 按照更新规则进行更新
        for i in range(len(self.road)):
            # 由于是循环结构,定义超出界限即回头
            forward = i+1
            if forward >= len(self.road):
                forward = 0
            back = i-1
            if back < 0:
                back = len(self.road) - 1
            if self.road[i] == 1:
                if self.road[forward] == 1:
                    new_road[i] = 1
                else:
                    new_road[i] = 0
            else:
                if self.road[back] == 1:
                    new_road[i] = 1
                else:
                    new_road[i] = 0
        return new_road

    # 模拟函数
    def simulation(self):
        speeds = []
        positions = []
        # 根据迭代次数,不停更新路况状态
        for iter in range(self.iterations):
            new_road = self.update()
            # 计算每一时刻移动车辆的数量,计算速度
            move_car = 0
            for i, j in zip(self.road,new_road):
                if i and i != j:
                    move_car += 1
            speed = move_car/sum(new_road)
            print(speed)
            self.road = new_road
            speeds.append(speed)
            positions.append(new_road[:])
        # 返回每一时刻的速度
        return speeds, positions

    # 速度函数
    def speed(self, show=False):
        # 根据模拟,得到每一时刻的速度
        speeds, positions = self.simulation()
        point_x = []
        point_y = []
        # 画出车辆图
        for i in range(len(positions)):
            for j in range(len(self.road)):
                if positions[i][j]:
                    point_x.append(i)
                    point_y.append(j)

        if show:
            plt.scatter(point_y, point_x)
            plt.ylabel('Positions')
            plt.xlabel('Time')
            plt.show()
        return speeds[-1]


# 按照100辆车 0.3的密度模拟,并画出车辆图
t = Traffic(100, 10, 0.6)
speed = t.speed(show=True)


# 将密度由0.01到0.99,分别求出平均速度趋势图
res_x = []
res_y = []
for i in range(1,100):
    density = i/100
    t = Traffic(100, 100, density)
    speed = t.speed(show=False)
    res_x.append(density)
    res_y.append(speed)
plt.plot(res_x,res_y)
plt.xlabel('Density')
plt.ylabel('Avg. Speed')
plt.show()
