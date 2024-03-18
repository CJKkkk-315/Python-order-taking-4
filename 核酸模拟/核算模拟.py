from random import random
while True:
    try:
        r = float(input('请输入阳性概率:'))
        p = int(input('请输入检测人数:'))
        break
    except:
        print('输入非数字！')

l = []
n = []
for i in range(p):
    if random() < r:
        n.append(1)
    else:
        n.append(0)
    if len(n) == 20:
        l.append(n)
        n = []
if n:
    l.append(n)
red = set()
yellow = set()
for i in range(len(l)):
    if 1 in l[i]:
        red.add(i)
        yellow.add(max(0,i-1))
        yellow.add(min(len(l)-1,i+1))

for i in red:
    if i in yellow:
        yellow.remove(i)

print('阳性人数:',sum([sum(l[i]) for i in list(red)]))

print('红码管号:',sorted(list(red)))
print('红码人数:',sum([len(l[i]) for i in list(red)]))

print('黄码管号:',sorted(list(yellow)))
print('黄码人数:',sum([len(l[i]) for i in list(yellow)]))


