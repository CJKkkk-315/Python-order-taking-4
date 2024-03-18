
# -*- coding: utf-8 -*-

import logging, time, os
import time
import os

# 当前路径
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# 定义日志文件路径
LOG_PATH = os.path.join(BASE_PATH, "log")
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger():
    _instance = None
    """
    打印log输出的模块：输出到控制台的同时输出到文件
    """
    def __init__(self):
        print("log存放位置:" + BASE_PATH)
        self.logname = os.path.join(LOG_PATH, "lunar.log")  # 日志的名称
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)

        self.formater = logging.Formatter(
            '[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]: %(message)s')

        self.filelogger = logging.FileHandler(self.logname, mode='a', encoding="UTF-8")
        self.console = logging.StreamHandler()
        self.console.setLevel(logging.DEBUG)
        self.filelogger.setLevel(logging.DEBUG)
        self.filelogger.setFormatter(self.formater)
        self.console.setFormatter(self.formater)
        self.logger.addHandler(self.filelogger)
        self.logger.addHandler(self.console)

    @classmethod
    def singleton(cls, *args, **kwargs):
        '''
        单例模式
        '''
        if not cls._instance:
            cls._instance = cls(*args, **kwargs)
        return cls._instance


if __name__ == '__main__':
    logger = Logger.singleton().logger
    logger.info("---测试开始111---")
    logger.debug("---测试结束222---")
    logger.error("---测试error---")


