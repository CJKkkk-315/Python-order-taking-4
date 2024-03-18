# 引入所需要的库
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from sklearn.preprocessing import MinMaxScaler,StandardScaler
import seaborn as sns
# 设置中文字体格式
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取数据
df = pd.read_excel('空气质量监测数据.xls',header=1)
# 去除无用数据
df.drop(['O3-8h','经度','纬度'],axis=1,inplace=True)
# 获取列名和数据内容
cname = df.columns
data = df.values
clean_data = np.empty(shape=[0,len(data[0])])
# 去除掉含有错误数据的行
for i in data:
    flag = 1
    for j in i:
        if isinstance(j, str) and 'E' in j:
            flag = 0
            break
    if flag:
        clean_data = np.append(clean_data,[i],axis=0)
# 将字符串转为时间类型
for i in range(len(clean_data)):
    clean_data[i,0] = datetime.datetime.strptime(clean_data[i,0],'%Y/%m/%d %H:%M:%S')

# 散点图画出SO2与NO2分布关系
plt.scatter(clean_data[:,1],clean_data[:,3])
plt.title('SO2与NO2关系')
plt.xlabel('SO2')
plt.ylabel('NO2')
plt.show()
# 折线图画出SO2与时间的走势关系
plt.plot(clean_data[:,0],clean_data[:,1])
plt.title('SO2与时间关系')
plt.xlabel('时间')
plt.ylabel('SO2')
plt.show()
# 对数据进行MinMax归一化
for i in range(1,clean_data.shape[1]):
    gy = MinMaxScaler()
    clean_data[:,i] = gy.fit_transform(clean_data[:,i].reshape(-1, 1)).reshape(1, -1)
dfg = pd.DataFrame(clean_data)
dfg.columns = cname
# 保存到CSV
dfg.to_csv('MinMax归一化.csv',index=False)
# 重新可视化
plt.scatter(clean_data[:,1],clean_data[:,3])
plt.title('SO2与NO2关系(MinMax归一化)')
plt.xlabel('SO2')
plt.ylabel('NO2')
plt.show()

plt.plot(clean_data[:,0],clean_data[:,1])
plt.title('SO2与时间关系(MinMax归一化)')
plt.xlabel('时间')
plt.ylabel('SO2')
plt.show()

# 对数据进行Standard归一化
for i in range(1,clean_data.shape[1]):
    gy = StandardScaler()
    clean_data[:,i] = gy.fit_transform(clean_data[:,i].reshape(-1, 1)).reshape(1, -1)
dfg = pd.DataFrame(clean_data)
dfg.columns = cname
dfg.to_csv('StandardScaler归一化.csv',index=False)
# 重新可视化
plt.scatter(clean_data[:,1],clean_data[:,3])
plt.title('SO2与NO2关系(Standard归一化)')
plt.xlabel('SO2')
plt.ylabel('NO2')
plt.show()

plt.plot(clean_data[:,0],clean_data[:,1])
plt.title('SO2与时间关系(Standard归一化)')
plt.xlabel('时间')
plt.ylabel('SO2')
plt.show()
plt.show()

# 将数据转为dataframe格式
dfo = pd.DataFrame(clean_data[:,1:])
dfo.columns = cname[1:]
# 类型转为浮点数类型
dfo = dfo.astype('float')
# 得到相关性矩阵
df_corr = dfo.corr()
# 热力图可视化
sns.heatmap(df_corr, center=0,cmap='Spectral_r')
plt.show()