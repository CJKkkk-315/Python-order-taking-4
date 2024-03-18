import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
df = pd.read_excel('economy.xls')
data = df.values.tolist()[1:-1]
data = [[i[0]] + i[1:][::-1] for i in data]
for i in data:
    print(i)
for i in data[1:]:
    plt.plot(data[0][1:],i[1:],label=i[0])
plt.legend()
plt.show()
d = {i[0].split('(')[0]:i[1:] for i in data[1:]}
df = pd.DataFrame(d)
df_corr = df.corr()
print(df_corr)
sns.heatmap(df_corr, annot=True, cmap="coolwarm")
plt.show()
plt.clf()