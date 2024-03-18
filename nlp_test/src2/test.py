#!usr/bin/env python  
#-*- coding:utf-8 _*-  
""" 
@author: hiyoung 
@file: Test.py 
@time: 2018/09/26
"""

import os
import jieba
import pkuseg
import thulac
from snownlp import SnowNLP
from src.fmm import FMMSegment
from src.rmm import RMMSegment
from src.bimm import BIMMSegment
from src.mmseg import MMSegment
from src.mpseg import MPSegment
from src.hmm import HMMSegment
from src.score import prf_score


def load_data(file):
    if not os.path.exists(file):
        return []
    result = []
    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            result.append(line)
    return result


if __name__ == '__main__':

    # train = []
    # train_path = '../data/corpus/train/'
    # for file in os.listdir(train_path):
    #     train.extend(load_data(train_path + file))
    # print(train[0])
    # print(len(train))
    #
    # test = []
    # test_path = '../data/corpus/val/test/'
    # for file in os.listdir(test_path):
    #     test.extend(load_data(test_path + file))
    # print(test[0])
    # print(len(test))
    #
    # gold = []
    # gold_path = '../data/corpus/val/gold/'
    # for file in os.listdir(gold_path):
    #     gold.extend(load_data(gold_path + file))
    #
    # print(gold[0])
    # print(len(gold))
    #
    # print('====== FMM =======')
    # pre1 = []
    # fmm = FMMSegment()
    # for sentence in test:
    #     pre1.append(' '.join([word for word in fmm.cut(sentence)]))
    # prf_score(pre1, gold)
    #
    # print('====== RMM =======')
    # pre2 = []
    # rmm = RMMSegment()
    # for sentence in test:
    #     pre2.append(' '.join([word for word in rmm.cut(sentence)]))
    # prf_score(pre2, gold)
    #
    # print('====== BIMM =======')
    # pre3 = []
    # bimm = BIMMSegment()
    # for sentence in test:
    #     pre3.append(' '.join([word for word in bimm.cut(sentence)]))
    # prf_score(pre3, gold)
    #
    # print('====== MMSEG =======')
    # pre4 = []
    # mmseg = MMSegment()
    # for sentence in test:
    #     pre4.append(' '.join([word for word in mmseg.cut(sentence)]))
    # prf_score(pre4, gold)
    #
    # print('====== MPSEG =======')
    # pre5 = []
    # mpseg = MPSegment()
    # for sentence in test:
    #     pre5.append(' '.join([word for word in mpseg.cut(sentence)]))
    # prf_score(pre5, gold)
    #
    # # text = u'虽然初步检测结果显示，姐姐的样本呈阴性，但医生仍怀疑她感染了禽流感，而弟弟则被确认感染了＜Ｅｎｇｌｉｓｈ＞Ｈ＜／Ｅｎｇｌｉｓｈ＞五＜Ｅｎｇｌｉｓｈ＞Ｎ＜／Ｅｎｇｌｉｓｈ＞一型高致病性禽流感病毒。'
    # print('====== HMM =======')
    # pre6 = []
    # hmm = HMMSegment()
    # hmm.train(train)
    # for sentence in test:
    #     pre6.append(' '.join([word for word in hmm.cut(sentence)]))
    # prf_score(pre6, gold)
    #
    # print('====== jieba =======')
    # pre7 = []
    # for sentence in test:
    #     pre7.append(' '.join([word for word in jieba.cut(sentence)]))
    # prf_score(pre7, gold)
    #
    # print('====== SnowNLP =======')
    # pre8 = []
    # for sentence in test:
    #     if not sentence or len(sentence) == 0:
    #         continue
    #     s = SnowNLP(sentence)
    #     pre8.append(' '.join([word for word in s.words]))
    # prf_score(pre8, gold)
    #
    # print('====== pkuseg =======')
    # pre9 = []
    # seg = pkuseg.pkuseg()
    # for sentence in test:
    #     pre9.append(' '.join([word for word in seg.cut(sentence)]))
    # prf_score(pre9, gold)
    #
    # print('====== thulac =======')
    # pre10 = []
    # thu_lac = thulac.thulac(seg_only=True)
    # for sentence in test:
    #     pre10.append(' '.join([word for word in thu_lac.cut(sentence, text=True)]))
    # prf_score(pre10, gold)

    gold = load_data('../data/msr.txt')
    test = load_data('../data/test_msr.txt')
    #
    # print('====== FMM =======')
    # pre1 = []
    # fmm = FMMSegment()
    # for sentence in test:
    #     pre1.append(' '.join([word for word in fmm.cut(sentence)]))
    # prf_score(pre1, gold)
    #
    # print('====== RMM =======')
    # pre2 = []
    # rmm = RMMSegment()
    # for sentence in test:
    #     pre2.append(' '.join([word for word in rmm.cut(sentence)]))
    # prf_score(pre2, gold)
    #
    # print('====== BIMM =======')
    # pre3 = []
    # bimm = BIMMSegment()
    # for sentence in test:
    #     pre3.append(' '.join([word for word in bimm.cut(sentence)]))
    # prf_score(pre3, gold)
    #
    # print('====== MMSEG =======')
    # pre4 = []
    # mmseg = MMSegment()
    # for sentence in test:
    #     pre4.append(' '.join([word for word in mmseg.cut(sentence)]))
    # prf_score(pre4, gold)
    #
    # print('====== MPSEG =======')
    # pre5 = []
    # mpseg = MPSegment()
    # for sentence in test:
    #     pre5.append(' '.join([word for word in mpseg.cut(sentence)]))
    # prf_score(pre5, gold)
    #
    # # text = u'虽然初步检测结果显示，姐姐的样本呈阴性，但医生仍怀疑她感染了禽流感，而弟弟则被确认感染了＜Ｅｎｇｌｉｓｈ＞Ｈ＜／Ｅｎｇｌｉｓｈ＞五＜Ｅｎｇｌｉｓｈ＞Ｎ＜／Ｅｎｇｌｉｓｈ＞一型高致病性禽流感病毒。'
    # print('====== HMM =======')
    # pre6 = []
    # hmm = HMMSegment()
    # hmm.train(gold)
    # for sentence in test:
    #     pre6.append(' '.join([word for word in hmm.cut(sentence)]))
    # prf_score(pre6, gold)

    print('====== jieba =======')
    pre7 = []
    for sentence in test:
        pre7.append(' '.join([word for word in jieba.cut(sentence)]))
    prf_score(pre7, gold)

    print('====== SnowNLP =======')
    pre8 = []
    for sentence in test:
        if not sentence or len(sentence) == 0:
            continue
        s = SnowNLP(sentence)
        pre8.append(' '.join([word for word in s.words]))
    prf_score(pre8, gold)

    print('====== pkuseg =======')
    pre9 = []
    seg = pkuseg.pkuseg()
    for sentence in test:
        pre9.append(' '.join([word for word in seg.cut(sentence)]))
    prf_score(pre9, gold)

    print('====== thulac =======')
    pre10 = []
    thu_lac = thulac.thulac(seg_only=True)
    for sentence in test:
        pre10.append(' '.join([word for word in thu_lac.cut(sentence, text=True)]))
    prf_score(pre10, gold)


