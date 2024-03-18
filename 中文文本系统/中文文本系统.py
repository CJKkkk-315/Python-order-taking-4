import jieba
import io
from snownlp import SnowNLP
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
import tkinter as tk
import numpy as np
from tkinter import simpledialog, filedialog, messagebox, ttk
from collections import Counter
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
file_path = ''
user_input = ''
ff_user_input = ''
# 读取停用词
wc_photos = []
titles = ["积极词云图", "中性词云图", "消极词云图"]
background_image_path = ''
def begin():
    def cluster_function():
        data_path = file_path

        # 加载停用词
        def load_stopwords(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                stopwords = [line.strip() for line in f.readlines()]
            return set(stopwords)

        stopwords_path = '停用词库.txt'
        stopwords = load_stopwords(stopwords_path)

        # 读取并预处理评论数据
        def preprocess_data(data_path):
            with open(data_path, 'r', encoding='utf-8') as f:
                raw_data = f.readlines()

            processed_data = []
            for line in raw_data:
                seg_list = jieba.cut(line.strip(), cut_all=False)
                filtered_words = [word for word in seg_list if word not in stopwords and len(word) > 1]
                processed_data.append(filtered_words)

            return processed_data

        reviews = preprocess_data(data_path)
        # 训练Word2Vec模型
        model = Word2Vec(reviews, vector_size=100, window=5, min_count=5, workers=4)

        # 提取词汇表中的词向量
        word_vectors = model.wv.vectors

        # 使用K-means聚类
        num_clusters = 20
        kmeans_clustering = KMeans(n_clusters=num_clusters)
        idx = kmeans_clustering.fit_predict(word_vectors)

        # 将词汇表中的单词映射到对应的聚类索引
        word_centroid_map = {model.wv.index_to_key[i]: idx[i] for i in range(len(model.wv.index_to_key))}

        ress = {}
        for cluster in range(num_clusters):
            words = [word for word, index in word_centroid_map.items() if index == cluster]
            if cluster not in ress:
                ress[cluster] = []
            ress[cluster].extend(words)
        plt.figure('文本聚类分析')
        plt.plot([j[0] for j in ress.values()], [len(j) for j in ress.values()],marker='*')
        plt.xlabel('特征词')
        plt.ylabel('聚类数量')
        plt.title('特征词聚类分析')

        plt.show()



    with open('停用词库.txt', 'r', encoding='utf-8') as f:
        stopwords = [line.strip() for line in f.readlines()]

    def select_background_image():
        global background_image_path
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            background_image_path = file_path
        return None

    # 分词和过滤停用词函数
    def preprocess_text():
        global ff_user_input
        save_path = filedialog.askdirectory()
        words = jieba.lcut(user_input)
        filtered_words = [word for word in words if word not in stopwords]
        ff_user_input = ' '.join(filtered_words)
        print(save_path)
        with open(save_path + '/filtered_words.txt','w') as ff:
            ff.write(ff_user_input)
        tk.messagebox.showinfo('成功！','处理过滤完成！')

    def word_frequency():
        words = ff_user_input.split()
        fy = sorted(Counter(words).items(),key=lambda x:x[1])[::-1][:10]
        plt.figure('词频统计')
        plt.bar([i[0] for i in fy],[i[1] for i in fy])
        plt.xlabel('词语')
        plt.ylabel('出现次数')
        plt.title('词频排行')
        plt.show()

        wc = WordCloud(
            font_path='C:/Windows/Fonts/simfang.ttf',
            background_color='white',
            max_words=280,
            max_font_size=150
        )
        # 生成词云

        wc.generate_from_frequencies(Counter(words))
        plt.figure('词频词云')
        plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
        plt.axis('off')
        plt.show()
    def generate_wordcloud(text):
        if background_image_path:
            background_image = Image.open(background_image_path).convert("RGBA")
            background_image_np = np.array(background_image)
            mask = ImageColorGenerator(background_image_np)
        else:
            background_image = None
        wordcloud = WordCloud(font_path="simhei.ttf", width=400, height=200, background_color="white",).generate_from_frequencies(text)
        mask = None
        if mask:
            return wordcloud.recolor(color_func=mask).to_image()
        else:
            return wordcloud.to_image()

    def resize_image(image, width, height):
        return image.resize((width, height), Image.ANTIALIAS)

    # 生成并排的Tkinter界面上的词云图
    def display_wordclouds(pos, mid, neg):
        tkwc = tk.Toplevel(root)
        tkwc.title("三张词云图")

        # 将词云图转换为PhotoImage对象
        def pil_image_to_photo(pil_image):
            img_byte_arr = io.BytesIO()
            pil_image.save(img_byte_arr, format="PNG")
            img_byte_arr = img_byte_arr.getvalue()
            return ImageTk.PhotoImage(data=img_byte_arr)

        wc_images = [generate_wordcloud(text) for text in [Counter(pos.split()), Counter(mid.split()), neg]]
        wc_images_resized = [resize_image(image, 400, 300) for image in wc_images]  # 调整图像大小
        wc_photos.clear()
        for image in wc_images_resized:
            wc_photos.append(pil_image_to_photo(image))

        # 在Tkinter界面上显示词云图
        for idx, photo in enumerate(wc_photos):
            title_label = ttk.Label(tkwc, text=titles[idx], font=("Arial", 14))
            title_label.grid(column=idx, row=0, padx=5, pady=5)

            label = ttk.Label(tkwc, image=photo)
            label.grid(column=idx, row=1, padx=5, pady=5)
        plt.figure('情感词语分布')
        plt.clf()

        plt.pie(x=[len(pos),len(mid),len(neg)],labels=[f'积极({len(pos)})',f'中性({len(mid)})',f'消极({len(neg)})'])
        plt.title('词语情感得分分布')

        plt.show()
        tkwc.mainloop()

    # 情感分析和词云生成函数
    def analyze_sentiment_and_generate_wordcloud():
        processed_text = ff_user_input
        pos = []
        poss = []
        mid = []
        mids = []
        neg = []
        negs = []
        all = []
        for word in processed_text.split():
            ss = SnowNLP(word).sentiments
            if ss > 0.8:
                pos.append(word)
                poss.append(ss)
            elif ss > 0.2:
                mid.append(word)
                mids.append(ss)
            else:
                neg.append(word)
                negs.append(-ss)
            all.append(ss)
        neg = {i:j for i,j in zip(neg,negs)}


        sentiment_score = sum(all)/len(all)

        if sentiment_score > 0.8:
            sentiment_label = "积极"
        elif sentiment_score > 0.2:
            sentiment_label = "中性"
        else:
            sentiment_label = "消极"
        messagebox.showinfo("分析结果", f"全文本情感预测: {sentiment_label} (得分: {sentiment_score:.2f})")
        display_wordclouds(' '.join(pos), ' '.join(mid), neg)

    # 从文件打开文本
    def open_file():
        global user_input
        global file_path
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if not file_path:
            return

        with open(file_path, 'r', encoding='utf8') as f:
            text = f.read()

        user_input = text

    # 手动输入文本
    def input_text():
        input_dialog = tk.Toplevel(root)
        input_dialog.title("请输入文本")
        input_dialog.geometry("500x800")

        text_widget = tk.Text(input_dialog, wrap="word", font=("Arial", 12))
        text_widget.pack(expand=True, fill=tk.BOTH, padx=20, pady=10)

        def save_input_and_close():
            global user_input
            user_input = text_widget.get(1.0, tk.END).strip()
            input_dialog.destroy()

        save_button = tk.Button(input_dialog, text="完成", command=save_input_and_close)
        save_button.pack(fill="x", padx=20, pady=10)

    # 分析手动输入的文本
    def analyze_input():
        if not user_input:
            messagebox.showerror("错误", "请手动输入文本或选择文本文件")
            return

        analyze_sentiment_and_generate_wordcloud()

    # 退出程序
    def exit_app():
        root.destroy()

    # 创建Tkinter窗口
    root = tk.Tk()
    root.title("中文情感分析及词云生成")
    root.geometry("400x300")

    open_file_button = tk.Button(root, text="选择文件文本", command=open_file)
    open_file_button.pack(fill="x", padx=20, pady=10)



    input_img_button = tk.Button(root, text="文本数据处理", command=preprocess_text)
    input_img_button.pack(fill="x", padx=20, pady=10)

    input_text_button = tk.Button(root, text="词频分析", command=word_frequency)
    input_text_button.pack(fill="x", padx=20, pady=10)

    analyze_button = tk.Button(root, text="情感分析", command=analyze_input)
    analyze_button.pack(fill="x", padx=20, pady=10)

    analyze_button = tk.Button(root, text="聚类分析", command=cluster_function)
    analyze_button.pack(fill="x", padx=20, pady=10)

    exit_button = tk.Button(root, text="退出", command=exit_app)
    exit_button.pack(fill="x", padx=20, pady=10)

    root.mainloop()
def your_function():
    begin()

def register():
    username = entry_new_username.get()
    password = entry_new_password.get()
    confirm_password = entry_confirm_password.get()

    if password != confirm_password:
        messagebox.showerror("注册失败", "两次输入的密码不匹配！")
        return

    with open("accounts.txt", "a") as file:
        file.write(f"{username},{password}\n")

    messagebox.showinfo("注册成功", "注册成功！现在可以登录。")
    now_acc.append([username, password])
    top_register.destroy()


def login():
    username = entry_username.get()
    password = entry_password.get()

    with open("accounts.txt", "r") as file:
        for line in file:
            user, pwd = line.strip().split(",")

            if user == username and pwd == password:
                messagebox.showinfo("登录成功", "登录成功！")
                root.destroy()
                your_function()
                return
    for i in now_acc:
        if user == i[0] and pwd == i[1]:
            messagebox.showinfo("登录成功", "登录成功！")
            root.destroy()
            your_function()
            return
    messagebox.showerror("登录失败", "用户名或密码错误！")

now_acc = []

root = tk.Tk()
root.geometry("400x300")
root.title("登录")

# 登录部分
frame_login = tk.Frame(root)
frame_login.pack(pady=10)

label_username = tk.Label(frame_login, text="用户名：")
label_username.grid(row=0, column=0, padx=5)

entry_username = tk.Entry(frame_login)
entry_username.grid(row=0, column=1, padx=5)

label_password = tk.Label(frame_login, text="密码：")
label_password.grid(row=1, column=0, padx=5)

entry_password = tk.Entry(frame_login, show="*")
entry_password.grid(row=1, column=1, padx=5)

button_login = tk.Button(root, text="登录", command=login)
button_login.pack(pady=10)

# 注册部分
button_register = tk.Button(root, text="注册新用户", command=lambda: top_register.deiconify())
button_register.pack(pady=10)

top_register = tk.Toplevel(root)
top_register.withdraw()
top_register.title("注册")

frame_register = tk.Frame(top_register)
frame_register.pack(pady=10)

label_new_username = tk.Label(frame_register, text="用户名：")
label_new_username.grid(row=0, column=0, padx=5)

entry_new_username = tk.Entry(frame_register)
entry_new_username.grid(row=0, column=1, padx=5)

label_new_password = tk.Label(frame_register, text="密码：")
label_new_password.grid(row=1, column=0, padx=5)

entry_new_password = tk.Entry(frame_register, show="*")
entry_new_password.grid(row=1, column=1, padx=5)

label_confirm_password = tk.Label(frame_register, text="确认密码：")
label_confirm_password.grid(row=2, column=0, padx=5)

entry_confirm_password = tk.Entry(frame_register, show="*")
entry_confirm_password.grid(row=2, column=1, padx=5)

button_confirm_register = tk.Button(top_register, text="注册", command=register)
button_confirm_register.pack(pady=10)

root.mainloop()
