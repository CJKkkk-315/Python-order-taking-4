data = open('policy.txt','r',encoding='utf8').readlines()
text = ''
for i in data:
    text += i.replace('\n',' ').replace(',',' ').replace('.',' ').replace('?',' ').replace('-',' ').replace('”',' ').replace('‘',' ')\
        .replace('(',' ').replace(')',' ').replace('’',' ').replace('“',' ').replace('!',' ')
words = text.split()
stopword = [i.replace('\n','') for i in open('stop_words.txt','r',encoding='utf8').readlines()]
clean_words = []
for word in words:
    if word not in stopword:
        clean_words.append(word)
from pandas import DataFrame
from collections import Counter
fre = Counter(clean_words)
q2df = {'word':[],'frequency':[]}
q2df_sample = {'word':[],'frequency':[]}
for i in fre:
    if fre[i] > 20:
        q2df_sample['word'].append(i)
        q2df_sample['frequency'].append(fre[i])
    q2df['word'].append(i)
    q2df['frequency'].append(fre[i])
q2df = DataFrame(q2df)
q2df_sample = DataFrame(q2df_sample)
q2df_sample = q2df_sample.sort_values(by='frequency',ascending=False,ignore_index=True)
import csv
values = q2df.values.tolist()
header = ['word','frequency']
with open('Q2_words.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    for row in values:
        f_csv.writerow(row)