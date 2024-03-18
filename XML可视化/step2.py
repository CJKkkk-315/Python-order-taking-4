import re
from step1 import preprocessLine


class Parser(object):
    # 初始化Parser实例
    def __init__(self, inputString):
        self.inputString = inputString

    # 重写str方法
    def __str__(self):
        return ','.join([self.getID(), self.getPostType(), self.getDateQuarter(), self.getCleanedBody()])

    # 通过re提取id
    def getID(self):
        return re.findall('Id="(.*?)"', self.inputString)[0]

    # 通过re提取问答类型
    def getPostType(self):
        postid = re.findall('PostTypeId="(.*?)"', self.inputString)[0]
        if postid == '1':
            return 'question'
        elif postid == '2':
            return 'answer'
        else:
            return 'others'

    # 通过re提取帖子时间，并通过月份判断季节
    def getDateQuarter(self):
        cd = re.findall('CreationDate="(.*?)"', self.inputString)[0]
        cd = cd.split('-')
        year = cd[0]
        s = (int(cd[1])-0.1)//3 + 1
        return year + 'Q' + str(int(s))

    # 通过第一题中的函数提取清洗完后的body
    def getCleanedBody(self):
        return preprocessLine(self.inputString)

    # 对清洗完的body按空格分割，并去除所有符号，统计词语数量
    def getVocabularySize(self):
        words_list = self.getCleanedBody().split()
        clean_words_list = set()
        for word in words_list:
            c = ''
            for i in word:
                if i.isalpha():
                    c += i
            if c:
                clean_words_list.add(c.lower())
        return len(clean_words_list)
