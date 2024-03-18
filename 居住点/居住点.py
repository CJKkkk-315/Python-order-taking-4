import pandas as pd
dis = ['1km','3km','5km','8.5km']
write = pd.ExcelWriter('4.xlsx',mode='w',engine='openpyxl')

gcx = pd.read_excel('3.xlsx',sheet_name='工厂')
xzlx = pd.read_excel('3.xlsx',sheet_name='写字楼')
xxx = pd.read_excel('3.xlsx', sheet_name='教育')
zfx = pd.read_excel('3.xlsx', sheet_name='政府')
for dd in range(len(dis)):
    pop = pd.read_excel('各居住点人口.xlsx')
    pop_list = []
    for i in pop.values:
        pop_list.append(list(i))
    pop_d = {}
    print(pop_list)
    for i in pop_list:
        pop_d[str(i[0])] = 0
    print(pop_d)
    xzl = open('写字楼.txt',encoding='utf8').read().split('\n')
    xzll = []
    for i in range(0,len(xzl),6):
        a = xzl[i]
        if a:
            b = xzl[i+dd+1].split('： ')[1].split(',')[:-1]
            xzll.append(b)
            for j in b:
                pop_d[j] += 1

    xx = open('学校.txt',encoding='utf8').read().split('\n')
    xxl = []
    for i in range(0,len(xx),6):
        a = xx[i]
        if a:
            b = xx[i+dd+1].split('： ')[1].split(',')[:-1]
            xxl.append(b)
            for j in b:
                pop_d[j] += 1

    gc = open('工厂.txt',encoding='utf8').read().split('\n')
    gcl = []
    for i in range(0,len(gc),6):
        a = gc[i]
        if a:
            b = gc[i+dd+1].split('： ')[1].split(',')[:-1]
            gcl.append(b)
            for j in b:
                pop_d[j] += 1

    zf = open('政府机构.txt',encoding='utf8').read().split('\n')
    zfl = []
    for i in range(0,len(zf),6):
        a = zf[i]
        if a:
            b = zf[i+dd+1].split('： ')[1].split(',')[:-1]
            zfl.append(b)
            for j in b:
                pop_d[j] += 1

    pop_num = {}
    for i in pop_list:
        if pop_d[str(i[0])]:
            pop_num[str(i[0])] = i[1]//pop_d[str(i[0])]

    print(pop_num)



    res = []
    for i in range(len(gcx['FID'])):
        r = 0
        for j in gcl[i]:
            r += pop_d[j]
        res.append(r)
    print(res)
    gcx[dis[dd]] = res




    res = []
    for i in range(len(xzlx['FID'])):
        r = 0
        for j in xzll[i]:
            r += pop_d[j]
        res.append(r)
    print(res)
    xzlx[dis[dd]] = res


    res = []
    for i in range(len(xxx['FID'])):
        r = 0
        for j in xxl[i]:
            r += pop_d[j]
        res.append(r)
    print(res)
    xxx[dis[dd]] = res



    res = []
    for i in range(len(zfx['FID'])):
        r = 0
        for j in zfl[i]:
            r += pop_d[j]
        res.append(r)
    print(res)
    zfx[dis[dd]] = res


gcx.to_excel(write,'工厂',index=False)
xzlx.to_excel(write,'写字楼',index=False)
xxx.to_excel(write,'教育',index=False)
zfx.to_excel(write,'政府',index=False)
jzd = pd.read_excel('3.xlsx',sheet_name='居住点')
jzd.to_excel(write,'居住点',index=False)

write.save()
write.close()
