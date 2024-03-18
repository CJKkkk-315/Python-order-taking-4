inpu = input()
key = []
for i in inpu:
    if i not in key:
        key.append(i)
for i in 'abcdefghijklmnopqrstuvwxyz'[::-1]:
    if i not in key:
        key.append(i)
zm = list('abcdefghijklmnopqrstuvwxyz')
s = open('encrypt.txt').read()
res = []
for i in s:
    if i.isalpha():
        res.append(key[zm.index(i)])
    else:
        res.append(i)
with open('output.txt','w') as f:
    f.write(''.join(res))
