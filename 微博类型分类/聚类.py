import pandas as pd
from bertopic import BERTopic
import jieba.posseg as pseg
import re

def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
# 读取csv文件
df = pd.read_excel("data/情感分析结果(编码中).xlsx")
# 假设你的文本在名为"发布内容"的列中
texts = df["发布内容"].tolist()
# 查看一共有多少行
print(len(texts))

print(texts)
for i in range(len(texts)):
    print(i)
    item = texts[i]
    item = find_chinese(item)
    words = pseg.cut(find_chinese(item))
    clean_word = []
    for word,pos in words:
        if word not in stopwords and pos in ['n','a','v']:
            clean_word.append(word)
    texts[i] = ' '.join(clean_word)
print(texts)
# 创建BERTopic模型
topic_model = BERTopic(embedding_model="bert-base-chinese",nr_topics=10)
# 训练模型
topics, probs = topic_model.fit_transform(texts)
# 查看首次训练的结果信息
print(topic_model.get_topic_info())
# 保存到df中
df['topics'] = topics
# 填充空值
df.fillna(0, inplace=True)
# 分别根据topics聚类求平均的转发数，评论数，点赞数
topic_average_time = df.groupby("topics")["转发数"].mean()
print(topic_average_time)

topic_average_time = df.groupby("topics")["评论数"].mean()
print(topic_average_time)

topic_average_time = df.groupby("topics")["点赞数"].mean()
print(topic_average_time)
# 将每条文本的聚类结果保存到res_df中
df.to_excel('res_df.xlsx',index=False)
# 将聚类的结果信息保存到topic_info中
df2 = topic_model.get_topic_info()
df2.to_excel('topic_info.xlsx',index=False)
# 将不平类别的平均点赞转发评论转为dataframe保存到topic_hot中
topic_average = {'点赞数':topic_average_time,'转发数':df.groupby("topics")["转发数"].mean(),'评论数':df.groupby("topics")["评论数"].mean()}
df3 = pd.DataFrame(topic_average)
df3.to_excel('topic_hot.xlsx',index=False)