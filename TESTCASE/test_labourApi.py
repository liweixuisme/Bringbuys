# coding=UTF-8
import unittest
from COMMON.apiCommon import *
import requests
import os
import json

class Test_case(unittest.TestCase,Common):
    logger=Common().outLog()
    s=requests.session()
    BaseUrl="http://labour.bringbuys.com/api/"

    s.post('http://labour.bringbuys.com/api/sys/login?username=liwei2&password=123456&captcha=33333')

    def setUp(self):
        self.logger.debug('setup 此用例开始执行'.center(50,'='))

    def test_employer_save(self):
        api="employer/save"
        url=os.path.join(self.BaseUrl,api)
        data={
            "businessNo": "SSS51553522",
            "nameCn": "手机制造有限公司",
            "shortName": "手机制造",
            "namePt": "手机制造PT",
            "industryId": 19,
            "address": "横琴跨境说公司",
            "jobCenterName": "厦门国际职介所",
            "phoneArea": "0756",
            "phone": "6354145",
            "fax": "8008208820",
            "cooperatorId": 46,
            "onlyEnName": 1,
            "remark": "横琴珠海横琴跨境说网络科技有限公司位于 珠海横琴新区",
            "pspCode": "PSP555664",
            "jobCenterId": 1
        }
        header={
            "Content-Type": "application/json;charset=UTF-8"
        }
        rp=self.s.post(url,json=data,headers=header)
        print(rp.text)

    def test_employer_list(self):
        api="employer/list"
        url=os.path.join(self.BaseUrl,api)
        data={
            "page":"1",
            "limit":"10",
        }

        rp=self.s.get(url,params=data)
        print(rp.text)

    def tearDown(self):
        self.logger.debug('tearDown 此用例执行完毕'.center(50,'='))

if __name__ == '__main__':
    unittest.main()
    # millis = int(round(time.time() * 10))
    # logging.info(millis)
    # msg=post("POST_petro_pos_staff_login","13763965477",millis)
    # logging.info(msg)
