import jieba
import re
# coding: utf8

'''
f0 = open('data/src_data/activity.txt', 'r', encoding='UTF-8-sig')
lines = f0.readlines()
line_set = set()
line_list = []
for line in lines:
    s = line.replace('\n', '').split('\t')
    ele = s[0]  #(s[1], s[2], s[4])
    #print(ele)
    #if ele not in loc_set:
    #    loc_set.add(ele)
    if ele not in line_set:
        line_set.add(ele)
        line_list.append(ele)
print(len(line_set), loc_set)
f2 = open('activity3.txt', 'w+', encoding='UTF-8-sig')
# for w in line_list:
#     f2.write(f'{w[0]},{w[1]},{w[2]}\n')
f3 = open('activity2.txt', 'w+', encoding='UTF-8-sig')
for w in line_list:
    f3.write(f'{w}\n')
print('end...')
'''


name_list = ['activity2', 'merchant_life3', 'func', 'merchant_bill4', 'product']
word = {}  # 分词后所有单词组成的词频字典
stop_words = ('的', '我')
N = len(name_list)

for id_part in range(N):
    name = name_list[id_part]
    f1 = open(f'data/src_data/{name}.txt', 'r', encoding='UTF-8-sig')
    data1 = f1.read()
    #f1.seek(0)
    f1.close()

    print('开始分词')
    seg = jieba.cut(data1, cut_all=True)
    #seg = jieba.cut(data1)
    #print(seg)
    #print('/'.join(seg))
    print('分词结束')

    for s in list(seg):
        #print("s:",s)
        if len(s)==0:
            continue;
        if (s[0]>= '\u4e00' and s[0] <= '\u9fa5') or (u'0' <= s[0] <= u'9')  or ((u'\u0041' <= s[0] <= u'\u005a') or (u'\u0061' <= s[0] <= u'\u007a')):  #中文、数字、英文
            if s in word:
                word[s]+=1
            else:
                word[s] = 1
    print(f'{id_part}、截至当前的分词的数量：{len(word)}')

for sw in stop_words:
    if sw in word:
        word.pop(sw)

# my_dict_set = set(open(f'data/src_data/my_dict.txt', 'r', encoding='UTF-8-sig').read().split('\n'))
# for w in my_dict_set:
#     if w not in word:
#         word[w] = 1

f2 = open(f'data/dict/dict_all_0720.txt', 'w+', encoding='UTF-8-sig')  # all模式的分词
#提取完关键词后输出写出到文件
for w in word:
    f2.write(w+' '+str(word[w])+'\n')
f2.close()
print(f'所有文档的分词的数量：{len(word)}')

for id_part in range(N):
    name = name_list[id_part]
    f1 = open(f'data/src_data/{name}.txt', 'r', encoding='UTF-8-sig')
    lines = f1.readlines()
    f1.close()

    seg_list = []
    db_list = []
    line_set = set()
    for line in lines:
        line2 = line.replace('\n', '')
        line_set.add(line2)
        db_list.append(line2)
        seg = list(jieba.cut(line2, cut_all=True))
        #seg = list(jieba.cut(line2))
        # print('/'.join(seg))
        seg_list.append(seg)  # 分词后的关键词列表
   #print('seg_list:', seg_list) #所有
    # print(db_list, line_set)


    print('开始建立倒索引')
    idx = 0  #每个文档的id
    inv_index_data = {}  # 倒索引
    for seg in seg_list:
        # print(idx, seg)
        for w in seg:
            if w in word:  # 不在关键词的词典里，不用记
                if w in inv_index_data:
                    inv_index_data[w].append(idx)
                else:
                    inv_index_data[w] = [idx]
        idx += 1
    #print(inv_index_data)
    #print('建立倒排索引完毕')

    f3 = open(f'data/inv_index/inv_index_{name}_0720.txt', 'w+', encoding='UTF-8-sig')
    for w in inv_index_data:
        f3.write(w + ':')
        # print(w+':')
        L = len(inv_index_data[w])
        for i in range(L):
            id_title = inv_index_data[w][i]
            f3.write( f'{id_title},')
        f3.write('\n')
    f3.close()


'''
#输入查询词，inv是倒排序文档，db是所有文档的列表，要从db里找到名字的id。
def query(q, inv_index_data, db_list):
    sub_query = list(jieba.cut(q))  #这里把list换成set，关键词的词频就会被忽略掉
    print(sub_query)
    q_reslt = {}
    for sub in sub_query:  #每个查询词的分词
        if sub in inv_index_data:
            L1_ID = inv_index_data[sub]  #某个分词命中的文档列表
            for id in L1_ID:
                if id in q_reslt:
                    q_reslt[id] += 1.0  #每命中一个关键词，加1分
                else:
                    q_reslt[id] = 1.0
    for k in q_reslt:
        if db_list[int(k)]==q:   #两者完全相同，加1分
            q_reslt[k]+=1
    q_reslt_sorted = sorted(q_reslt.items(), key=lambda x: x[1], reverse=True)
    return q_reslt_sorted


q = '幼儿园'

r = query(q, inv_index_data, db_list)
print('结果共有几个：', len(r))
for s in r:
    id = int(s[0])
    score = s[1]
    print(id, db_list[id], score)
'''

'''
def merge_dict():
    name_list = ['activity2', 'merchant_life3', 'func', 'merchant_bill3']
    dict_merge = {}
    for id in range(4):
        name2 = name_list[id]
        path_dict = f'data/dict/dict_{name2}.txt'
        print(path_dict)
        f1 = open(path_dict, 'r', encoding='UTF-8-sig')
        lines = f1.readlines()
        for line in lines:
            sub = line.split(' ')
            w = sub[0]
            n = int(sub[1])
            #print(sub)

            if w in dict_merge:
                dict_merge[w]+=n
            else:
                dict_merge[w] = n
            if w == '转账':
                w = w
                print(w, dict_merge[w])
    print('L1:', len(dict_merge), dict_merge)

    f2 = open('data/dict/dict_merge.txt', 'w+', encoding='UTF-8-sig')
    for w in dict_merge:
        n = dict_merge[w]
        f2.write(w + ' ' + str(n)+'\n')
    return dict_merge

dict_merge = merge_dict();

'''


'''
####这段是缴费商户的地区名词专门处理
f1 = open(f'data/src_data/merchant_bill3.txt', 'r', encoding='UTF-8-sig')
lines = f1.readlines()
f1.close()
f4 = open(f'data/src_data/merchant_bill4.txt', 'w+', encoding='UTF-8-sig')

loc_set = set()  # 分词后所有单词组成的词频字典
merch_set = set()
for line in lines:
    subs = line.replace('\n', '').split(',')
    type = subs[0]
    merch = subs[1]
    loc = subs[2]
    loc_set.add(loc)
    merch2 = type+','+merch
    if merch2 not in merch_set:
        merch_set.add(merch2)
    f4.write(f'{type},{merch}\n')

#os.pause()


idx = 0
dict_loc = {}
for line in lines:
    subs = line.replace('\n', '').split(',')
    type = subs[0]
    merch = subs[1]
    loc = subs[2]
    if loc in dict_loc:
        dict_loc[loc].append(idx)
    else:
        dict_loc[loc] = [idx]
    idx+=1

print('dict_loc:', dict_loc)


f4.close()
print(len(loc_set), loc_set)

f3 = open(f'data/inv_index/loc_0720.txt', 'w+', encoding='UTF-8-sig')
f4 = open(f'data/inv_index/loc_inv_index_0720.txt', 'w+', encoding='UTF-8-sig')

for loc in loc_set:
    f3.write(loc+',')
    f4.write(loc+':')
    id_list = dict_loc[loc]
    for id in id_list:
        f4.write(str(id) + ',')
    f4.write('\n')
f3.close()
f4.close()
#####这段结束
'''
