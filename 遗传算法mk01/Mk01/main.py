import numpy as np
from data_read import data_deal
from FJSP import FJSP
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
from ga import GA

# 初始化参数
oj=data_deal(10,6)
Tmachine,Tmachinetime,tdx,work,tom,machines=oj.cacu()
parm_data=[Tmachine,Tmachinetime,tdx,work,tom,machines]
to=FJSP(10,6,0.3,0.4,parm_data)
res_list = []
# 初始相对温度 设置为0-1之间
T = 0.5
for e in range(100):
    ho=GA(50,100,to,0.8,0.1,0.5,parm_data,4)
    job,machine,machine_time,result=ho.ga()
    result=np.array(result).reshape(len(result),2)
    res_list.append(result)
    print(f'第{e+1}次算法进行结果：{result[:,1][-1]}')
res_list.sort(key=lambda x:x[:,1][-1])
final_result = res_list[0]
print('遗传算法结合退火算法最优解完工时间',final_result[:,1][-1])
# 绘制迭代图
plt.plot(final_result[:,0],final_result[:,1])
plt.xlabel("迭代次数")
plt.ylabel("时间")
plt.show()
