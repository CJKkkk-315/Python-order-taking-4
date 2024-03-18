import netCDF4 as nc
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 打开NC文件
dataset = nc.Dataset('333.nc')

# 读取时间变量并转换为cftime对象
times = dataset.variables['time']
cf_dates = nc.num2date(times[:], units=times.units)
print(cf_dates)
# 将cftime对象转换为可以用于创建DatetimeIndex的列表
dates_list = [pd.to_datetime(f"{date.year}-{date.month}-{date.day} {date.hour}:{date.minute}:{date.second}")
              for date in cf_dates]
dates = pd.DatetimeIndex(dates_list)

# 读取变量数据并转换为numpy数组
hs = dataset.variables['hs'][:]
hs_data = np.array(hs)
# 创建一个空的3D数组用于存储每个月的平均值
monthly_avg = np.zeros((12, hs_data.shape[1], hs_data.shape[2]))

# 对每个月，从原始数据中提取该月的数据，计算每个网格点的平均值，并将结果存储在新的3D数组中
for month in range(1, 13):
    monthly_data = hs_data[(dates.month == month), :, :]
    monthly_avg[month-1] = monthly_data.mean(axis=0)[::-1,:]

# 创建12个子图，对每个月，使用imshow函数将结果可视化
# 创建12个子图，对每个月，使用pcolormesh函数将结果可视化

fig, axs = plt.subplots(3, 4, figsize=(15, 10))
for month in range(1, 13):
    ax = axs[(month-1) // 4, (month-1) % 4]
    im = ax.imshow(monthly_avg[month-1], cmap='jet')
    ax.set_title(f'Month {month}')
    ax.set_yticks(range(29), dataset.variables['latitude'][::-1])
    ax.set_xticks(range(29), dataset.variables['longitude'][:], rotation=90)
    fig.colorbar(im, ax=ax)
plt.show()
for month in range(1, 13):
    im = plt.imshow(monthly_avg[month-1], cmap='jet')
    plt.title(f'Month {month}')
    plt.colorbar(im)
    plt.yticks(range(29),dataset.variables['latitude'][::-1])
    plt.xticks(range(29),dataset.variables['longitude'][:],rotation=90)
    plt.tight_layout()
    plt.show()

# 关闭NC文件
dataset.close()
