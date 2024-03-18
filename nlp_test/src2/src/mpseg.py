#!usr/bin/env python
#-*- coding:utf-8 -*-

import math
from src.dag import DAG
from src.base import BaseSegment


class MPSegment(BaseSegment):
    def __init__(self, file: str = '../data/dict.txt'):
        super(MPSegment, self).__init__()
        self.load_dict(file)

    def dp(self, sentence, dag, dp):
        n = len(sentence)
        dp[n] = (0, 0)
        log_total = math.log(self.trie.total_word_freq)
        for idx in range(n - 1, -1, -1):
            dp[idx] = max((math.log(self.trie.get_freq(sentence[idx:x + 1]) or 1) -
                           log_total + dp[x + 1][0], x) for x in dag.get(idx))

    def cut(self, sentence):
        if sentence is None or len(sentence) == 0:
            return []

        dag = DAG(sentence, self.trie)
        dp = {}
        self.dp(sentence, dag, dp)
        n = len(sentence)
        x = 0
        while x < n:
            y = dp[x][1] + 1
            word = sentence[x:y]
            x = y
            yield word


if __name__ == '__main__':
    text = '南京市长江大桥上的汽车'
    segment = MPSegment()
    print(' '.join(segment.cut(text)))