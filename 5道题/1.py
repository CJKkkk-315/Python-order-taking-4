


# 1
l = [11,22,33,44,55,66,77,88,99,90]
d = {'bigger':[],'smaller':[]}
for i in l:
    if i > 50:
        d['bigger'].append(i)
    else:
        d['smaller'].append(i)
print(d)


# 2

list1=[1,10,100,25,356,500]
max_n = list1[0]
min_n = list1[0]
for i in list1:
    if max_n < i:
        max_n = i
    if min_n > i:
        min_n = i
print(max_n)
print(min_n)
# 3
def jiechen(n):
    a = 1
    for i in range(1,n+1):
        a *= i
    return a
e = 0
n = int(input())
for i in range(n+1):
    e += 1/jiechen(i)
print(e)

# 4
n = int(input())
flag = 1
if n <= 1:
    print('不是素数')
    flag = 0
for i in range(2, int(n**0.5 + 1)):
    if n % i == 0:
        print('不是素数')
        flag = 0
if flag:
    print('是素数')

# 5
n = input()
s = 0
for i in n:
    s += int(i) ** len(n)
if s == int(n):
    print('是水仙花数')
else:
    print('不是水仙花数')