# 生成测试报告,是要先执行测试用例

# 导包
import os
import time
import unittest
# 创建测试套件
import HTMLTestRunner_PY3

import app
from script.test_emp_params import TestIHRMEmployee
from script.test_login_params import TestIHRMLoginParams

# os.path.dirname(os.path.abspath(__file__))可以定位到当前项目的目录

base_dir = os.path.dirname(os.path.abspath(__file__))
suite = unittest.TestSuite()

# 将测试用例添加到测试套件
suite.addTest(unittest.makeSuite(TestIHRMLoginParams))
suite.addTest(unittest.makeSuite(TestIHRMEmployee))

# 定义测试报告的目录和报告名称
report_path = app.BASE_DIR + "/report/tihrm{}.html".format(time.strftime('%Y%m%d%H%M%S'))

# 生成测试报告
with open(report_path, mode="wb") as  f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, verbosity=1,
                                               title="IHRM接口测试",
                                               description="更加美观的测试报告")

    # 实例化runner运行测试套件,生成测试报告
    runner.run(suite)
