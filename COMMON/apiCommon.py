#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: apiCommon.py
@time: 2021/2/23 5:32 下午
"""
import logging
from CONFIG import settings
class Common:

    def outLog(self,logFile=settings.LOG_FILE,logLevel=settings.LOG_LEVEL):
        logger=logging.getLogger()
        fh=logging.FileHandler(logFile)
        ch=logging.StreamHandler()
        fomatter1=logging.Formatter(settings.formatter1)
        fomatter2=logging.Formatter(settings.formatter2)
        fh.setFormatter(fomatter1)
        ch.setFormatter(fomatter2)
        logger.addHandler(fh)
        logger.addHandler(ch)
        logger.setLevel(logLevel)
        return logger





if __name__ == '__main__':
    logger=Common().outLog('test.log',logging.INFO)
    logger.info('测试日志打印函数封装')
