# 导包
import logging
import unittest

# 创建unittest的类
from api.login_api import LoginApi
from utils import assert_count


class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self):
        self.login_api = LoginApi()

    def tearDown(self):
        pass

    # 编写登录成功函数
    def test_01_login_success(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("登录结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, True, 10000, "操作成功", response)
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))

    #     手机号码为空
    def test_02_mobile_is_empty(self):
        response = self.login_api.login({"mobile": "", "password": "234567"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("手机号码为空结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, response.json().get("success"))
        # self.assertEqual(10000, response.json().get("code"))
        # self.assertIn("操作成功", response.json().get("message"))

    #         手机号码不存在
    def test_03_mobile_is_not_exists(self):
        response = self.login_api.login({"mobile": "13800123456", "password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("手机号码不存在结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    # 密码错误
    def test_04_password_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "error"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("密码错误:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    # 无参
    def test_05_params_is_none(self):
        response = self.login_api.login({},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("无参结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    # 传入NULL
    def test_06_params_is_null(self):
        response = self.login_api.login(None,
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("传入null结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 99999, "抱歉，系统繁忙，请稍后重试！", response)

    # 多参
    def test_07_more_params(self):
        response = self.login_api.login({"mobile": "13800000002", "password": "123456", "more_params": "1"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("多参结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, True, 10000, "操作成功", response)

    #         少参-缺少mobile
    def test_08_less_params_mobile(self):
        response = self.login_api.login({"password": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("少参结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    #         少参-缺少password
    def test_09_less_password(self):
        response = self.login_api.login({"mobile": "13800000002"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("少参结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    #     错误参数
    def test_10_params_is_error(self):
        response = self.login_api.login({"mobile": "13800000002", "possword": "123456"},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("错误参数结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)

    #     密码为空
    def test_11_password_is_emprty(self):
        response = self.login_api.login({"mobile": "13800000002", "password": ""},
                                        {"Content-Type": "application/json"})

        # 打印响应结果
        logging.info("密码为空结果:{}".format(response.json()))

        # 断言
        assert_count(self, 200, False, 20001, "用户名或密码错误", response)
