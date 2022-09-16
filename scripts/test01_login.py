import pytest

import page
from page.page_in import PageIn
from tools.get_driver import GetDriver
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()


class TestLogin:

    # 初始化
    def setup_class(self):
        # 1. 获取driver
        driver = GetDriver.get_web_driver(page.url)
        # 2. 通过统一入口类获取PageMpLogin对象
        self.login = PageIn(driver).get_page_login()

    # 结束
    def teardown_class(self):
        # 调用关闭driver
        GetDriver.quit_web_driver()

    # 测试业务方法
    @pytest.mark.parametrize("phone,pwd,secret,expect", read_yaml("login.yaml"))
    def test_login(self, phone, pwd, secret, expect):
        # 调用登录业务方法
        self.login.page_login_role(phone, pwd, secret)
        # 断言
        print("\n 获取的租户名称为", self.login.page_get_tenant_name())
        try:
            assert expect == self.login.page_get_tenant_name()
        except Exception as e:
            log.error("断言出错，错误信息：{}".format(e))
            # 输出错误原因
            print("错误原因: ", e)
            # 截图
            self.login.base_screenshot()
            # 抛出异常
            raise