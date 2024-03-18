#!usr/bin/env python
#-*- coding:utf-8 -*-

from src.base import BaseSegment
from src.fmm import FMMSegment
from src.rmm import RMMSegment


class BIMMSegment(BaseSegment):
    def __init__(self, file: str = '../data/dict.txt'):
        super(BIMMSegment, self).__init__()
        self.FMM = FMMSegment()
        self.RMM = RMMSegment()
        self.load_dict(file)

    def cut(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []
        res_fmm = [word for word in self.FMM.cut(sentence)]
        res_rmm = [word for word in self.RMM.cut(sentence)]
        if len(res_fmm) == len(res_rmm):
            if res_fmm == res_rmm:
                result = res_fmm
            else:
                f_word_count = len([w for w in res_fmm if len(w) == 1])
                r_word_count = len([w for w in res_rmm if len(w) == 1])
                result = res_fmm if f_word_count < r_word_count else res_rmm
        else:
            result = res_fmm if len(res_fmm) < len(res_rmm) else res_rmm
        for word in result:
            yield word


if __name__ == '__main__':
    text = '南京市长江大桥上的汽车'
    segment = BIMMSegment()
    print(' '.join(segment.cut(text)))