# edit by JBR，2020年10月31日
import numpy as np
import math
import matplotlib.pyplot as plt
x = np.linspace(0, 6, 30)
x_size = x.size
y = np.zeros((x_size, 1))
for i in range(x_size):
    y[i] = math.sin(x[i])+0.01*math.e**x[i]  # 被拟合函数
hidesize = 5  # 隐层数量
W1 = np.random.random((hidesize, 1))  # 输入层与隐层之间的权重
B1 = np.random.random((hidesize, 1))  # 隐含层神经元的阈值
W2 = np.random.random((1, hidesize))  # 隐含层与输出层之间的权重
B2 = np.random.random((1, 1))  # 输出层神经元的阈值
threshold = 0.005  # 迭代速度
max_steps = 5000  # 迭代最高次数，超过此次数即会退出
def sigmoid(x_):
    y_ = 1 / (1 + math.exp(-x_))
    return y_
E = np.zeros((max_steps, 1))  # 误差随迭代次数的变化
Y = np.zeros((x_size, 1))  # 模型的输出结果
for k in range(max_steps):   # k是会自加的，傻了傻了，找了半天的k=k+1
    temp = 0
    for i in range(x_size):
        hide_in = np.dot(x[i], W1) - B1  # 隐含层输入数据,W1,hidesize行，1列
        # print(x[i])
        hide_out = np.zeros((hidesize, 1))  # hide_out是隐含层的输出数据，这里初始化
        for j in range(hidesize):
            hide_out[j] = sigmoid(hide_in[j])  # 计算hide_out
        y_out = np.dot(W2, hide_out) - B2  # 模型输出
        Y[i] = y_out
        # print(i,Y[i])
        e = y_out - y[i]  # 模型输出减去实际结果。得出误差
        ##反馈，修改参数
        dB2 = -1 * threshold * e
        dW2 = e * threshold * np.transpose(hide_out)
        dB1 = np.zeros((hidesize, 1))
        for j in range(hidesize):
            dB1[j] = np.dot(np.dot(W2[0][j], sigmoid(hide_in[j])), (1 - sigmoid(hide_in[j])) * (-1) * e * threshold)
            # np.dot((sigmoid(hide_in[j])), (1 - sigmoid(hide_in[j])))为sigmoid(hide_in[j])的导数
        dW1 = np.zeros((hidesize, 1))
        for j in range(hidesize):
            dW1[j] = np.dot(np.dot(W2[0][j], sigmoid(hide_in[j])), (1 - sigmoid(hide_in[j])) * x[i] * e * threshold)
        W1 = W1 - dW1
        B1 = B1 - dB1
        W2 = W2 - dW2
        B2 = B2 - dB2
        temp = temp + abs(e)
    E[k] = temp
    if k % 50 == 0:
        print(k)
plt.figure()
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.xlabel("x")
plt.ylabel("y,Y")
plt.title('y=sinx+0.01e^x')
plt.plot(x, y)
plt.plot(x, Y, color='red', linestyle='--')
plt.show()
