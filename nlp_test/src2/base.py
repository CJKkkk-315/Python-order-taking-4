#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
from src.trie import Trie


class BaseSegment:

    def __init__(self):
        self.trie = Trie()

    def cut(self, sentence: str):
        pass

    def load_dict(self, file):
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            line = line.split()
            if len(line) == 3:
                self.trie.insert(line[0], int(line[1]), line[2])
            elif len(line) == 2:
                self.trie.insert(line[0], int(line[1]))
            else:
                self.trie.insert(line[0])
        #print('词典加载完成！')
        file.close()
