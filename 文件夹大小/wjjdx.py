import os
from os.path import join, getsize
def getdirsize(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name)) for name in files])
    return size

if __name__ == '__main__':
    res = []
    files = os.listdir('E:\PYTHON接单4')
    for file in files:
        if os.path.isdir(f'E:\\PYTHON接单4\\{file}'):
            size = getdirsize(f'E:\\PYTHON接单4\\{file}')
            res.append([file,size / 1024 / 1024])
    res.sort(key=lambda x:x[1],reverse=True)
    for i in res:
        print(i)
