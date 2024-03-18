import pandas as pd
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from matplotlib import ticker
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
width = 0.4
df = pd.read_excel('工作簿1.xlsx')
df = df.values[:,1:]
# plt.subplot(521)
target = df[:,3]
SV = SVR()
BP = MLPRegressor(max_iter=20000)
SV.fit(df[:,:3],df[:,3])
BP.fit(df[:,:3],df[:,3])
SV_ans = SV.predict(df[:,:3])
BP_ans = BP.predict(df[:,:3])
plt.plot([i for i in range(len(df[:,3]))],target,marker='v',label='True')
plt.plot([i for i in range(len(df[:,3]))],SV_ans,marker='o',label='Support Vector Machine')
plt.plot([i for i in range(len(df[:,3]))],BP_ans,marker='*',label='BP')
plt.legend()
plt.ylabel('宽高比')
plt.show()

# plt.subplot(522)
plt.bar([i for i in range(len(df[:,3]))],(SV_ans-target)/target,width=width,label='Support Vector Machine')
plt.bar([i+width for i in range(len(df[:,3]))],(BP_ans-target)/target,width=width,label='BP')
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
plt.ylabel('相对误差')
plt.legend()
plt.show()

# plt.subplot(523)
target = df[:,4]
SV = SVR()
BP = MLPRegressor(max_iter=20000)
SV.fit(df[:,:3],target)
BP.fit(df[:,:3],target)
SV_ans = SV.predict(df[:,:3])
BP_ans = BP.predict(df[:,:3])
plt.plot([i for i in range(len(df[:,3]))],target,marker='v',label='True')
plt.plot([i for i in range(len(df[:,3]))],SV_ans,marker='o',label='Support Vector Machine')
plt.plot([i for i in range(len(df[:,3]))],BP_ans,marker='*',label='BP')
plt.legend()
plt.ylabel('稀释率')
plt.show()

# plt.subplot(524)
plt.bar([i for i in range(len(df[:,3]))],(SV_ans-target)/target,width=width,label='Support Vector Machine')
plt.bar([i+width for i in range(len(df[:,3]))],(BP_ans-target)/target,width=width,label='BP')
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
plt.ylabel('相对误差')
plt.legend()
plt.show()


# plt.subplot(525)
target = df[:,5]
SV = SVR()
BP = MLPRegressor(max_iter=20000)
SV.fit(df[:,:3],target)
BP.fit(df[:,:3],target)
SV_ans = SV.predict(df[:,:3])
BP_ans = BP.predict(df[:,:3])
plt.plot([i for i in range(len(df[:,3]))],target,marker='v',label='True')
plt.plot([i for i in range(len(df[:,3]))],SV_ans,marker='o',label='Support Vector Machine')
plt.plot([i for i in range(len(df[:,3]))],BP_ans,marker='*',label='BP')
plt.ylabel('气孔率')

plt.legend()
plt.show()

# plt.subplot(526)
plt.bar([i for i in range(len(df[:,3]))],(SV_ans-target)/target,width=width,label='Support Vector Machine')
plt.bar([i+width for i in range(len(df[:,3]))],(BP_ans-target)/target,width=width,label='BP')
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
plt.ylabel('相对误差')
plt.legend()
plt.show()


# plt.subplot(527)
target = df[:,6]
SV = SVR()
BP = MLPRegressor(max_iter=20000)
SV.fit(df[:,:3],target)
BP.fit(df[:,:3],target)
SV_ans = SV.predict(df[:,:3])
BP_ans = BP.predict(df[:,:3])
plt.plot([i for i in range(len(df[:,3]))],target,marker='v',label='True')
plt.plot([i for i in range(len(df[:,3]))],SV_ans,marker='o',label='Support Vector Machine')
plt.plot([i for i in range(len(df[:,3]))],BP_ans,marker='*',label='BP')
plt.ylabel('热影响区深度')
plt.legend()
plt.show()

# plt.subplot(528)
plt.bar([i for i in range(len(df[:,3]))],(SV_ans-target)/target,width=width,label='Support Vector Machine')
plt.bar([i+width for i in range(len(df[:,3]))],(BP_ans-target)/target,width=width,label='BP')
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))
plt.ylabel('相对误差')
plt.legend()
plt.show()


# plt.subplot(529)
target = df[:,7]
SV = SVR()
BP = MLPRegressor(max_iter=20000)
SV.fit(df[:,:3],target)
BP.fit(df[:,:3],target)
SV_ans = SV.predict(df[:,:3])
BP_ans = BP.predict(df[:,:3])
plt.plot([i for i in range(len(df[:,3]))],target,marker='v',label='True')
plt.plot([i for i in range(len(df[:,3]))],SV_ans,marker='o',label='Support Vector Machine')
plt.plot([i for i in range(len(df[:,3]))],BP_ans,marker='*',label='BP')
plt.ylabel('硬度')

plt.legend()
plt.show()

# plt.subplot(5,2,10)
plt.bar([i for i in range(len(df[:,3]))],(SV_ans-target)/target,width=width,label='Support Vector Machine')
plt.bar([i+width for i in range(len(df[:,3]))],(BP_ans-target)/target,width=width,label='BP')
plt.legend()
plt.ylabel('相对误差')
plt.gca().yaxis.set_major_formatter(ticker.PercentFormatter(xmax=1, decimals=1))


plt.show()

