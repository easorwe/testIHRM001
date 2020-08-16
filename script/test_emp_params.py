# 导包
import logging
import unittest
from parameterized import parameterized

# 创建测试类
import app
from api.IHRM_API import EmployeeApi
from api.login_api import LoginApi
from utils import assert_count, read_emp_data


class TestIHRMEmployee(unittest.TestCase):
    # 初始化unittest的函数
    def setUp(self):
        #     实例化登录
        self.login_api = LoginApi()
        #     实例化员工
        self.emp_api = EmployeeApi()

    def tearDown(self):
        pass

    # 实现登录成功的接口
    def test_01_login_success(self):
        # 发送登录接口请求
        jsonData = {"mobile": "13800000002", "password": "123456"}
        response = self.login_api.login(jsonData,
                                        {"Content-Type": "application/json"}
                                        )
        # 打印登录接口返回结果
        logging.info("登录结果:{}".format(response.json()))
        # 提取登录令牌
        token = "Bearer " + response.json().get('data')
        # 把令牌拼接成HEADERS并保存到全局变量
        app.HEADERS = {"Content-Type": "application/json", "Authorization": token}
        # 打印请求头
        logging.info("全局变量的请求头:{}".format(app.HEADERS))

        # 断言
        assert_count(self, 200, True, 10000, "操作成功", response)

        # 定义员工模块的文件路径

    emp_filepath = app.BASE_DIR + "/data/emp_data.json"

    @parameterized.expand(read_emp_data(emp_filepath, "add_emp"))
    def test_02_add_emp(self, username, mobile, success, code, message, http_code):
        # logging.info("app.HEADERS的值是：{}".format(app.HEADERS))
        # 发送添加员工的接口请求
        response = self.emp_api.add_emp(username, mobile, app.HEADERS)
        # 提取员工的令牌保存到全局变量
        app.EMP_ID = response.json().get("data").get("id")
        # 打印保存的员工ID
        logging.info("全局变量的ID为:{}".format(app.EMP_ID))
        # 断言
        assert_count(self, http_code, success, code, message, response)

    # 查询员工
    @parameterized.expand(read_emp_data(emp_filepath, "query_emp"))
    def test_03_query_emp(self, success, code, message, http_code):
        #         发送查询员工的接口
        response = self.emp_api.query_emp(app.EMP_ID, app.HEADERS)
        #         打印查询员工的数据
        logging.info("查询员工的结果:{}".format(response.json()))
        assert_count(self, http_code, success, code, message, response)

    #     修改员工
    @parameterized.expand(read_emp_data(emp_filepath, "modify_emp"))
    def test_04_modify_emp(self, username, success, code, message, http_code):
        #         发送修改员工的接口
        response = self.emp_api.modify_emp(app.EMP_ID, app.HEADERS, {"username": username})
        # 打印修改员工的数据
        logging.info("修改员工:{}".format(response.json()))
        assert_count(self, http_code, success, code, message, response)

    # 删除员工
    @parameterized.expand(read_emp_data(emp_filepath, "delete_emp"))
    def test_05_delete_emp(self, success, code, message, http_code):
        #         发送删除员工接口
        response = self.emp_api.delete_emp(app.EMP_ID, app.HEADERS)

        # 打印删除员工的结果
        logging.info("删除员工:{}".format(response.json()))
        assert_count(self, http_code, success, code, message, response)
