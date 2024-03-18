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
# 创建一个空的3D数组用于存储每个季度的平均值
quarterly_avg = np.zeros((4, hs_data.shape[1], hs_data.shape[2]))

# 对每个季度，从原始数据中提取该季度的数据，计算每个网格点的平均值，并将结果存储在新的3D数组中
for quarter in range(1, 5):
    quarterly_data = hs_data[(dates.quarter == quarter), :, :]
    quarterly_avg[quarter-1] = quarterly_data.mean(axis=0)[::-1,:]


# 创建4个子图，对每个季度，使用imshow函数将结果可视化
fig, axs = plt.subplots(2, 2, figsize=(10, 10))
for quarter in range(1, 5):
    ax = axs[(quarter-1) // 2, (quarter-1) % 2]
    im = ax.imshow(quarterly_avg[quarter-1], cmap='jet')
    ax.set_title(f'Quarter {quarter}')
    ax.set_yticks(range(29), dataset.variables['latitude'][::-1])
    ax.set_xticks(range(29), dataset.variables['longitude'][:], rotation=90)
    fig.colorbar(im, ax=ax)
plt.show()
for quarter in range(1, 5):
    im = plt.imshow(quarterly_avg[quarter-1], cmap='jet')
    plt.title(f'Quarter {quarter}')
    plt.yticks(range(29),dataset.variables['latitude'][::-1])
    plt.xticks(range(29),dataset.variables['longitude'][:],rotation=90)
    plt.colorbar(im)
    plt.tight_layout()
    plt.show()

# 关闭NC文件
dataset.close()
