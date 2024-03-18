# encoding=utf-8

"""

@desc:main函数，整合整个处理流程。

"""
import jena_sparql_endpoint
import question2sparql

if __name__ == '__main__':
    # TODO 连接Fuseki服务器。
    fuseki = jena_sparql_endpoint.JenaFuseki()
    # TODO 初始化自然语言到SPARQL查询的模块，参数是外部词典列表。
    q2s = question2sparql.Question2Sparql()

    while True:
        question = input()
        my_query = q2s.get_sparql(question)

        if my_query is not None:

            result = fuseki.get_sparql_result(my_query)
            value = fuseki.parse_result(result)
            print(value)
            # TODO 查询结果为空，根据OWA，回答“不知道”
            # if len(value) == 0:
            #     print('I don\'t know. :(')
            # elif len(value) == 1:
            #     print (value[0])
            # else:
            #     output = ''
            #     for v in value:
            #         output += v + "\n"
            #     print (output[0:-1])

        else:
            # TODO 自然语言问题无法匹配到已有的正则模板上，回答“无法理解”
            print ('I can\'t understand. :(')

        print ('#' * 100)
# 谁是迈克尔乔丹?
# 迈克尔乔丹的数据
# 休斯顿火箭队