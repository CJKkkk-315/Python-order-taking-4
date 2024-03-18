import requests
from bs4 import BeautifulSoup
import warnings
warnings.filterwarnings('ignore')
import jieba
import wordcloud
from collections import Counter
import matplotlib.pyplot as plt
res_str = ''
for i in range(32,0,-1):
    res = requests.get(f'https://news.swufe.edu.cn/zhxw/{i}.htm')
    soup = BeautifulSoup(res.text)
    a = soup.find_all(class_='jiequ')
    for j in a:
        sub_url = 'https://news.swufe.edu.cn/'
        sub_res = requests.get(sub_url + j['href'])
        sub_res.encoding = 'utf-8'
        sub_soup = BeautifulSoup(sub_res.text)
        res_str += sub_soup.find(class_='nr_c').text.replace(' ','').replace('\n','')
    break
print(res_str)
res_word = []
seg_list_exact = jieba.cut(res_str, cut_all=False, HMM=True)
for word in seg_list_exact:
    if len(word) > 2:
        res_word.append(word)
print(res_word)

wc = wordcloud.WordCloud(
        font_path='C:/Windows/Fonts/simfang.ttf',
        background_color='white',
        max_words=280,
        max_font_size=150
    )
# 生成词云
res_count = Counter(res_word)
max_word = '已下单'
res_count[max_word] = max([i for i in res_count.values()]) + 10
wc.generate_from_frequencies(res_count)
plt.figure('词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis('off')
plt.show()