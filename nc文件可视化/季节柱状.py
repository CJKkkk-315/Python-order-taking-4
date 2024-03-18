import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 打开NC文件
dataset = nc.Dataset('333.nc')

# 读取时间变量并转换为cftime对象
times = dataset.variables['time']
cf_dates = nc.num2date(times[:], units=times.units)

# 将cftime对象转换为可以用于创建DatetimeIndex的列表
dates_list = [pd.to_datetime(f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}")
              for date in cf_dates]
dates = pd.DatetimeIndex(dates_list)

# 读取变量数据并转换为numpy数组
hs = dataset.variables['hs'][:]
hs_data = np.array(hs)

# 创建一个空的数组用于存储每个季度的平均值
quarterly_avg = np.zeros(4)

# 对每个季度，从原始数据中提取该季度的数据，计算所有网格点的平均值，并将结果存储在新的数组中
for quarter in range(1, 5):
    quarterly_data = hs_data[(dates.quarter == quarter), :, :]
    quarterly_data[quarterly_data == 9.96921e+36] = 0
    quarterly_avg[quarter-1] = quarterly_data.mean()
# 使用bar函数创建柱状图
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
plt.bar(quarters, quarterly_avg)
plt.title('Quarterly Average HS')
plt.xlabel('Quarter')
plt.ylabel('HS')
plt.show()

# 关闭NC文件
dataset.close()
