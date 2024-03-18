data = open('属性-p.csv').read().split('\n')
data = [i.split(',')[1:] for i in data if i][1:]
res = [[0 for _ in range(9)] for _ in range(9)]

for row in data:
    for i in range(0,9):
        for j in range(0,9):
            if row[i] == '1' and row[j] == '1' and i != j:
                res[i][j] += 1
with open('res.csv','w',newline='') as f:
    for i in res:
        f.write(','.join(list(map(str,i))) + '\n')