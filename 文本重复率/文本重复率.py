import pandas as pd
import re
import numpy as np
import difflib

def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
def compare1(a, b):
    a = find_chinese(a)
    b = find_chinese(b)
    c = 0
    for i in a:
        if i in b:
            c += 1
    return c / max(len(a),len(b))
def compare2(a, b):
    df = difflib.SequenceMatcher(None, a, b)
    score = df.quick_ratio()
    return score
kd = pd.read_excel('kaodian-excel.xlsx')
zt = pd.read_excel('zhenti-excel.xlsx')
kd = np.c_[kd.values[:,0], kd.values[:,20]]
zt = np.c_[zt.values[:,0], zt.values[:,20]]
for i in kd:
    for j in zt:
        res1 = compare1(i[1],j[1])
        res2 = compare2(i[1],j[1])
        if res1 > 0.8 and res2 > 0.8:
            print(f'考点{i[0]}与真题{j[0]}重复率{(res1*100 + res2*100)/2}%')