import pandas as pd
import os

files = []
for file in os.listdir('data'):
    files.append(file)

df = pd.read_excel('特征词.xlsx',header=None)
words = df[0]
words = words.values.tolist()

for file in files:

    wb = pd.read_excel('data/' + file)
    res = []

    for i,value in wb.iterrows():
        flag = 1
        for word in words:
            if word in value['发布内容']:
                flag = 0
                res.append('参与类')
                break

        if flag:
            res.append('信息类')

    wb['分类结果'] = res

    wb.to_excel('res/' + file + '（已完成）.xlsx',index=False)
