from itertools import combinations
import random
number = list('0123456789')
com = [list(i) for i in combinations(number,3)]
sample = ''.join([str(random.randint(0,9)) for _ in range(100)])
sample = '1592031702759587822156762852538723849432483846169884100396119701292502982752144094869909176507227529'
print(sample)

# for t in range(1,100):
#     res = 0
#     for c in com:
#         aw_sample = sample[::]
#         for i in c:
#             aw_sample = aw_sample.replace(i,c[0])
#         res += aw_sample.count(c[0]*t)
#     print(t,'次:',res)

yilou_res = []
max_list = []
d = {}
for t in range(1,100):
    res = 0
    for c in com:
        aw_sample = ''.join([i if i in c else 'A' for i in sample])
        ti = aw_sample.count('A'*t)
        if ti != 0:
            d[''.join(c)] = t
        res += ti
    yilou_res.append(res)
    max_list.append(sorted([[j,i] for i,j in d.items()])[-1])
for i in range(len(yilou_res)-1,-1,-1):
    yilou_res[i] -= sum(yilou_res[i+1:])
for i in range(len(yilou_res)):
    print(i+1,'次：',yilou_res[i])

