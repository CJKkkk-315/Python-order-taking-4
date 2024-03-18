hand = input().split(',')
hand = list(map(list,hand))
newhand = []
def check(l):
    for i in range(1,len(l)):
        if l[i] != l[i-1] + 1:
            return False
    return True
for i in hand:
    if i[1] == 'T':
        i[1] = 10
    if i[1] == 'J':
        i[1] = 11
    if i[1] == 'Q':
        i[1] = 12
    if i[1] == 'K':
        i[1] = 13
    if i[1] == 'A':
        i[1] = 14
    newhand.append([i[0],int(i[1])])
d = {'S':[],'D':[],'H':[],'C':[]}
flag = 0
for i in newhand:
    d[i[0]].append(i[1])

for key in d.keys():
    d[key] = sorted(d[key])
    for i in range(len(d[key])-4):
        if check(d[key][i:i+5]):
            flag = 1
if flag:
    print(True)
else:
    print(False)

