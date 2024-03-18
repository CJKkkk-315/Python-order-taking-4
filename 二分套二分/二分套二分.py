import matplotlib.pyplot as plt
LONG = 1
position = 1
rp = 8
place = 40
min_pre = 0.2
start_pre = 0.4
l = [-6,-8,-4,-4,0,0,10,11,14,22,15,4,5,7,2,0,-3,-10,-12,-7]
s = rp
m = s
a = 1
b = 0
p = 1
n = 1
c = 0.05


def check(s,a,b,p,m,n):
    h = abs(max(list(map(abs,l))) - m)
    h_p = h
    h_n = -h
    g_p = 0
    g_n = 0
    for i in l:
        if h_n < i < h_p:
            pass
        elif i < h_n:
            g_n += abs(h_n-i) * LONG
        elif i > h_p:
            g_p += abs(h_p-i) * LONG
    if g_p > place*(1-min_pre) or g_n > place*(1-min_pre):
        return [False,0,0,0,[0 for _ in range(len(l))]]
    g_n = -g_n
    g = g_p + g_n
    if g > 0:
        ln = list(map(lambda x: x + p,l))
        tg = 0
        for i in ln:
            tg += abs(p) * LONG
        c1 = max(ln+l)
        d1 = min(ln+l)
    else:
        ln = list(map(lambda x: x - p, l))
        tg = 0
        for i in ln:
            tg += abs(p) * LONG
        c1 = max(ln + l)
        d1 = min(ln + l)
    if abs(tg) > g:
        while True:
            f = 0.5*(c1+d1)
            tg = []
            if g > 0:
                for i in ln:
                    if i - p > f:
                        tg.append(0)
                    else:
                        tg.append(min(abs(f - i),abs(p)) * LONG)
            else:
                for i in ln:
                    if i - p < f:
                        tg.append(0)
                    else:
                        tg.append(min(abs(f - i),abs(p)) * LONG)
            if abs(sum(tg)) > 1.05*abs(g):
                c1 = f
            elif abs(sum(tg)) < 0.95*abs(g):
                d1 = f
            else:
                if g > 0:
                    ltime = start_pre*rp + abs(sum(tg))
                else:
                    ltime = start_pre*rp - abs(sum(tg))
                if not rp > ltime > min_pre*rp:
                    return [False,0,0,0,[0 for _ in range(len(l))]]
                if abs(f) > abs(h):
                    return [False,0,0,0,[0 for _ in range(len(l))]]
                F = 0
                for i,j in zip(l,tg):
                    if h > i > -h:
                        F += abs(j) * LONG
                sk = []
                for i in l:
                    if i > h_p:
                        sk.append(abs(i-h_p))
                    elif i < h_n:
                        sk.append(-abs(i-h_n))
                    else:
                        if g > 0:
                            if i - p > f:
                                sk.append(0)
                            else:
                                sk.append(-min(abs(f - i), abs(p)))
                        else:
                            if i - p < f:
                                sk.append(0)
                            else:
                                sk.append(min(abs(f - i), abs(p)))

                return [True,g,F,m,sk[::],tg[::]]
    elif abs(tg) < g:
        return [False,0,0,0,[0 for _ in range(len(l))]]
    else:
        if g > 0:
            ltime = start_pre * rp + abs(tg)
        else:
            ltime = start_pre * rp - abs(tg)
        if not rp > ltime > min_pre * rp:
            return [False,0,0,0,[0 for _ in range(len(l))]]
        F = 0
        for i in l:
            if h > i > -h:
                F += abs(p) * LONG
        sk = []
        for i in l:
            if i > h_p:
                sk.append(abs(i - h_p))
            elif i < h_n:
                sk.append(-abs(i - h_n))
            else:
                if g > 0:
                    sk.append(-abs(p))
                else:
                    sk.append(abs(p))
        return [True,g,F,m,sk[::],tg[::]]


flags = check(s,a,b,p,m,n)
if flags[0]:
    g = flags[1]
    F = flags[2]
    m = flags[3]
    sk = flags[4]
    tg = flags[5]
    if g > 0:
        print(g+s*start_pre-F)
        print(m)
        print(sk)
    else:
        print(1-g-F)
        print(m)
        print(sk)
else:
    while True:
        p = 0.5*(a+b)
        n = n + 1
        m = p*s
        l_flags = flags[::]
        flags = check(s, a, b, p, m, n)
        if flags[0]:
            if a-p < c:
                g = flags[1]
                F = flags[2]
                m = flags[3]
                sk = flags[4]
                tg = flags[5]
                if g > 0:
                    print(g + s * start_pre - F)
                    print(m)
                    print(sk)
                else:
                    print(1 - g - F)
                    print(m)
                    print(sk)
                break
            else:
                a = p
        else:
            if a-p < c:
                g = l_flags[1]
                F = l_flags[2]
                m = l_flags[3]
                sk = l_flags[4]
                tg = l_flags[5]
                if g > 0:
                    print(g + s * start_pre - F)
                    print(m)
                    print(sk)
                else:
                    print(1 - g - F)
                    print(m)
                    print(sk)
                break
            else:
                b = p

for i in range(len(l)):
    plt.axhline(l[i],xmin=i*1/len(l),xmax=(i+1)*1/len(l))
plt.show()

for i in range(len(sk)):
    plt.axhline(sk[i],xmin=i*1/len(sk),xmax=(i+1)*1/len(sk))
plt.show()
tgline = [start_pre]
for i in tg:
    tgline.append(tgline[-1]+i)
plt.plot([i*LONG for i in range(len(tgline))],tgline)
plt.show()