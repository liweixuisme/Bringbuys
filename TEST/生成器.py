#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: 生成器.py
@time: 2021/3/1 10:18 上午
"""
import random

def operateSource():
    with open("source.txt",'a') as f:
        for x in range(100000000):
            for i in range(5):
                ran=random.randrange(10)
                f.write(str(ran))
            f.write("\n")

def readLine():
    with open("source.txt",'r') as f:
        count=0
        for i in f :
            count+=1

    print(count)


if __name__ == '__main__':
    readLine()