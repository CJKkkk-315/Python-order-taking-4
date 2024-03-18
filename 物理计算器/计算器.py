from math import exp
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.messagebox

def jiaozheng(A,a,B,b,x,y0):
    print(A,a,B,b,y0)
    if B == 0 and b == 0:
        b = 1
    return (A * exp(-x/a) + B * exp(-x/b) + y0) / 100

def biaozhun(a,b,y):
    print(a,b)
    return (y - b)/a

def final(QDs,T,F,tt,c0):
    T_d = {25:0,60:1,90:2}
    A_list = [25.49271, 28.29691, 31.06839, 28.51175, 29.54201, 28.19352, 19.67917, 24.32273, 27.1014, 14.98148, 15.61372, 12.03429, 14.5643, 21.57182, 19.43577, 9.35463, 13.04213, 17.1355, 10.14878, 16.17299, 20.95763, 11.37012, 16.08455, 18.44116, 4.40994, 9.68268, 10.77244, 13.47589, 21.62167, 19.33142]
    a_list = [10.51829, 11.22841, 7.68258, 8.18137, 10.03299, 10.20132, 8.58307, 10.79333, 8.76787, 1.402, 0.91238, 0.67185, 0.83609, 0.8036, 9.15306, 0.24721, 0.23267, 0.29197, 0.26919, 0.21729, 0.17756, 0.27376, 15.67028, 0.21428, 0.79649, 0.29737, 0.16545, 0.59783, 0.68617, 0.24957]
    y0_list = [74.6421, 70.81354, 69.18667, 70.22801, 70.59231, 71.6904, 80.4767, 75.84537, 72.93658, 74.46431, 63.76571, 68.37826, 61.32824, 57.86721, 56.22526, 85.77825, 81.00363, 76.81934, 81.35836, 76.18486, 71.27194, 79.9983, 75.77719, 73.7952, 86.38288, 81.37173, 79.79507, 71.34038, 63.5606, 54.91859]
    B_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 11.03577, 20.71367, 19.47553, 24.07059, 20.96299, 24.78894, 4.85591, 5.95189, 6.04358, 8.49005, 7.64163, 7.77015, 8.62901, 8.13847, 7.76105, 9.1804, 8.93901, 9.43249, 14.94806, 14.13495, 25.74803]
    b_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 12.22729, 9.47141, 8.60987, 8.15288, 10.20819, 0.98497, 15.81635, 21.27825, 22.47588, 9.77616, 9.9092, 9.14443, 16.58166, 15.67028, 15.55599, 24.50964, 21.12395, 18.03609, 17.42193, 0.25964, 12.7819]
    a0_list = [10433.5751, 1242.6934, 20725.697, 1069.9435, 5995.0226, 18942.9259, 19461.91009, 8344.18432, 10634.76113, 2022.99983]
    b0_list = [110.5882, 31.1426, -605.9643, -60.0908, -386.7436, 392.54319, 395.76342, 564.26985, 426.19894, 167.68603]
    QDs_list = [[] for _ in range(10)]
    ii = 0
    for a,b,c,d,e in zip(A_list,a_list,B_list,b_list,y0_list):
        QDs_list[ii].append([a,b,c,d,e])
        if len(QDs_list[ii]) == 3:
            ii += 1
    a0 = a0_list[QDs-1]
    b0 = b0_list[QDs-1]
    A,a,B,b,y0 = QDs_list[QDs-1][T_d[T]]
    Fj = round(F / jiaozheng(A,a,B,b,tt,y0),5)
    print(Fj)
    ci = biaozhun(a0,b0,Fj)
    print(ci)
    mi = ci / c0
    # tkinter.messagebox.showinfo(title='结果',message='F校=' + str(Fj) + '\n' + '返排率=' + str(res) + '%')
    return mi
def two():
    ress = []
    for i in range(10):
        T = radio2.get()
        QDs = int(nl[i].get().split('-')[1])
        try:
            ev= float(evl[i].get())
            et= float(etl[i].get())
            ef= float(efl[i].get())
            res = final(QDs, T, ef, et, ev)
        except:
            res = 0
        ress.append(res)
    ress = [i/sum(ress) for i in ress]
    for i in range(10):
        elabel[i].config(text=f'该段产液量占比:{round(ress[i],5)}')
def _quit():
    win1.quit()
    win1.destroy()
win1 = Tk()
win1.protocol("WM_DELETE_WINDOW", _quit)
win1.title('水平井各段产液比例计算')
win1.geometry("1500x850")
Label(win1,text='储层类型：',).place(x=10,y=10)
radio1 = IntVar()
R1 = Radiobutton(win1, text="页岩", variable=radio1, value=1,)
R1.place(x=70,y=10)
R2 = Radiobutton(win1, text="砂岩", variable=radio1, value=2, )
R2.place(x=120,y=10)
R3 = Radiobutton(win1, text="碳酸盐岩", variable=radio1, value=3,)
R3.place(x=170,y=10)
Label(win1,text='储层温度：',).place(x=290,y=10)
radio2 = IntVar()
R4 = Radiobutton(win1, text="25°C", variable=radio2, value=25,)
R4.place(x=350,y=10)
R5 = Radiobutton(win1, text="60°C", variable=radio2, value=60, )
R5.place(x=400,y=10)
R6 = Radiobutton(win1, text="90°C", variable=radio2, value=90,)
R6.place(x=450,y=10)
nl = []
evl = []
etl = []
efl = []
elabel = []
for i in range(5):
    Label(win1,text=f'第{i+1}段').place(x=10+i*300,y=50)

    Label(win1,text='选用量子点类型').place(x=10+i*300,y=90)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win1, width=12, textvariable=number)
    numberChosen['values'] = ['QDS-' + str(i) for i in [1,2,3,4,5,6,7,8,9,10]]
    numberChosen.place(x=150+i*300,y=90)
    numberChosen.current(0)
    Label(win1,text='选用量子点浓度(mg/L)：').place(x=10+i*300,y=130)
    ev = Entry(win1)
    ev.place(x=150+i*300,y=130)

    Label(win1, text='压裂液停留时间(d)：').place(x=10+i*300, y=170)
    et = Entry(win1)
    et.place(x=150+i*300, y=170)

    Label(win1,text='检测量子点光强(a.u.)：').place(x=10+i*300,y=210)
    el = Label(win1, text='该段产液量占比:')
    el.place(x=10 + i * 300, y=250)
    ef = Entry(win1)
    ef.place(x=150+i*300,y=210)
    nl.append(number)
    evl.append(ev)
    etl.append(et)
    efl.append(ef)
    elabel.append(el)

for i in range(5):
    Label(win1,text=f'第{i+6}段').place(x=10+i*300,y=50+250)

    Label(win1,text='选用量子点类型').place(x=10+i*300,y=90+250)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win1, width=12, textvariable=number)
    numberChosen['values'] = ['QDS-' + str(i) for i in [1,2,3,4,5,6,7,8,9,10]]
    numberChosen.place(x=150+i*300,y=90+250)
    numberChosen.current(0)
    Label(win1,text='选用量子点浓度(mg/L)：').place(x=10+i*300,y=130+250)
    ev = Entry(win1)
    ev.place(x=150+i*300,y=130+250)

    Label(win1, text='压裂液停留时间(d)：').place(x=10+i*300, y=170+250)
    et = Entry(win1)
    et.place(x=150+i*300, y=170+250)

    Label(win1,text='检测量子点光强(a.u.)：').place(x=10+i*300,y=210+250)
    el = Label(win1, text='该段产液量占比:')
    el.place(x=10 + i * 300, y=250 + 250)
    ef = Entry(win1)
    ef.place(x=150+i*300,y=210+250)
    nl.append(number)
    evl.append(ev)
    etl.append(et)
    efl.append(ef)
    elabel.append(el)

for i in range(5):
    Label(win1,text=f'第{i+11}段').place(x=10+i*300,y=50+500)

    Label(win1,text='选用量子点类型').place(x=10+i*300,y=90+500)
    number = tk.StringVar()
    numberChosen = ttk.Combobox(win1, width=12, textvariable=number)
    numberChosen['values'] = ['QDS-' + str(i) for i in [1,2,3,4,5,6,7,8,9,10]]
    numberChosen.place(x=150+i*300,y=90+500)
    numberChosen.current(0)
    Label(win1,text='选用量子点浓度(mg/L)：').place(x=10+i*300,y=130+500)
    ev = Entry(win1)
    ev.place(x=150+i*300,y=130+500)

    Label(win1, text='压裂液停留时间(d)：').place(x=10+i*300, y=170+500)
    et = Entry(win1)
    et.place(x=150+i*300, y=170+500)

    Label(win1,text='检测量子点光强(a.u.)：').place(x=10+i*300,y=210+500)
    el = Label(win1, text='该段产液量占比:')
    el.place(x=10 + i * 300, y=250 + 500)
    ef = Entry(win1)
    ef.place(x=150+i*300,y=210+500)
    nl.append(number)
    evl.append(ev)
    etl.append(et)
    efl.append(ef)
    elabel.append(el)

Button(win1, text='计算',command=two,width=15,height=2).place(x=690,y=780)


# Label(win1,text='返排速度v(m3/h)：').place(x=10,y=130)
# e2 = Entry(win1)
# e2.place(x=150,y=130)
# Label(win1).pack()
#
# Label(win1,text='排液时间t(h)：').place(x=10,y=170)
# e3 = Entry(win1)
# e3.place(x=150,y=170)
# Label(win1).pack()
#
# Label(win1,text='检测量子点光强F：').place(x=10,y=210)
# e4 = Entry(win1)
# e4.place(x=150,y=210)
# Label(win1).pack()
#
# Label(win1,text='投入量子点质量M(g)：').place(x=10,y=250)
# e1 = Entry(win1)
# e1.place(x=150,y=250)
# Label(win1).pack()


# Button(win1,text='语音意识测试').pack()
# Label(win1).pack()
# Button(win1,text='语素意识测试').pack()
# Label(win1).pack()
# Button(win1,text='正字法意识测试').pack()
win1.mainloop()