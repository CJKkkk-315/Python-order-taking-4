def scalar_product(v1,v2):
    assert isinstance(v1,tuple) and isinstance(v2,tuple)
    assert len(v1) == len(v2)
    assert all([isinstance(i,(float,int)) for i in v1]) and all([isinstance(i,(float,int)) for i in v2])
    res = 0
    for i,j in zip(v1,v2):
        res += i*j
    return res


def projection(u,v):
    assert len(u) == len(v)
    assert any(u) and any(v)
    d = scalar_product(u,v)/scalar_product(u,u)
    return tuple([d*i for i in u])


def projection_orthogonal(u,v):
    assert len(u) == len(v)
    assert any(u) and any(v)
    return [i-j for i,j in zip(v,projection(u,v))]


def projection_on_set(v,U):
    t = set([len(i) for i in U + [v]])
    assert len(t) == 1
    for i in range(len(U)):
        for j in range(i,len(U)):
            for i1 in range(len(U[i])):
                for j1 in range(len(U[i])):
                    if i1 == j1:
                        assert U[i][i1] * U[j][j1] == 1
                    else:
                        assert U[i][i1] * U[j][j1] == 0


    assert len(t) == 1 and t[0] == 1
    return tuple([projection(i,v) for i in U])
projection_on_set((1,5,3),[(1,0,1/2),(1,0,-2)])