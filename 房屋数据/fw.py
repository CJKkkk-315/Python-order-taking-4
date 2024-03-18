import pandas as pd
import os
from tkinter import *
import shutil
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox
import tkinter.font as tkFont
pd.set_option('display.max_columns', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
jsd = '模拟1'
dcd = '导出结果'
def export(file_res):
    if not os.path.exists(dcd):
        os.makedirs(dcd)
    for i in file_res:
        shutil.copyfile(f'{jsd}/{i}', f'{dcd}/{i}')
    tkinter.messagebox.showinfo(title='导出结果',message='导出成功!')

def open_d():
    os.startfile(jsd)
def ex_d():
    os.startfile(dcd)
def check():
    def back():
        win2.destroy()
        win1.deiconify()
    # print('请输入要检索的关键项，如跳过则直接回车')
    number_d = {'':'','3人以下':[1,3],'3-10人':[3,11],'10人以上':[11,999999]}
    name = name1.get()
    state = state1.get()
    address = address1.get()
    stu = stu1.get()
    number = number_d[number1.get()]
    use = use1.get()
    have_m = have_m1.get()
    yh = yh1.get()
    phone = phone1.get()
    files = os.listdir(jsd)
    file_res = []
    for file in files:
        if file[0] == '~':
            continue
        df = pd.read_excel(f'{jsd}/' + file,sheet_name='封面')
        df = list(df.values)

        if (not state) or (df[8][1] == state):
            pass
        else:
            continue

        df = pd.read_excel(f'{jsd}/' + file, sheet_name='房屋公共')

        df = list(df.values)
        for i in df:
            print(i)
        if not name or df[0][1] == name:
            pass
        else:
            continue
        if (not address) or address in df[1][0].replace(' ', ''):
            pass
        else:
            continue

        if not stu or 'R' in df[0][5] and df[0][5][df[0][5].index('R')+1:df[0][5].index('R')+3] == stu:
            pass
        else:
            continue
        try:
            people = int(df[1][-1].split('：')[1].replace('人', '').replace(' ', ''))
        except:
            people = 0
        if (not number) or number[1] > people >= number[0]:
            pass
        else:
            continue

        if (not use) or 'R' in df[4][1] and df[4][1][df[4][1].index('R')+1:df[4][1].index('R')+3] == use:
            pass
        else:
            continue
        if (not have_m) or 'R' in df[2][8] and df[2][8][df[2][8].index('R')+1:df[2][8].index('R')+2] == have_m:
            pass
        else:
            continue
        if (not phone) or df[0][4] == float(phone):
            pass
        else:
            continue
        flag = 1
        if yh:
            flag = 0
            df = pd.read_excel(f'{jsd}/' + file, sheet_name='房屋公共')
            df = list(df.values)
            for i in range(5,5+19):
                if str(df[i][-2]) == 'nan' or 'R' not in df[i][-2] or df[i][-2][df[i][-2].index('R')+1:df[i][-2].index('R')+2] != yh:
                    pass
                else:
                    flag = 1
            df = pd.read_excel(f'{jsd}/' + file, sheet_name='一层')
            df = list(df.values)
            for i in range(10, 10 + 25):
                if str(df[i][-1]) == 'nan' or 'R' not in df[i][-1] or df[i][-1][df[i][-1].index('R') + 1:df[i][-1].index('R') + 2] != yh:
                    pass
                else:
                    flag = 1
            df = pd.read_excel(f'{jsd}/' + file, sheet_name='二层及以上')
            df = list(df.values)
            for i in range(5, 5 + 25):
                if str(df[i][-1]) == 'nan' or 'R' not in df[i][-1] or df[i][-1][df[i][-1].index('R') + 1:df[i][-1].index('R') + 2] != yh:
                    pass
                else:
                    flag = 1
        if flag:
            file_res.append(file)

    win2 = Toplevel(win1)
    win1.withdraw()
    win2.title('数据导出')
    win2.geometry("400x580")
    Label(win2, text=f'共有{len(file_res)}条结果',font=ft).pack()
    Label(win2).pack()
    gd = Scrollbar(win2)
    gd.pack(side=RIGHT,fill=Y)
    t = Text(win2,yscrollcommand=gd.set,width=40,height=25)
    t.pack()
    for i in file_res:
        t.insert(END,i+'\n')
    gd.config(command=t.yview)
    Button(win2, text='全部导出', command=lambda :export(file_res)).place(x=170, y=390)
    Button(win2, text='重新检索', command=back).place(x=170, y=430)
    Button(win2, text='打开检索文件夹', command=open_d).place(x=150, y=470)
    Button(win2, text='打开导出文件夹', command=ex_d).place(x=150, y=510)
    win2.mainloop()

def _quit():
    win1.quit()
    win1.destroy()
win1 = Tk()
win1.protocol("WM_DELETE_WINDOW", _quit)
win1.title('数据导出')
win1.geometry("400x550")
ft = tkFont.Font(family='Fixdsys', size=20, weight=tkFont.BOLD)

Label(win1,text='请输入要检索的关键项，如跳过则空白').place(x=10,y=5)

Label(win1,text='房东姓名：').place(x=10,y=30)
name1 = Entry(win1)
name1.place(x=150,y=30)

Label(win1,text='经营情况：').place(x=10,y=70)
state1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=state1)
numberChosen['values'] = ['','有','无']
numberChosen.place(x=150,y=70)


Label(win1,text='小区名：').place(x=10,y=110)
address1 = Entry(win1)
address1.place(x=150,y=110)

Label(win1,text='房屋结构：').place(x=10,y=150)
stu1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=stu1)
numberChosen['values'] = ['','钢混','砖混','砖木','其他']
numberChosen.place(x=150,y=150)

Label(win1,text='承租人数：').place(x=10,y=190)
number1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=number1)
numberChosen['values'] = ['','3人以下','3-10人','10人以上']
numberChosen.place(x=150,y=190)


Label(win1,text='使用性质：').place(x=10,y=230)
use1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=use1)
numberChosen['values'] = ['','出租','经营','居住','自用']
numberChosen.place(x=150,y=230)


Label(win1,text='二层及以上是否存在\n生产经营行为：').place(x=10,y=270)
have_m1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=have_m1)
numberChosen['values'] = ['','是','否']
numberChosen.place(x=150,y=270)


Label(win1,text='是否存在隐患：').place(x=10,y=310)
yh1 = tk.StringVar()
numberChosen = ttk.Combobox(win1, width=12, textvariable=yh1)
numberChosen['values'] = ['','是','否']
numberChosen.place(x=150,y=310)

Label(win1,text='手机号：').place(x=10,y=350)
phone1 = Entry(win1)
phone1.place(x=150,y=350)

Button(win1, text='筛选',command=check).place(x=180,y=390)
Button(win1, text='打开检索文件夹',command=open_d).place(x=150,y=430)
Button(win1, text='打开导出文件夹',command=ex_d).place(x=150,y=470)
win1.mainloop()
# print(file_res)