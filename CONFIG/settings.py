#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: settings.py
@time: 2021/3/15 11:03 上午
"""
import logging
import os
BaseDir=os.path.dirname(os.path.dirname(__file__))
LOG_FILE=os.path.join(BaseDir,"LOG/log.log")
formatter1='%(asctime)s - %(module)s - %(thread)d - %(filename)s - [line:%(lineno)d]- %(levelname)s : %(message)s'
formatter2='%(asctime)s - %(module)s - %(thread)d - %(filename)s - [line:%(lineno)d]- %(levelname)s : %(message)s'
LOG_LEVEL=logging.INFO


if __name__ == '__main__':
    pass