import pandas as pd
import numpy as np
detail = pd.read_csv("C:/Users/Administrator\/Desktop/SUOYOU/各组残差值统计-原值.csv",index_col=0,encoding="gbk")

#自定义标准差标准化函数
def StandardScaler(data):
    data = (data-data.mean())/data.std()
    return data
#做离差标准化
data1 = StandardScaler(detail['主动-->主动'])
data2 = StandardScaler(detail['主动-->交互'])
data3 = StandardScaler(detail['主动-->建构'])
data4 = StandardScaler(detail['主动-->被动'])
data5 = StandardScaler(detail['交互-->主动'])
data6 = StandardScaler(detail['交互-->交互'])
data7 = StandardScaler(detail['交互-->建构'])
data8 = StandardScaler(detail['交互-->被动'])
data9 = StandardScaler(detail['建构-->主动'])
data10 = StandardScaler(detail['建构-->交互'])
data11 = StandardScaler(detail['建构-->建构'])
data12 = StandardScaler(detail['建构-->被动'])
data13 = StandardScaler(detail['被动-->主动'])
data14 = StandardScaler(detail['被动-->交互'])
data15 = StandardScaler(detail['被动-->建构'])
data16 = StandardScaler(detail['被动-->被动'])
data17 = pd.concat([data1,data2,data3,data4,data5,data6,data7,data8,data9,data10,data11,data12,data13,data14,data15,data16],axis=1)
print("标准差标准化之前数据为：\n",  detail[['主动-->主动','主动-->交互','主动-->建构','主动-->被动',
                                    '交互-->主动','交互-->交互','交互-->建构','交互-->被动',
                                    '建构-->主动','建构-->交互','建构-->建构','建构-->被动',
                                    '被动-->主动','被动-->交互','被动-->建构','被动-->被动'
                                    ]].head())

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',100)
#data17.DataFrame.to_csv('C:/Users/Administrator/Desktop/WCY/XiaoYaData/group6.5/聚类/jieguo.csv',sep=',',index=False,header=True)

print('标准差标准化之后数据为：\n', data17)

