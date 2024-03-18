import os


def print_files_R(path):
    lsdir = os.listdir(path)
    dirs = sorted([i for i in lsdir if os.path.isdir(os.path.join(path, i))])
    files = sorted([i for i in lsdir if os.path.isfile(os.path.join(path, i))])
    res = []
    if files:
        for f in files:
            res.append(os.path.join(path, f))
    if dirs:
        for d in dirs:
            res += print_files_R(os.path.join(path, d))
    return res


path = 'jfreechart-master'
all_files = print_files_R(path)
java_files = [i for i in all_files if i.split('.')[-1] == 'java']
java_row = 0
for file in java_files:
    row = len(open(file,encoding='utf8').readlines())
    java_row += row
print('java:',java_row)
java_files = [i for i in all_files if i.split('.')[-1] == 'html']
html_row = 0
for file in java_files:
    row = len(open(file,encoding='utf8').readlines())
    html_row += row
print('html:',html_row)