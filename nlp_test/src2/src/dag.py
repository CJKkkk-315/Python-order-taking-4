#!usr/bin/env python
#-*- coding:utf-8 -*-


class DAG:
    def __init__(self, sentence, relation):
        self.dag = {}
        self.relation = relation
        self._dag(sentence)

    def _dag(self, sentence):
        N = len(sentence)
        for k in range(N):
            tmp_list = []
            i = k
            frag = sentence[k]
            while i < N and self.relation.search(frag):
                if self.relation.get_freq(frag):
                    tmp_list.append(i)
                i += 1
                frag = sentence[k:i + 1]
            if not tmp_list:
                tmp_list.append(k)
            self.dag[k] = tmp_list

    def __iter__(self):
        return iter(self.dag)

    def items(self):
        return self.dag.items()

    def get(self, key: str, default=None):
        return self.dag.get(key, default)