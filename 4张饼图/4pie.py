import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('原始数据.xlsx')
df_gril = df[df['1、您的性别是'] == '女'].copy()
df_boy = df[df['1、您的性别是'] == '男'].copy()

colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']

f1 = Counter(df_gril['2、您认为脱口秀未来的发展状况是怎样的'].values)
plt.pie(f1.values(),labels=sorted(f1.keys()),colors=colors)
plt.title('女性对脱口秀未来的发展状况的态度')
plt.show()

f2 = Counter(df_boy['2、您认为脱口秀未来的发展状况是怎样的'].values)
plt.pie(f2.values(),labels=sorted(f2.keys()),colors=colors)
plt.title('男性对脱口秀未来的发展状况的态度')
plt.show()


f3 = Counter(df_gril['3、您观看节目的频率'].values)
plt.pie(f3.values(),labels=sorted(f3.keys()),colors=colors)
plt.title('女性观看脱口秀的频率')
plt.show()


f4 = Counter(df_boy['3、您观看节目的频率'].values)
plt.pie(f4.values(),labels=sorted(f4.keys()),colors=colors)
plt.title('男性观看脱口秀的频率')
plt.show()