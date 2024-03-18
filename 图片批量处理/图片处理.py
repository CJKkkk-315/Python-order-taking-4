import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
files = os.listdir('picture')
# 读取图片
for file in files:
    pic_file = 'picture/' + file
    img_bgr = cv2.imread(pic_file, cv2.IMREAD_COLOR)
    # cv2.imshow("input", img_bgr)
    # 分别获取三个通道的ndarray数据
    img_b = img_bgr[:, :, 0]
    img_g = img_bgr[:, :, 1]
    img_r = img_bgr[:, :, 2]

    '''按R、G、B三个通道分别计算颜色直方图'''
    b_hist = cv2.calcHist([img_bgr], [0], None, [256], [0, 255])
    g_hist = cv2.calcHist([img_bgr], [1], None, [256], [0, 255])
    r_hist = cv2.calcHist([img_bgr], [2], None, [256], [0, 255])
    m, dev = cv2.meanStdDev(img_bgr)  # 计算G、B、R三通道的均值和方差
    # img_r_mean=np.mean(r_hist)  #计算R通道的均值
    # print(m)
    # print(dev)

    '''显示三个通道的颜色直方图'''
    plt.plot(b_hist, label='B', color='blue')
    plt.plot(g_hist, label='G', color='green')
    plt.plot(r_hist, label='R', color='red')
    plt.legend(loc='best')
    plt.xlim([0, 256])
    plt.savefig('res/'+file)
    plt.clf()
