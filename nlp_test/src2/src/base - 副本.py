#!usr/bin/env python
#-*- coding:utf-8 -*-

import os
from src.trie import Trie


class BaseSegment:

    def __init__(self):
        self.trie = Trie()

    def cut(self, sentence: str):
        pass

    def load_dict(self, file: str):
        if not os.path.exists(file):
            print('%s 不存在！' % file)
            return

        with open(file, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                line = line.split()
                #print(line)
                #if len(line)!=2:continue
                if len(line) == 3:
                    self.trie.insert(line[0], int(line[1]), line[2])
                elif len(line) == 2:
                    self.trie.insert(line[0], int(line[1]))
                else:
                    self.trie.insert(line[0])
        f.close()
        #print('词典加载完成！')
