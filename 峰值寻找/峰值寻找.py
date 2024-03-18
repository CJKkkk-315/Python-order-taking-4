import pandas as pd

import numpy as np
from scipy.signal import find_peaks

df = pd.read_excel('1111.xlsx')
data = df.values[2:,1:-1]
x = data[0,:225]
y = data[0,225:450]
print(x)
print(y)

peaks, _ = find_peaks(y)

# 输出峰值的数量
print("峰值数量:", len(peaks))

# # 输出峰值的x和y坐标
# print("峰值的x坐标:", x[peaks])
# print("峰值的y坐标:", y[peaks])
