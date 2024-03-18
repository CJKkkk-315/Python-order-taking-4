import matplotlib.pyplot as plt
from collections import Counter
import jieba
import numpy
from PIL import Image
import wordcloud
import re
import tkinter as tk
from tkinter import filedialog

plt.rcParams['font.sans-serif'] = ['SimHei']
# 定义保留中文的函数，方便后续对内容进行处理
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
def word_cloud(file1,file2,file3):
    file1 = file1.get()
    file2 = file2.get()
    file3 = file3.get()
    print(file3)
    content = open(file1).read()
    object_list = []
    #进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(find_chinese(content), cut_all=False, HMM=True)
    with open(file2, 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    # 去除用户选择的停用词
    stopwords.add(' ')
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)
    # 生成用户选择的背景图
    mask = numpy.array(Image.open(file3))
    wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        mask=mask,
        max_words=280,
        max_font_size=150
    )
    # 生成词云
    wc.generate_from_frequencies(Counter(object_list))
    wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
    plt.figure('前半段正面词词云')
    plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis('off')
    plt.show()


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
button2 = tk.Button(root, text="选择非敏感词文件")
button2.pack()
tk.Label(root).pack()
button3 = tk.Button(root, text="选择图片")
button3.pack()
tk.Label(root).pack()
button4 = tk.Button(root, text="生成词云")
button4.pack()
tk.Label(root).pack()
# 创建函数用于处理第一个按钮的点击事件
def select_file1():
    filepath = filedialog.askopenfilename()
    file1.set(filepath)

# 创建函数用于处理第二个按钮的点击事件
def select_file2():
    filepath = filedialog.askopenfilename()
    file2.set(filepath)

# 创建函数用于处理第二个按钮的点击事件
def select_file3():
    filepath = filedialog.askopenfilename()
    file3.set(filepath)

# 创建函数用于处理第三个按钮的点击事件
def call_function():
    word_cloud(file1,file2,file3)

# 将函数与按钮的点击事件关联起来
button1.config(command=select_file1)
button2.config(command=select_file2)
button3.config(command=select_file3)
button4.config(command=call_function)

# 启动窗口的消息循环
root.mainloop()
