from tkinter import *
import tkinter as tk
import tkinter.messagebox
def funciton(s,e,path,name):
    with open(path+'\\'+name,'w') as f:
        data = [str(i) for i in range(int(s),int(e)+1)]
        data = ','.join(data)
        f.write(data)
root = Tk()
root.geometry('600x550')
e1 = Entry(root)
e1.place(x=150,y=70)
e2 = Entry(root)
e2.place(x=150,y=170)
e3 = Entry(root)
e3.place(x=150,y=270)
e4 = Entry(root)
e4.place(x=150,y=370)
Button(root, width=13, height=2, text='生成',command=lambda :funciton(e1.get(),e2.get(),e3.get(),e4.get())).place(x=150,y=470)

Label(root,text='起始范围:').place(x=150,y=45)
Label(root,text='结束范围:').place(x=150,y=145)
Label(root,text='生成路径:').place(x=150,y=245)
Label(root,text='文件名称:').place(x=150,y=345)

root.mainloop()