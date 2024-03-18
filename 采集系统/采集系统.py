import tkinter as tk
import random

def generate_data():
    temp.set(random.randint(1, 100))
    vibration.set(random.randint(1, 100))
    pressure.set(random.randint(1, 100))

def quit_app():
    root.destroy()

root = tk.Tk()
root.title("海工平台健康数据采集系统")
root.geometry("600x250")
temp = tk.StringVar()
vibration = tk.StringVar()
pressure = tk.StringVar()

tk.Label(root, text="海工平台健康数据采集系统").grid(row=0, column=0)
tk.Label(root, text="温度").grid(row=4, column=0)
tk.Entry(root, textvariable=temp, bg='white').grid(row=4, column=1)

tk.Label(root, text="震动").grid(row=6, column=0)
tk.Entry(root, textvariable=vibration, bg='white').grid(row=6, column=1)

tk.Label(root, text="压力").grid(row=8, column=0)
tk.Entry(root, textvariable=pressure, bg='white').grid(row=8, column=1)

tk.Label(root, text="                                      ").grid(row=3, column=2)
tk.Label(root, text="                                      ").grid(row=5, column=2)
tk.Button(root, text="采集", command=generate_data).grid(row=5, column=5)
tk.Button(root, text="退出", command=quit_app).grid(row=7, column=5)

root.mainloop()
