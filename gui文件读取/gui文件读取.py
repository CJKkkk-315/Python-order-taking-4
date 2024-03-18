import tkinter as tk
import tkinter.messagebox
from tkinter import filedialog
import pandas as pd

# 创建一个新的 Tkinter 窗口
root = tk.Tk()
root.geometry("300x230")
# 创建一个新的 DataFrame
df = pd.DataFrame()


def open_file():
    global df
    filename = filedialog.askopenfilename()

    if filename.endswith('.csv'):
        df = pd.read_csv(filename)
    elif filename.endswith('.xlsx'):
        df = pd.read_excel(filename)
    else:
        return

    # 显示文件名，行数（规模），特征数，以及前五个特征的名称
    tk.messagebox.showinfo(title='File Information',
                           message=f"数据集名称: {filename.split('/')[-1]}\n"
                                   f"规模: {df.shape[0]}\n"
                                   f"特征数: {df.shape[1]}\n"
                                   f"主要特征名称: {df.columns[:5].tolist()}")


# 创建一个新的按钮，点击时会打开文件选择器
open_button = tk.Button(root, text='Open File', command=open_file)
open_button.pack()

# 开始 Tkinter 的事件循环
root.mainloop()
