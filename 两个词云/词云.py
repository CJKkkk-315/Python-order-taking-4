import matplotlib.pyplot as plt
from collections import Counter
import jieba
import wordcloud
import pandas as pd
plt.rcParams['font.sans-serif'] = ['SimHei']
cn = pd.read_excel('中文文献1.xls')
en = pd.read_excel('外文文献.xls')
data = [str(i).lower() for i in en['Abstract'].values.tolist()]
data = ' '.join(data)
object_list = []
#进行jieba分词处理，模式选择精确分词模式
seg_list_exact = data.split()
with open('stopword.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
#打开停用词文件，将分词成果去掉所有的停用词
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)

#设置词云的一些参数，字体，背景，词语数量以及词语大小等
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words=100,
    max_font_size=150
)
cc = Counter(object_list)

wc.generate_from_frequencies(cc)
plt.figure('外文词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

cc = sorted(cc.items(),key=lambda x:x[1],reverse=True)
with open('外文词频.txt','w',encoding='utf8') as f:
    for i in cc:
        f.write(i[0] + ' ' + str(i[1]) + '\n')


data = ' '.join(cn['Summary-摘要'].values.tolist())
object_list = []
#进行jieba分词处理，模式选择精确分词模式
seg_list_exact = jieba.cut(data, cut_all=False, HMM=True)
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
#打开停用词文件，将分词成果去掉所有的停用词
for word in seg_list_exact:
    if word not in stopwords and len(word) >= 2:
        object_list.append(word)

#设置词云的一些参数，字体，背景，词语数量以及词语大小等
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    max_words=100,
    max_font_size=150
)
cc = Counter(object_list)

wc.generate_from_frequencies(cc)
plt.figure('中文词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

cc = sorted(cc.items(),key=lambda x:x[1],reverse=True)
with open('中文词频.txt','w') as f:
    for i in cc:
        f.write(i[0] + ' ' + str(i[1]) + '\n')