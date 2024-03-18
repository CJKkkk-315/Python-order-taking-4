import random
import re
import string
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
def parse_file(file):
    with open(file, 'r') as input:
        content = input.readlines()
    preprocessed = []
    for line in content:
        line = line.strip().lower()
        #remove punctuation
        line = line.translate(str.maketrans('', '', string.punctuation))
        #remove stop words that care no specific meaning
        line = remove_stopwords(line)
        #remove numbers
        line = re.sub('\d+','', line)
        #remove extra white space
        line = re.sub(' +', ' ', line)
        if line:
            preprocessed.extend(line.split(" "))
    # print(" ".join(preprocessed))
    return preprocessed
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stop_words])



# 闭散列（线性探测法）
class ClosedHashTable:
    def __init__(self, size=1000):
        self.size = size  # 哈希表的大小
        self.table = [[] for _ in range(size)]  # 初始化哈希表

    # 从文件中加载数据
    def load_from_file(self, file_path):
        words = parse_file(file_path)
        for word in words:
            self.insert(word)  # 插入单词

    # 哈希函数
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size  # 将单词转换为哈希值
    # 插入操作
    def insert(self, key):
        index = self.hash_function(key)  # 计算哈希值
        while self.table[index]:  # 如果当前位置已经被占用
            if self.table[index][0] == key:  # 如果是同一个单词，更新频次
                self.table[index] = (key, self.table[index][1] + 1)
                return
            index = (index + 1) % self.size  # 否则，尝试下一个位置
        self.table[index] = (key, 1)  # 插入单词

    # 查找操作
    def search(self, key):
        index = self.hash_function(key)  # 计算哈希值
        steps = 1
        while self.table[index]:  # 如果当前位置不为空
            if self.table[index][0] == key:  # 如果找到目标，返回步数
                return steps
            steps += 1
            index = (index + 1) % self.size  # 否则，尝试下一个位置
        return -1  # 如果没有找到，返回 -1


# 开散列（分离链表法）
class OpenHashTable:
    def __init__(self, size=1000):
        self.size = size  # 哈希表的大小
        self.table = [[] for _ in range(size)]  # 初始化哈希表

    # 从文件中加载数据
    def load_from_file(self, file_path):
        words = parse_file(file_path)
        for word in words:
            self.insert(word)  # 插入单词

    # 哈希函数
    def hash_function(self, key):
        return sum(ord(c) for c in key) % self.size  # 将单词转换为哈希值
    # 插入操作
    def insert(self, key):
        index = self.hash_function(key)  # 计算哈希值
        if not self.table[index]:  # 如果当前位置为空
            self.table[index] = [(key, 1)]  # 插入单词
        else:
            for i, item in enumerate(self.table[index]):  # 遍历链表
                if item[0] == key:  # 如果是同一个单词，更新频次
                    self.table[index][i] = (key, item[1] + 1)
                    return
            self.table[index].append((key, 1))  # 否则，将单词添加到链表末尾

    # 查找操作
    def search(self, key):
        index = self.hash_function(key)  # 计算哈希值
        if not self.table[index]:  # 如果当前位置为空，返回 -1
            return -1
        for i, item in enumerate(self.table[index]):  # 遍历链表
            if item[0] == key:  # 如果找到目标，返回步数
                return i + 1
        return -1   # 如果没有找到，返回 -1


def search_performance(hash_table, search_list):
    for k in search_list:
        steps = hash_table.search(k)
        print(f"Search '{k}': steps: {steps}")

if __name__ == "__main__":
    file_path = "A3test.txt"
    words = parse_file(file_path)
    k_values = [10, 20, 30, 40, 50]
    for k in k_values:
        closed_hash_table = ClosedHashTable()
        closed_hash_table.load_from_file(file_path)

        open_hash_table = OpenHashTable()
        open_hash_table.load_from_file(file_path)

        search_list = []
        while True:
            word = random.sample(words,1)[0]
            if word not in search_list:
                search_list.append(word)
                if len(search_list) == k//2:
                    break
        for i in range(k//2):
            search_list.append('UnknowWord')
        print(f"\nclosed hash table, K = {k}:")
        search_performance(closed_hash_table, search_list)

        print(f"\nopen hash table, K = {k}:")
        search_performance(open_hash_table, search_list)
