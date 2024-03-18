import re


def preprocessLine(inputLine):
    # 提取body中的内容
    inputLine = re.findall('Body="(.*?)"', inputLine)[0]
    # 定义需要替换的字符串列表
    retag = [['&lt;','<'],['&gt;','>'],['&apos;',"'"],['&quot;','"'],['&amp;','&']]
    # 循环替换所有
    for i in retag:
        inputLine = inputLine.replace(i[0],i[1])
    # 讲两种特殊标记替换为空格
    inputLine = inputLine.replace('&#xA;',' ')
    inputLine = inputLine.replace('&#xD;',' ')
    # 删除所有<*>标签
    pattern = re.compile(r'<[^>]+>', re.S)
    inputLine = pattern.sub('', inputLine)
    return inputLine


def splitFile(inputFile, outputFile_question, outputFile_answer):
    # 读取xml中所有行，除了第一二和最后一行
    data = [i[:-1] for i in open(inputFile,encoding='utf8').readlines()][2:-1]
    question_file = open(outputFile_question,'w',encoding='utf8')
    answer_file = open(outputFile_answer, 'w', encoding='utf8')
    # 对每一行判断问答类型，并通过preprocessLine函数处理写入txt中
    for line in data:
        if re.findall('PostTypeId="(.*?)"', line)[0] == '1':
            content = preprocessLine(line)
            question_file.write(content + '\n')
        elif re.findall('PostTypeId="(.*?)"', line)[0] == '2':
            content = preprocessLine(line)
            answer_file.write(content + '\n')

