import random
# 存储全部单词
words = []
# 加载单词文件
def load_data():
    with open('data.txt',encoding='utf8') as f:
        for i in f.readlines():
            words.append(i.replace('\n','').split())
# 存储单词文件
def save_data():
    with open('data.txt','w',encoding='utf8') as f:
        for i in words:
            f.write(' '.join(i)+'\n')
# 展示所有单词
def all_word():
    if not words:
        print('当前生词本没有单词！')
        return
    for i in words:
        print(' '.join(i))
# 随机抽取单词考试
def exam_word():
    word = random.sample(words,1)[0]
    print(f'{word[0]}的中文意思是：')
    c = input()
    if c == word[1]:
        print('正确！')
    else:
        print('错误！')
# 添加单词
def add_word():
    word = input('请输入你要添加的单词：')
    c = input('请输入中文意思')
    for i in words:
        if i[0] == word:
            print('该单词已经存在！')
            return
    words.append([word,c])
    print('添加成功')
# 删除单词
def dele_word():
    word = input('请输入你要添加的单词：')
    for i in words:
        if i[0] == word:
            words.remove(i)
            print('删除成功！')
            return
    print('没有该单词！')
# 清空单词
def clean_word():
    global words
    words = []
    print('清空成功！')
# 主程序
if __name__ == '__main__':
# 开始先加载单词数据
    load_data()
# 编写菜单
    info = '''
    1.查看所有生词
    2.背单词功能
    3.添加新单词功能
    4.删除单词功能
    5.清空生词本功能
    6.退出生词本功能
    '''
# 循环读入用户选项
    while True:
        print(info)
        c = input('请输入你的选择：')
        if c == '1':
            all_word()
        elif c == '2':
            exam_word()
        elif c == '3':
            add_word()
        elif c == '4':
            dele_word()
        elif c == '5':
            clean_word()
        elif c == '6':
            break
# 退出后清空数据
    save_data()
