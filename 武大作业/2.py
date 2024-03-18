s = ' '.join([i.replace('\n','') for i in open('in.txt').readlines()])
s = s.replace("'",' ')
s = s.replace('.',' ')
words = s.split()
ind = [i.replace('\n','') for i in open('index.txt').readlines()]
res = []
for i in words:
    w = i.lower()
    aw = ''
    for j in w:
        if j.isalpha():
            aw += j
    if aw and aw not in ind:
        res.append(aw)
res.sort()
with open('error.txt','w') as f:
    for i in res:
        f.write(i+'\n')