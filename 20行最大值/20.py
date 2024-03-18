
data = [i.split() for i in open('数据.txt').read().split('\n') if i]
res = []
for i in range(0,len(data),20):
    row = data[i:i+20]
    res.append(max(row,key=lambda x:int(x[-1])))
with open('res.txt','w') as f:
    for i in res:
        f.write('\t'.join(i)+'\n')
