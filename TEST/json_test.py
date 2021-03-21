#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 0.1
@author: feikon
@license: Apache Licence
@contact: crossfirestarer@gmail.com
@site: https://github.com/feikon
@software: PyCharm
@file: json_test.py
@time: 2021/2/27 5:16 下午
"""
import json
str='''[('100006180837', '探路者（TOREAD）官方旗舰店 儿童童装男中大童秋季涤纶高弹轻薄运动长裤百搭卫裤QAMI83058-C82X 太空蓝 120', 'jfs/t1/144086/37/7201/88524/5f4dc3cbEf279cb41/ee89526763eda3ea.jpg', '["jfs/t1/144086/37/7201/88524/5f4dc3cbEf279cb41/ee89526763eda3ea.jpg","jfs/t1/147774/13/9001/57233/5f68a46dEe4c8dfd0/8800ab1630943afe.jpg","jfs/t1/133805/31/10472/105436/5f68a43fE1ea43e6c/0a4c100c73aa490d.jpg","jfs/t1/132798/8/8534/77894/5f4dc3ceE14065600/21e9e21ff6d72b53.jpg","jfs/t1/111825/18/16879/79975/5f4dc3d0Edb34bf6f/e6fd4d6ad5caa9b3.jpg","jfs/t1/129129/20/11529/102285/5f4dc3d1E4a97f230/48d36da535481735.jpg"]', '[1319,11842,11224]', '["母婴","童装","裤子"]')]'''
rp=json.dumps(str)
print(rp)
if __name__ == '__main__':
    pass