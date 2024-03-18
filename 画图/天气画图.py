import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter
# 设置中文字体
mpl.rcParams['font.family'] = 'SimHei'
colors = ['green','pink','blue','yellow']
from sklearn.cluster import KMeans
# 读取数据转换为列表
data = [eval(i.replace('\n','')) for i in open('天气.txt',encoding='utf8').readlines()]
# 数据清理，去除多余空格，转换类型
for i in range(len(data)):
    data[i][3] = int(data[i][3].replace(' ',''))
    data[i][-1] = int(data[i][-1])
    data[i][0] = int(data[i][0])
# kmeans聚类
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit([[i[3],i[5]] for i in data])
kmeans_label = kmeans.labels_
kmeans_center = kmeans.cluster_centers_
# 划分x y轴
x = [i[3] for i in data]
y = [i[-1] for i in data]
# 根据不同类别定义颜色
cmap = [colors[i] for i in kmeans_label]
# 添加聚类中心为红色
for i in kmeans_center:
    x.append(i[0])
    y.append(i[1])
    cmap.append('red')
# 绘制散点图
plt.subplot(121)
plt.scatter(x,y)
plt.subplot(122)
plt.scatter(x,y,c=cmap)
plt.show()
# 以第一列为x轴 第四列为y轴绘制折线图
d = [[i[0],i[3]] for i in data]
plt.plot([i[0] for i in d],[i[1] for i in d])
plt.show()
# 以第一列为x轴 倒数第一列为y轴绘制直方图
d = [[i[0],i[-1]] for i in data]
plt.bar([i[1] for i in d],[i[0] for i in d])
plt.show()
