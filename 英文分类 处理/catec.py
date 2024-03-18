import csv
import time
import re
from gensim import corpora, models, similarities
data = []
with open('PERMNO_dt.csv',encoding='utf8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        data.append(i[1])
data = data[1:]
data_o = []
for i in data:
    if i not in data_o:
        data_o.append(i)
data = data_o[:]

query = []
d = {}
with open('patent_latest_owner_dt.csv',encoding='utf8') as f:
    f_csv = csv.reader(f)
    for i in f_csv:
        if i[8] == '2010':
            d[re.sub('[^a-zA-Z]',' ',i[2])] = ''
for i in d:
    query.append(i)

texts = []
for i in data:
    content = i[0]
    texts.append(content)
texts = [text.split() for text in texts]
dictionary = corpora.Dictionary(texts)
feature_cnt = len(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]
tfidf = models.TfidfModel(corpus)
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)

res = []

for i in query:
    m = 0
    t = -1
    keyword = i
    kw_vector = dictionary.doc2bow(keyword.split())
    for j in range(len(index[tfidf[kw_vector]])):
        pp = index[tfidf[kw_vector]][j]
        if pp > m and pp > 0:
            m = pp
            t = j
    if t == -1:
        rr = 'None'
    else:
        rr = data[t]
    res.append([keyword,rr])
    print(keyword,'||',rr)
    time_tuple = time.localtime(time.time())
    now_time = str(time_tuple[3]) + '.' + str(time_tuple[4]) + '.' + str(time_tuple[5])
    print(now_time)
with open('res.csv','w',encoding='utf8',newline='') as f:
    f_csv = csv.writer(f)
    for i in res:
        f_csv.writerow(i)
