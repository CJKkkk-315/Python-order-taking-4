import matplotlib.pyplot as plt
with open('G1R.txt','r') as f:
    data = [i.replace('\n','').split() for i in f.readlines()[14:]]
line1_x = []
line1_y = []
for i in data:
    line1_x.append(eval(i[0]))
    line1_y.append(eval(i[1]))
with open('G2R.txt','r') as f:
    data = [i.replace('\n','').split() for i in f.readlines()[14:]]
line2_x = []
line2_y = []
for i in data:
    line2_x.append(eval(i[0]))
    line2_y.append(eval(i[1]))
with open('G3R.txt','r') as f:
    data = [i.replace('\n','').split() for i in f.readlines()[14:]]
line3_x = []
line3_y = []
for i in data:
    line3_x.append(eval(i[0]))
    line3_y.append(eval(i[1]))
line4_x = [(i+j+k)/3 for i,j,k in zip(line1_x,line2_x,line3_x)]
line4_y = [(i+j+k)/3 for i,j,k in zip(line1_y,line2_y,line3_y)]
# fig是图像对象，axes坐标轴对象
fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(12,10))
# k代表颜色，marker标记
line1 = axes.plot(line1_x,line1_y, 'blue')
# line2 = axes.plot(line2_x,line2_y, 'red')
# line3 = axes.plot(line3_x,line3_y, 'black')
# line4 = axes.plot(line4_x,line4_y, 'green')
# 图例
axes.legend()
plt.xlim(400,850)
plt.ylim(0,50)
plt.show()