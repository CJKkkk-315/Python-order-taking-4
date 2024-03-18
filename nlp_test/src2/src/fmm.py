#!usr/bin/env python
#-*- coding:utf-8 -*-

from src.base import BaseSegment


class FMMSegment(BaseSegment):
    def __init__(self, file: str = '../data/dict.txt'):
        super(FMMSegment, self).__init__()
        self.load_dict(file)

    def cut(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []

        index = 0
        text_size = len(sentence)
        while text_size > index:
            word = ''
            for size in range(self.trie.max_word_len+index, index, -1):
                word = sentence[index:size]
                if self.trie.search(word):
                    index = size - 1
                    break
            index = index + 1
            yield word


if __name__ == '__main__':
    text = '南京市长江大桥上的汽车'
    segment = FMMSegment()
    print(' '.join(segment.cut(text)))
