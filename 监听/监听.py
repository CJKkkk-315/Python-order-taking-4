import time
import os
import shutil
odl_d = 'E:\\test_ddd\\'
new_d = 'D:\\test_ddd\\'
time_delay = 1
old_files = os.listdir(odl_d)
while True:
    files = os.listdir(odl_d)
    new_files = [i for i in files if i not in old_files]
    if new_files:
        shutil.rmtree(new_d)
        os.mkdir(new_d)
    for i in new_files:
        shutil.copy(odl_d+i,new_d+i)
    time.sleep(time_delay)
    old_files = files[::]