import random
n = int(input('请输入随机分配总次数:'))
r = input('请输入红色小球编号，空格分隔:').split()
b = input('请输入蓝色小球编号，空格分隔:').split()
res = {i+1:0 for i in range(12)}
for _ in range(n):
    o = [0 for _ in range(12)]
    for i in r:
        o[int(i)-1] = 1
    if b:
        for i in b:
            o[int(i) - 1] = 2
    t = []
    for i in range(len(o)):
        if o[i] == 0:
            t.append(i)
    tt = random.sample(t,k=len(t)-4)
    for i in tt:
        o[i] = 2
    for i in range(len(o)):
        if o[i] == 2:
            res[i+1] += 1
res = sorted(res.items(),key=lambda x:x[1],reverse=True)
for i in res:
    print('编号：',i[0],end=' ')
    print('次数：',i[1])

input()

