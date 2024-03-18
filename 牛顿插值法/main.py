import matplotlib.pyplot as plt
from pylab import mpl
import math

"""
牛顿插值法
插值的函数表为
xi      0.4，       0.55，     0.65，      0.80，       0.90，   1.05
f(xi)   0.41075,    0.57815,   0.69675,    0.88811,    1.02652,  1.25382
"""

x = [0.0, 12.67, 17.88, 29.54, 31.60, 39.25, 47.63, 64.88, 79.71, 89.35, 100.0]
y = [1.4953, 1.4751, 1.4671, 1.4493, 1.4468, 1.4368, 1.4247, 1.4112, 1.3839, 1.3718, 1.3604]

"""计算五次差商的值"""


def five_order_difference_quotient(x, y):
    # i记录计算差商的次数，这里循环5次，计算5次差商。
    i = 0
    quotient = [0 for _ in range(11)]
    while i < 10:
        j = 10
        while j > i:
            if i == 0:
                quotient[j] = ((y[j] - y[j - 1]) / (x[j] - x[j - 1]))
            else:
                quotient[j] = (quotient[j] - quotient[j - 1]) / (x[j] - x[j - 1 - i])
            j -= 1
        i += 1
    return quotient


def function(data):
    return x[0] + parameters[1] * (data - 0.0) + parameters[2] * (data - 0.0) * (data - 12.67) + \
           parameters[3] * (data - 0.0) * (data - 12.67) * (data - 17.88) \
           + parameters[4] * (data - 0.0) * (data - 12.67) * (data - 29.54)


"""计算插值多项式的值和相应的误差"""


def calculate_data(x, parameters):
    returnData = []
    for data in x:
        returnData.append(function(data))
    return returnData


"""画函数的图像
newData为曲线拟合后的曲线
"""


def draw(newData):
    plt.scatter(x, y, label="离散数据", color="red")
    plt.plot(x, newData, label="牛顿插值拟合曲线", color="black")
    plt.scatter(10, function(10), label="预测函数点", color="blue")
    plt.title("牛顿插值法")
    mpl.rcParams['font.sans-serif'] = ['SimHei']
    mpl.rcParams['axes.unicode_minus'] = False
    plt.legend(loc="upper left")
    plt.show()


parameters = five_order_difference_quotient(x, y)
yuanzu = calculate_data(x, parameters)
draw(yuanzu)