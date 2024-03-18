import os
import csv
def is_float(s):
    try:
        float(s)
        return True
    except:
        return False
final = []
for file in os.listdir('res_str2'):
    try:
        ans = []
        res = []
        with open('res_str2/' + file,encoding='utf8') as f:
            data = f.read().split('\n')
        for i in data:
            if '姓名' in i:
                nnn = data.index(i)
                break
        data = data[nnn:]
        for i in range(20):
            if data[i] == '1':
                del data[i]
                break
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
            if '值' in res[i][0]:
                en = i
                break
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
        pass
with open('新1-11第2列189例.csv','w',newline='') as f:
    fcsv = csv.writer(f)
    fcsv.writerows(['姓名,性别,年龄,科室,住院号,测试号,身高,体重'.split(',')] + final)


