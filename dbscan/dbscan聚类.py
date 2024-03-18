from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import pandas as pd
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
df = pd.read_excel('排行(1).xlsx')
pid = df[df.columns[0]].values
# print(pid)
df.drop(df.columns[0],axis=1,inplace=True)
# print(df)

for c in df.columns:
    ss = StandardScaler()
    df[c] = ss.fit_transform(df[c].values.reshape(-1, 1))

# print(df)
for eps in np.arange(0.001,1,0.05):
    for min_samples in range(2,10):
        dbc = DBSCAN(eps=eps,min_samples=min_samples)
        dbc.fit(df)
        res = Counter(list(dbc.labels_))
        if max(list(res)) == 2:
            pass
            # print(res,eps,min_samples)

dbc = DBSCAN(eps=0.301,min_samples=7)
dbc.fit(df)
res = Counter(list(dbc.labels_))
x = [i for i in res.keys()]
y = [i for i in res.values()]
plt.pie(labels=x,x=y)
plt.show()
print(res)
df['label'] = dbc.labels_

for i in np.c_[pid,dbc.labels_]:
    print(i)
