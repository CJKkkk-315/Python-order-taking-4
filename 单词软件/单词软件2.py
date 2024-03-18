import random
# 循环print打印所有单词
def printw():
    if len(data) == 0:
        print('当前生词本没有单词！')
        return
    for word in data:
        print(word[0] + ' ' + word[1])
# random函数随机抽取单词检测
def check():
    word = data[random.randint(0,len(data)-1)]
    print('考核单词：' + word[0])
    ans = input('请输入中文意思：')
    if ans == word[1]:
        print('回答正确！')
    else:
        print('回答错误')
# 读取用户输入的单词存储到单词列表中
def addw():
    word = input('要添加单词的单词英文：')
    ans = input('要添加单词的中文：')
    if word in [i[0] for i in data]:
        print('该单词已经存在！')
        return
    data.append([word,ans])
    print('添加成功')
# 读取用户输入的单词从单词列表中移除
def removew():
    word = input('要删除的单词英文：')
    if word in [i[0] for i in data]:
        del data[[i[0] for i in data].index(word)]
        print('删除成功')
        return
    print('该单词不存在')
# 将单词列表中所有单词移除
def removeall():
    del data[:]
    print('清空成功！')

# 程序开始 data列表存储从文件读取的单词
data = [i.replace('\n','').split() for i in open('word.txt',encoding='utf8')]
menu = '''
1.显示所有生词
2.背单词
3.增加单词
4.删除单词
5.清空单词
6.退出
'''
# 死循环使得程序不会退出 直到用户选择退出选项
while True:
    print(menu)
    c = input('请输入选项')
    # 执行相对应的函数
    if c == '1':
        printw()
    elif c == '2':
        check()
    elif c == '3':
        addw()
    if c == '4':
        removew()
    if c == '5':
        removeall()
    if c == '6':
        break
# 存储数据
f = open('word.txt', 'w', encoding='utf8')
for i in data:
    f.write(' '.join(i) + '\n')
f.close()
