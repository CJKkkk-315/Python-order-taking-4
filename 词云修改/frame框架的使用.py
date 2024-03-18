import tkinter as tk
import tkinter.filedialog as fd
import CustomWordCloud as cwc
from tkinter import filedialog
from PIL import Image,ImageTk
def select_dlg():
    file_path=fd.askopenfilename(title='请选择文件')
    if file_path=='':
        return
    else:
        en1_var.set(file_path)#设置选择的文件名到文件输入框
def sele():
    filepath = filedialog.askopenfilename()
    file2.set(filepath)
#生成词云
def gerate_pic():
    global pic
    tmp_s=en2_var.get()#获取排除词语输入框的值
    stop_words=tmp_s.split(' ')#使用空格进行分词

    cwc.GenerateFile(pic_path='ress.png',
                     file_path=en1_var.get(),
                     mask_path=file2.get(),
                     stop_words=stop_words,width=100,height=80)
    pic = Image.open('ress.png')
    pic.thumbnail((500,400))
    img = ImageTk.PhotoImage(pic)

    lb3.config(image=img)
    lb3.image = img

def tmp():
    return
def clear():
    en2_var.set('')
    en1_var.set('')



root=tk.Tk()
root.geometry('800x600')
root.title('词云分析')
root.config(bg='cyan')
file2 = tk.StringVar()
#gui窗口默认使用字体
v_font=('宋体',14)
#——————第一行————————
fr1=tk.Frame(root,bd=2,width=600,height=60)
fr1.pack()
lb1=tk.Label(fr1,text='文件名：',font=v_font)
lb1.pack(side='left',)
en1_var=tk.StringVar()
en1_var.set('')
en1=tk.Entry(fr1,textvariable=en1_var,font=v_font)
en1.pack(side='left')
bt1=tk.Button(fr1,text='选择...',font=v_font,command=select_dlg)
bt1.pack(side='left')
#————————第二行————————
fr2 = tk.Frame(root,bd=2, width=600, height=60)
fr2.pack(pady=10)
lb2 = tk.Label(fr2, text='删除词汇', font=v_font)
lb2.pack(side='left')
en2_var = tk.StringVar()
en2_var.set('')
en2=tk.Entry(fr2,textvariable=en2_var,font=v_font)
en2.pack(side='left')
bt2 = tk.Button(fr2, text='清   空', font=v_font, command=clear)
bt2.pack(side='left')
#————————第三行————————
fr3=tk.Frame(root,bd=2,width=600,height=60)
fr3.pack(pady=10)
bt3 = tk.Button(fr3, text='选择蒙版', font=v_font, command=sele)
bt3.pack(side='left',padx=100)
bt4 = tk.Button(fr3, text='生   成', font=v_font, command=gerate_pic)
bt4.pack(side='left',padx=100)

lb3 = tk.Label(root)
lb3.pack()



root.mainloop()