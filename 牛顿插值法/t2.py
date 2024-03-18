import matplotlib.pyplot as plt


def Newton(xi, yi, n, x):
    """

    """"""
    计算差商：
    f[x0,x1] = f(x0) - f(x1) / x0 - x1
    f[x0,x1,x2] = f[x0,x1] - f[x1,x2] / x0 - x2
    f[x0,x1,x2,x3] = f[x0,x1,x2] - f[x1,x2,x3] / x0 - x3
    .....
    """
    diff_quot = [[] for i in range(n)]
    for j in range(1, n + 1):
        if j == 1:
            for i in range(n + 1 - j):
                diff_quot[j - 1].append((yi[i] - yi[i + 1]) / (xi[i] - xi[i + 1]))
        else:
            for i in range(n + 1 - j):
                diff_quot[j - 1].append((diff_quot[j - 2][i] - diff_quot[j - 2][i + 1]) / (xi[i] - xi[i + j]))

    """
    插值公式：f(x) = f(x0) + f[x0,x1](x-x0) + f[x0,x1,x2](x-x0)(x-x1) + .... + f[x0,...,xn](x-x0)...(x-xn-1)
    """
    f = yi[0]
    v = []
    r = 1
    for i in range(n):
        r *= (x - xi[i])
        v.append(r)
        f += diff_quot[i][0] * v[i]
    return f


x = [0.0, 12.67, 17.88, 29.54, 31.60, 39.25, 47.63, 64.88, 79.71, 89.35, 100.0]
y = [1.4953, 1.4751, 1.4671, 1.4493, 1.4468, 1.4368, 1.4247, 1.4112, 1.3839, 1.3718, 1.3604]
plt.scatter(x,y)


plt.plot([i for i in range(101)],[Newton(x, y, 2, i) for i in range(101)])
plt.show()
