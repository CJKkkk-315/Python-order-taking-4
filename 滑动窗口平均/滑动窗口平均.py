name = 'FGOALS-g3(1).txt'
data = [[int(i.split()[0]),float(i.split()[1])] for i in open(name).read().split('\n') if i]
res = []
for i in range(len(data)-30):
    year = data[i][0]
    n = sum([j[1] for j in data[i:i+30]])/30
    res.append([str(year),str(round(n,4))])
with open(name,'w') as f:
    for i in res:
        f.write(' '.join(i)+'\n')
