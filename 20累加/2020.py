from math import e
sa = [list(map(int,i.split()[1:])) for i in open('sa_TSS.txt').read().split('\n') if i]
tb = [list(map(int,i.split()[1:])) for i in open('tb.txt').read().split('\n') if i]
f = open('res.txt','w')
for i in range(0,len(sa),20):
    ai = 0
    for j in range(20):
        d = abs((sa[i+j][-2] + sa[i+j][-3])/2 - (tb[i//20][-2] + tb[i//20][-3])/2)
        ai += sa[i+j][-1] * e ** (-d/100)
    f.write(str(ai) + '\n')
