from refo import finditer, Predicate, Star, Any, Disjunction
import re
import jieba.posseg as pseg
from random import randint
from SPARQLWrapper import SPARQLWrapper, JSON
SPARQL_PREXIX = """
PREFIX res: <http://baike.com/resource/>
PREFIX info: <http://baike.com/info/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
"""
SPARQL_TEM = "{preamble}\n" + \
             "SELECT {select} WHERE{{\n" + \
             "{expression}\n" + \
             "}}\n"

SPARQL_SELECT_TEM = u"{prefix}\n" + \
             u"SELECT {select} WHERE {{\n" + \
             u"{expression}\n" + \
             u"}}\n"
class W(Predicate):
    def __init__(self, token=".*", pos=".*"):
        self.token = re.compile(token + "$")
        self.pos = re.compile(pos + "$")
        super(W, self).__init__(self.match)

    def match(self, word):
        m1 = self.token.match(word.token)
        m2 = self.pos.match(word.pos)
        return m1 and m2


class Rule(object):
    def __init__(self, condition_num, condition=None, action=None):
        assert condition and action
        self.condition = condition
        self.action = action
        self.condition_num = condition_num

    def apply(self, sentence):
        matches = []
        for m in finditer(self.condition, sentence):
            i, j = m.span()
            matches.extend(sentence[i:j])

        return self.action(matches), self.condition_num
pos_person = "nr"
pos_song = "nz"
pos_album = "nz"

person_entity = (W(pos=pos_person))
song_entity = (W(pos=pos_song))
album_entity = (W(pos=pos_album))
person = (W(pos="nr") | W(pos="x") | W(pos="nrt"))

singer = (W("歌手") | W("歌唱家") | W("艺术家") | W("艺人") | W("歌星"))
album = (W("专辑") | W("合辑") | W("唱片"))
song = (W("歌") | W("歌曲"))

category = (W("类型") | W("种类"))
several = (W("多少") | W("几部"))

higher = (W("大于") | W("高于"))
lower = (W("小于") | W("低于"))
compare = (higher | lower)
about = W("介绍")
birth = (W("生日") | W("出生") + W("日期") | W("出生"))
birth_place = (W("出生地") | W("出生"))
english_name = (W("英文名") | W("英文") + W("名字"))
introduction = (W("介绍") | W("是") + W("谁") | W("简介"))
person_basic = (birth | birth_place | english_name | introduction)

song_content = (W("歌词") | W("歌") | W("内容"))
release = (W("发行") | W("发布") | W("发表") | W("出"))
movie_basic = (introduction | release)

when = (W("何时") | W("时候"))
where = (W("哪里") | W("哪儿") | W("何地") | W("何处") | W("在") + W("哪"))
data = (W("数据") | W("得分") | W("篮板") | W("助攻") | W("命中率") | W("犯规"))
class QuestionSet:
    def __init__(self):
        pass

    def whose_data_question(x):
        select = "?s ?p ?o"
        sparql = None
        for w in x:
            if w.pos == "nrt":
                e = f"?s ?p ?o\n" + \
                    "FILTER regex(str(?s), '" + w.token + "' ) . \n"
                for w2 in x:
                    if w2.pos == "nr":
                        e += "FILTER regex(str(?s), '" + w2.token + "' ) . \n"
                        e += "FILTER regex(str(?s), 'http://baike.com/res/') \n"
                sparql = SPARQL_TEM.format(preamble=SPARQL_PREXIX, select=select, expression=e)
                break
        return sparql


    def which_question(x):
        select = "?s ?p ?o"
        # ns2:{w.token}
        sparql = None
        for w in x:
            if w.pos == "n":
                e = f"?s info:BaiduCARD ?o\n" + \
                    "FILTER regex(str(?s), '" + w.token + "' )  \n"
                for w2 in x:
                    if w2.pos == "nr":
                        e += "FILTER regex(str(?s), '" + w2.token + "' ) . \n"
                sparql = SPARQL_TEM.format(preamble=SPARQL_PREXIX, select=select, expression=e)
                break
        return sparql

    def who_is_question_E(x):
        select = "?s ?p ?o"
        # ns2:{w.token}
        sparql = None
        for w in x:
            if w.pos == "nrt" or w.pos == "x":
                e = f"?s info:BaiduCARD ?o\n" + \
                    "FILTER regex(str(?s), '" + w.token + "' ) . \n"
                for w2 in x:
                    if w2.pos == "nr":
                        e += "FILTER regex(str(?s), '" + w2.token + "' ) . \n"
                sparql = SPARQL_TEM.format(preamble=SPARQL_PREXIX, select=select, expression=e)
                break
        return sparql

    @staticmethod
    def has_album(word_object):
        #周杰伦的专辑
        select = u"?x"
        sparql = None

        for w in word_object:
            if w.pos == pos_person:
                e = u" :{person} :release ?o."\
                    u" ?o :album_name ?x.".format(person=w.token.decode('utf-8'))
            sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                              select=select,
                                              expression=e)
            break
        return sparql
    @staticmethod
    def has_content(word_object):
        #晴天的歌词
        select = u"?o"
        sparql = None

        for w in word_object:
            if w.pos == pos_song:
                e = u" :{song} :song_content ?o.".format(song=w.token.decode('utf-8'))
            sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                              select=select,
                                              expression=e)
            break
        return sparql

    @staticmethod
    def person_inroduction(word_object):
        # 周杰伦的介绍
        select = u"?o"
        sparql = None

        for w in word_object:
            if w.pos == pos_person:
                e = u" :{person} :singer_introduction ?o.".format(person=w.token.decode('utf-8'))
            sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                              select=select,
                                              expression=e)
            break
        return sparql

    @staticmethod
    def stay_album(word_object):
        # 以父之名是哪个专辑的歌曲
        select = u"?x"
        sparql = None

        for w in word_object:
            if w.pos == pos_song:
                e = u" :{song} :include_by ?o."\
                    u" ?o :album_name ?x.".format(song=w.token.decode('utf-8'))
            sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                              select=select,
                                              expression=e)
            break
        return sparql

    @staticmethod
    def release_album(word_object):
        # 叶惠美是哪一年发行的
        select = u"?o"
        sparql = None

        for w in word_object:
            if w.pos == pos_album:
                e = u" :{album} :album_release_date ?o." .format(album=w.token.decode('utf-8'))
            sparql = SPARQL_SELECT_TEM.format(prefix=SPARQL_PREXIX,
                                              select=select,
                                              expression=e)
            break
        return sparql
rules = [
    Rule(condition_num=2,condition=W(pos="r") + W("是") + person + W(pos="nr") | person + W(pos="nr") + W("是") + W(pos="r") , action=QuestionSet.who_is_question_E),
    Rule(condition_num=2,condition=W(pos="nr") + person + W("是") + W(pos="r") | W(pos="r") + W("是") + W(pos="nr") + person, action=QuestionSet.who_is_question_E),
    Rule(condition_num=2, condition=Star(Any(), greedy=False) + about + Star(Any(), greedy=False) + W(pos="n") | Star(Any(), greedy=False) + W(pos="n") + Star(Any(), greedy=False),
         action=QuestionSet.which_question),
    Rule(condition_num=2, condition=person + W(pos="nr") + Star(Any(), greedy=False) + data |
                       W(pos="nr") + person + Star(Any(), greedy=False) + data , action=QuestionSet.whose_data_question),
]
class Word(object):
    """treated words as objects"""
    def __init__(self, token, pos):
        self.token = token
        self.pos = pos

class Question2Sparql:
    def __init__(self):
        self.rules = rules

    def get_sparql(self, question):
        # 进行语义解析，找到匹配的模板，返回对应的SPARQL查询语句
        # word_objects = self.tw.get_word_objects(question)
        words = pseg.cut(question)
        word_objects = [Word(word, flag) for word, flag in words]
        queries_dict = dict()
        for rule in self.rules:
            query, num = rule.apply(word_objects)
            if query is not None:
                queries_dict[num] = query
        if len(queries_dict) == 0:
            return None
        elif len(queries_dict) == 1:
            return list(queries_dict.values())[0]
        else:
            # TODO 匹配多个语句，以匹配关键词最多的句子作为返回结果
            sorted_dict = sorted(queries_dict.items(), key=lambda item: item[0], reverse=True)
            return sorted_dict[0][1]
class JenaFuseki:
    def __init__(self, endpoint_url='http://localhost:3030/nbaa/query'):
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
# TODO 连接Fuseki服务器。
fuseki = JenaFuseki()
# TODO 初始化自然语言到SPARQL查询的模块，参数是外部词典列表。
q2s = Question2Sparql()
def generate_response(user_input):
    question = user_input
    my_query = q2s.get_sparql(question)

    if my_query is not None:

        result = fuseki.get_sparql_result(my_query)
        value = fuseki.parse_result(result)
        return value
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
        return 'I can\'t understand. :('
