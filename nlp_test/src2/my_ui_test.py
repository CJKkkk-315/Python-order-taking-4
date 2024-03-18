#!usr/bin/env python
# -*- coding:utf-8 -*-

from src.base import BaseSegment
import time


class FMMSegment(BaseSegment):
    def __init__(self, file_dict_lines):
        super(FMMSegment, self).__init__()
        self.load_dict(file_dict_lines)

    def cut(self, sentence: str):
        if sentence is None or len(sentence) == 0:
            return []

        index = 0
        text_size = len(sentence)
        while text_size > index:
            word = ''
            for size in range(self.trie.max_word_len + index, index, -1):
                word = sentence[index:size]
                if self.trie.search(word):
                    index = size - 1
                    break
            index = index + 1
            yield word
def allf(text):
    # ['func', 'product', 'merchant_bill3', 'merchant_life3', 'activity2'], ['功能', '产品', '缴费', '生活', '活动']
    name_list = ['func', 'product', 'merchant_bill3', 'merchant_life3', 'activity2']  # 原始文档标题
    name_list2 = ['func', 'product', 'merchant_bill4', 'merchant_life3', 'activity2']  # 缴费把城市去掉，倒索引文档所在
    name_chinese = ['功能', '产品', '缴费', '生活', '活动']
    N = len(name_list)
    doc_list = [[], [], [], [], []]
    inv_index = [{}, {}, {}, {}, {}]  # 都是二维数组
    loc_set = set()
    dict_loc = {}
    similar_words_dict = {}
    similar_words_list = []
    file_dict_lines = 0





    def read_similar_words():  # 输入一个词语，返回的是该词的近义词的集合
        nonlocal similar_words_dict, similar_words_list
        f1 = open('../data/similar_words.txt', 'r', encoding='UTF-8-sig')
        lines = f1.readlines()
        for line in lines:
            sub = line.replace('\n', '').split(':')
            id = sub[0]
            words = set(sub[1].split(','))  # 近义词的集合
            # print(id, words)
            similar_words_list.append(words)
            for w in words:
                if w not in similar_words_dict:
                    similar_words_dict[w] = id
        # print(similar_words_dict, similar_words_list)


    def get_similar(word):  # 输入一个词语，返回的是该词的近义词的集合
        nonlocal similar_words_dict, similar_words_list
        id = int(similar_words_dict[word])
        sim_words = similar_words_list[id].copy()
        # print('sim_words:', word, sim_words)
        sim_words.remove(word)
        return sim_words


    def init():
        nonlocal inv_index, name_list, doc_list, loc_set, dict_loc, file_dict_lines, N
        # name = 'merchant_life3'
        path_dict = f'../data/dict/dict_all_0720.txt'
        file_dict = open(path_dict, 'r', encoding='UTF-8-sig')
        file_dict_lines = file_dict.readlines()
        file_dict.close()

        path_loc = f'../data/inv_index/loc_0716.txt'
        loc_set = set(open(path_loc, 'r', encoding='UTF-8-sig').read().split(',')[0:-1])  # 最后一个为空，舍弃掉
        # print('data_loc:', loc_set)

        for id in range(N):
            name = name_list[id]
            name_inv = name_list2[id]
            path_src_data = f'../data/src_data/{name}.txt'
            path_inv = f'../data/inv_index/inv_index_{name_inv}_0720.txt'
            lines1 = open(path_inv, 'r', encoding='UTF-8-sig').readlines()
            for line in lines1:
                split_subs1 = line.split(':')
                word = split_subs1[0]
                id_data = split_subs1[1].split(',')[:-1]  # 最后一个为空，舍弃掉
                inv_index[id][word] = id_data
                # print(word, id_data)
            # print(inv_index)
            lines2 = open(path_src_data, 'r', encoding='UTF-8-sig').readlines()
            for line in lines2:
                word = line.replace('\n', '')
                doc_list[id].append(word)
        # print('文档列表doc_list:', doc_list)

        read_similar_words()

        path_loc_set = '../data/inv_index/loc_inv_index_0716.txt'
        lines = open(path_loc_set, 'r', encoding='UTF-8-sig').readlines()
        for line in lines:
            split_subs = line.split(':')
            loc = split_subs[0]
            id_data = split_subs[1].split(',')[:-1]  # 最后一个为空，舍弃掉
            dict_loc[loc] = id_data
        # print('dict_loc:', dict_loc)


    def app_segment(q):  # 分词函数，输入为q
        # path_dict = f'../data/dict/dict_all_0716.txt'
        stop_words = ('的', '我', '在', '怎么', '要')  # 停用词
        num = 0  # 除去近义词以外的关键词个数
        sub_query = list((FMMSegment(file_dict_lines).cut(q)))  # 分词结果
        sub_query2 = sub_query.copy()
        num = len(sub_query2)
        for ele in sub_query:
            if ele in stop_words:
                sub_query2.remove(ele)  # 去掉停用词
                num -= 1
        for ele in sub_query:
            if ele in similar_words_dict:
                similar_words = list(get_similar(ele))
                sub_query2 += similar_words
        # print('query分词结果sub_query:', sub_query2)

        return sub_query2, num


    # q是输入查询词，inv是倒索引文档，db_list是所有文档的列表，要从db_list里找到名字的id。
    def query(seg_q, num, inv_index, db_list, id_part):
        q_score = {}  # 结果字典，key是文档id，value是分数
        q_word = {}  # key是文档id，v是命中的关键词列表
        loc_sel_set = set()
        for sub in seg_q:  # 每个查询词的分词
            loc_sel_set1 = set()
            loc_sel_set2 = set()
            if sub in dict_loc:
                loc_sel_set.update(set(dict_loc[sub]))  # 通过城市条件筛选的集合
            if (sub + '市') in dict_loc:
                loc_sel_set.update(set(dict_loc[sub + '市']))
        if len(loc_sel_set) == 0:  # 检索词里没有地址则默认为北京
            loc_sel_set = set(dict_loc['北京'])

        id_sub = 0

        for sub in seg_q:  # 每个查询词的分词
            id_sub += 1

            if (name_list[id_part] == 'merchant_bill3') and (
                    sub in dict_loc or (sub + '市') in dict_loc):  # 搜索生活缴费时，需把地区从分词列表中滤掉。
                continue;
            if sub in inv_index:  # 在倒索引里
                L1_ID = inv_index[sub]  # 某个分词命中的文档列表
                for id in L1_ID:  # id是文档也就是标题的id
                    if (name_list[id_part] == 'merchant_bill3' and id in loc_sel_set) or (
                            name_list[id_part] != 'merchant_bill3'):  # id_part == 3表示属于缴费类型，做特殊处理
                        if id in q_score:
                            if id_sub <= num:
                                q_score[id] += 1.0  # 每命中一个关键词，加1分
                            else:
                                q_score[id] += 0.8  # 每命中一个关键词，加1分
                            q_word[id].add(sub)
                        else:
                            if id_sub <= num:
                                q_score[id] = 1.0
                            else:
                                q_score[id] = 0.8
                            q_word[id] = {sub}

        for k in q_score:
            if int(k) <= len(db_list) - 1 and db_list[int(k)] == q:  # 两者完全相同，加1分
                q_score[k] *= 5
        q_score_sorted = sorted(q_score.items(), key=lambda x: x[1], reverse=True)  # 最多返回100个
        # print('id_part, q_score_sorted, q_word:', id_part, q_score_sorted, q_word)
        return q_score_sorted, q_word  # 输出是结果、分数、命中的关键词列表

    uires = [[] for _ in range(5)]
    q = text

    init()  # 初始化，加载各种文件

    start_time = time.time()  # 程序开始时间

    for i in range(10):  # 循环十遍，计算平均时间
        res = app_segment(q)  # 分词的结果和个数
        seg_q = res[0]
        num = res[1]
    # print('seg_q, num:', seg_q, num)

    for id_part in range(N):  # 对N类文档循环。分好词后，匹配几乎不耗时间
        R = query(seg_q, num, inv_index[id_part], doc_list[id_part], id_part)
        r = R[0]
        w = R[1]
        name_ch = name_chinese[id_part]
        num = 1
        for s in r:
            id = int(s[0])
            score = s[1]
            key_word = w[s[0]]
            if id <= len(doc_list[id_part]) - 1:
                uires[id_part].append([num, doc_list[id_part][id], key_word])  # 输出序号、文档内容、命中的关键词
            num += 1
    return uires

    # end_time = time.time()  # 程序结束时间
    # run_time = end_time - start_time  # 程序的运行时间，单位为秒
    # print('run_time:', run_time * 100)











