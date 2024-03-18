import matplotlib.pyplot as plt
from collections import Counter
import snownlp
import jieba
import numpy
from PIL import Image
import wordcloud
plt.rcParams['font.sans-serif'] = ['SimHei']
import re

content = open('longzu.txt',encoding='utf8').read()
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
posi_word = []
neg_word = []
for i in object_list:
    sc = snownlp.SnowNLP(i).sentiments
    if sc > 0.9:
        posi_word.append(i)
    elif sc < 0.1:
        neg_word.append(i)
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
wc.generate_from_frequencies(Counter(posi_word))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('前半段正面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.generate_from_frequencies(Counter(neg_word))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('前半段负面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()


object_list = []
seg_list_exact = jieba.cut(find_chinese(down_content), cut_all=False, HMM=True)
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)
posi_word = []
neg_word = []
for i in object_list:
    sc = snownlp.SnowNLP(i).sentiments
    if sc > 0.9:
        posi_word.append(i)
    elif sc < 0.1:
        neg_word.append(i)
mask = numpy.array(Image.open('1.png'))
wc = wordcloud.WordCloud(
    font_path='C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_words=280,
    max_font_size=150
)
wc.generate_from_frequencies(Counter(posi_word))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('后半段正面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

wc.generate_from_frequencies(Counter(neg_word))
wc.recolor(color_func=wordcloud.ImageColorGenerator(mask))
plt.figure('后半段负面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()

