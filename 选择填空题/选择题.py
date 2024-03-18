import random
with open('选择题库.txt',encoding='utf8') as f:
    data = [i.split('\t') for i in f.read().split('\n')]
random.shuffle(data)
t = 0
for i in data:
    t += 1
    print(t,'.',i[0])
    print('(A)',i[1],end=' ')
    print('(B)', i[2],end=' ')
    print('(C)', i[3],end=' ')
    print('(D)', i[4])
