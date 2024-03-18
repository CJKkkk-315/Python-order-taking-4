import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('data.csv',encoding='gbk')
df['参考总价'] = df['参考总价'].apply(lambda x:float(x.replace('万','')))
df['参考单价'] = df['参考单价'].apply(lambda x:float(x.replace('元/平米','')))
df['建筑面积'] = df['建筑面积'].apply(lambda x:float(x.replace('㎡','')))

df.boxplot(column='参考单价')
plt.axhline(df['参考单价'].mean(),linestyle='--')
plt.grid(False)
plt.title('参考单价箱型图')
plt.show()
d = {'东':[],'南':[],'西':[],'北':[]}
for row in df.iterrows():
    for i in row[1]['房屋朝向'].replace(' ',''):
        d[i].append(row[1]['参考单价'])
plt.bar(d.keys(),[sum(i)/len(i) for i in d.values()])
plt.ylim(80000,85000)
plt.xlabel('房屋朝向')
plt.ylabel('平均单价')
plt.title('不同房屋朝向的平均单价')
plt.show()

qy = df['区域.1'].values.tolist()
qy = Counter(qy)
plt.pie(labels=qy.keys(),x=qy.values())
plt.title('不同区域房源数量')
plt.show()
