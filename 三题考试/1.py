from collections import Counter
data = open('input.txt').read().split('.')
data = [i + '.' for i in data if i]
for i in data:
    print(i)


res = []
for i in data:
    row = i.split()
    for j in row:
        res.append(j.replace('’','').replace(',','').replace('.','').lower())
res = Counter(res)
print(res)

res = sorted(res.items(),key=lambda x:x[1])[::-1]
with open('out.txt','w') as f:
    for i in res:
        if i[1] >= 2:
            f.write(i[0] + ' : ' + str(i[1]) + '\n')

position = []
for r in res:
    word = r[0]
    row = []
    for i in range(len(data)):
        if word in data[i]:
            for j in range(len(data[i].split())):
                if word == data[i].split()[j].replace('’','').replace(',','').replace('.','').lower():
                    row.append([word,i+1,j+1])
    position.append(row)
with open('position.txt','w') as f:

    for i in position:
        if not i:
            continue
        row = []
        for j in i:
            row.append(f'第 {j[1]} 个句子第 {j[2]} 个单词')
        f.write(j[0] + '：' + '，'.join(row) + '。' + '\n')
