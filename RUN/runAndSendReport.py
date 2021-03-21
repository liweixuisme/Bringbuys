# coding=UTF-8
import os
import sys


import unittest
BaseDir=os.path.dirname(os.path.dirname(__file__))
sys.path.append(BaseDir)
from COMMON.BSTestRunner import BSTestRunner
import time
from COMMON.email_report import *

test_dir = os.path.join(BaseDir,'TESTCASE')
report_dir = os.path.join(BaseDir,'REPORT')



# 加载测试用例
def run():
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*.py')
    # 定义测试报告格式
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    report_name = os.path.join(report_dir , ''.join([now,'test_report.html']))
    # 运行并生成测试报告
    with open(report_name, 'wb') as file:
        runner = BSTestRunner(stream=file, title='Test report', description='Test report')
        runner.run(discover)
    EmailReport().sendEmail(report_name)

if __name__ == '__main__':
    run()
