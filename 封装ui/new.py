# 第四步
# coding=utf-8
import datetime
import chardet
import pandas as pd
import numpy as np
import math
from graphviz import Digraph  # 画图变量
import os
import sys
import csv
os.environ['path'] = r'C:\Program Files\Graphviz\bin'


# path路径包含文件位置和选择的行数
def function(path):
    pathSplit = path.split("&&")
    file_csv = pathSplit[0]
    # fileSuffix=""
    if "csv" in file_csv:
        filePropertiesPath = pathSplit[0].replace(".csv", ".txt")
        fileName = file_csv.replace(".csv", "").split('\\')[-1]  # 文件名为了输出的几个文件
        fileDicnationnary = file_csv.replace(".csv", "").replace(fileName, "")
    # elif "xlsx" in file_csv:
    #     filePropertiesPath = pathSplit[0].replace(".xlsx", ".txt")
    #     fileName = file_csv.replace(".xlsx", "").split('/')[-1]  # 文件名为了输出的几个文件
    #     fileSuffix="xlsx"
    # elif "xls" in file_csv:
    #     filePropertiesPath = pathSplit[0].replace(".xls", ".txt")
    #     fileName = file_csv.replace(".xls", "").split('/')[-1]  # 文件名为了输出的几个文件
    #     fileSuffix="xls"
    colNumber = int(pathSplit[1])

    #####################   自动获取获取格式信息
    def getFormat(pathFormat):
        try:
            f = open(pathFormat, 'rb')
            r = f.read()
            # 获取文本的编码方式
            f_charInfo = chardet.detect(r)

            format = f_charInfo['encoding']

            f.close()
            return format
        except:
            if f:
                f.close()

    #####数据清洗

    fileProperties = open(filePropertiesPath, "r", encoding=getFormat(filePropertiesPath))
    properties = fileProperties.read().splitlines()  # 包含所有键值对
    keysOrder = []
    propertiesMap = {}
    flag = False
    flagZero = False
    for one in properties:
        if one.strip() == "order":
            flag = True
            continue
        if one.strip() == "zero":
            flagZero = True
            continue
        if one == "":
            continue
        if one == "//":
            break
        splitArray = one.split("=")
        propertiesMap[splitArray[0]] = splitArray[1]
        keysOrder.append(splitArray[0])

    #####  解析配置文件运算符

    def readNoset(data: str, event: str):  # 无集合运算
        if data == event:
            return True
        return False

    def readUnion(data: str, event: str):  # 只有并集
        paraValue = data.split("||")
        for temp in paraValue:
            if temp == event:
                return True
        return False

    def readMix(data: str, event: str):  # 只有交集
        paraValue = data.split("&")
        count = 0
        for temp in paraValue:
            if temp in event:
                count = count + 1
        if count == len(paraValue):
            return True
        return False

    def readUnionAndMix(data: str, event: str):  # 交集并集和无集合均有
        count = 0
        paraValue = data.split("||")
        for temp in paraValue:
            if "&" in temp:
                if readMix(temp, event):
                    count = count + 1
            else:
                if readNoset(temp, event):
                    count = count + 1
        if count != 0:
            return True
        return False

    def tid_maker():  # 生成唯一字符串
        return '{0:%Y%m%d%H%M%S%f}'.format(datetime.datetime.now())

    with open(file_csv, 'r', encoding=getFormat(file_csv)) as file:
        data = csv.reader(file)
        eventsID = []
        for rows in data:
            if len(rows)==0:
                continue
            print(rows)
            event = rows[colNumber].replace(" ", "")
            if event == "#":
                eventsID.append("#")
            for action in propertiesMap.values():
                if "&" in action and "||" not in action:
                    if readMix(action, event):
                        eventsID.append(list(propertiesMap.keys())[list(propertiesMap.values()).index(action)])
                elif "||" in action and "&" not in action:
                    if readUnion(action, event):
                        eventsID.append(list(propertiesMap.keys())[list(propertiesMap.values()).index(action)])
                elif "||" in action and "&" in action:
                    if readUnionAndMix(action, event):
                        eventsID.append(list(propertiesMap.keys())[list(propertiesMap.values()).index(action)])
                else:
                    if readNoset(action, event):
                        eventsID.append(list(propertiesMap.keys())[list(propertiesMap.values()).index(action)])

    # print(eventsID)
    individual = {}
    for index, value in enumerate(eventsID):
        if value == "#":
            individual[eventsID[index - 1]] = eventsID[index + 1]  # 获得独立个体的相邻两个序列
    while "#" in eventsID:
        eventsID.remove("#")
    # print(eventsID)
    file.close()
    #############
    #####残差值计算
    eventsIDTemp = []
    nodes = len(set(eventsID))
    eventsIDtemp2 = sorted(set(eventsID))
    for c in eventsID:
        eventsIDTemp.append(eventsIDtemp2.index(c))
    freqs = np.zeros((nodes, nodes))
    for num in range(0, len(eventsIDTemp) - 1):
        if num + 1 <= len(eventsIDTemp) - 1:
            freqs[eventsIDTemp[num]][eventsIDTemp[num + 1]] = freqs[eventsIDTemp[num]][
                                                                  eventsIDTemp[num + 1]] + 1  # 相邻节点加一
    individualPd = pd.DataFrame(freqs, index=eventsIDtemp2, columns=eventsIDtemp2)
    for k, v in zip(individual.keys(), individual.values()):  # 遍历村的相邻个体行为序列
        individualPd.at[k, v] = individualPd.loc[k][v] - 1
    freqs = individualPd.values  # 将其转回数组
    rowtots = freqs.sum(axis=1)  # 行和
    coltots = freqs.sum(axis=0)  # 列和·
    ntrans = sum(rowtots)  # 元素总和
    #############

    freqsTemp = np.row_stack((freqs, coltots))  # 扩充行
    coltotsTemp = np.append(rowtots, ntrans)
    freqsTemp = np.column_stack((freqsTemp, coltotsTemp))  # 扩充列
    eventsIDtemp2.append("total")
    JNTF = pd.DataFrame(freqsTemp, index=eventsIDtemp2, columns=eventsIDtemp2)  # 扩充行列的储存
    if not flag and not flagZero:
        frequencyConversionName = fileDicnationnary + fileName + "_频率转换表_" + tid_maker() + ".xlsx"
        JNTF.to_excel(frequencyConversionName, index=True, header=True)
    ##########按照配置文件顺序出现索引

    elif flag and not flagZero:
        freqOrderByProperties = np.zeros((len(eventsIDtemp2), len(eventsIDtemp2)))
        orderByPro = []  # 按配置文件顺序的索引
        for order in keysOrder:
            if eventsIDtemp2.__contains__(order):
                orderByPro.append(order)
        orderByPro.append("total")
        JNTFOrder = pd.DataFrame(freqOrderByProperties, orderByPro, orderByPro)
        for i in eventsIDtemp2:
            for j in eventsIDtemp2:
                JNTFOrder.at[i, j] = JNTF.loc[i][j]
        frequencyConversionName = fileDicnationnary + fileName + "order_频率转换表_" + tid_maker() + ".xlsx"
        JNTFOrder.to_excel(frequencyConversionName, index=True, header=True)
    else:
        lengthZero = len(keysOrder) + 1
        freqOrderZero = np.zeros((lengthZero, lengthZero))
        keysOrderTemp = keysOrder
        keysOrderTemp.append("total")
        JNTFOrderZero = pd.DataFrame(freqOrderZero, keysOrderTemp, keysOrderTemp)
        for i in eventsIDtemp2:
            for j in eventsIDtemp2:
                JNTFOrderZero.at[i, j] = JNTF.loc[i][j]
        frequencyConversionName = fileDicnationnary + fileName + "order_zero频率转换表_" + tid_maker() + ".xlsx"
        JNTFOrderZero.to_excel(frequencyConversionName, index=True, header=True)

    # print("顺序对比")
    # print(eventsIDtemp2)
    # print(orderByPro)

    ######################
    prows = rowtots / ntrans  # probability for each row
    pcols = coltots / ntrans  # probability for each column  生成的是列表
    expfreq = np.full((nodes, nodes), -1.001)
    zadjres = expfreq
    for i in range(0, nodes):
        for j in range(0, nodes):
            expfreq[i][j] = rowtots[i] * coltots[j] / ntrans
            if (expfreq[i][j] * (1 - pcols[j]) * (1 - prows[i])) > 0:
                zadjres[i][j] = (freqs[i][j] - expfreq[i][j]) / math.sqrt(
                    expfreq[i][j] * (1 - pcols[j]) * (1 - prows[i]))
    codes_levels = sorted(set(eventsID))
    dot = Digraph(comment='行为转移关系', format="pdf",
                  edge_attr={"style": 'dashed', "arrowhead": 'empty', "splines": 'spline'},
                  node_attr={"fontname": "FANGSONG"})
    # """绘制边"""
    #########残差值输出

    df = pd.DataFrame(zadjres, index=codes_levels, columns=codes_levels)  # 将数组存入DF数据结构
    if not flag and not flagZero:
        outputpath = fileDicnationnary + fileName + "_残差表_" + tid_maker() + ".xlsx"
        df.round(2).to_excel(outputpath, index=True, header=True)
        dfTemp = df.where(df > 1.96)
        dfTemp.dropna(axis=0, how='all', inplace=True)
        dfTemp.dropna(axis=1, how='all', inplace=True)  # 删除行列没有1.96的行列
        outputpath = fileDicnationnary + fileName + "_残差表大于1.96_" + tid_maker() + ".xlsx"
        dfTemp.round(2).to_excel(outputpath, index=True, header=True)
    #################按照配置输出
    elif flag and not flagZero:
        freqOrderByPro = np.zeros((len(codes_levels), len(codes_levels)))
        orderByPro.pop()
        dfOrder = pd.DataFrame(freqOrderByPro, index=orderByPro, columns=orderByPro)
        # print(dfOrder)
        for i in codes_levels:
            for j in codes_levels:
                dfOrder.at[i, j] = df.loc[i][j]
        outputpath = fileDicnationnary + fileName + "order_残差表_" + tid_maker() + ".xlsx"
        dfOrder.round(2).to_excel(outputpath, index=True, header=True)
        dfOrder = dfOrder.where(df > 1.96)  # 删除小于1.96的
        dfOrder.dropna(axis=0, how='all', inplace=True)
        dfOrder.dropna(axis=1, how='all', inplace=True)  # 删除行列没有1.96的行列
        outputpath = fileDicnationnary + fileName + "order_残差表大于1.96_" + tid_maker() + ".xlsx"
        dfOrder.round(2).to_excel(outputpath, index=True, header=True)
    #############
    else:
        keysOrder.pop()
        freqOrderZero = np.zeros((len(keysOrder), len(keysOrder)))
        dfOrderZero = pd.DataFrame(freqOrderZero, index=keysOrder, columns=keysOrder)
        for i in codes_levels:
            for j in codes_levels:
                dfOrderZero.at[i, j] = df.loc[i][j]
        outputpath = fileDicnationnary + fileName + "order_zero残差表_" + tid_maker() + ".xlsx"
        dfOrderZero.round(2).to_excel(outputpath, index=True, header=True)
        dfOrderZero = dfOrderZero.where(df > 1.96)
        outputpath = fileDicnationnary + fileName + "order_zero残差表大于1.96_" + tid_maker() + ".xlsx"
        dfOrderZero.round(2).to_excel(outputpath, index=True, header=True)
    row_events = df.keys().values.tolist()
    for row_event in row_events:
        for line_event in df.columns.values:
            value = df.round(2).loc[row_event, line_event]  # 将残差值保留2位小数
            if value >= 1.96:  # 选择符合条件的Z-score阈值   本来应为1.96
                first_event = str(row_event)
                second_event = str(line_event)
                str_value = str(value)
                dot.edge(first_event, second_event, str_value, fontname="Microsoft YaHei")  # 画图
                ################
    pdfName = fileDicnationnary + fileName + "_行为转换图_" + tid_maker()
    dot.view(filename=pdfName)
    sys.exit(0)


if __name__ == '__main__':
    function('E:\PYTHON接单4\封装ui\导出的匹配好的数据\G1\G1A.csv&&0')
