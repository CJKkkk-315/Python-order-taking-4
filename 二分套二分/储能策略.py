import sys
import matplotlib.pyplot as plt
import ast
import time

LONG = 1  # 录入每次采样时间间隔为1h
position = 1
"""
P_m = input("请输入储能额定功率，单位为kW：")
rp = float(P_m)
S_n = input("请输入储能容量，单位为kWh：")
place = float(S_n)
CSDL = input("请输入储能初始电量百分比,单位为%")
start_pre = float(CSDL) / 100
ZXDL = input("请输入储能最小电量百分比,单位为%")
min_pre = float(ZXDL) / 100
jfh = ast.literal_eval(input("请按顺序录入各典型时刻净负荷特性，单位为kw，并以逗号分隔开："))
l = []
for item in jfh:
    l.append(float(item))

"""
rp = 8
place = 40
min_pre = 0.2
start_pre = 0.4
#l = [-6, -8, -4, -4, 0, 0, 10, 11, 14, 15, 22, 4, 5, 7, 2, 0, -3, -10, -12, -7]#正向单峰
# l = [-3, -1, -5, -2, 0, 0, 14, 15, 12, 20, 22, 4, 5, 7, 2, 0, -3, -10, -12, -7,-2,-1]#正向双峰
# l = [-6, -8, -4, -4, 0, 0, 10, 11, 14, 10, 22, 4, 5, 7, 2, 0, -3, -19, -15, -7]#正单峰、负单峰
# l = [6, 8, 4, 4, 0, 0, -10, -11, -14, -15, -22, -4, -5, -7, -2, 0, 3, 10, 12, 7]#反向单峰
#以上代码为调试用

s = rp
m = s
# S为最大削峰功率，m为每次削峰功率
a = 1
b = 0
p = 1
# 设置二分法参数
n = 1
c = 0.05
# 设置迭代次数和收敛精度

if not rp > 0:
    print("输入错误，储能额定功率应大于0")
    sys.exit()
if not place > 0:
    print("输入错误，储能容量应大于0")
    sys.exit()
if not 0 < min_pre < 1:
    print("输入错误，储能最小SOC应大于0小于1")
    sys.exit()
if not min_pre < start_pre < 1:
    print("输入错误，储能初始SOC应大于储能最小SOC并小于1")
    sys.exit()
# 以上为判断录入数据是否有问题

def check(s, a, b, p, m, n):
    h = abs(max(list(map(abs, l))) - m)  # 得到削峰值
    h_p = h
    h_n = -h
    g_p = 0
    g_n = 0
    g_min = []
    for i in l:
        if h_n < i < h_p:
            pass
        elif i < h_n:
            g_n += abs(h_n - i) * LONG # 得到反向削峰电量
            g_min.append(l.index(i))
        elif i > h_p:
            g_p += abs(h_p - i) * LONG  # 得到正向削峰点亮
            g_min.append(l.index(i))
    if g_p > place * (1 - min_pre) or g_n > place * (1 - min_pre):
        return [False, 0, 0, 0, [0 for _ in range(len(l))]]  # 判断本次策略不行，但若只能输出本次策略则输出储能功率全为0的列表，即不进行削峰填谷
    g_n = -g_n
    g = g_p + g_n  # 得到削峰时段所需电量
    g_minn = min(g_min)#得到削峰时段开始时间
    #检测（可删除），以上代码调试无问题
    if g > 0:
        ln = list(map(lambda x: x + m, l))# 若削峰电量为正，填谷时段需充电
        #print(ln)
        tg = 0
        for i in ln:
            if h_n < i - m < h_p:
                tg -= abs(m) * LONG
        c1 = max(ln)
        d1 = min(l)
    else:
        ln = list(map(lambda x: x - m, l))  # 若削峰电量为负，填谷时段需放电
        tg = 0
        for i in ln:
            if h_n< i+m <h_p:
                tg += abs(m) * LONG
        c1 = max(l)
        d1 = min(ln)
    if abs(tg) > abs(g):  # 若最大填谷电量能满足需求，则开始而二分
        while True:
            f = 0.5 * (c1 + d1)  # 设置填谷线

            tg = []
            if g > 0:
                for i in l:
                    if i > f:
                        tg.append(0)
                    else:
                        tg.append(-min(abs(f - i), abs(m)) * LONG)
            else:
                for i in l:
                    if i < f:
                        tg.append(0)
                    else:
                        tg.append(min(abs(f - i), abs(m)) * LONG)
            #以下为判断是否达到收敛条件
            if abs(sum(tg)) > 1.05 * abs(g):
                c1 = f
            elif abs(sum(tg)) < 0.95 * abs(g):
                d1 = f
            else:
                if g > 0:
                    ltime = start_pre * place + abs(sum(tg))
                else:
                    ltime = start_pre * place - abs(sum(tg))
                if not place > ltime > min_pre * place:
                    return [False, 0, 0, 0, [0 for _ in range(len(l))]]
                if abs(f) > abs(h): #判断是否有新的峰产生
                    return [False, 0, 0, 0, [0 for _ in range(len(l))]]
                F = 0
                for i, j in zip(l, tg):
                    if h > i > -h:
                        if i < g_minn:
                            F += abs(j) * LONG
                sk = []
                for i in l:
                    if i > h_p:
                        sk.append(abs(i - h_p))
                    elif i < h_n:
                        sk.append(-abs(i - h_n))
                    else:
                        if g > 0:
                            if i > f:
                                sk.append(0)
                            else:
                                sk.append(-min(abs(f - i), abs(m)))
                        else:
                            if i < f:
                                sk.append(0)
                            else:
                                sk.append(min(abs(f - i), abs(m)))

                return [True, g, F, m, sk[::], tg[::]]
    elif abs(tg) < abs(g):
        return [False, 0, 0, 0, [0 for _ in range(len(l))]]
    else:
        if g > 0:
            ltime = start_pre * place + abs(tg)
        else:
            ltime = start_pre * place - abs(tg)
        if not place > ltime > min_pre * place:
            return [False, 0, 0, 0, [0 for _ in range(len(l))]]
        F = 0
        for i in l:
            if h > i > -h:
                F += abs(m) * LONG
        sk = []
        for i in l:
            if i > h_p:
                sk.append(abs(i - h_p))
            elif i < h_n:
                sk.append(-abs(i - h_n))
            else:
                if g > 0:
                    sk.append(-abs(m))
                else:
                    sk.append(abs(m))
        return [True, g, F, m, sk[::], tg[::]]


flags = check(s, a, b, p, m, n)
if flags[0]:  # 若第一次可行，则直接输出本次程序
    g = flags[1]
    F = flags[2]
    m = flags[3]
    sk = flags[4]
    tg = flags[5]
    if g > 0:
        print("最小储能SOC百分比为：", max(float(g + place * start_pre - F) / place, min_pre * 100), "%")
        print("最大削峰功率为：", m, "kW")
        print("储能各时刻典型出力为：", sk)
    else:
        print("最大储能SOC百分比为：", min(float(place - g - F) / float(place), 100), "%")
        print("最大削峰功率为：", m, "kW")
        print("储能各时刻典型出力为：", sk)
else:
    while True:
        p = 0.5 * (a + b)
        n = n + 1
        m = p * s
        l_flags = flags[::]
        flags = check(s, a, b, p, m, n)
        if flags[0]:
            if a - p < c:
                g = flags[1]
                F = flags[2]
                m = flags[3]
                sk = flags[4]
                tg = flags[5]
                if g > 0:
                    print("最小储能SOC百分比为：", max(float(g + place * start_pre - F) / place, min_pre * 100), "%")
                    print("最大削峰功率为：", m, "kW")
                    print("储能各时刻典型出力为：", sk)

                else:
                    print("最大储能SOC百分比为：", min(float(place - g - F) / float(place), 100), "%")
                    print("最大削峰功率为：", m, "kW")
                    print("储能各时刻典型出力为：", sk)

                break
            else:
                a = p
        else:
            if a - p < c:
                g = l_flags[1]
                F = l_flags[2]
                m = l_flags[3]
                sk = l_flags[4]
                #tg = l_flags[5]
                if g > 0:
                    print("最小储能SOC百分比为：", max(float(g + place * start_pre - F) / place, min_pre * 100), "%")
                    print("最大削峰功率为：", m, "kW")
                    print("储能各时刻典型出力为：", sk)
                else:
                    print("最大储能SOC百分比为：", min(float(place - g - F) / float(place), 100), "%")
                    print("最大削峰功率为：", m, "kW")
                    print("储能各时刻典型出力为：", sk)
                break
            else:
                b = p

for i in range(len(l)):
    #plt.axhline(l[i], xmin=i * 1 / len(l), xmax=(i + 1) * 1 / len(l))
    plt.axhline(l[i], xmin=i * 1 / len(l), xmax=(i + 1) * 1 / len(l))
plt.xlim(0,len(l))
plt.ylabel("Initial Net Load Curve(KW)")
plt.xlabel("Time")
plt.show()

for i in range(len(sk)):
    plt.axhline(-sk[i]+l[i], xmin=i * 1 / len(sk), xmax=(i + 1) * 1 / len(sk))
plt.xlim(0,len(sk))
plt.ylabel("Net load curve after peak shaving and valley filling (KW)")
plt.xlabel("Time ")
plt.show()

"""
tgline = [start_pre]
for i in tg:
    tgline.append(tgline[-1] + i)
plt.plot([i * LONG for i in range(len(tgline))], tgline,)
plt.ylabel("Energy storage SOC curve")
plt.xlabel("Time")
plt.show()
"""
#以上为错误代码，可删，本人留作检测用

tgline = [start_pre*100]
for i in sk:
    tgline.append(tgline[-1]+i*LONG*100/place)
plt.plot([i * LONG for i in range(len(tgline))], tgline )
plt.ylabel("Energy storage SOC curve(%)")
plt.xlabel("Time")
plt.show()