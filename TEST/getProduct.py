#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: getProduct.py
@time: 2021/3/3 3:43 下午
"""
import re
with open('tt_test.txt') as f:
    data=f.read()
rule=re.compile("https:.*?jpg|https:.*?jpeg|https:.*?png")
ll=rule.findall(data)
for i in ll:
    print(i)
if __name__ == '__main__':
    pass