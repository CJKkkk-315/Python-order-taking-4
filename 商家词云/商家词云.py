import matplotlib.pyplot as plt
from collections import Counter
import wordcloud
import jieba
import csv
import re
data = []
def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
with open('comment1.csv',encoding='UTF8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i)
data = {i[0]:eval(i[1]) for i in data[1:]}

c = input('请输入商家名称:')
words = ' '.join(data[c])

seg_list_exact = jieba.cut(find_chinese(words), cut_all=False, HMM=True)
wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        max_words=280,
        max_font_size=150
    )
object_list = []
wc.generate_from_frequencies(Counter(seg_list_exact))
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()