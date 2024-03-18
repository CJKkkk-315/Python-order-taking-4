import pandas as pd
import matplotlib.pyplot as plt
import seaborn
df = pd.read_csv('data.csv')
df = df[df['Year'] == 2000]
df = pd.DataFrame(df.groupby('Age')['People'].sum())
df['Age'] = df.index
x = df['Age']
y = df['People']
y /= 10000
y = y.apply(int)
res = []
for i,j in zip(x,y):
    res.extend([i]*j)
plt.hist(res)
plt.show()