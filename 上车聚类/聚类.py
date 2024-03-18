import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 打开NC文件
dataset = nc.Dataset('your_file.nc')

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

# 计算每个时间步长的平均值
hs_data_avg = hs_data.mean(axis=(1,2))

# 创建一个包含时间索引和平均值的pandas DataFrame
data = pd.DataFrame(hs_data_avg, index=dates, columns=['hs'])

# 按月计算平均值
monthly_avg = data.resample('M').mean()

# 可视化结果
plt.figure(figsize=(12, 6))
plt.plot(monthly_avg.index, monthly_avg['hs'])
plt.title('Monthly Average HS')
plt.xlabel('Month')
plt.ylabel('HS')
plt.grid()
plt.show()

# 关闭NC文件
dataset.close()
