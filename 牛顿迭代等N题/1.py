# 2.
from math import *
n = int(input('please input:'))
p = [i for i in range(n+1)]
for i in range(2,n+1):
    for j in range(2*i,n+1,i):
        p[j] = 0
for i in range(2,n+1):
    if p[i]:
        print(p[i])
# 3.
import random
t = (random.randint(10,99) for i in range(100))
d = {i:0 for i in range(10,100)}
for i in t:
    d[i] += 1
for k in d:
    print(k,d[k])

#1.
x = int(input('please input a num:'))
a = set()
for i in range(5):
    n = int(input('please input a num:'))
    a.add(n)
b = {1,2,3,4}
c = {5,6,7}
if x in a:
    y = 1
elif x in b:
    y = 2
elif x in c:
    y = 3
else:
    y = 4
print('y=',y)

#2.
d = {'Monday':'星期一','Tuesday':'星期二','Wednesday':'星期三','Thursday':'星期四','Friday':'星期五','Saturday':'星期六','Sunday':'星期日'}
print(list(d.keys()))
print(list(d.values()))
print(list(d.items()))

#3.
import math

def f(x):
    return math.exp(-x) - x

def df(x):
    return -math.exp(-x) - 1

def newton_iteration(x0, tol=1e-6, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) <= tol:
            return x_next
        x = x_next

x0 = -2
root = newton_iteration(x0)
print("方程e^x - x = 0 在x = -2附近的一个实根是:", root)

#4.
p = (1,2,3)
pfh = (p[0]**2 + p[1]**2 + p[2]**2)**0.5
a = p[0] / pfh
b = p[1] / pfh
c = p[2] / pfh
print('cos α = ',a)
print('cos β = ',b)
print('cos γ = ',c)
#5.
def nk(n,k):
    return str(n)[-k]
#6.
def nd(n,d):
    return str(d) in str(n)

#7.
def s(x,n):
    ss = 0
    for i in range(1,n+1):
        jx = 1
        for j in range(1,i+1):
            jx *= j
        ss += (x**i)/jx
    return ss
x = float(input('please input x:'))
n = int(input('please input n:'))
y = s(x,n)/(s(x+1.75,n) + s(x,n+5))
print(y)