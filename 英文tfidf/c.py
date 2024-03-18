import string
from collections import Counter
import numpy as np

def tokenize(text):
    words = text.split()
    clean_words = []
    for word in words:
        while True:
            if word[0] in string.punctuation:
                word = word[1:]
            else:
                break

        while True:
            if word[-1] in string.punctuation:
                word = word[:-1]
            else:
                break
        if len(word) > 1:
            clean_words.append(word.lower())
    return Counter(clean_words)


def get_dtm(sents):
    dics = [tokenize(sent) for sent in sents]
    unique_words = set()
    for dic in dics:
        for key in dic:
            unique_words.add(key)
    unique_words = list(unique_words)
    dtm = np.zeros((len(sents),len(unique_words)))
    for i in range(len(dics)):
        for key in dics[i]:
            dtm[i,unique_words.index(key)] = dics[i][key]
    return dtm,unique_words


def analyze_dtm(dtm,words,sents):
    df = np.zeros((len(words,)))
        

sents = ["it's a !!!hello world!!!","it's a !!!hello world!!!","it's a !!!hello test"]
dtm,words = get_dtm(sents)
print(analyze_dtm(dtm,words,sents))