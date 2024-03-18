import numpy as np
from data_solve import data_deal
from fjsp import FJSP
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']  # 添加这条可以让图形显示中文
from ga import GA


oj=data_deal(10,6)               #工件数，机器数
Tmachine,Tmachinetime,tdx,work,tom,machines=oj.cacu()
parm_data=[Tmachine,Tmachinetime,tdx,work,tom,machines]
to=FJSP(10,6,0.3,0.4,parm_data)      #工件数，机器数，3种选择的概率和mk01的数据

ho=GA(50,100,to,0.8,0.1,parm_data,4)     #4个数依次是迭代次数，种群规模，交叉概率，变异概率和锦标赛选择框的大小
job,machine,machine_time,result=ho.ga_total()
result=np.array(result).reshape(len(result),2)
plt.plot(result[:,0],result[:,1])                   #画完工时间随迭代次数的变化
font1={'weight':'bold','size':22}
plt.xlabel("迭代次数",font1)
plt.title("完工时间变化图",font1)
plt.ylabel("完工时间",font1)
plt.show()

# to.draw(job,machine,machine_time)#画甘特图