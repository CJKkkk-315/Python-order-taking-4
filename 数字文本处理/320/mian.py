import os
f_save = open('连不中.txt','w')
all_res = []
files = [i for i in os.listdir('data') if i.split('.')[-1] == 'txt']
files.sort(key=lambda x:int(x.split('.')[0]))
for file in files:
    res_max = [0 for _ in range(49)]
    res = [0 for _ in range(49)]
    data = open('data/' + file).read().split('\n')
    if '〓' in data[2]:
        data = data[4:]
    if data[0][0] == '◆':
        data = [i.split()[1] for i in data if i]
    data = [i.split(',')[:-1] for i in data]
    data = [list(map(int,i)) for i in data]
    for i in data:
        for n in range(1,50):
            if n not in i:
                res[n-1] += 1
            else:
                res_max[n-1] = max(res_max[n-1],res[n-1])
                res[n-1] = 0
    f_save.write('\n')
    f_save.write(f'〓〓〓〓文本{file.split(".")[0]}中,连不中的情况:〓〓〓〓' + '\n')
    for time in range(min(res_max),max(res_max)+1):
        row = []
        for i in range(len(res_max)):
            if res_max[i] == time:
                s = str(i+1)
                if len(s) == 1:
                    s = '0' + s
                row.append(s)
        if row:
            row.append('')
            f_save.write(f'共{time}次:'+','.join(row) + '\n')
    all_res.append(res_max[:])
start = int(input())
end = int(input())
f_save.write('\n')
f_save.write(f'〓〓〓〓选取{start}-{end}次综合统计〓〓〓〓' + '\n')
d = [0 for _ in range(49)]
for i in all_res:
    for j in range(len(i)):
        if end >= i[j] >= start:
            d[j] += 1
for time in range(min(d), max(d) + 1):
    row = []
    for i in range(len(d)):
        if d[i] == time:
            s = str(i + 1)
            if len(s) == 1:
                s = '0' + s
            row.append(s)
    l = len(row)
    if row:
        row.append('')
        f_save.write(f'共{time}次:' + ','.join(row) + f' ({l} 码)' + '\n')
f_save.close()