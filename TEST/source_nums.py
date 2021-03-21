#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: source_nums.py
@time: 2021/3/4 4:38 下午
"""
import re
import json
with open("num_test_source.txt","w") as ff:
    pass
with open('num_test.txt','r') as f:
    for i in f:
        i=eval(i)
        print(i['result'])
        # rp=rule.search(i)
        # if rp:
        #     WAN=rp.group("WAN")
        #     QIAN=rp.group("QIAN")
        #     BAI=rp.group("BAI")
        #     SHI=rp.group("SHI")
        #     GE=rp.group("GE")
        # print(''.join([WAN,QIAN,BAI,SHI,GE]))
if __name__ == '__main__':
    pass