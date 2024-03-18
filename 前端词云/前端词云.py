import matplotlib.pyplot as plt
from collections import Counter
import jieba
import csv
import wordcloud
import re
import tkinter.messagebox
import tkinter as tk
from tkinter import filedialog

plt.rcParams['font.sans-serif'] = ['SimHei']
# 定义保留中文的函数，方便后续对内容进行处理
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
def word_cloud(file1):
    file1 = file1.get()
    content = open(file1,encoding='utf8').read()
    #进行jieba分词处理，模式选择精确分词模式
    object_list = jieba.cut(find_chinese(content), cut_all=False, HMM=True)
    # 生成用户选择的背景图
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        max_words=280,
        max_font_size=150
    )
    # 生成词云
    wc.generate_from_frequencies(Counter(object_list))
    plt.figure('词云')
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()


def word_count(file1):
    file1 = file1.get()
    content = open(file1,encoding='utf8').read()
    # 进行jieba分词处理，模式选择精确分词模式
    object_list = jieba.cut(find_chinese(content), cut_all=False, HMM=True)
    res = sorted(Counter(object_list).items(),key=lambda x:x[1])[::-1]
    # plt.bar([i[0] for i in res[:30]],[i[1] for i in res[:30]])
    # plt.show()
    with open('词频.csv','w',newline='') as f:
        f_csv = csv.writer(f)
        f_csv.writerows(res)

    tkinter.messagebox.showinfo(title='成功！',message='词频已保存为res.csv！')


# 创建tkinter窗口
root = tk.Tk()

# 设置窗口标题
root.title("词云生成器")

# 设置窗口大小
root.geometry("300x230")

# 创建按钮并添加到窗口
file1 = tk.StringVar()
file2 = tk.StringVar()
file3 = tk.StringVar()
button1 = tk.Button(root, text="选择文本文件")
button1.pack()
tk.Label(root).pack()
button2 = tk.Button(root, text="生成词云")
button2.pack()
tk.Label(root).pack()
button3 = tk.Button(root, text="生成词频")
button3.pack()
tk.Label(root).pack()
# 创建函数用于处理第一个按钮的点击事件
def select_file():
    filepath = filedialog.askopenfilename()
    file1.set(filepath)

# 创建函数用于处理第二个按钮的点击事件
def ciyun():
    word_cloud(file1)

# 创建函数用于处理第二个按钮的点击事件
def cipin():
    word_count(file1)

# 创建函数用于处理第三个按钮的点击事件

# 将函数与按钮的点击事件关联起来
button1.config(command=select_file)
button2.config(command=ciyun)
button3.config(command=cipin)

# 启动窗口的消息循环
root.mainloop()
