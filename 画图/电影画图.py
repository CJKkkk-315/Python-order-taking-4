import matplotlib.pyplot as plt
import matplotlib as mpl
from collections import Counter
from sklearn.cluster import KMeans
# 显示中文
mpl.rcParams['font.family'] = 'SimHei'
colors = ['green','pink','blue','yellow']
# 读取数据 转为列表
data = [eval(i.replace('\n','')) for i in open('电影3.txt',encoding='utf8').readlines()]
# 去空值
data = [i for i in data if None not in i]
# 清洗数据 将字符类型转为数字类型
for i in range(len(data)):
    data[i][0] = int(data[i][0][:4])
    data[i][-1] = int(data[i][-1].replace('↗',''))
# Kmeans聚类
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit([[i[0],i[-1]] for i in data])
kmeans_label = kmeans.labels_
kmeans_center = kmeans.cluster_centers_
# 颜色归类
cmap = [colors[i] for i in kmeans_label]
# 添加聚类中心
x = [i[0] for i in data]
y = [i[-1] for i in data]
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
# 统计每个年份电影数量
d = Counter([i[0] for i in data])
d = [[i,j] for i,j in d.items()]
# 按照年份排序
d.sort()
# 绘制折线图
plt.plot([i[0] for i in d],[i[1] for i in d])
plt.show()

# 讲数据按照最后一列排序
d = [[i[-1],i[1]] for i in data]
d.sort(reverse=True)
# 最后一列为y轴 电影名为x轴绘制直方图
plt.bar([i[1] for i in d[:10]],[i[0] for i in d[:10]])
plt.show()
