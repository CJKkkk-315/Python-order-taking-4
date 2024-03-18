from keras.models import load_model

model = load_model('poetry_model.hdf5')
# 诗data的地址
poetry_data_path = "poetry.txt"
# 如果诗词中出现这些词，则将诗舍弃
DISALLOWED_WORDS = ['（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']']
# 取3000个字作诗,其中包括空格字符
WORD_NUM = 3000
# 将出现少的字使用空格代替
UNKONW_CHAR = " "
# 根据前6个字预测下一个字，比如说根据“寒随穷律变，”预测“春”
TRAIN_NUM = 6
# 保存诗词
poetrys = []
# 保存在诗词中出现的字
all_word = []

with open(poetry_data_path,encoding="utf-8") as f:
    for line in f:
        # 获得诗的内容
        poetry = line.split(":")[1].replace(" ","")
        flag = True
        # 如果在句子中出现'（', '）', '(', ')', '__', '《', '》', '【', '】', '[', ']'则舍弃
        for dis_word in DISALLOWED_WORDS:
            if dis_word in poetry:
                flag = False
                break

        # 只需要5言的诗（两句诗包括标点符号就是12个字），假如少于两句诗则舍弃
        if  len(poetry) < 12 or poetry[5] != '，' or (len(poetry)-1) % 6 != 0:
            flag = False

        if flag:
            # 统计出现的词
            for word in poetry:
                all_word.append(word)
            poetrys.append(poetry)
from collections import Counter
# 对字数进行统计
counter = Counter(all_word)
# 根据出现的次数，进行从大到小的排序
word_count = sorted(counter.items(),key=lambda x : -x[1])
most_num_word,_ = zip(*word_count)
# 取前2999个字，然后在最后加上" "
use_words = most_num_word[:WORD_NUM - 1] + (UNKONW_CHAR,)
# word 到 id的映射 {'，': 0,'。': 1,'\n': 2,'不': 3,'人': 4,'山': 5,……}
word_id_dict = {word:index for index,word in enumerate(use_words)}

# id 到 word的映射 {0: '，',1: '。',2: '\n',3: '不',4: '人',5: '山',……}
id_word_dict = {index:word for index,word in enumerate(use_words)}

import numpy as np
def word_to_one_hot(word):
    """将一个字转成onehot形式

    :param word: [一个字]
    :type word: [str]
    """
    one_hot_word = np.zeros(WORD_NUM)
    # 假如字是生僻字，则变成空格
    if word not in word_id_dict.keys():
        word = UNKONW_CHAR
    index = word_id_dict[word]
    one_hot_word[index] = 1
    return one_hot_word

def phrase_to_one_hot(phrase):
    """将一个句子转成onehot

    :param phrase: [一个句子]
    :type poetry: [str]
    """
    one_hot_phrase = []
    for word in phrase:
        one_hot_phrase.append(word_to_one_hot(word))
    return one_hot_phrase
import numpy as np
def predict_next(x):

    predict_y = model.predict(x)[0]
    # 获得最大概率的索引
    index = np.argmax(predict_y)
    if(index == 2999):
       predict_y = np.delete(predict_y, index)
       index = np.argmax(predict_y)
    return index

def generate_sample_result(predict_sen):
    predict_data = predict_sen
    # 生成的4句五言诗（4 * 6 = 24）
    while len(predict_sen) < 24:
        X_data = np.array(phrase_to_one_hot(predict_data)).reshape(1,TRAIN_NUM,WORD_NUM)
        # 根据6个字符预测下一个字符
        y = predict_next(X_data)
        predict_sen = predict_sen+ id_word_dict[y]
        # “寒随穷律变，” ——> “随穷律变，春”
        predict_data = predict_data[1:]+id_word_dict[y]
    print(predict_sen)

x = "床前明月光，"
generate_sample_result(x)