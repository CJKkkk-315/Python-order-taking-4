import os
import shutil


def print_files_R(path):
    '''Output all files (including subdirectories)'''
    lsdir = os.listdir(path)
    dirs = sorted([i for i in lsdir if os.path.isdir(os.path.join(path, i))])
    files = sorted([i for i in lsdir if os.path.isfile(os.path.join(path, i))])
    res = []
    if files:
        for f in files:
            print(os.path.join(path, f))
            res.append(os.path.join(path, f))
    if dirs:
        for d in dirs:
            res += print_files_R(os.path.join(path, d))
    return res


def print_files_D(path):
    '''Output all files (excluding subdirectories)'''
    lsdir = os.listdir(path)
    files = sorted([i for i in lsdir if os.path.isfile(os.path.join(path, i))])
    res = []
    if files:
        for f in files:
            print(os.path.join(path, f))
            res.append(os.path.join(path, f))
    return res


def select_A(files):
    """Select All Files"""
    res = []
    for i in files:
        print(i)
        res.append(i)
    return res


def select_N(files,name):
    """Select specified file name Files"""
    res = []
    for i in files:
        if i.split('\\')[-1] == name:
            print(i)
            res.append(i)
    return res


def select_T(files,content):
    """Select files containing the specified content"""
    res = []
    for i in files:
        try:
            all_content = ''.join(open(i).readlines())
            if content in all_content:
                print(i)
                res.append(i)
        except:
            continue
    return res


def select_E(files,ext):
    """Select specified extension files"""
    ext = ext.replace('.','')
    res = []
    for i in files:
        if i.split('\\')[-1].split('.')[-1] == ext:
            print(i)
            res.append(i)
    return res


def select_big(files,size):
    """Select files larger than the specified size"""
    res = []
    for i in files:
        file_size = os.path.getsize(i)
        if file_size > int(size):
            print(i)
            res.append(i)
    return res


def select_small(files,size):
    """Select files smaller than the specified size"""
    res = []
    for i in files:
        file_size = os.path.getsize(i)
        if file_size < int(size):
            print(i)
            res.append(i)
    return res


def action_F(files):
    """First line of output file"""
    for i in files:
        try:
            first_row = open(i).readlines()[0].replace('\n','')
            print(first_row)
        except:
            print('NOT TEXT')


def action_D(files):
    """Copy file"""
    for i in files:
        shutil.copyfile(i, i+'.dup')


def action_T(files):
    """Touch file"""
    for i in files:
        os.utime(i,times=None)


if __name__ == '__main__':
    while True:
        try:
            c,path = input().split()
            if c == 'D':
                files = print_files_D(path)
                break
            elif c == 'R':
                files = print_files_R(path)
                break
            else:
                print('ERROR')
                continue
        except:
            print('ERROR')

    while True:
        try:
            cs = input()
            if cs == 'A':
                files = select_A(files)
                break
            elif cs[0] == 'N':
                c,name = cs.split()
                files = select_N(files,name)
                break
            elif cs[0] == 'E':
                c,ext = cs.split()
                files = select_E(files,ext)
                break
            elif cs[0] == 'T':
                c,content = cs.split()
                files = select_T(files,content)
                break
            elif cs[0] == '>':
                c,size = cs.split()
                files = select_big(files,size)
                break
            elif cs[0] == '<':
                c,size = cs.split()
                files = select_small(files,size)
                break
            else:
                print('ERROR')
                continue
        except:
            print('ERROR')

    while True:
        try:
            c = input()
            if c == 'F':
                action_F(files)
                break
            elif c == 'D':
                action_D(files)
                break
            elif c == 'T':
                action_T(files)
                break
            else:
                print('ERROR')
                continue
        except:
            print('ERROR')



