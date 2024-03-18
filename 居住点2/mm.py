import csv

from geopy.distance import great_circle as GRC
import pandas as pd
gc = list(pd.read_excel('早高峰.xlsx',sheet_name='工厂').values)
xzl = list(pd.read_excel('早高峰.xlsx',sheet_name='写字楼').values)
jy = list(pd.read_excel('早高峰.xlsx', sheet_name='教育机构').values)
zf = list(pd.read_excel('早高峰.xlsx', sheet_name='政府').values)
sq = list(pd.read_excel('早高峰.xlsx', sheet_name='社区').values)
gj = list(pd.read_excel('早高峰.xlsx', sheet_name='公交站点').values)
dt = list(pd.read_excel('早高峰.xlsx', sheet_name='地铁站点').values)

def ff(need,sq,gj,dt):
    need_res_gj = []
    need_res_dt = []
    for i in need:
        print(i)
        dfw_gj = []
        dfw_dt = []
        dfw_sq_5 = []
        dfw_sq_8 = []
        res_gj = []
        res_dt = []
        for j in sq:
            if GRC((i[2],i[1]),(j[2],j[1])).m < 5000:
                dfw_sq_5.append(j)
            elif 5000 < GRC((i[2],i[1]),(j[2],j[1])).m < 8500:
                dfw_sq_8.append(j)
        for j in gj:
            if GRC((i[2],i[1]),(j[2],j[1])).m < 5000:
                dfw_gj.append(j)
        for j in dt:
            if GRC((i[2],i[1]),(j[2],j[1])).m < 8500:
                dfw_dt.append(j)
        for j in dfw_sq_5:
            sl_gj = 0
            for k in dfw_gj:
                if GRC((j[2], j[1]), (k[2], k[1])).m < 400:
                    sl_gj += 1
            res_gj.append(sl_gj/len(dfw_gj))
        for j in dfw_sq_8:
            sl_dt = 0
            for k in dfw_dt:
                if GRC((j[2], j[1]), (k[2], k[1])).m < 400:
                    sl_dt += 1
            res_dt.append(sl_dt/len(dfw_dt))
        need_res_gj.append(sum(res_gj)/len(res_gj))
        need_res_dt.append(sum(res_dt) / len(res_dt))
    return need_res_gj,need_res_dt
need_res_gj,need_res_dt = ff(gc,sq,gj,dt)
with open('工厂.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i,j in zip(need_res_gj,need_res_dt):
        f_csv.writerow([i,j])

need_res_gj,need_res_dt = ff(xzl,sq,gj,dt)
with open('写字楼.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i,j in zip(need_res_gj,need_res_dt):
        f_csv.writerow([i,j])
need_res_gj,need_res_dt = ff(jy,sq,gj,dt)
with open('教育机构.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i,j in zip(need_res_gj,need_res_dt):
        f_csv.writerow([i,j])
need_res_gj,need_res_dt = ff(zf,sq,gj,dt)
with open('政府.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i,j in zip(need_res_gj,need_res_dt):
        f_csv.writerow([i,j])

