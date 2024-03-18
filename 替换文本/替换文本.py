import pandas as pd
data = pd.read_excel('弹状病毒科所有数据.xlsx',sheet_name='下载数据')
D = data.values[:,3]
E = data.values[:,4]
context = open('result.phy.treefile').read()
for i in range(len(D)):
    context = context.replace(D[i], E[i])
    context = context.replace(E[i] + '.1', E[i])
with open('new.result.phy.treefile','w') as f:
    f.write(context)