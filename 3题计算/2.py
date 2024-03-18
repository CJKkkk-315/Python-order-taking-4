def cube_root(a,e,x0):
    assert a > 0 and e > 0 and x0 > 0
    n = 0
    xn = x0
    while True:
        xn = (1/3)*(2*xn + a/xn**2)
        n += 1
        if abs(xn**3 - a) <= e:
            break
    return xn,n


def cube_root_list(a,e,x0):
    assert a > 0 and e > 0 and x0 > 0
    xn = x0
    res = [xn]
    while True:
        xn = (1/3)*(2*xn + a/xn**2)
        res.append(xn)
        if abs(xn**3 - a) <= e:
            break
    return res


import pylab

xk_list = cube_root_list(20000,1e-10,1)
pylab.scatter([i for i in range(len(xk_list))],xk_list)
pylab.axhline(20000**(1/3),c='red',label='y=20000**(1/3)')
pylab.xlabel('X')
pylab.ylabel('Y')
pylab.legend()
pylab.savefig('outputimage.png')