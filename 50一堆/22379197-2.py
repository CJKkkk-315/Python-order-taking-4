import numpy as np
import matplotlib.pyplot as plt
#本任务中并不要求必须使用中文文字
#如需使用中文，需要使用下面的语句将中文字体设置为黑体
#如果系统原因显示不出来中文，无需纠结，英文亦可
plt.rcParams["font.sans-serif"]=["SimHei"]

#-------下划线和省略号处需要替换成相应的代码

#表1中的数据——两个列表
#为了便于标签显示，建议年列表设计为字符串列表
years = ['2019','2020','2021','2022']
distance = [357.70,242.85,403.35,451.30]
#计算累计行驶距离，存储在另一个列表中
reduce_dis = []
for i in range(1, len(years)+1):
    reduce_dis.append(sum(distance[:i]))


#绘制饼图和折线图，figsize用于设置图片尺寸，建议保留
plt.figure(figsize=(12, 6))

#第一个子图绘制饼图
plt.subplot(121)
plt.pie(
    distance ,  #此处填写年行驶距离列表
    labels=years, #此处填写年列表，作为图的标签
    autopct='%.2f%%', #饼图上显示的比例值，保留两位小数的百分数
)
plt.title('月兔二号行驶距离比例') #此处填写饼图的Title

#第二个子图绘制折线图
plt.subplot(122)
plt.plot(years,reduce_dis,marker='o')
plt.xlabel('年')
plt.ylabel('累计行驶距离(米)')
plt.title('月兔二号累计行驶距离')
#保存图
plt.savefig('22379197-2.png')

#显示统计图
plt.show()
