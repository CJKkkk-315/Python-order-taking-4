n,x,y = input().split()
n = int(n)
x = int(x)
y = int(y)
l = []
for i in range(n):
    a,b = input().split()
    a = int(a)
    b = int(b)
    l.append([i+1,a,b])
l.sort(key=lambda t:((x-t[1])**2+(y-t[2])**2)**0.5)
for i in range(3):
    print(f'编号：{l[i][0]}')
