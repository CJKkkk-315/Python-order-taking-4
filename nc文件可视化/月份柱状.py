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

# 创建一个空的数组用于存储每个月的平均值
monthly_avg = np.zeros(12)

# 对每个月，从原始数据中提取该月的数据，将空值替换为0，然后计算所有网格点的平均值，并将结果存储在新的数组中
for month in range(1, 13):
    monthly_data = hs_data[(dates.month == month), :, :]
    monthly_data[monthly_data == 9.96921e+36] = 0
    monthly_avg[month-1] = monthly_data.mean()

# 使用bar函数创建柱状图
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
plt.bar(months, monthly_avg)
plt.title('Monthly Average HS')
plt.xlabel('Month')
plt.ylabel('HS')
plt.show()

# 关闭NC文件
dataset.close()
