from tkinter import *
import tkinter as tk
import tkinter.messagebox
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
def c():
    res = []
    df = pd.read_excel('工作簿1.xlsx')
    df = df.values[:, 1:]
    target = df[:, 3]
    LR = LinearRegression()
    LR.fit(df[:, :3], target)
    LR_ans = LR.predict([[float(e1.get()),float(e2.get()),float(e3.get())]])
    res.append(LR_ans)

    target = df[:, 4]
    LR = LinearRegression()
    LR.fit(df[:, :3], target)
    LR_ans = LR.predict([[float(e1.get()),float(e2.get()),float(e3.get())]])
    res.append(LR_ans)

    target = df[:, 5]
    LR = LinearRegression()
    LR.fit(df[:, :3], target)
    LR_ans = LR.predict([[float(e1.get()),float(e2.get()),float(e3.get())]])
    res.append(LR_ans)

    target = df[:, 6]
    LR = LinearRegression()
    LR.fit(df[:, :3], target)
    LR_ans = LR.predict([[float(e1.get()),float(e2.get()),float(e3.get())]])
    res.append(LR_ans)

    target = df[:, 7]
    LR = LinearRegression()
    LR.fit(df[:, :3], target)
    LR_ans = LR.predict([[float(e1.get()),float(e2.get()),float(e3.get())]])
    res.append(LR_ans)
    Label(win1, text='').pack()
    Label(win1,text=f'宽高比：{res[0][0]}').pack()
    Label(win1, text=f'稀释率：{res[1][0]}').pack()
    Label(win1, text=f'气孔率：{res[2][0]}').pack()
    Label(win1, text=f'热影响区深度：{res[3][0]}').pack()
    Label(win1, text=f'硬度：{res[4][0]}').pack()
    print(res)

win1 = Tk()
win1.title('预测系统')
win1.geometry("400x350")
Label(win1,text='功率：').pack()
e1 = Entry(win1)
e1.pack()
Label(win1,text='扫描速度：').pack()
e2 = Entry(win1)
e2.pack()
Label(win1,text='送粉速度：').pack()
e3 = Entry(win1)
e3.pack()
Label(win1,text='').pack()
Button(win1,text='预测',command=c).pack()


win1.mainloop()