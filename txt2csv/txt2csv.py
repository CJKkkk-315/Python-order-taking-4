import csv
import pandas as pd
data = [i for i in open('log_114946.txt').read().split('\n')][26:]
data = [i for i in data if i]
res_data = []
row = []
for i in data:
    row.append(i)
    if i[:5] == 'Total':
        res_data.append(row)
        row = []
res_data.append(row)
ress = {'in cmb':[],'-c (cpu core mak)':[],'-q (Queue Depth)':[],'-P (Queue Num Per core)':[],'-M (Read Percentage)':[],'-o (cmd size)':[],'Speed (IOPS)':[],'Speed (MiB/s)':[]}
for i in res_data:
    c = i[0].split('-c')[1].split()[0]
    q = i[0].split('-q')[1].split()[0]
    p = i[0].split('-P')[1].split()[0]
    m = i[0].split('-M')[1].split()[0]
    o = i[0].split('-o')[1].split()[0]
    iops = i[-1].split(':')[1].split()[0]
    mib = i[-1].split(':')[1].split()[1]
    ress['in cmb'].append('sq,cq,list,data')
    ress['-c (cpu core mak)'].append(c)
    ress['-q (Queue Depth)'].append(q)
    ress['-P (Queue Num Per core)'].append(p)
    ress['-M (Read Percentage)'].append(m)
    ress['-o (cmd size)'].append(o)
    ress['Speed (IOPS)'].append(iops)
    ress['Speed (MiB/s)'].append(mib)
ress = pd.DataFrame(ress)
ress.to_excel('res.xlsx',index=False)