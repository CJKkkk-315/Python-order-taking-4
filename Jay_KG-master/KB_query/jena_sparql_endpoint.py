# encoding=utf-8

"""

@desc:利用SOARQKWrapper向Fuseki发送SPARQL查询，解析返回的结果

"""
from random import randint

from SPARQLWrapper import SPARQLWrapper, JSON
from collections import OrderedDict


class JenaFuseki:
    def __init__(self, endpoint_url='http://localhost:3030/ds/query'):
        self.sparql_conn = SPARQLWrapper(endpoint_url)

    def get_sparql_result(self, query):
        self.sparql_conn.setQuery(query)
        self.sparql_conn.setReturnFormat(JSON)
        return self.sparql_conn.query().convert()

    @staticmethod
    def parse_result(query_result):
        """
        解析返回的结果
        :param query_result:
        :return:
        """
        try:
            if not query_result["results"]["bindings"]:
                return "No answer found"
            elif "http://baike.com/res/" in query_result["results"]["bindings"][0]["s"]["value"]:
                text = ""
                for result in query_result["results"]["bindings"]:
                    str = result["p"]["value"].strip("http://baike.com/res/") + ": " + result["o"]["value"]
                    text+=str
                return text
            else:
                result_index = randint(0, len(query_result["results"]["bindings"]) - 1)
                result = query_result["results"]["bindings"][result_index]
                return result["o"]["value"]
            # print("Result: ", result["o"]["value"])
            # query_head = query_result['head']['vars']
            # query_results = list()
            # for r in query_result['results']['bindings']:
            #     temp_dict = OrderedDict()
            #     for h in query_head:
            #         temp_dict[h] = r[h]['value']
            #     query_results.append(temp_dict)
            # return query_head, query_results
        except KeyError:
            query_result['boolean']

    # def print_result_to_string(self, query_result):
    #     """
    #     直接打印结果，用于测试
    #     :param query_result:
    #     :return:
    #     """
    #     query_result = self.parse_result(query_result)
    #     print (query_result)
        # if query_head is None:
        #     if query_result is True:
        #         print('Yes')
        #     else:
        #         print('False')
        #     print()
        # else:
        #     for h in query_head:
        #         print(h, ' '*5),
        #     print()
        #     for qr in query_result:
        #         for _, value in qr.items():
        #             print(value, ' '),
        #         print()

    def get_sparql_result_value(self, query_result):
        """
        用列表存储结果的值
        :param query_result:
        :return:
        """
        query_head, query_result = self.parse_result(query_result)
        if query_head is None:
            values = list()
            values.append(query_result)
            return values
        else:
            values = list()
            for qr in query_result:
                for _, value in qr.items():
                    values.append(value)
            return values
