import csv
n = 1
a = ['名字','密码','n']
b = ['test','123',n]
with open(f'data({n}).csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(a)
    f_csv.writerow(b)