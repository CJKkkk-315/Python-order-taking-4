from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import time
import datetime
item_idx = 0
l_time = time.time()
res_text = ''
def begin(type_no):

    def flash(data, l, e, ll, win2):
        global item_idx,l_time,res_text

        item_idx += 1
        if item_idx == len(data):
            win2.destroy()
            win1.deiconify()
            with open('res/res.csv','a+') as f:
                f.write(res_text+'\n')
            return
        item = data[item_idx]

        if item[0] == '示例':
            text = item[0] + '\n\n' + item[1] + '\n\n' + item[2] + '\n\n' + item[3] + '\n\n' + item[4] + '\n\n' + item[
                5] + '\n\n' + '正确答案:' + item[6]
            l.config(text=text)
            ll.pack_forget()
            e.pack_forget()
        else:
            if item_idx != 1:
                use_time = round(time.time() - l_time, 3)
                res_text += str(use_time) + ',' + e.get() + ','

                l_time = time.time()
            text = item[0] + '\n\n' + item[1] + '\n\n' + item[2] + '\n\n' + item[3] + '\n\n'
            e.delete('0', 'end')
            ll.pack()
            e.pack()
            l.config(text=text)
        l_time = time.time()

    global item_idx,res_text
    item_idx = 0
    res_text = ''
    res_text += e1.get() + ',' + e2.get() + ',' + e3.get() + ',' + e4.get() + ',' + e5.get() + ','
    win1.withdraw()
    win2 = Toplevel(win1)
    win2.title('答题系统')
    win2.geometry("900x850")
    data = []
    with open('data/' + str(radio.get()) + '_' + type_no + '.csv') as f:
        f_csv = csv.reader(f)
        for i in f_csv:
            data.append(i)
    item = data[0]
    if item[0] == '示例':
        text = item[0] + '\n\n' + item[1] + '\n\n' + item[2] + '\n\n' + item[3] + '\n\n' + item[4] + '\n\n' + item[5] + '\n\n' + '正确答案:' + item[6]
        l = Label(win2,text=text, font=ft)
        l.pack()

    ll = Label(win2,text='请输入答案：', font=ft)


    e = Entry(win2, width=35)

    b = Button(win2, text='确认', command=lambda: flash(data,l,e,ll,win2), font=ft).pack(side='bottom')


# 主页面
win1 = Tk()
ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)
win1.title('答题系统')
win1.geometry("900x850")
# 为不同按钮绑定不同函数
Label(win1,text='姓名：', font=ft).pack()
e1 = Entry(win1,width=35)
e1.pack()
Label(win1,text='性别：', font=ft).pack()
e2 = Entry(win1,width=35)
e2.pack()
Label(win1,text='出生年月：', font=ft).pack()
e3 = Entry(win1,width=35)
e3.pack()
Label(win1,text='年级：', font=ft).pack()
e4 = Entry(win1,width=35)
e4.pack()
Label(win1,text='最近2次语文测验成绩：', font=ft).pack()
e5 = Entry(win1,width=35)
e5.pack()
radio = IntVar()
R1 = Radiobutton(win1, text="1-2年级", variable=radio, value=1, font=ft)
R1.pack()
R2 = Radiobutton(win1, text="3-4年级", variable=radio, value=2, font=ft)
R2.pack()
R3 = Radiobutton(win1, text="5-6年级", variable=radio, value=3, font=ft)
R3.pack()
Label(win1).pack()
Button(win1,text='语音意识测试',command=lambda: begin('语音意识测试'), font=ft).pack()
Label(win1).pack()
Button(win1,text='语素意识测试',command=lambda: begin('语素意识测试'), font=ft).pack()
Label(win1).pack()
Button(win1,text='正字法意识测试',command=lambda: begin('正字法意识测试'), font=ft).pack()
win1.mainloop()