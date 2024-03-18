import csv
from geopy.distance import great_circle as GRC
import pandas as pd
gc = list(pd.read_excel('早高峰.xlsx',sheet_name='工厂').values)
xzl = list(pd.read_excel('早高峰.xlsx',sheet_name='写字楼').values)
jy = list(pd.read_excel('早高峰.xlsx', sheet_name='教育机构').values)
zf = list(pd.read_excel('早高峰.xlsx', sheet_name='政府').values)
gj = list(pd.read_excel('早高峰.xlsx', sheet_name='公交站点').values)
dt = list(pd.read_excel('早高峰.xlsx', sheet_name='地铁站点').values)
def ff(need,gj,dt):
    res = []
    for i in need:
        gj_400 = 0
        gj_8500 = 0
        dt_400 = 0
        dt_8500 = 0
        for j in gj:
            if GRC((i[2],i[1]),(j[2],j[1])).m < 400:
                gj_400 += 1
            if GRC((i[2],i[1]),(j[2],j[1])).m < 8500:
                gj_8500 += 1
        for j in dt:
            if GRC((i[2], i[1]), (j[2], j[1])).m < 400:
                dt_400 += 1
            if GRC((i[2], i[1]), (j[2], j[1])).m < 8500:
                dt_8500 += 1
        res.append([gj_400,gj_8500,dt_400,dt_8500])
    return res
res = ff(gc,gj,dt)
with open('工厂_晚.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)

res = ff(xzl,gj,dt)
with open('写字楼_晚.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
res = ff(jy,gj,dt)
with open('教育机构_晚.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
res = ff(zf,gj,dt)
with open('政府_晚.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)