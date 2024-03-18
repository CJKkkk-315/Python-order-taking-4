data = open('SCI影响因子.csv').read().split('\n')
data = [i.split(',') for i in data[1:]]
r = open('需要检索的杂志列表.txt').read().split('\n')
r = [i for i in r if i]
for t in r:
    for i in data:
        if i[0].lower() == t.lower():
            print('期刊名字:', i[0][0].upper()+i[0][1:].lower())
            print('20年IF:', i[1])
            print('21年IF:', i[2])
            print('JCR分区:', i[5])
            print('中科院分区:', i[6])