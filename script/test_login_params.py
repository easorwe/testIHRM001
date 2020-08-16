# 导包
import logging
import unittest
from parameterized import parameterized
# 创建unittest的类
import app
from api.login_api import LoginApi
from utils import assert_count, read_lohin_data


class TestIHRMLoginParams(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 定义登录数据文件的文件
    filepath = app.BASE_DIR + "/data/login_data.json"

    @parameterized.expand(read_lohin_data(filepath))
    # 编写登录成功函数
    def test_01_login(self, case_name, request_body, success, code, message, http_code):
        response = self.login_api.login(request_body,
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("登录结果:{}".format(response.json()))

        # 断言
        assert_count(self, http_code, success, code, message, response)
