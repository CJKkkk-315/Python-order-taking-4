a, b = input().split()
a = int(a)
b = int(b)
q = [0 for _ in range(a)]
flag = [0 for _ in range(a)]
for i in range(b):
    x, y = input().split()
    x = int(x) - 1
    if not flag[x]:
        if y == 'AC':
            flag[x] = 1
        q[x] += 1
res = 0

for i in q:
    if i == 0:
        res += 0
    elif i == 1:
        res += 10
    elif i <= 3:
        res += 7
    elif i <= 5:
        res += 5
    elif i <= 10:
        res += 3
    else:
        res += 1
print(res)


