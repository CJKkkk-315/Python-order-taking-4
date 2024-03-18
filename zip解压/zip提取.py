from shutil import copy,rmtree,copytree
import os
from zipfile import ZipFile


def support_gbk(zip_file: ZipFile):
    name_to_info = zip_file.NameToInfo
    # copy map first
    for name, info in name_to_info.copy().items():
        real_name = name.encode('cp437').decode('gbk')
        if real_name != name:
            info.filename = real_name
            del name_to_info[name]
            name_to_info[real_name] = info
    return zip_file



def re_check(old_file):

    now_d = 'aw'
    flag = 1
    for i in os.listdir(now_d):
        if os.path.isdir(os.path.join(now_d,i)):
            n_file = os.listdir(os.path.join(now_d,i))
            for nn in n_file:
                copy(os.path.join(now_d,i,nn),os.path.join(now_d,nn))
            flag = 0
            break
        elif i.split('.')[1] == 'zip':
            f = support_gbk(ZipFile(os.path.join(now_d,i)))
            for zip_f in f.namelist():
                f.extract(zip_f,'aw')
            f.close()
            flag = 0
            break
    if flag:
        return 0

    else:

        for file in old_file:
            pp = os.path.join(now_d, file)
            if os.path.isdir(pp):
                rmtree(pp)
            else:
                os.remove(pp)
        re_check(os.listdir('aw'))


if os.path.exists('aw'):
    rmtree('aw')
os.mkdir('aw')
files = os.listdir('data')
for file in files:
    rmtree('aw')
    os.mkdir('aw')
    copytree(os.path.join('data',file),os.path.join('aw',file))
    re_check(os.listdir('aw'))
    for need in os.listdir('aw'):
        copy(os.path.join('aw', need), os.path.join('data',file))

rmtree('aw')