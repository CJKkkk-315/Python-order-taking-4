import csv

import matplotlib.pyplot as plt
from collections import Counter
import snownlp
import jieba
import numpy
from PIL import Image
import wordcloud
plt.rcParams['font.sans-serif'] = ['SimHei']
import re

content = open('工管1班许智博.txt').read()
up_content = content[:len(content)//2]
down_content = content[len(content)//2:]
# 定义保留中文的函数，方便后续对内容进行处理
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
object_list = []
#进行jieba分词处理，模式选择精确分词模式
seg_list_exact = jieba.cut(find_chinese(up_content), cut_all=False, HMM=True)
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
#打开停用词文件，将分词成果去掉所有的停用词
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)

wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words=280,
    max_font_size=150
)
wc.generate_from_frequencies(Counter(object_list))
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

csv_list = sorted(Counter(object_list).items(),key=lambda x:x[1],reverse=True)
with open('词频排行.csv','w',newline='',) as f:
    f_csv = csv.writer(f)
    f_csv.writerows(csv_list)