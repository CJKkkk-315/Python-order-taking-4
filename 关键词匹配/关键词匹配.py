s = '''目标1：贫穷、落后
目标2：饥饿、粮食、营养、可持续农业、农业、农民
目标3：健康、生活方式
目标4：教育、学习机会
目标5：妇女、儿童
目标6：饮用水、水、水源、水质
目标7：能源、煤矿、煤、发电、风能、可再生能源
目标8：经济、就业
目标9：技术、创新、科技、再生、可再生
目标10：国家之间、国家内部
目标11：城市、COVID-19、疫情、人类住宅、城区、极端事件、社会责任
目标12：消费、贸易、生产、污染、工业、材料、技术进步、可持续、循环经济、清洁生产、清洁、排放、碳排放、减排、绿色
目标13：空气、气候、气候变化、二氧化碳、碳排放、减排
目标14：海洋、海洋资源
目标15：生态、环境、排放、生态系统、森林、雨林、荒漠化、土地、土壤、生物多样性
目标16：包容性社会、司法
目标17：全球伙伴、实施手段'''
s = [i.split('：')[1].split('、') for i in s.split('\n')]


import pandas as pd
import csv
data = pd.read_excel('译个人任务.xlsx',header=None)
d = {}
for i in data[0]:
    d[i] = [0 for _ in range(17)]
for i in data.values:
    for j in range(len(s)):
        for k in s[j]:
            if k in i[1] or k in i[2]:
                d[i[0]][j] = 1
for i in d:
    if sum(d[i]) == 0:
        print(d[i])

res = [[str(i) for i in range(1,18)]]
res[0].append('')
for key in d:
    row = ['1' if i else '' for i in d[key]]
    res.append(row + [key])
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(res)

from collections import Counter
print(Counter([sum(i) for i in d.values()]))
for i in d:
    print(d[i])