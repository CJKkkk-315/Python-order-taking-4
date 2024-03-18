import nltk
from nltk.corpus import PlaintextCorpusReader
nltk.download('punkt')
corpus_root = 'data'
DNClist = PlaintextCorpusReader(corpus_root, '.*')
print(DNClist.fileids())

print(DNClist.sents('新建 文本文档.txt'))
print(type(DNClist))
print(str(DNClist))