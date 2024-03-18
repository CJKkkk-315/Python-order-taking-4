#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import json

def read_from_jsonFile(file_path):
    '''
    :param file_path: Json文件的路径
    return:Json文件中的数据
    '''
    with open(file_path, 'r', encoding='utf-') as fp:
        json_data = json.load(fp)
    fp.close()
    return json_data


def write_into_jsonFile(file_path, json_data):
    '''
    :param file_path: Json文件的路径
    :param json_data: 要写入Json文件中的数据
    '''
    with open(file_path,'w',encoding='utf-8') as fp:#path为json文件路径
        json.dump(json_data, fp)
    fp.close()


if __name__ == "__main__":
    dict = {"name":"zhangsan", "age":18, "sex":"男"}
    write_into_jsonFile("/Users/mac/1.json", dict)
    dict1 = read_from_jsonFile("/Users/mac/1.json")
    print(dict1)
    print(type(dict1))