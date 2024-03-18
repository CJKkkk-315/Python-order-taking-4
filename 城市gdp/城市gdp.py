import pandas as pd
df = pd.read_excel('CRE_Gdpct.xlsx')
data = df.values.tolist()[2:]
res = []
for i in data:
    m = []
    for j in data:
        if i[0] == j[0] and i[5] == j[5]:
            m.append(j)
    m.sort(key=lambda x:abs(x[-1]-i[-1]))
    res.append(f'{i[0]},{i[1]},{",".join([t[1] for t in m][1:4])}')
with open('res.csv','w',encoding='gbk',newline='') as f:
    f.write('年份,地级市,邻1,邻2,邻3\n')
    for i in res:
        f.write(i+'\n')