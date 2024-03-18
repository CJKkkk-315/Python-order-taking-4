import os
import csv
import shutil
def is_float(s):
    try:
        float(s)
        return True
    except:
        return False
head = '姓名,性别,年龄,科室,住院号,测试号,身高,体重'.split(',')
head_tail = []
for i in 'VC MAX,VT,BF,MV,ERV,FVC,FEV 1,FEV1%F,FEV1%M,PEF,FEF25,FEF50,FEF75,MMEF,MVV,FEV*30,Z5Hz,Rc,Rp,Fres.,R5Hz,R20Hz,R35Hz,X5Hz,RV-SB,RV%TLC,TLC-SB,FRC,FRC%TC,DLCOSB'.split(','):
    head_tail.append(i + ' 预计值')
    head_tail.append(i + ' 实际值')
    head_tail.append(i + ' 实/预')
head += head_tail
final = [head]
for file in os.listdir('res_str'):
    try:
        ans = []
        res = []
        try:
            with open('res_str/' + file, encoding='gbk') as f:
                data = f.read().split('\n')
        except:
            with open('res_str/' + file, encoding='utf8') as f:
                data = f.read().split('\n')
        now = []
        for i in data:
            if not is_float(i) or len(now) == 4:
                res.append(now[:])
                now = [i]
            else:
                now.append(i)
        res.append(now[:])
        sn = 1
        en = 15
        for i in range(len(res)):
            if not res[i]:
                continue
            if '姓名' in res[i][0]:
                sn = i
            if 'Table' in res[i][0]:
                en = i
        row = []
        for i in res[sn:en]:
            for j in i:
                row.append(j)
        ans.append(row)
        sn = 23
        for i in range(len(res)):
            if not res[i]:
                continue
            if 'VC' in res[i][0]:
                sn = i
                break
        for i in res[sn:]:
            if not i:
                ans.append(i)
            if is_float(i[0]):
                ans.append(i)
            else:
                ans.append(i[1:])
        if not ans[-1]:
            ans = ans[:-1]
        now_p = [ans[0][1],ans[0][3],ans[0][5].replace(' ','').replace('Years',''),ans[0][7],ans[0][9],ans[0][11],ans[0][13].replace(' ','').replace('cm',''),ans[0][15].replace(' ','').replace('kg','')]
        for i in ans[1:]:
            if len(i) == 0:
                now_p.extend(['', '', ''])
            if len(i) == 1:
                now_p.extend(['',i[0],''])
            else:
                now_p.extend(i)
        final.append(now_p)
    except:
        continue
with open('老38-75第2列汇总1193例.csv','w',newline='', encoding='utf8') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(final)


