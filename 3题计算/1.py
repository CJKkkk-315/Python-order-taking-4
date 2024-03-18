import math

def bernoulli(m):
    res = 0
    for k in range(m+1):
        for v in range(k+1):
            res += (-1)**v * math.comb(k,v) * (v**m/(k+1))
    return res

def pn(n,x):
    res = 0
    for k in range(1,n+1):
        res += (bernoulli(2*k)/(math.factorial(2*k))) * (-4)**k * (1-4**k) * x**(2*k-1)
    return res


import pylab
import math
x = []
p = -math.pi/3
while p <= math.pi/3:
    x.append(p)
    p += 0.1

pylab.plot(x,[math.tan(i) for i in x],label='tan(x)')
pylab.plot(x,[pn(1,i) for i in x],label='p1(x)')
pylab.plot(x,[pn(2,i) for i in x],label='p2(x)')
pylab.plot(x,[pn(3,i) for i in x],label='p3(x)')
pylab.legend()
pylab.xlabel('X')
pylab.ylabel('Y')
pylab.savefig('outputimage.png')