import pandas as pd
import numpy as np
from tkinter import filedialog
from tkinter import ttk
import tkinter as tk
from tkinter import *
import tkinter.messagebox

all_res = []
# 将列表转为xlsx文件
def to_xlsx():
    df = pd.DataFrame({'组别':[i[0] for i in all_res],'类别':[i[1] for i in all_res],'建议':[i[2] for i in all_res]})
    df.to_excel('res.xlsx',index=False)
    tkinter.messagebox.showinfo(title='结果',message='导出成功')
# 计算两个向量间距离
def distance(x,y):
    dis = (x - y)**2
    dis = dis.sum()
    return dis**0.5
# 标准化
def StandardScaler(data):
    if data.std() == 0:
        return 0
    data = (data-data.mean())/data.std()
    return data
# 处理主函数
def cl():
    o_data = '''-0.179223	0.372327	0	1.265663	-0.030132	-0.856502	0	1.030364	0	0	0.709338	0	1.26558	0	0	0.68525	3
    -0.476191	0.00951	0	-0.7265	-0.095033	-0.09511	0	-0.486088	0	0	-0.47714	0	-0.846134	0	0	-0.907014	2
    0.670414	0.039468	0	0.611657	-1.194285	0.954418	0	2.051776	0	0	0.406083	0	0.696175	0	0	0.773956	3
    -1.344987	-0.979081	0	-0.913239	-0.358691	-0.800405	0	-0.486088	0	0	-1.761918	0	-0.976196	0	0	-1.188654	2
    2.620969	2.149795	0	1.357776	2.837658	-1.146678	0	-0.486088	0	0	2.227578	0	1.103771	0	0	2.431271	1
    -0.283125	-0.979081	0	-0.466908	-1.194285	0.441893	0	-0.486088	0	0	-0.760243	0	-0.749868	0	0	-0.274248	2
    -0.146063	-0.979081	0	-0.24751	0.042881	0.792756	0	-0.486088	0	0	-0.40489	0	-0.119016	0	0	-0.428004	2
    -0.143115	0.302426	0	0.679486	0.363327	-0.421494	0	-0.486088	0	0	0.01485	0	0.620391	0	0	-0.524841	3
    -0.53809	0.116025	0	-0.188055	0.030712	0.681581	0	-0.486088	0	0	-0.110973	0	-0.070883	0	0	-0.239505	2
    0.458189	1.757021	0	0.325268	0.452565	-1.653593	0	2.264832	0	0	0.603666	0	0.370508	0	0	0.963194	1
    1.139815	-0.27342	0	1.115769	0.412002	2.194166	0	-0.486088	0	0	1.094673	0	1.278893	0	0	0.811656	3
    -0.475454	-0.979081	0	-2.333461	-1.194285	0.028304	0	-0.486088	0	0	-1.298926	0	-2.236874	0	0	-0.855269	2
    -0.095954	0.422256	0	-0.496216	0.059106	-0.488811	0	-0.486088	0	0	-0.166513	0	-0.505105	0	0	-0.40361	2
    -1.207188	-0.979081	0	0.016269	-0.131539	0.369477	0	-0.486088	0	0	-0.075586	0	0.168759	0	0	-0.844181	2'''
    path = tk.filedialog.askopenfilename()
    text_d = {2:'进步型:无建议',3:'稳定型:建议多进行小组交互',1:'退步型:建议多巩固个人知识,完善个人知识体系构建'}
    d = {1:[],2:[],3:[]}
    # 读取基础聚类
    o_data = [[float(j) for j in i.split()] for i in o_data.split('\n')]
    # 将原始数据根据类别归纳
    for i in o_data:
        d[int(i[-1])].append(np.array(i[:-1]))
    # 读取要分类的数据
    df = pd.read_excel(path).values
    # 进行标准化处理
    for i in range(1,df.shape[1]):
        df[:,i] = StandardScaler(df[:,i])
    r = ''
    # 依次计算每一行数据
    for row in df:
        s_l = []
        # 计算和三个类别的平均距离
        for idx in range(1,4):
            s = []
            for item in d[idx]:
                s.append(distance(item,row[1:]))
            s_l.append(sum(s)/len(s))
        # 读取最小的距离及逆行分类
        all_res.append([row[0],s_l.index(min(s_l))+1,text_d[s_l.index(min(s_l))+1]])
        # 记录对应的建议
        r += row[0] + ',' + text_d[s_l.index(min(s_l))+1]
        r += '\n'
    # 展示在文本框中
    t.insert(END,r)

# 主界面
win1 = Tk()
win1.title('数据导出')
win1.geometry("560x500")
# 布置文本框
t = Text(win1,width=55,height=30)
t.pack()
# 布置按钮
Button(win1, text='选择文件',command=cl).place(x=250,y=410)
Button(win1, text='导出数据',command=to_xlsx).place(x=250,y=450)
win1.mainloop()