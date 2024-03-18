import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

df = pd.read_csv('Movies.csv')

df.head()
df_Popular = df.sort_values(by='IMDb',ascending=False)

df_top200 = df_Popular[:200]

df_top200.set_index('Title', inplace=True)
print(df_top200)


movies_df = df_top200.copy()

# 初始化一个空的dataframe来存储国家及其出现次数
country_count_df = pd.DataFrame(columns=['Country', '出现次数'])

# 遍历原始dataframe的每一行
def fun(key):
    C_d = {}

    for index, row in movies_df.iterrows():
        if str(row[key]) != 'nan':
            clist = row[key].split(',')
            for c in clist:
                C_d[c] = C_d.get(c,0) + 1
    C_l = sorted(C_d.items(),key=lambda x:x[1],reverse=True)
    C_l = C_l[:6] + [('other', sum([i[1] for i in C_l[6:]]))]
    C_l.sort(key=lambda x: x[1], reverse=True)
    plt.subplot(121)
    plt.bar([i[0] for i in C_l],[i[1] for i in C_l])
    plt.subplot(122)
    plt.pie(labels=[i[0] for i in C_l],x=[i[1] for i in C_l])
    plt.show()


    new_df = pd.DataFrame({key:[i[0] for i in C_l],'time':[i[1] for i in C_l]},index=None)
    print(new_df)

fun('Country')
fun('Genres')
fun('Language')