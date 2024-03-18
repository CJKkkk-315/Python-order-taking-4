import pandas as pd
juzhuqu = pd.read_excel('区域可达性.xlsx',sheet_name='居住区')
midu = {}
for i,j in juzhuqu.iterrows():
    midu[j['FID']] = j['晚上21：30']
print(midu)
for gcname in ['工厂','写字楼','学校','政府机构']:
    gc = open(f'{gcname}.txt',encoding='utf8').read().split('\n')
    gc_res = [[],[],[],[]]
    for dd in range(4):

        for i in range(0,len(gc),6):
            a = gc[i]
            if a:
                b = gc[i+dd+1].split('： ')[1].split(',')[:-1]
                now = [midu[int(ii)] for ii in b]
                gc_res[dd].append(sum(now)/len(now))
    res = []
    for i in range(len(gc_res[0])):
        row = []
        for j in range(len(gc_res)):
            row.append(gc_res[j][i])
        res.append(row)
    import csv
    with open(f'{gcname}.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(res)