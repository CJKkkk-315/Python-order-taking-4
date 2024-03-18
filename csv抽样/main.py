import random
import csv
data = []
with open('media.csv',encoding='utf8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
for i in data:
    print(i)
p = 0.5
n = int(p * len(data))
res = random.sample(data,n)
with open('res.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)

import xlwt
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1', cell_overwrite_ok=True)
    style = xlwt.XFStyle()
    align = xlwt.Alignment()
    align.horz = 1
    style.alignment = align
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i, j, data[j], style=style)
        i = i + 1
    f.save(file_path)
data_write('res.xls',res)