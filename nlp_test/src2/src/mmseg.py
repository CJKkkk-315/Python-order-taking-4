#!usr/bin/env python
#-*- coding:utf-8 -*-

"""
    MMSeg: mmseg分词算法
"""


from src.chunk import Chunk
from src.base import BaseSegment


class MMSegment(BaseSegment):

    def __init__(self, file: str = '../data/dict.txt', chunk_num: int = 3):
        super(MMSegment, self).__init__()
        self.load_dict(file)
        self.chunk_num = chunk_num

    def get_chunks(self, sentence: str) -> list:
        result = []

        def iter_chunk(sub_sentence, num, tmp_seg_words):
            if (len(sub_sentence) == 0 or num == 0) and tmp_seg_words:
                result.append(Chunk(tmp_seg_words, [self.trie.get_freq(x) for x in tmp_seg_words]))
            else:
                match_words = self.match_all(sub_sentence)
                for word in match_words:
                    iter_chunk(sub_sentence[len(word):], num - 1, tmp_seg_words + [word])

        iter_chunk(sentence, num=self.chunk_num, tmp_seg_words=[])
        return result

    def match_all(self, sentence: str) -> list:
        words = []
        for i in range(len(sentence)):
            word = sentence[0:i+1]
            if self.trie.search(word):
                words.append(word)
        if len(words) == 0:
            words.append(sentence[0])
        return words

    def cut(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []

        while sentence:
            chunks = self.get_chunks(sentence)
            word = max(chunks).words[0]
            sentence = sentence[len(word):]
            yield word


if __name__ == '__main__':
    text = '南京市长江大桥上的汽车'
    segment = MMSegment()
    print(' '.join(segment.cut(text)))
