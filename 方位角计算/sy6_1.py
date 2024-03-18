from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
import math

data = []
save_str = ''


class Point3d:
    def __init__(self,no,x,y,z):
        self.no = no
        self.x = x
        self.y = y
        self.z = z


def duTdfm(x):
    d = int(x)
    f = int((x - d) * 60) / 100
    fs = str(f*100)[:2].replace('.','')
    if len(fs) == 1:
        fs = '0' + fs
    s = (x - d - (int((x - d) * 60) / 60)) * 3600 / 10000
    ss = str(s*10000)[:2].replace('.','')
    if len(ss) == 1:
        ss = '0' + ss
    return str(d) + '°' + fs + "'" + ss + '"'


def azimuthAngle(p1,p2):
    return duTdfm((math.degrees(math.atan2(p1.y - p2.y, p1.x - p2.x))+180) % 360)


def open_file():
    global save_str
    path_=askopenfilename()
    rows = open(path_).read().split('\n')
    rows = [i.split(',') for i in rows]
    for i in rows:
        data.append(Point3d(int(i[0]),float(i[3]),float(i[2]),float(i[4])))
    for i in data:
        text1.insert('end',str(i.no) + ',' + ','.join(list(map(lambda x:'%.3f' % x,[i.x,i.y,i.z])))+'\n')
    i = data[0]
    last = i
    for i in data[1:]:
        save_str += str(last.no) + ',' + ','.join(list(map(lambda x: '%.3f' % x, [last.x, last.y, last.z]))) + '\n'
        text2.insert('end', str(last.no) + ',' + ','.join(list(map(lambda x: '%.3f' % x, [last.x, last.y, last.z]))) + '\n')
        save_str += str(i.no) + ',' + ','.join(list(map(lambda x:'%.3f' % x,[i.x,i.y,i.z])))+'\n'
        text2.insert('end',str(i.no) + ',' + ','.join(list(map(lambda x:'%.3f' % x,[i.x,i.y,i.z])))+'\n')
        save_str +=  f'点{last.no}至点{i.no}的坐标方位角为：{azimuthAngle(last,i)}\n'
        text2.insert('end', f'点{last.no}至点{i.no}的坐标方位角为：{azimuthAngle(last,i)}\n')
        last = i

def save_file():
    file_path = asksaveasfilename(title=u'保存文件')
    with open(file_path,'w') as f:
        f.write(save_str)

root = Tk()
root.geometry('800x490')
path = StringVar()
Button(root, width = 13, height = 2,text='打开文件', command=open_file).place(x=30,y=30)
Button(root, width = 13, height = 2,text='保存文件', command=save_file).place(x=30,y=400)
l1 = Label(root,text='原始文本框：')
l1.place(x=150,y=20)
text1 = Text(root, width=40, height=30)
text1.place(x=150,y=40)
l2 = Label(root,text='计算结果展示框：')
l2.place(x=450,y=20)
text2 = Text(root, width=40, height=30)
text2.place(x=450,y=40)
root.mainloop()