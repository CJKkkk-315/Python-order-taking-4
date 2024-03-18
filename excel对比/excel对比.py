import pandas as pd
import numpy as np
import os
X = 0.3
Y = 0.9
check_df = pd.read_excel('涉法条专利.xlsx',sheet_name='26.4+20.1')
check_n = []
output_file = []
nan_file = []
for i in check_df.values:
    s = ''
    for j in i[0]:
        if '9' >= j >= '0':
            s += j
    check_n.append(s)
files = os.listdir('vaild')
for file in files:
    df = pd.read_excel('vaild/' + file).values[:,1:]
    data = df.reshape(-1,)

    res = [i for i in data if Y > i > X]
    if not res:
        check_nan = [np.isnan(i) for i in data]
        if not all(check_nan):
            output_file.append(file)
        else:
            nan_file.append([file])
import csv
with open('res1.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows([[i] for i in output_file])
final_file = []
for file in output_file:
    s = ''
    for j in file:
        if '9' >= j >= '0':
            s += j
    if s not in check_n:
        final_file.append([file])
import csv
with open('res2.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(final_file)

with open('res3.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(nan_file)