import csv
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime
import snownlp
import jieba
import numpy
from PIL import Image
import wordcloud
plt.rcParams['font.sans-serif'] = ['SimHei']
import re

# 定义保留中文的函数，方便后续对内容进行处理
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese

data = []
# 读取文件中的数据
with open('疫情.csv',encoding='utf8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = data[1:]

# 将数据按照日期归类
date_emo = {}
for i in data:
    date = i[12].split()[0]
    if date not in date_emo:
        date_emo[date] = []
    # 计算每一条内容的情感得分
    date_emo[date].append(snownlp.SnowNLP(i[4]).sentiments)
# 计算每一天的平均情感得分
xy = []
for k,v in date_emo.items():
    xy.append([k,sum(v)/len(v)])
xy.sort()
x = [i[0] for i in xy]
y = [i[1] for i in xy]
# 折线图可视化
plt.plot(x,y,marker='o')
plt.xticks(rotation=60)
plt.grid()
plt.title('不同时间下的情感')
plt.xlabel('时间')
plt.ylabel('情感评分')
plt.show()

# 按照日期计算微博数量
date_number = {}
for i in data:
    date = i[12].split()[0]
    if date not in date_number:
        date_number[date] = 0
    date_number[date] += 1
xy = []
for k,v in date_number.items():
    xy.append([k,v])
xy.sort()
# 折线图展示
x = [i[0] for i in xy]
y = [i[1] for i in xy]
plt.plot(x,y,marker='o')
plt.xticks(rotation=60)
plt.grid()
plt.title('不同时间下的评论数量')
plt.xlabel('时间')
plt.ylabel('评论数量')
plt.show()

user_number = {}
for i in data:
    user = i[3]
    if user not in user_number:
        user_number[user] = 0
    user_number[user] += 1
xy = []
for k,v in user_number.items():
    xy.append([k,v])
xy.sort(reverse=True,key=lambda x:x[1])
# 折线图展示
x = [i[0] for i in xy[:20]]
y = [i[1] for i in xy[:20]]
plt.plot(x,y,marker='o')
plt.xticks(rotation=30)
plt.grid()
plt.title('不同用户的评论数量')
plt.xlabel('用户')
plt.ylabel('评论数量')
plt.show()


user_emo= {}
for i in data:
    user = i[3]
    if user not in user_emo:
        user_emo[user] = []
    user_emo[user].append(snownlp.SnowNLP(i[4]).sentiments)
xy = []
for k,v in user_emo.items():
    xy.append([len(v),k,sum(v)/len(v)])
xy.sort(reverse=True)
# 折线图展示
x = [i[1] for i in xy[:20]]
y = [i[2] for i in xy[:20]]
plt.plot(x,y,marker='o')
plt.xticks(rotation=30)
plt.grid()
plt.title('不同用户的情感得分')
plt.xlabel('用户')
plt.ylabel('情感得分')
plt.show()

object_list = []
for i in data:
    #对每一条内容，进行jieba分词处理，模式选择精确分词模式
    seg_list_exact = jieba.cut(find_chinese(i[4]), cut_all=False, HMM=True)
    with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    #打开停用词文件，将分词成果去掉所有的停用词
    for word in seg_list_exact:
        if word not in stopwords:
            object_list.append(word)

#打开我们预先选择好的词云背景图
mask = numpy.array(Image.open('1.png'))
#设置词云的一些参数，字体，背景，词语数量以及词语大小等
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_words=280,
    max_font_size=150
)
#利用Counter对词频进行统计
res = Counter(object_list)
rows = []
for i,j in res.items():
    rows.append([i,j])
wc.generate_from_frequencies(Counter(object_list))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

rows.sort(key=lambda x:x[1],reverse=True)
x = [i[0] for i in rows[:20]]
y = [i[1] for i in rows[:20]]
plt.bar(x,y)
plt.xticks(rotation=30)
plt.grid()
plt.title('词频统计')
plt.xlabel('词语')
plt.ylabel('出现次数')
plt.show()