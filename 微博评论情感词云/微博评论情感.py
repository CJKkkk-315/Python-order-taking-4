from snownlp import SnowNLP
import pandas as pd
import jieba
import wordcloud
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime, date

df = pd.read_csv('微博评论终.csv',encoding='gbk')

words = df['评论内容'].values.tolist()
content = ' '.join([i for i in words if str(i) != 'nan'])
seg_list_exact = jieba.cut(content, cut_all=False, HMM=True)
object_list = []
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
# 去除用户选择的停用词
stopwords.add(' ')
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)
# 生成用户选择的背景图
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words=280,
    max_font_size=150
)
# 生成词云
wc.generate_from_frequencies(Counter(object_list))
plt.figure('前半段正面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

data = df.values.tolist()
pos = [0 for _ in range(150)]
neg = [0 for _ in range(150)]
for i in data[:-1]:

    hour = (int(i[2].split('/')[2].split()[0]) - 21) * 24 + int(i[2].split()[1].split(':')[0]) - 12
    if SnowNLP(i[1]).sentiments > 0.5:
        pos[hour] += 1
    else:
        neg[hour] += 1
plt.plot([i for i in range(150)],pos,label='pos',marker='*')
plt.plot([i for i in range(150)],neg,label='neg',marker='o')
plt.legend()
plt.show()
print(pos)
print(neg)

