data = open('SCI影响因子.csv').read().split('\n')
data = [i.split(',') for i in data[1:]]
for t in range(10):
    flag = 0
    name = input('请输入要查询期刊的名字:')
    for i in data:
        if i[0].lower() == name.lower():
            print('期刊名字:',i[0])
            print('20年IF:',i[1])
            print('21年IF:',i[2])
            print('JCR分区:',i[5])
            print('中科院分区:',i[6])
            flag = 1
            break
    if not flag:
        print('对不起，期刊未检索到！')
