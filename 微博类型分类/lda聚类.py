import gensim
from gensim import corpora
import jieba
import pandas as pd
import re

# 聚类数量
num_topics = 30
# eta越小,一个主题可能更偏向于只包含少数词汇
eta = 10
# 随机数
random_state = 88
# 每个聚类输出的词数量
num_words = 5


def find_chinese(file):
    pattern = re.compile(r'[^\u4e00-\u9fa5]')
    chinese = re.sub(pattern, '', file)
    return chinese
def preprocess(text, stop_words):
    text = text.replace('北京','').replace('上海','').replace('深圳','').replace('广州','').replace('微博','').replace('视频','')
    tokens = jieba.cut(text)
    tokens = [t for t in tokens if t not in stop_words]
    return tokens

df = pd.read_excel("data/情感分析结果(编码中).xlsx")
texts = df["发布内容"].tolist()
texts = [find_chinese(i) for i in texts]
with open('停用词库.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
# stopwords.add('北京')
# stopwords.add('上海')
# stopwords.add('深圳')
# stopwords.add('广州')
# stopwords.add('微博')
# stopwords.add('视频')
# stopwords.add('好')

texts = [preprocess(text, stopwords) for text in texts]

dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=30, eta=10, random_state=88)

def print_topics(lda_model, num_words):
    for idx, topic in lda_model.show_topics(formatted=False, num_topics=30, num_words=num_words):
        print(f"Topic {idx}:")
        topic_words = [word for word, _ in topic]
        print(", ".join(topic_words))
        print("\n")

print_topics(lda_model, num_words)


def assign_topic_to_text(new_text, lda_model, dictionary):
    # preprocessed_text = preprocess(new_text, stop_words)

    bow_vector = dictionary.doc2bow(new_text)

    topic_distribution = lda_model[bow_vector]

    main_topic, score = max(topic_distribution, key=lambda tup: tup[1])

    return main_topic, score

ct = []
for text in texts:
    main_topic, score = assign_topic_to_text(text, lda_model, dictionary)
    ct.append(main_topic)
from collections import Counter
print(Counter(ct))
