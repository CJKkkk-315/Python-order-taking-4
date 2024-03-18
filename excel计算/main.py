import pandas as pd
import numpy as np
d1 = {}
d2 = {}
data = pd.read_excel('input.xlsx')
c = data.columns
res = []
data = data.values.tolist()
for i in data:
    if np.nan in i:
        continue
    if i[2] == '-':
        continue
    name = i[0]
    if name not in d1:
        d1[name] = []
    d1[name].append(i+[''])
    if name not in d2:
        d2[name] = 0
    d2[name] += i[7]
for i in d1:
    for j in d1[i]:
        res.append(j)
    res[-1][-1] = d2[i]


# res = [c] + res
print(res)
df = pd.DataFrame([],columns=list(c)+[''])
s = 1
for i in res:
    df.loc[s] = i
    s += 1
df.to_excel('output.xlsx',index=False)