import pandas as pd
import matplotlib.pyplot as plt
import random
import jieba
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('满江红影评.xlsx')
yy = []
dy = []
tc = []
for k,v in df.iterrows():
    content = v['短评'] + v['小标题']
    if '演员' in content:
        yy.append(v['星级'])
    if '导演' in content:
        dy.append(v['星级'])
    if '题材' in content:
        tc.append(v['星级'])

plt.hist(yy, bins=range(1, 7), edgecolor='black', align='left', rwidth=0.8, density=True)
plt.xticks(range(1, 6))
plt.title('演员')
plt.xlabel('星级')
plt.ylabel('频率')
plt.show()
plt.hist(dy, bins=range(1, 7), edgecolor='black', align='left', rwidth=0.8, density=True)
plt.xticks(range(1, 6))
plt.title('导演')
plt.xlabel('星级')
plt.ylabel('频率')
plt.show()
plt.hist(tc, bins=range(1, 7), edgecolor='black', align='left', rwidth=0.8, density=True)
plt.xticks(range(1, 6))
plt.title('题材')
plt.xlabel('星级')
plt.ylabel('频率')
plt.show()

# 统计不同星级的评价数量
counts = df['星级'].value_counts().sort_index()

# 绘制柱状图
plt.bar(counts.index, counts.values)
plt.xlabel('星级')
plt.ylabel('评价数量')
plt.title('评价数量分布')
plt.show()


# 计算所有评价的平均星级
average_rating = df['星级'].mean()
print('平均评分:', average_rating)


from wordcloud import WordCloud
import jieba

# 将所有的评论内容连接成一个长字符串
text = ' '.join(df['短评'])

# 使用jieba进行分词
seg_list = jieba.cut(text, cut_all=False)
seg_text = ' '.join([i for i in seg_list if len(i) >= 2])

# 创建词云
wordcloud = WordCloud(font_path='simhei.ttf').generate(seg_text)

# 展示词云图
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()


# 首先，确保发布时间是datetime类型
df['发布时间'] = pd.to_datetime(df['发布时间'])

# 按月份统计评价数量
monthly_reviews = df.resample('M', on='发布时间', closed='right').size()
# 绘制折线图
plt.plot(monthly_reviews.index, monthly_reviews.values)
plt.xlabel('时间')
plt.ylabel('评价数量')
plt.title('评价时间趋势')
plt.show()




