import pandas as pd
df = pd.read_excel('教务导出德育成绩.xlsx')
kcxf = {}
xh = {}
xhxm = {}
for i,v in df.iterrows():
    xm = v['专业名称']
    bm = v['班级']
    if v['课程名称'] not in kcxf:
        kcxf[v['课程名称']] = float(v['学分'])
    if v['学号'] not in xh:
        xh[v['学号']] = {}
    xh[v['学号']][v['课程名称']] = v['折算成绩']
    xhxm[v['学号']] = v['姓名']
print(xh)
rs = len(xh)
res = []
for i in xh:
    for kc in kcxf:
        if kc not in xh[i]:
            xh[i][kc] = 0
    row = []
    for j in xh[i]:
        row.append([j,xh[i][j]])
    print(row)
    row.sort()
    print(row)
    res.append([i] + row)
res.sort()
ress = []
for i in res:
    sall = 0
    for j in i[1:]:
        if j[1] >= 60:
            sall += ((j[1]-60)/10 + 1) * kcxf[j[0]]
        else:
            sall += 0
    sall /= sum([i for i in kcxf.values()])
    jd = round(sall, 3)
    if jd == 0:
        zcj = 0
    else:
        zcj = 50 + 10*jd
    zcj = round(zcj, 1)
    ress.append([str(i[0])] + [k[1] for k in i[1:]] + [zcj] + [jd] + [round(zcj*0.6, 2)])
    ress[-1].insert(1, xhxm[i[0]])
kc_all = [i for i in kcxf]
ress = [i[:2] + ['',''] + i[2:] for i in ress]
head0 = ['','','','','2022-2023学年第一学期学生综合测评评分表']
head = ['学号','姓名','德育','40%'] + sorted(kc_all) + ['平均学分成绩','平均学分绩点','60%','综合测评总分','名次','获奖等级']
head2 = [xm+'系', bm, '总人数',rs,'','','','给定获奖指标','30%']
xfrow = ['','','',''] + [i for i in kcxf.values()] + ['','','']
import csv
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head0)
    f_csv.writerow(head2)
    f_csv.writerow(head)
    f_csv.writerow(xfrow)
    f_csv.writerows(ress)
