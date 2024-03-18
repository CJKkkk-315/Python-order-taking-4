import matplotlib.pyplot as plt
from step2 import Parser


def visualizeVocabularySizeDistribution(inputFile, outputImage):
    # 读取xml中所有行，除了第一二和最后一行
    data = [i[:-1] for i in open(inputFile, encoding='utf8').readlines()][2:-1]
    # 初始化每一间隔的帖子数量
    draw_res = [0 for _ in range(11)]
    # 对每一行提取词汇量，并将对应区间的数量+1
    for row in data:
        p = Parser(row)
        n = p.getVocabularySize()
        draw_res[min(n//10,10)] += 1
    # 定义x轴坐标
    x = ['0-10','10-20','20-30','30-40','40-50','50-60','60-70','70-80','80-90','90-100','others']
    # 画条形图
    plt.bar(x,draw_res)
    # 设置字体大小
    plt.tick_params(labelsize=9)
    # 保存为文件
    plt.savefig(outputImage)


def visualizePostNumberTrend(inputFile, outputImag):
    # 定义问答字典，方便分类每个季度
    q_line = {}
    a_line = {}
    data = [i[:-1] for i in open(inputFile, encoding='utf8').readlines()][2:-1]
    # 循环遍历每一行
    for row in data:
        # 初始化Parser类实例
        p = Parser(row)
        # 判断帖子的问答类型，并在字典中对应季度的数量+1
        if p.getPostType() == 'question':
            q_line[p.getDateQuarter()] = q_line.get(p.getDateQuarter(),0) + 1
        elif p.getPostType() == 'answer':
            a_line[p.getDateQuarter()] = a_line.get(p.getDateQuarter(), 0) + 1
    # 将字典的键值对转换为列表
    q_line = [[i, j] for i, j in q_line.items()]
    a_line = [[i, j] for i,j in a_line.items()]
    # 对列表按照季度进行排序
    q_line.sort(key=lambda x:int(x[0].replace('Q','')))
    a_line.sort(key=lambda x: int(x[0].replace('Q','')))
    # 从列表中提取x y轴
    q_x = [i[0] for i in q_line]
    q_y = [i[1] for i in q_line]
    a_x = [i[0] for i in a_line]
    a_y = [i[1] for i in a_line]
    # 清空画布
    plt.clf()
    # 分别绘制问答曲线
    plt.plot(q_x, q_y, 'blue',label='question')
    plt.plot(a_x, a_y, 'red',label='answer')
    # 设置坐标轴字体大小
    plt.tick_params(labelsize=5)
    # 显示图例
    plt.legend()
    # 保存为文件
    plt.savefig(outputImag)


visualizeVocabularySizeDistribution('data.xml','vocabularySizeDistribution.png')
visualizePostNumberTrend('data.xml','postNumberTrend.png')